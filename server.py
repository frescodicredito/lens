"""Lens MCP Server — cognitive infrastructure for LLM reasoning.

Serves constraint library, persona templates, topologies, and provides
prompt composition and session management.
"""

import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional

from fastmcp import FastMCP

from constraints.composer import (
    compose_baseline_prompt,
    compose_prompt,
    compose_persona_prompt,
    compose_sequential_prompt,
    load_library,
    load_persona,
    safe_identifier,
    suggest_constraints,
)
from meta.analytics import (
    constraint_efficacy,
    implementation_rate,
    pattern_mining,
    roi_estimate,
    sequence_efficacy,
    smart_defaults,
    suggest_from_history,
    topology_efficacy,
)
from integrations.miner import (
    save_miner_persona,
    transform_all_personas,
    transform_miner_persona,
)
from output.formatter import format_session_summary

BASE_DIR = Path(__file__).parent
SESSIONS_DIR = BASE_DIR / "sessions"
TOPOLOGIES_PATH = BASE_DIR / "topologies" / "definitions.json"
PERSONAS_DIR = BASE_DIR / "personas" / "templates"

SESSIONS_DIR.mkdir(exist_ok=True)


def _load_session_file(path: Path) -> Optional[dict]:
    """Load a single session JSON, returning None if missing or corrupt."""
    try:
        with open(path, encoding="utf-8") as fp:
            return json.load(fp)
    except (json.JSONDecodeError, OSError):
        return None


def _write_json_atomic(path: Path, data: dict) -> None:
    """Write JSON atomically (temp file + replace) to avoid partial/corrupt files."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


mcp = FastMCP(
    "Lens",
    instructions=(
        "Lens is a cognitive infrastructure system. "
        "It does not produce content: it produces ways of looking at problems. "
        "The primitive is the cognitive constraint, not the persona. "
        "Constraints navigate the tails of the LLM distribution, "
        "where creativity, unusual connections, and non-linear perspectives live."
    ),
)


# --- Constraint Tools ---


@mcp.tool
def lens_list_constraints(category: Optional[str] = None) -> str:
    """List available cognitive constraints from the library.

    Args:
        category: Filter by category (structural, temporal, semantic, modal, creative, analytical).
                  If None, returns all constraints.
    """
    library = load_library()
    constraints = library["constraints"]

    if category:
        constraints = [c for c in constraints if c.get("category") == category]

    result = []
    for c in constraints:
        result.append({
            "id": c["id"],
            "name": c["name"],
            "category": c["category"],
            "description": c["description"],
            "theory": c["theory"],
        })

    categories = sorted(set(c["category"] for c in library["constraints"]))
    return json.dumps({
        "count": len(result),
        "categories": categories,
        "constraints": result,
    }, ensure_ascii=False, indent=2)


@mcp.tool
def lens_get_constraint(constraint_id: str) -> str:
    """Get full details of a specific constraint.

    Args:
        constraint_id: The constraint ID (e.g., 'inversion', 'temporal', 'bisociative').
    """
    library = load_library()
    for c in library["constraints"]:
        if c["id"] == constraint_id:
            return json.dumps(c, ensure_ascii=False, indent=2)
    return json.dumps({"error": f"Constraint '{constraint_id}' not found"})


# --- Persona Tools ---


@mcp.tool
def lens_list_personas() -> str:
    """List available persona templates."""
    result = []
    for f in sorted(PERSONAS_DIR.glob("*.json")):
        with open(f, encoding="utf-8") as fp:
            persona = json.load(fp)
        result.append({
            "id": persona["id"],
            "name": persona["name"],
            "description": persona["description"],
            "constraints_count": len(persona.get("constraints", [])),
        })

    return json.dumps({"count": len(result), "personas": result}, ensure_ascii=False, indent=2)


@mcp.tool
def lens_get_persona(persona_id: str) -> str:
    """Get full details of a specific persona template.

    Args:
        persona_id: The persona ID (e.g., 'cto-skeptic', 'early-adopter').
    """
    try:
        persona = load_persona(persona_id)
        return json.dumps(persona, ensure_ascii=False, indent=2)
    except ValueError as e:
        return json.dumps({"error": str(e)})


# --- Topology Tools ---


@mcp.tool
def lens_list_topologies(mode: Optional[str] = None) -> str:
    """List available cognitive topologies.

    Args:
        mode: Filter by mode ('QUICK' or 'DEEP'). If None, returns all.
    """
    with open(TOPOLOGIES_PATH, encoding="utf-8") as f:
        data = json.load(f)

    topologies = data["topologies"]
    if mode:
        topologies = [t for t in topologies if t.get("mode") == mode.upper()]

    result = []
    for t in topologies:
        result.append({
            "id": t["id"],
            "name": t["name"],
            "description": t["description"],
            "mode": t["mode"],
            "agent_count": t["agent_count"],
            "rounds": t["rounds"],
            "best_for": t.get("best_for", []),
        })

    return json.dumps({"count": len(result), "topologies": result}, ensure_ascii=False, indent=2)


@mcp.tool
def lens_get_topology(topology_id: str) -> str:
    """Get full details of a specific topology including workflow definition.

    Args:
        topology_id: The topology ID (e.g., 'cascade', 'star', 'adversarial_jury').
    """
    with open(TOPOLOGIES_PATH, encoding="utf-8") as f:
        data = json.load(f)

    for t in data["topologies"]:
        if t["id"] == topology_id:
            return json.dumps(t, ensure_ascii=False, indent=2)
    return json.dumps({"error": f"Topology '{topology_id}' not found"})


# --- Composition Tools ---


@mcp.tool
def lens_compose_prompt(
    topic: str,
    constraints: str,
    output_format: str = "perspective_card",
    intensity: int = 3,
    extra_instructions: Optional[str] = None,
) -> str:
    """Compose a structured prompt from constraints + topic.

    This is the core tool: transforms constraint specifications into
    a complete system prompt ready for a subagent.

    Args:
        topic: The topic or problem to analyze.
        constraints: JSON string of constraint list. Each constraint is an object
                     with 'type' and optional parameters.
                     Example: [{"type": "inversion"}, {"type": "temporal", "value": "2030"}]
        output_format: Output schema (perspective_card, field_map, delta_report, raw).
        intensity: Constraint intensity 1-5 (1=soft, 3=firm, 5=absolute).
        extra_instructions: Additional instructions to append.
    """
    try:
        constraints_list = json.loads(constraints)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON in constraints parameter"})

    result = compose_prompt(
        constraints=constraints_list,
        topic=topic,
        output_format=output_format,
        intensity=intensity,
        extra_instructions=extra_instructions,
    )

    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool
def lens_compose_persona(
    persona_id: str,
    topic: str,
    output_format: str = "perspective_card",
    intensity: int = 3,
) -> str:
    """Compose a prompt from a persona template.

    Loads the persona's constraints and psychology, then generates
    a structured prompt.

    Args:
        persona_id: The persona template ID (e.g., 'cto-skeptic').
        topic: The topic or problem to analyze.
        output_format: Output schema (perspective_card, field_map, delta_report, raw).
        intensity: Constraint intensity 1-5.
    """
    try:
        result = compose_persona_prompt(
            persona_id=persona_id,
            topic=topic,
            output_format=output_format,
            intensity=intensity,
        )
        return json.dumps(result, ensure_ascii=False, indent=2)
    except ValueError as e:
        return json.dumps({"error": str(e)})


@mcp.tool
def lens_suggest_constraints(
    topic: str,
    goal: str,
    max_constraints: int = 4,
) -> str:
    """Suggest optimal constraints for a topic + goal.

    Uses data-driven suggestions from session history when available,
    falls back to heuristic-based suggestions otherwise.

    Args:
        topic: The topic or problem.
        goal: What you want to achieve (e.g., 'stressare questo claim',
              'generare idee creative', 'analizzare rischi').
        max_constraints: Maximum number of constraints to suggest (default 4).
    """
    # Try data-driven first
    data_suggestions = suggest_from_history(topic, goal, max_constraints)
    if data_suggestions:
        return json.dumps({
            "source": "data-driven + heuristic",
            "topic": topic,
            "goal": goal,
            "data_driven": data_suggestions,
            "heuristic": suggest_constraints(topic, goal, max_constraints),
        }, ensure_ascii=False, indent=2)

    # Pure heuristic fallback
    suggestions = suggest_constraints(topic, goal, max_constraints)
    return json.dumps({
        "source": "heuristic",
        "topic": topic,
        "goal": goal,
        "suggestions": suggestions,
    }, ensure_ascii=False, indent=2)


@mcp.tool
def lens_compose_baseline(
    topic: str,
    output_format: str = "perspective_card",
) -> str:
    """Compose a clean unconstrained baseline prompt for a topic.

    Use this in the baseline+delta workflow: run baseline first for standard
    analysis, then run lens_compose_prompt with constraints for the delta.
    The combined output is more valuable than either alone.

    Args:
        topic: The topic or problem to analyze.
        output_format: Output schema (perspective_card, field_map, raw).
    """
    result = compose_baseline_prompt(topic=topic, output_format=output_format)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool
def lens_compose_sequential(
    topic: str,
    constraints: str,
    intensity: int = 3,
    insert_anchor_break: bool = True,
) -> str:
    """Compose a sequence of prompts for sequential deep chain analysis.

    Generates ordered prompts for a single-agent sequential chain where each
    round applies a different constraint, integrating all previous output.

    Use this for deep epistemic analysis, steelmanning, hypothesis exploration.
    The skill /lens-deep orchestrates the execution of these prompts.

    Args:
        topic: The topic or problem to analyze deeply.
        constraints: JSON string of ordered constraint list. ORDER MATTERS:
                     first constraint = primary lens, subsequent = refinements.
                     Example: [{"type": "steelman"}, {"type": "inversion"}, {"type": "abductive"}]
        intensity: Constraint intensity 1-5 (default 3).
        insert_anchor_break: Insert anchor_break between rounds to fight path dependency (default True).
    """
    try:
        constraints_list = json.loads(constraints)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON in constraints parameter"})

    result = compose_sequential_prompt(
        constraints=constraints_list,
        topic=topic,
        intensity=intensity,
        insert_anchor_break=insert_anchor_break,
    )

    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool
def lens_quick_start(
    topic: str,
    goal: Optional[str] = None,
) -> str:
    """Get a complete ready-to-use Lens configuration for any topic.

    One-stop tool: analyzes topic, suggests skill, topology, constraints,
    and intensity. Based on session history when available, heuristics otherwise.

    The user can accept the configuration as-is or modify it.

    Args:
        topic: The topic or problem to analyze.
        goal: Optional goal description (e.g., 'stressare questo claim',
              'trovare assunzioni nascoste', 'generare idee creative').
    """
    result = smart_defaults(topic, goal)
    return json.dumps(result, ensure_ascii=False, indent=2)


# --- Session Tools ---


@mcp.tool
def lens_session_save(
    topology: str,
    topic: str,
    agents_count: int,
    rounds_count: int,
    output: str,
    constraints_used: Optional[str] = None,
    constraint_sequence: Optional[str] = None,
    useful: Optional[bool] = None,
    surprising: Optional[bool] = None,
    implemented: Optional[bool] = None,
    implementation_note: Optional[str] = None,
    delta_unique_insights: Optional[int] = None,
) -> str:
    """Save a Lens session output for future reference and Meta-Lens analysis.

    Args:
        topology: Topology ID used (e.g., 'cascade', 'star', 'sequential_chain').
        topic: The topic analyzed.
        agents_count: Number of agents used.
        rounds_count: Number of rounds executed.
        output: The full session output (markdown).
        constraints_used: JSON string of constraint types used (unordered set).
                          Example: '["inversion", "steelman", "abductive"]'
        constraint_sequence: JSON string of ordered constraint sequence (for sequential_chain).
                             Example: '["steelman", "anchor_break", "inversion", "abductive"]'
        useful: Was the session useful? (optional, for efficacy tracking).
        surprising: Did the session produce surprising insights? (optional).
        implemented: Was the insight actually used in real work? (optional).
        implementation_note: How/where the insight was used (optional).
        delta_unique_insights: Count of unique insights vs baseline (optional).
    """
    session_id = f"lens-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"

    parsed_constraints = []
    if constraints_used:
        try:
            parsed_constraints = json.loads(constraints_used)
        except json.JSONDecodeError:
            parsed_constraints = []

    parsed_sequence = None
    if constraint_sequence:
        try:
            parsed_sequence = json.loads(constraint_sequence)
        except json.JSONDecodeError:
            parsed_sequence = None

    efficacy = {
        "rated": useful is not None or surprising is not None,
        "useful": useful,
        "surprising": surprising,
        "implemented": implemented,
        "implementation_note": implementation_note,
        "delta_unique_insights": delta_unique_insights,
    }

    summary = format_session_summary(
        session_id=session_id,
        topology=topology,
        topic=topic,
        agents_count=agents_count,
        rounds_count=rounds_count,
        output=output,
        constraints_used=parsed_constraints,
        constraint_sequence=parsed_sequence,
        efficacy=efficacy,
    )

    session_file = SESSIONS_DIR / f"{session_id}.json"
    _write_json_atomic(session_file, summary)

    return json.dumps({
        "session_id": session_id,
        "saved_to": f"sessions/{session_id}.json",
        "efficacy": efficacy,
    }, ensure_ascii=False, indent=2)


@mcp.tool
def lens_session_update(
    session_id: str,
    implemented: Optional[bool] = None,
    implementation_note: Optional[str] = None,
    useful: Optional[bool] = None,
    surprising: Optional[bool] = None,
) -> str:
    """Update efficacy rating for an existing session.

    Use this to mark sessions as implemented after using the insights
    in real work. This is the key metric for non-circular evaluation.

    Args:
        session_id: The session ID to update (e.g., 'lens-20260228-225903-249ddd').
        implemented: Was the insight actually used in real work?
        implementation_note: How/where it was used (e.g., 'Used in brief for client X').
        useful: Override usefulness rating.
        surprising: Override surprise rating.
    """
    try:
        safe_identifier(session_id, "session_id")
    except ValueError:
        return json.dumps({"error": "Invalid session_id"})

    session_file = SESSIONS_DIR / f"{session_id}.json"
    if not session_file.exists():
        return json.dumps({"error": f"Session '{session_id}' not found"})

    data = _load_session_file(session_file)
    if data is None:
        return json.dumps({"error": f"Session '{session_id}' is corrupt or unreadable"})

    efficacy = data.get("efficacy", {})

    if implemented is not None:
        efficacy["implemented"] = implemented
    if implementation_note is not None:
        efficacy["implementation_note"] = implementation_note
    if useful is not None:
        efficacy["useful"] = useful
        efficacy["rated"] = True
    if surprising is not None:
        efficacy["surprising"] = surprising
        efficacy["rated"] = True

    data["efficacy"] = efficacy

    _write_json_atomic(session_file, data)

    return json.dumps({
        "session_id": session_id,
        "updated": True,
        "efficacy": efficacy,
    }, ensure_ascii=False, indent=2)


@mcp.tool
def lens_session_list(limit: int = 10) -> str:
    """List recent Lens sessions.

    Args:
        limit: Maximum number of sessions to return (default 10).
    """
    sessions = []
    session_files = sorted(SESSIONS_DIR.glob("*.json"), reverse=True)

    for f in session_files[:limit]:
        data = _load_session_file(f)
        if data is None:
            continue
        sessions.append({
            "session_id": data.get("session_id", f.stem),
            "timestamp": data.get("timestamp"),
            "topology": data.get("topology", "unknown"),
            "topic": data.get("topic", ""),
            "agents_count": data.get("agents_count"),
            "efficacy": data.get("efficacy", {}),
        })

    return json.dumps({"count": len(sessions), "sessions": sessions}, ensure_ascii=False, indent=2)


@mcp.tool
def lens_efficacy_report() -> str:
    """Generate an efficacy report from all saved sessions.

    Aggregates usefulness and surprise ratings across sessions,
    broken down by topology and constraint type.
    """
    session_files = list(SESSIONS_DIR.glob("*.json"))

    if not session_files:
        return json.dumps({"message": "No sessions saved yet.", "sessions_count": 0})

    total = 0
    rated = 0
    useful_count = 0
    surprising_count = 0
    by_topology = {}

    for f in session_files:
        data = _load_session_file(f)
        if data is None:
            continue

        total += 1
        topology = data.get("topology", "unknown")
        efficacy = data.get("efficacy", {})

        if topology not in by_topology:
            by_topology[topology] = {"total": 0, "useful": 0, "surprising": 0, "rated": 0}

        by_topology[topology]["total"] += 1

        if efficacy.get("rated"):
            rated += 1
            by_topology[topology]["rated"] += 1
            if efficacy.get("useful"):
                useful_count += 1
                by_topology[topology]["useful"] += 1
            if efficacy.get("surprising"):
                surprising_count += 1
                by_topology[topology]["surprising"] += 1

    return json.dumps({
        "total_sessions": total,
        "rated_sessions": rated,
        "useful_rate": f"{useful_count}/{rated}" if rated > 0 else "N/A",
        "surprising_rate": f"{surprising_count}/{rated}" if rated > 0 else "N/A",
        "by_topology": by_topology,
    }, ensure_ascii=False, indent=2)


# --- Meta-Lens Tools ---


@mcp.tool
def lens_meta_constraint_efficacy() -> str:
    """Analyze which constraints produce the most useful and surprising sessions.

    Returns effectiveness scores per constraint, sorted by impact.
    Score = (useful_rate * 0.6) + (surprising_rate * 0.4).
    Requires rated sessions to produce meaningful results.
    """
    result = constraint_efficacy()
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool
def lens_meta_topology_efficacy() -> str:
    """Analyze which topologies produce the best results.

    Returns usage stats, efficacy rates, average agent count,
    and most-used constraints per topology.
    """
    result = topology_efficacy()
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool
def lens_meta_patterns() -> str:
    """Find constraint combinations that frequently appear in successful sessions.

    Identifies pairs and triples of constraints that co-occur
    in sessions rated as useful or surprising.
    """
    result = pattern_mining()
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool
def lens_meta_suggest(
    topic: str,
    goal: Optional[str] = None,
    max_suggestions: int = 4,
) -> str:
    """Suggest constraints based on session history (data-driven).

    Uses topic similarity and efficacy ratings from past sessions
    to suggest constraints that worked well on similar topics.
    Falls back to heuristic suggestions if insufficient history.

    Args:
        topic: The topic or problem to analyze.
        goal: What you want to achieve (optional).
        max_suggestions: Maximum number of suggestions (default 4).
    """
    data_suggestions = suggest_from_history(topic, goal, max_suggestions)

    if data_suggestions:
        return json.dumps({
            "source": "data-driven",
            "topic": topic,
            "goal": goal,
            "suggestions": data_suggestions,
        }, ensure_ascii=False, indent=2)

    # Fallback to heuristic
    heuristic = suggest_constraints(topic, goal or "", max_suggestions)
    return json.dumps({
        "source": "heuristic",
        "note": "Sessioni insufficienti per suggerimenti data-driven. Usando euristica.",
        "topic": topic,
        "goal": goal,
        "suggestions": heuristic,
    }, ensure_ascii=False, indent=2)


@mcp.tool
def lens_meta_sequence_efficacy() -> str:
    """Analyze constraint sequence effectiveness for sequential chain sessions.

    Tracks which orderings of constraints produce the best results,
    not just which individual constraints work well.
    """
    result = sequence_efficacy()
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool
def lens_meta_implementation_rate() -> str:
    """Track implementation rate — the key non-circular metric.

    Shows what percentage of Lens sessions produced insights that were
    actually used in real work, broken down by topology and constraint.
    """
    result = implementation_rate()
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool
def lens_meta_roi() -> str:
    """Estimate ROI of Lens usage based on implementation data.

    Simple proxy: most productive topologies and constraints based on
    implementation rate rather than self-reported usefulness.
    """
    result = roi_estimate()
    return json.dumps(result, ensure_ascii=False, indent=2)


# --- Miner Integration Tools ---


@mcp.tool
def lens_persona_from_miner(
    miner_persona_json: str,
    save: bool = True,
) -> str:
    """Transform a Miner AudiencePersona into a Lens persona template.

    Takes a single persona from Miner's audience-profiler output and converts it
    into a Lens cognitive template with data-grounded constraints.

    Mapping:
    - demographics + occupation → role constraint
    - psychographics.values + attitudes → modal constraint
    - VALS segment → ELM route (central/peripheral processing)
    - pain_points → psychology.fears
    - goals → psychology.primary_goal
    - decision_making_style → convincement_threshold

    Args:
        miner_persona_json: JSON string of a single Miner AudiencePersona object.
        save: Whether to save the persona template to disk (default True).
    """
    try:
        miner_persona = json.loads(miner_persona_json)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON in miner_persona_json parameter"})

    template = transform_miner_persona(miner_persona)

    if save:
        filepath = save_miner_persona(template)
        return json.dumps({
            "status": "saved",
            "persona_id": template["id"],
            "saved_to": f"personas/templates/{filepath.name}",
            "template": template,
        }, ensure_ascii=False, indent=2)

    return json.dumps({
        "status": "preview",
        "persona_id": template["id"],
        "template": template,
    }, ensure_ascii=False, indent=2)


@mcp.tool
def lens_personas_from_miner_batch(
    miner_output_json: str,
    save: bool = True,
) -> str:
    """Transform all personas from a Miner AudienceProfilerOutput into Lens templates.

    Batch version: takes the full Miner audience-profiler output and converts
    all personas at once.

    Args:
        miner_output_json: JSON string of the full Miner AudienceProfilerOutput
                           (must contain a 'personas' array).
        save: Whether to save persona templates to disk (default True).
    """
    try:
        miner_output = json.loads(miner_output_json)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON in miner_output_json parameter"})

    templates = transform_all_personas(miner_output, save=save)

    results = []
    for t in templates:
        results.append({
            "persona_id": t["id"],
            "name": t["name"],
            "constraints_count": len(t.get("constraints", [])),
            "source_confidence": t.get("source_confidence", 0),
        })

    return json.dumps({
        "status": "saved" if save else "preview",
        "count": len(results),
        "personas": results,
    }, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    mcp.run()

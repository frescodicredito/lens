"""Lens Constraint Composer — transforms constraint configurations into structured prompts."""

import json
import re
from pathlib import Path
from typing import Optional

_SAFE_ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")


def safe_identifier(value: str, kind: str = "identifier") -> str:
    """Validate an id used to build a file path.

    Rejects path separators and traversal so a caller-supplied id can never
    escape its intended directory. Returns the value unchanged if valid.
    """
    if (
        not isinstance(value, str)
        or value in (".", "..")
        or not _SAFE_ID_RE.fullmatch(value)
    ):
        raise ValueError(f"Invalid {kind}")
    return value

LIBRARY_PATH = Path(__file__).parent / "library.json"
PERSONAS_PATH = Path(__file__).parent.parent / "personas" / "templates"

OUTPUT_SCHEMAS = {
    "perspective_card": """
## Output Format: Perspective Card

Structure your response EXACTLY in this format:

### CLAIM
[Your main position in 1-2 sentences]

### SUPPORT
[3-5 pieces of evidence, reasoning, or data that support the claim]

### BLIND SPOT
[1-3 aspects this perspective might miss or underestimate]

### CONFIDENCE
[High/Medium/Low] — [1 sentence explaining why]
""",
    "field_map": """
## Output Format: Field Map

Structure your response EXACTLY in this format:

### CONVERGENCES
[Points the different perspectives agree on]

### DIVERGENCES
[Points of substantial disagreement, with each perspective's position]

### OUTLIERS
[Surprising or unexpected insights that emerged from the analysis]

### SYNTHESIS
[An integration that honors the divergences without forcing artificial consensus]
""",
    "delta_report": """
## Output Format: Delta Report

Structure your response EXACTLY in this format:

### BASELINE
[What a standard, unconstrained analysis would say]

### DELTA
[What emerges DIFFERENTLY thanks to the applied constraints]

### UNIQUE INSIGHTS
[Insights that would NOT have emerged without the structural constraints]

### ADDED VALUE
[Why these insights matter for the decision]
""",
    "chain_output": """
## Output Format: Chain Output

Structure your response EXACTLY in this format:

### CURRENT POSITION
[Your position after integrating all previous rounds. 2-3 sentences.]

### EVOLUTION
[How your position changed relative to previous rounds. What did you add, modify, abandon?]

### UNRESOLVED TENSIONS
[Contradictions or tensions that remain open. Do not force an artificial resolution.]

### CALIBRATED CONFIDENCE
[High/Medium/Low] — [What would make you more/less certain]
""",
    "decision_brief": """
## Output Format: Decision Brief

Structure your response EXACTLY in this format:

### RECOMMENDATION
[The specific, concrete recommended action, in 1-2 sentences]

### CONFIDENCE
[High/Medium/Low] — [Rationale in 1 sentence]

### ARGUMENTS IN FAVOR
1. [Strongest argument]
2. [Second argument]
3. [Third argument]

### RISKS
1. [Most significant risk]
2. [Second risk]
3. [Third risk]

### WHAT TO VERIFY BEFORE PROCEEDING
1. [Concrete test or check #1]
2. [Concrete test or check #2]
""",
    "executive_extract": """
## Output Format: Executive Extract

Structure your response in AT MOST 5 bullet points:
- Every bullet is actionable (who does what, when)
- No background or context — only actions
- If there is a decision to make, state it explicitly
- If there is a critical risk, flag it explicitly
""",
    "raw": "",
}


def load_library() -> dict:
    """Load the constraint library from JSON."""
    with open(LIBRARY_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_persona(persona_id: str) -> dict:
    """Load a persona template by ID."""
    safe_identifier(persona_id, "persona_id")
    persona_file = PERSONAS_PATH / f"{persona_id}.json"
    if not persona_file.exists():
        raise ValueError(f"Persona '{persona_id}' not found")
    with open(persona_file, encoding="utf-8") as f:
        return json.load(f)


def get_constraint(library: dict, constraint_id: str) -> dict:
    """Get a constraint by ID from the library."""
    for c in library["constraints"]:
        if c["id"] == constraint_id:
            return c
    raise ValueError(f"Constraint '{constraint_id}' not found in library")


def check_compatibility(constraints: list[dict], library: dict) -> list[str]:
    """Check constraint compatibility, return list of warnings."""
    warnings = []
    constraint_ids = [c.get("type", c.get("id", "")) for c in constraints]

    for c in constraints:
        c_id = c.get("type", c.get("id", ""))
        try:
            lib_constraint = get_constraint(library, c_id)
        except ValueError:
            continue

        incompatible = lib_constraint.get("incompatible_with", [])
        for other_id in constraint_ids:
            if other_id != c_id and other_id in incompatible:
                warnings.append(
                    f"Constraint '{c_id}' is incompatible with '{other_id}'"
                )

    return warnings


def _substitute_variables(text: str, variables: dict) -> str:
    """Substitute {key} placeholders in text with values from variables dict."""
    for key, value in variables.items():
        if key == "type":
            continue
        if isinstance(value, str):
            text = text.replace(f"{{{key}}}", value)
        elif isinstance(value, list):
            text = text.replace(f"{{{key}}}", ", ".join(str(v) for v in value))
        elif isinstance(value, (int, float, bool)):
            text = text.replace(f"{{{key}}}", str(value))
    return text


def render_constraint(constraint_config: dict, library: dict, intensity: int = 3) -> str:
    """Render a single constraint into a prompt fragment."""
    c_type = constraint_config.get("type", "")

    try:
        lib_constraint = get_constraint(library, c_type)
    except ValueError:
        return ""

    intensity = max(1, min(5, intensity))
    template = lib_constraint.get("prompt_template", "")
    intensity_key = str(intensity)
    intensity_levels = lib_constraint.get("intensity_levels", {})
    intensity_text = intensity_levels.get(intensity_key, intensity_levels.get("3", ""))

    # Build the rendered text: intensity text + full template for context
    # Both get variable substitution to ensure all placeholders are filled
    rendered = _substitute_variables(intensity_text, constraint_config) if intensity_text else ""
    template_rendered = _substitute_variables(template, constraint_config)

    # If intensity text doesn't contain the key details from the template,
    # append the template (with substitutions) for full context
    if rendered and template_rendered and rendered != template_rendered:
        # Check if rendered is missing key information from the config
        has_all_values = True
        for key, value in constraint_config.items():
            if key == "type":
                continue
            if isinstance(value, str) and len(value) > 3 and value not in rendered:
                has_all_values = False
                break
        if not has_all_values:
            rendered = f"{template_rendered} {rendered}"
    elif not rendered:
        rendered = template_rendered

    # Append special sub-type details
    appendices = []

    if c_type == "scamper" and "operation" in constraint_config:
        ops = lib_constraint.get("scamper_operations", {})
        op = constraint_config["operation"]
        if op in ops:
            appendices.append(f"Operation: {ops[op]}")

    if c_type == "elm_route" and "route" in constraint_config:
        routes = lib_constraint.get("elm_routes", {})
        route = constraint_config["route"]
        if route in routes:
            appendices.append(routes[route])

    if c_type == "concept_fan" and "level" in constraint_config:
        levels = lib_constraint.get("abstraction_levels", {})
        level = constraint_config["level"]
        if level in levels:
            appendices.append(levels[level])

    if c_type == "wise_mind" and "mind_type" in constraint_config:
        types = lib_constraint.get("mind_types", {})
        mind = constraint_config["mind_type"]
        if mind in types:
            appendices.append(types[mind])

    if appendices:
        rendered += " " + " ".join(appendices)

    return rendered


def compose_prompt(
    constraints: list[dict],
    topic: str,
    output_format: str = "perspective_card",
    intensity: int = 3,
    extra_instructions: Optional[str] = None,
) -> dict:
    """Compose a complete structured prompt from constraints + topic.

    Returns dict with 'system_prompt', 'warnings', and 'metadata'.
    """
    intensity = max(1, min(5, intensity))
    library = load_library()

    # Check compatibility
    warnings = check_compatibility(constraints, library)

    # Flag unknown constraint types so they don't get silently dropped
    valid_ids = {c["id"] for c in library.get("constraints", [])}
    for c in constraints:
        c_type = c.get("type", c.get("id", ""))
        if c_type and c_type not in valid_ids:
            warnings.append(f"Constraint '{c_type}' is unknown: ignored (not present in the library)")

    # Render each constraint
    rendered_constraints = []
    for i, c in enumerate(constraints, 1):
        rendered = render_constraint(c, library, intensity)
        if rendered:
            rendered_constraints.append(f"{i}. {rendered}")

    # Build system prompt
    parts = [
        "You are an analyst bound by the following cognitive rules.",
        "These rules are NOT suggestions: they are RIGID constraints that define how you think.",
        "Respond in the same language as the Topic below.",
        "",
    ]

    if rendered_constraints:
        parts.append("## Active constraints")
        parts.append("")
        parts.extend(rendered_constraints)
        parts.append("")

    if extra_instructions:
        parts.append("## Additional instructions")
        parts.append(extra_instructions)
        parts.append("")

    # Add output schema
    schema = OUTPUT_SCHEMAS.get(output_format, OUTPUT_SCHEMAS["raw"])
    if schema:
        parts.append(schema)

    parts.append("## Topic")
    parts.append("")
    parts.append(topic)

    system_prompt = "\n".join(parts)

    return {
        "system_prompt": system_prompt,
        "warnings": warnings,
        "metadata": {
            "constraints_count": len(constraints),
            "constraint_types": [c.get("type", "unknown") for c in constraints],
            "intensity": intensity,
            "output_format": output_format,
        },
    }


def compose_persona_prompt(
    persona_id: str,
    topic: str,
    output_format: str = "perspective_card",
    intensity: int = 3,
) -> dict:
    """Compose a prompt from a persona template."""
    intensity = max(1, min(5, intensity))
    persona = load_persona(persona_id)

    constraints = persona["constraints"]
    psychology = persona.get("psychology", {})

    extra = []
    if psychology:
        extra.append(f"Your primary goal: {psychology.get('primary_goal', '')}")
        fears = psychology.get("fears", [])
        if fears:
            extra.append(f"Your fears: {', '.join(fears)}")
        style = psychology.get("decision_style", "")
        if style:
            extra.append(f"Your decision style: {style}")
        threshold = psychology.get("convincement_threshold", "")
        if threshold:
            extra.append(f"To convince you requires: {threshold}")

    result = compose_prompt(
        constraints=constraints,
        topic=topic,
        output_format=output_format,
        intensity=intensity,
        extra_instructions="\n".join(extra) if extra else None,
    )

    result["metadata"]["persona_id"] = persona_id
    result["metadata"]["persona_name"] = persona["name"]

    return result


def suggest_constraints(
    topic: str, goal: str, max_constraints: int = 4
) -> list[dict]:
    """Suggest optimal constraints for a topic+goal.

    Simple heuristic-based suggestion. Meta-Lens (Phase 3) will replace this
    with data-driven suggestions.
    """
    library = load_library()
    suggestions = []

    goal_lower = goal.lower()

    # Heuristic mapping. Keyword lists are bilingual (EN + IT) so the goal can be
    # expressed in either language.
    if any(w in goal_lower for w in ["stress", "attack", "verify", "test", "stressare", "attaccare", "verificare", "testare"]):
        suggestions.extend([
            {"type": "inversion", "_reason": "Attack the position to find weaknesses"},
            {"type": "abductive", "_reason": "Look for non-obvious explanations"},
        ])

    if any(w in goal_lower for w in ["creativ", "innovat", "idea", "new", "innova", "ide", "nuov"]):
        suggestions.extend([
            {"type": "bisociative", "domain_forced": "[domain to specify]", "_reason": "Collision between incompatible frames"},
            {"type": "provocation", "po_statement": "[provocation to specify]", "_reason": "An impossible starting point"},
            {"type": "defamiliarize", "perspective": "an alien anthropologist", "_reason": "Break familiarity"},
        ])

    if any(w in goal_lower for w in ["risk", "premortem", "failure", "danger", "rischio", "fallimento", "pericol"]):
        suggestions.extend([
            {"type": "premortem", "date": "2028", "_reason": "Analysis from a future where it failed"},
            {"type": "modal", "mode": "only risks, no benefits", "_reason": "Exclusive focus on the downside"},
        ])

    if any(w in goal_lower for w in ["assumption", "hidden", "blind", "assunzion", "nascost"]):
        suggestions.extend([
            {"type": "assumption_reversal", "assumption": "[to specify]", "reversed": "[to specify]", "_reason": "Invert the foundational assumptions"},
            {"type": "concept_fan", "level": "purpose", "_reason": "Dig down to the fundamental need"},
        ])

    if any(w in goal_lower for w in ["decision", "choice", "dilemma", "balance", "scelt", "equilibr"]):
        suggestions.extend([
            {"type": "wise_mind", "mind_type": "wise", "_reason": "Integrate emotion and reason"},
            {"type": "janusian", "thesis": "[to specify]", "antithesis": "[to specify]", "_reason": "Transcend the contradiction"},
        ])

    if any(w in goal_lower for w in ["argument", "convince", "robust", "strong", "argoment", "convinc", "forte"]):
        suggestions.extend([
            {"type": "steelman", "_reason": "Build the strongest version"},
            {"type": "elm_route", "route": "central", "focus": "logic and evidence", "_reason": "Rigorous central-route analysis"},
        ])

    # Fallback: always useful constraints
    if not suggestions:
        suggestions = [
            {"type": "inversion", "_reason": "The opposite perspective as a useful default"},
            {"type": "defamiliarize", "perspective": "an observer outside the industry", "_reason": "Fresh eyes"},
            {"type": "limit", "constraint": "at most 3 arguments, each with one concrete data point", "_reason": "Force concreteness"},
        ]

    return suggestions[:max_constraints]


def compose_sequential_prompt(
    constraints: list[dict],
    topic: str,
    output_format: str = "chain_output",
    intensity: int = 3,
    insert_anchor_break: bool = True,
    anchor_break_after: list[int] | None = None,
) -> dict:
    """Compose a sequence of prompts for sequential chain topology.

    Each prompt is designed to be used in order. Round N receives the output
    of all previous rounds as context, plus a new constraint.

    Args:
        constraints: Ordered list of constraints (order matters for chain).
        topic: The topic to analyze.
        output_format: Output schema for the final round.
        intensity: Constraint intensity 1-5.
        insert_anchor_break: Whether to insert anchor_break between rounds.
        anchor_break_after: After which round numbers (1-indexed) to insert anchor_break.
                           Default: after round 1.
    """
    intensity = max(1, min(5, intensity))
    library = load_library()

    if anchor_break_after is None:
        anchor_break_after = [1]

    # Build the full constraint sequence, inserting anchor_breaks
    full_sequence = []
    for i, c in enumerate(constraints):
        full_sequence.append(c)
        round_num = i + 1
        if insert_anchor_break and round_num in anchor_break_after:
            full_sequence.append({"type": "anchor_break"})

    # Check compatibility across all constraints
    warnings = check_compatibility(full_sequence, library)

    # Generate prompts for each round
    prompts = []
    for i, c in enumerate(full_sequence):
        round_num = i + 1
        is_last = i == len(full_sequence) - 1
        c_type = c.get("type", "unknown")

        # Render the constraint
        rendered = render_constraint(c, library, intensity)
        if not rendered:
            continue

        # Build system prompt parts
        parts = [
            "You are an analyst in a sequential deepening process.",
            f"This is round {round_num} of {len(full_sequence)}.",
            "Respond in the same language as the Topic below.",
            "",
        ]

        # Context instruction for rounds after the first
        context_instruction = None
        if round_num == 1:
            parts.append("## Active constraint")
            parts.append("")
            parts.append(f"1. {rendered}")
            parts.append("")
        else:
            context_instruction = (
                "## Context: output of previous rounds\n\n"
                "{previous_output}\n\n"
                "## New constraint for this round\n\n"
                f"1. {rendered}\n\n"
                "## Instruction\n\n"
                "Integrate the previous context with the new constraint. "
                "Do not repeat what has already been said. "
                "Add, contradict, deepen, or transcend."
            )
            parts.append("## Active constraint")
            parts.append("")
            parts.append(f"1. {rendered}")
            parts.append("")
            parts.append("NOTE: you will receive the output of previous rounds as context. "
                        "Integrate it with the active constraint.")
            parts.append("")

        # Output schema only for the last round
        round_format = output_format if is_last else "raw"
        schema = OUTPUT_SCHEMAS.get(round_format, OUTPUT_SCHEMAS["raw"])
        if schema:
            parts.append(schema)

        parts.append("## Topic")
        parts.append("")
        parts.append(topic)

        prompts.append({
            "round": round_num,
            "constraint_type": c_type,
            "system_prompt": "\n".join(parts),
            "context_instruction": context_instruction,
            "output_format": round_format,
        })

    return {
        "prompts": prompts,
        "total_rounds": len(prompts),
        "warnings": warnings,
        "metadata": {
            "constraint_sequence": [c.get("type", "unknown") for c in full_sequence],
            "anchor_breaks_at": anchor_break_after if insert_anchor_break else [],
            "intensity": intensity,
            "output_format": output_format,
            "topic": topic,
        },
    }


def compose_baseline_prompt(
    topic: str,
    output_format: str = "perspective_card",
) -> dict:
    """Compose a clean unconstrained prompt for the same topic.

    Used in baseline+delta workflow: run this first for the standard analysis,
    then run compose_prompt with constraints for the delta.
    """
    schema = OUTPUT_SCHEMAS.get(output_format, OUTPUT_SCHEMAS["raw"])

    parts = [
        "Analyze the following topic with a thorough, structured analysis.",
        "Respond in the same language as the Topic below.",
        "",
    ]

    if schema:
        parts.append(schema)

    parts.append("## Topic")
    parts.append("")
    parts.append(topic)

    return {
        "system_prompt": "\n".join(parts),
        "metadata": {
            "type": "baseline",
            "output_format": output_format,
        },
    }

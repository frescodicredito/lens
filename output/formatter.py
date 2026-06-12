"""Lens Output Formatter — structures agent outputs into standardized formats."""

from datetime import datetime
from typing import Optional


def format_perspective_card(
    agent_output: str,
    constraint_types: list[str],
    persona_name: Optional[str] = None,
    topic: str = "",
) -> str:
    """Format a single agent's output as a Perspective Card.

    If the agent already followed the Perspective Card schema, this wraps it
    with metadata. If not, it adds structure.
    """
    header = "# Perspective Card"
    if persona_name:
        header += f" — {persona_name}"

    meta_parts = []
    if constraint_types:
        meta_parts.append(f"Constraints: {', '.join(constraint_types)}")
    if topic:
        meta_parts.append(f"Topic: {topic}")
    meta_parts.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    meta = " | ".join(meta_parts)

    return f"{header}\n\n> {meta}\n\n{agent_output}"


def format_field_map(
    agent_outputs: list[dict],
    topic: str = "",
    synthesis: Optional[str] = None,
) -> str:
    """Format multiple agent outputs as a Field Map.

    agent_outputs: list of {"agent_id": str, "output": str, "constraints": list, "persona": str|None}
    """
    parts = ["# Field Map"]
    if topic:
        parts.append(f"\n> Topic: {topic}")
    parts.append(f"> Agents: {len(agent_outputs)}")
    parts.append(f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    parts.append("")

    # Individual perspectives
    parts.append("---")
    parts.append("")
    parts.append("## Individual perspectives")
    parts.append("")

    for i, agent in enumerate(agent_outputs, 1):
        label = agent.get("persona") or f"Agent {i}"
        constraints_str = ", ".join(agent.get("constraints", []))
        parts.append(f"### {label}")
        if constraints_str:
            parts.append(f"> Constraints: {constraints_str}")
        parts.append("")
        parts.append(agent["output"])
        parts.append("")

    # Synthesis
    if synthesis:
        parts.append("---")
        parts.append("")
        parts.append("## Synthesis")
        parts.append("")
        parts.append(synthesis)

    return "\n".join(parts)


def format_delta_report(
    baseline_output: str,
    lens_output: str,
    constraint_types: list[str],
    topic: str = "",
) -> str:
    """Format a comparison between baseline and Lens output."""
    parts = [
        "# Delta Report",
        "",
        f"> Topic: {topic}" if topic else "",
        f"> Constraints applied: {', '.join(constraint_types)}",
        f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        "## Baseline (unconstrained)",
        "",
        baseline_output,
        "",
        "---",
        "",
        "## Lens output (constrained)",
        "",
        lens_output,
        "",
        "---",
        "",
        "## Delta Analysis",
        "",
        "### Insights present ONLY in the Lens output",
        "[To be filled in during evaluation]",
        "",
        "### Insights present in both",
        "[To be filled in during evaluation]",
        "",
        "### Insights present ONLY in the baseline",
        "[To be filled in during evaluation]",
        "",
        "### Evaluation",
        "- Unique Lens insights: [count]",
        "- Blind preference: [baseline / lens]",
        "- Added value: [high / medium / low]",
    ]

    return "\n".join(parts)


def format_cascade_output(
    rounds: list[dict],
    topic: str = "",
    surviving_core: Optional[str] = None,
) -> str:
    """Format cascade/adversarial output showing progression through rounds.

    rounds: list of {"round": int, "role": str, "agent_output": str, "constraints": list}
    """
    parts = [
        "# Cascade Report",
        "",
    ]
    if topic:
        parts.append(f"> Topic: {topic}")
    parts.append(f"> Round: {len(rounds)}")
    parts.append(f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    parts.append("")

    for r in rounds:
        round_num = r.get("round", "?")
        role = r.get("role", "agent")
        constraints_str = ", ".join(r.get("constraints", []))

        parts.append("---")
        parts.append("")
        parts.append(f"## Round {round_num} — {role}")
        if constraints_str:
            parts.append(f"> Constraints: {constraints_str}")
        parts.append("")
        parts.append(r["agent_output"])
        parts.append("")

    if surviving_core:
        parts.append("---")
        parts.append("")
        parts.append("## Surviving core")
        parts.append("")
        parts.append(surviving_core)

    return "\n".join(parts)


def format_chain_output(
    rounds: list[dict],
    topic: str = "",
    final_position: Optional[str] = None,
) -> str:
    """Format sequential chain output showing the evolution of thinking.

    rounds: list of {"round": int, "constraint": str, "output": str}
    """
    parts = [
        "# Sequential Chain Report",
        "",
    ]
    if topic:
        parts.append(f"> Topic: {topic}")

    constraint_names = [r.get("constraint", "?") for r in rounds]
    parts.append(f"> Round: {len(rounds)} | Constraints: {', '.join(constraint_names)}")
    parts.append(f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    parts.append("")

    for r in rounds:
        round_num = r.get("round", "?")
        constraint = r.get("constraint", "?")

        parts.append("---")
        parts.append("")
        parts.append(f"## Round {round_num} — {constraint}")
        parts.append("")
        parts.append(r["output"])
        parts.append("")

    if final_position:
        parts.append("---")
        parts.append("")
        parts.append("## Final position")
        parts.append("")
        parts.append(final_position)

    return "\n".join(parts)


def format_executive_extract(
    full_output: str,
    topic: str = "",
) -> str:
    """Create an executive extract wrapper around Lens output."""
    parts = [
        "---",
        "",
        "## Executive Extract",
        "",
        f"> From: Lens analysis of \"{topic}\"",
        "",
        full_output,
    ]
    return "\n".join(parts)


def format_decision_brief(
    recommendation: str,
    confidence: str,
    arguments_for: list[str],
    risks: list[str],
    verifications: list[str],
    topic: str = "",
) -> str:
    """Format a structured decision brief."""
    parts = [
        "# Decision Brief",
        "",
    ]
    if topic:
        parts.append(f"> Topic: {topic}")
    parts.append(f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    parts.append("")
    parts.append("## Recommendation")
    parts.append("")
    parts.append(recommendation)
    parts.append("")
    parts.append(f"## Confidence: {confidence}")
    parts.append("")
    parts.append("## Arguments in favor")
    parts.append("")
    for i, arg in enumerate(arguments_for, 1):
        parts.append(f"{i}. {arg}")
    parts.append("")
    parts.append("## Risks")
    parts.append("")
    for i, risk in enumerate(risks, 1):
        parts.append(f"{i}. {risk}")
    parts.append("")
    parts.append("## What to verify before proceeding")
    parts.append("")
    for i, v in enumerate(verifications, 1):
        parts.append(f"{i}. {v}")

    return "\n".join(parts)


def format_session_summary(
    session_id: str,
    topology: str,
    topic: str,
    agents_count: int,
    rounds_count: int,
    output: str,
    constraints_used: Optional[list[str]] = None,
    constraint_sequence: Optional[list[str]] = None,
    efficacy: Optional[dict] = None,
) -> dict:
    """Create a session summary for storage."""
    default_efficacy = {
        "rated": False,
        "useful": None,
        "surprising": None,
        "unique_insights": None,
        "implemented": None,
        "implementation_note": None,
        "delta_unique_insights": None,
    }
    if efficacy:
        default_efficacy.update(efficacy)

    result = {
        "session_id": session_id,
        "timestamp": datetime.now().isoformat(),
        "topology": topology,
        "topic": topic,
        "agents_count": agents_count,
        "rounds_count": rounds_count,
        "constraints_used": constraints_used or [],
        "output_preview": output[:500] if len(output) > 500 else output,
        "output_full": output,
        "efficacy": default_efficacy,
    }
    if constraint_sequence:
        result["constraint_sequence"] = constraint_sequence

    return result

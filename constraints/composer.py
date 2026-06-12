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

Struttura la tua risposta ESATTAMENTE in questo formato:

### CLAIM
[La tua posizione principale in 1-2 frasi]

### SUPPORTO
[3-5 evidenze, ragionamenti o dati che supportano il claim]

### BLIND SPOT
[1-3 aspetti che questa prospettiva potrebbe non vedere o sottovalutare]

### CONFIDENZA
[Alta/Media/Bassa] — [1 frase che spiega perche']
""",
    "field_map": """
## Output Format: Field Map

Struttura la tua risposta ESATTAMENTE in questo formato:

### CONVERGENZE
[Punti su cui le diverse prospettive concordano]

### DIVERGENZE
[Punti di disaccordo sostanziale, con le posizioni di ciascuna prospettiva]

### OUTLIER
[Insight sorprendenti o inaspettati emersi dall'analisi]

### SINTESI
[Integrazione che onora le divergenze senza forzare consenso artificiale]
""",
    "delta_report": """
## Output Format: Delta Report

Struttura la tua risposta ESATTAMENTE in questo formato:

### BASELINE
[Cosa direbbe un'analisi standard senza vincoli]

### DELTA
[Cosa emerge di DIVERSO grazie ai vincoli applicati]

### INSIGHT UNICI
[Intuizioni che NON sarebbero emerse senza i vincoli strutturali]

### VALORE AGGIUNTO
[Perche' questi insight sono rilevanti per la decisione]
""",
    "chain_output": """
## Output Format: Chain Output

Struttura la tua risposta ESATTAMENTE in questo formato:

### POSIZIONE ATTUALE
[La tua posizione dopo aver integrato tutti i round precedenti. 2-3 frasi.]

### EVOLUZIONE
[Come la tua posizione e' cambiata rispetto ai round precedenti. Cosa hai aggiunto, modificato, abbandonato?]

### TENSIONI IRRISOLTE
[Contraddizioni o tensioni che rimangono aperte. Non forzare una risoluzione artificiale.]

### CONFIDENZA CALIBRATA
[Alta/Media/Bassa] — [Cosa ti renderebbe piu'/meno sicuro]
""",
    "decision_brief": """
## Output Format: Decision Brief

Struttura la tua risposta ESATTAMENTE in questo formato:

### RACCOMANDAZIONE
[Azione specifica e concreta raccomandata, in 1-2 frasi]

### CONFIDENZA
[Alta/Media/Bassa] — [Motivazione in 1 frase]

### ARGOMENTI A FAVORE
1. [Argomento piu' forte]
2. [Secondo argomento]
3. [Terzo argomento]

### RISCHI
1. [Rischio piu' significativo]
2. [Secondo rischio]
3. [Terzo rischio]

### COSA VERIFICARE PRIMA DI PROCEDERE
1. [Test o verifica concreta #1]
2. [Test o verifica concreta #2]
""",
    "executive_extract": """
## Output Format: Executive Extract

Struttura la tua risposta in MASSIMO 5 bullet point:
- Ogni bullet e' actionable (chi fa cosa quando)
- Nessun background o contesto — solo azioni
- Se c'e' una decisione da prendere, indicala esplicitamente
- Se c'e' un rischio critico, indicalo esplicitamente
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
                    f"Vincolo '{c_id}' e' incompatibile con '{other_id}'"
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
            appendices.append(f"Operazione: {ops[op]}")

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
            warnings.append(f"Vincolo '{c_type}' sconosciuto: ignorato (non presente nella libreria)")

    # Render each constraint
    rendered_constraints = []
    for i, c in enumerate(constraints, 1):
        rendered = render_constraint(c, library, intensity)
        if rendered:
            rendered_constraints.append(f"{i}. {rendered}")

    # Build system prompt
    parts = [
        "Sei un analista vincolato dalle seguenti regole cognitive.",
        "Queste regole NON sono suggerimenti: sono vincoli RIGIDI che definiscono come pensi.",
        "",
    ]

    if rendered_constraints:
        parts.append("## Vincoli attivi")
        parts.append("")
        parts.extend(rendered_constraints)
        parts.append("")

    if extra_instructions:
        parts.append("## Istruzioni aggiuntive")
        parts.append(extra_instructions)
        parts.append("")

    # Add output schema
    schema = OUTPUT_SCHEMAS.get(output_format, OUTPUT_SCHEMAS["raw"])
    if schema:
        parts.append(schema)

    parts.append(f"## Topic")
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
        extra.append(f"Il tuo obiettivo primario: {psychology.get('primary_goal', '')}")
        fears = psychology.get("fears", [])
        if fears:
            extra.append(f"Le tue paure: {', '.join(fears)}")
        style = psychology.get("decision_style", "")
        if style:
            extra.append(f"Il tuo stile decisionale: {style}")
        threshold = psychology.get("convincement_threshold", "")
        if threshold:
            extra.append(f"Per convincerti serve: {threshold}")

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

    # Heuristic mapping
    if any(w in goal_lower for w in ["stressare", "attaccare", "verificare", "testare"]):
        suggestions.extend([
            {"type": "inversion", "_reason": "Attacca la posizione per trovare debolezze"},
            {"type": "abductive", "_reason": "Cerca spiegazioni non ovvie"},
        ])

    if any(w in goal_lower for w in ["creativ", "innova", "ide", "nuov"]):
        suggestions.extend([
            {"type": "bisociative", "domain_forced": "[dominio da specificare]", "_reason": "Collisione tra frame incompatibili"},
            {"type": "provocation", "po_statement": "[provocazione da specificare]", "_reason": "Punto di partenza impossibile"},
            {"type": "defamiliarize", "perspective": "un antropologo alieno", "_reason": "Rompi la familiarita'"},
        ])

    if any(w in goal_lower for w in ["rischio", "premortem", "fallimento", "pericol"]):
        suggestions.extend([
            {"type": "premortem", "date": "2028", "_reason": "Analisi dal futuro del fallimento"},
            {"type": "modal", "mode": "solo rischi, nessun beneficio", "_reason": "Focus esclusivo su downside"},
        ])

    if any(w in goal_lower for w in ["assunzion", "assumption", "nascost", "blind"]):
        suggestions.extend([
            {"type": "assumption_reversal", "assumption": "[da specificare]", "reversed": "[da specificare]", "_reason": "Inverti le assunzioni fondamentali"},
            {"type": "concept_fan", "level": "purpose", "_reason": "Scava fino al bisogno fondamentale"},
        ])

    if any(w in goal_lower for w in ["decision", "scelt", "dilemma", "equilibr"]):
        suggestions.extend([
            {"type": "wise_mind", "mind_type": "wise", "_reason": "Integra emozione e ragione"},
            {"type": "janusian", "thesis": "[da specificare]", "antithesis": "[da specificare]", "_reason": "Trascendi la contraddizione"},
        ])

    if any(w in goal_lower for w in ["argoment", "convinc", "robust", "forte"]):
        suggestions.extend([
            {"type": "steelman", "_reason": "Costruisci la versione piu' forte"},
            {"type": "elm_route", "route": "central", "focus": "logica e evidenze", "_reason": "Analisi centrale rigorosa"},
        ])

    # Fallback: always useful constraints
    if not suggestions:
        suggestions = [
            {"type": "inversion", "_reason": "Prospettiva opposta come default utile"},
            {"type": "defamiliarize", "perspective": "un osservatore esterno al settore", "_reason": "Occhi freschi"},
            {"type": "limit", "constraint": "massimo 3 argomenti, ognuno con un dato concreto", "_reason": "Forza concretezza"},
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
            "Sei un analista in un processo di approfondimento sequenziale.",
            f"Questo e' il round {round_num} di {len(full_sequence)}.",
            "",
        ]

        # Context instruction for rounds after the first
        context_instruction = None
        if round_num == 1:
            parts.append("## Vincolo attivo")
            parts.append("")
            parts.append(f"1. {rendered}")
            parts.append("")
        else:
            context_instruction = (
                "## Contesto: output dei round precedenti\n\n"
                "{previous_output}\n\n"
                "## Nuovo vincolo per questo round\n\n"
                f"1. {rendered}\n\n"
                "## Istruzione\n\n"
                "Integra il contesto precedente con il nuovo vincolo. "
                "Non ripetere cio' che e' gia' stato detto. "
                "Aggiungi, contraddici, approfondisci o trascendi."
            )
            parts.append("## Vincolo attivo")
            parts.append("")
            parts.append(f"1. {rendered}")
            parts.append("")
            parts.append("NOTA: riceverai l'output dei round precedenti come contesto. "
                        "Integralo con il vincolo attivo.")
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
        "Analizza il seguente topic con un'analisi approfondita e strutturata.",
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

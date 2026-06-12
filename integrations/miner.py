"""Miner Integration — transforms Miner audience personas into Lens persona templates.

Miner's audience-profiler produces structured personas from real social media data.
This module converts those data-grounded personas into Lens constraint bundles,
creating cognitive templates backed by empirical audience research rather than
LLM-generated profiles.

Flow:
  Miner collect → Miner analyze(audience) → AudiencePersona JSON
  → lens_persona_from_miner() → Lens persona template JSON
  → lens_compose_persona() → structured prompt for subagent
"""

import json
import re
from pathlib import Path

PERSONAS_DIR = Path(__file__).parent.parent / "personas" / "templates"


def transform_miner_persona(miner_persona: dict) -> dict:
    """Transform a Miner AudiencePersona into a Lens persona template.

    Mapping strategy:
    - demographics + occupation → role constraint (who they are)
    - psychographics.values + attitudes → modal constraint (how they think)
    - psychographics.vals_segment → elm_route (processing style)
    - pain_points → psychology.fears
    - goals → psychology.primary_goal
    - decision_making_style → psychology.decision_style + convincement_threshold
    - behaviors.interaction_style → exclusion constraint (vocabulary they avoid)

    Args:
        miner_persona: Dict matching Miner's AudiencePersona schema. Fields are
            read defensively, so a partial or loosely-typed dict will not crash.

    Returns:
        Dict matching Lens persona template format (ready to save or use directly).
    """
    name = str(miner_persona.get("name") or "Persona Miner")
    tagline = miner_persona.get("tagline", "")

    demographics = miner_persona.get("demographics", {})
    psychographics = miner_persona.get("psychographics", {})
    interests = miner_persona.get("interests", {})
    behaviors = miner_persona.get("behaviors", {})
    pain_points = miner_persona.get("pain_points", [])
    goals = miner_persona.get("goals", [])

    # --- Build constraints ---
    constraints = []

    # 1. Role constraint from demographics + tagline
    role_parts = []
    if tagline:
        role_parts.append(tagline)
    age = demographics.get("age_range", "")
    if age:
        role_parts.append(f"{age} anni")
    occupations = demographics.get("occupation_indicators", [])
    if occupations:
        role_parts.append(", ".join(occupations[:3]))
    location = demographics.get("location_indicators", [])
    if location:
        role_parts.append(f"zona {', '.join(location[:2])}")

    # Bias from psychographics
    bias_parts = []
    values = psychographics.get("values", [])
    if values:
        bias_parts.append(f"valori: {', '.join(values[:4])}")
    vals_segment = psychographics.get("vals_segment", "")
    if vals_segment:
        bias_parts.append(f"segmento VALS: {vals_segment}")
    motivation = psychographics.get("primary_motivation", "unknown")
    if motivation != "unknown":
        bias_parts.append(f"motivazione: {motivation}")

    constraints.append({
        "type": "role",
        "role": ". ".join(role_parts) if role_parts else name,
        "bias": ". ".join(bias_parts) if bias_parts else "profilo derivato da dati reali",
    })

    # 2. Modal constraint from attitudes and lifestyle
    attitudes = psychographics.get("attitudes", {})
    lifestyle = psychographics.get("lifestyle_indicators", [])
    modal_parts = []
    if attitudes:
        # Use top 2-3 attitudes as modal lens
        for topic_key, attitude in list(attitudes.items())[:3]:
            modal_parts.append(f"{topic_key}: {attitude}")
    if lifestyle:
        modal_parts.append(f"stile di vita: {', '.join(lifestyle[:3])}")

    if modal_parts:
        constraints.append({
            "type": "modal",
            "mode": "; ".join(modal_parts),
        })

    # 3. ELM route from VALS + decision making style
    decision_style = str(behaviors.get("decision_making_style") or "")
    resource_level = psychographics.get("resource_level", "unknown")

    if decision_style or resource_level != "unknown":
        # High resources + researched → central route
        # Low resources + impulsive → peripheral route
        if any(w in decision_style.lower() for w in ["research", "analiz", "dati", "evidenz"]):
            route = "central"
            focus = "dati, evidenze, ROI, casi studio"
        elif any(w in decision_style.lower() for w in ["impuls", "emozion", "intuit", "veloc"]):
            route = "peripheral"
            focus = "testimonianze, brand appeal, social proof, semplicita'"
        elif resource_level == "high":
            route = "central"
            focus = "qualita' delle argomentazioni e delle evidenze"
        else:
            route = "peripheral"
            focus = "credibilita' della fonte e appeal emotivo"

        constraints.append({
            "type": "elm_route",
            "route": route,
            "focus": focus,
        })

    # 4. Exclusion constraint from what they DON'T engage with
    # (infer from interaction style and interests)
    interaction_style = str(behaviors.get("interaction_style") or "")
    if interaction_style:
        exclusion_words = []
        if "like" in interaction_style.lower() and "comment" not in interaction_style.lower():
            # Passive engager → exclude jargon, complexity
            exclusion_words.extend(["paradigm shift", "disruptive", "leverage"])
        if any(w in interaction_style.lower() for w in ["share", "condivid"]):
            # Active sharer → they want shareable language
            pass  # No exclusion needed
        if exclusion_words:
            constraints.append({
                "type": "exclusion",
                "words": exclusion_words,
            })

    # --- Build psychology ---
    psychology = {}

    if goals:
        psychology["primary_goal"] = goals[0]

    if pain_points:
        psychology["fears"] = pain_points[:5]

    if decision_style:
        psychology["decision_style"] = decision_style

    # Convincement threshold from VALS + behavior
    threshold_parts = []
    if vals_segment:
        vals_thresholds = {
            "Innovators": "novita' e visione, non necessita di social proof",
            "Thinkers": "evidenze solide, analisi approfondita, referenze accademiche",
            "Believers": "tradizione, affidabilita', referenze di fiducia",
            "Achievers": "status, risultati dimostrabili, successo degli altri",
            "Strivers": "aspirazione, accessibilita' economica, appartenenza",
            "Makers": "praticita', funzionalita', rapporto qualita'-prezzo",
            "Experiencers": "esperienza diretta, coinvolgimento, novita'",
            "Survivors": "necessita' immediata, sicurezza, prezzo",
        }
        threshold = vals_thresholds.get(vals_segment, "")
        if threshold:
            threshold_parts.append(threshold)

    if threshold_parts:
        psychology["convincement_threshold"] = ". ".join(threshold_parts)

    # --- Build persona ID ---
    # Sanitize name for ID
    slug = name.lower().replace(" ", "-")
    for char in "àèìòù":
        slug = slug.replace(char, char[0])
    # Keep only safe characters so the id can never escape the templates dir.
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    slug = re.sub(r"-+", "-", slug).strip("-") or "persona"
    persona_id = "miner-" + slug

    # --- Build description ---
    desc_parts = [tagline] if tagline else [name]
    if age:
        desc_parts.append(f"eta' {age}")
    if occupations:
        desc_parts.append(", ".join(occupations[:2]))
    confidence = miner_persona.get("confidence_score", 0)
    segment_size = miner_persona.get("segment_size_estimate", 0)
    if isinstance(segment_size, (int, float)) and segment_size > 0:
        desc_parts.append(f"~{int(segment_size * 100)}% dell'audience")

    # --- Assemble template ---
    template = {
        "id": persona_id,
        "name": name,
        "description": ". ".join(desc_parts),
        "source": "miner",
        "source_confidence": confidence,
        "constraints": constraints,
        "psychology": psychology,
    }

    # Add raw Miner data as metadata for reference
    template["miner_data"] = {
        "demographics": demographics,
        "psychographics": psychographics,
        "interests": {
            "primary": interests.get("primary_interests", [])[:5],
            "topics_of_engagement": interests.get("topics_of_engagement", [])[:5],
        },
        "behaviors": {
            "interaction_style": interaction_style,
            "decision_making_style": decision_style,
        },
    }

    return template


def save_miner_persona(persona_template: dict) -> Path:
    """Save a Miner-derived persona template to disk.

    Args:
        persona_template: Output of transform_miner_persona().

    Returns:
        Path to the saved file.
    """
    PERSONAS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = PERSONAS_DIR / f"{persona_template['id']}.json"
    # Defense in depth: never write outside the templates directory.
    if filepath.resolve().parent != PERSONAS_DIR.resolve():
        raise ValueError("Invalid persona id")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(persona_template, f, ensure_ascii=False, indent=2)
    return filepath


def transform_all_personas(
    miner_output: dict,
    save: bool = True,
) -> list[dict]:
    """Transform all personas from a Miner AudienceProfilerOutput.

    Args:
        miner_output: Dict matching Miner's AudienceProfilerOutput schema.
        save: Whether to save each persona to disk (default True).

    Returns:
        List of Lens persona templates.
    """
    personas = miner_output.get("personas", [])
    results = []

    for persona in personas:
        template = transform_miner_persona(persona)
        if save:
            save_miner_persona(template)
        results.append(template)

    return results

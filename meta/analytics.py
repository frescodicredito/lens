"""Meta-Lens Analytics — learns from session history to improve constraint selection.

Provides:
- Constraint efficacy tracking (which constraints produce useful/surprising sessions)
- Topology efficacy tracking
- Pattern mining (which constraint combinations work well together)
- Sequence efficacy (which constraint orderings work best)
- Smart defaults (auto-configuration based on topic/goal)
- Implementation rate (non-circular metric: was the insight actually used?)
- ROI estimation
- Data-driven constraint suggestions based on session history
"""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Optional

SESSIONS_DIR = Path(__file__).parent.parent / "sessions"


def _load_sessions() -> list[dict]:
    """Load all session files, skipping any that are corrupt or unreadable."""
    sessions = []
    for f in sorted(SESSIONS_DIR.glob("*.json"), reverse=True):
        try:
            with open(f, encoding="utf-8") as fp:
                sessions.append(json.load(fp))
        except (json.JSONDecodeError, OSError):
            # A single malformed session file must not break all analytics.
            continue
    return sessions


def constraint_efficacy() -> dict:
    """Analyze which constraints produce the most useful and surprising sessions.

    Returns efficacy stats per constraint type, sorted by effectiveness score.
    Score = (useful_rate * 0.6) + (surprising_rate * 0.4)
    """
    sessions = _load_sessions()

    if not sessions:
        return {"message": "Nessuna sessione disponibile.", "constraints": []}

    constraint_stats: dict[str, dict] = defaultdict(
        lambda: {"total": 0, "rated": 0, "useful": 0, "surprising": 0}
    )

    for session in sessions:
        constraints = session.get("constraints_used", [])
        efficacy = session.get("efficacy", {})
        is_rated = efficacy.get("rated", False)

        for c in constraints:
            constraint_stats[c]["total"] += 1
            if is_rated:
                constraint_stats[c]["rated"] += 1
                if efficacy.get("useful"):
                    constraint_stats[c]["useful"] += 1
                if efficacy.get("surprising"):
                    constraint_stats[c]["surprising"] += 1

    # Calculate effectiveness score
    results = []
    for c_id, stats in constraint_stats.items():
        if stats["rated"] > 0:
            useful_rate = stats["useful"] / stats["rated"]
            surprising_rate = stats["surprising"] / stats["rated"]
            score = (useful_rate * 0.6) + (surprising_rate * 0.4)
        else:
            useful_rate = 0
            surprising_rate = 0
            score = 0

        results.append({
            "constraint": c_id,
            "total_uses": stats["total"],
            "rated_sessions": stats["rated"],
            "useful_rate": round(useful_rate, 2),
            "surprising_rate": round(surprising_rate, 2),
            "effectiveness_score": round(score, 2),
        })

    results.sort(key=lambda x: x["effectiveness_score"], reverse=True)

    return {
        "total_sessions": len(sessions),
        "constraints_tracked": len(results),
        "constraints": results,
    }


def topology_efficacy() -> dict:
    """Analyze which topologies produce the best results."""
    sessions = _load_sessions()

    if not sessions:
        return {"message": "Nessuna sessione disponibile.", "topologies": []}

    topology_stats: dict[str, dict] = defaultdict(
        lambda: {"total": 0, "rated": 0, "useful": 0, "surprising": 0,
                 "avg_agents": 0, "constraints_used": Counter()}
    )

    for session in sessions:
        topology = session.get("topology", "unknown")
        efficacy = session.get("efficacy", {})
        constraints = session.get("constraints_used", [])

        topology_stats[topology]["total"] += 1
        topology_stats[topology]["avg_agents"] += session.get("agents_count", 0)

        for c in constraints:
            topology_stats[topology]["constraints_used"][c] += 1

        if efficacy.get("rated"):
            topology_stats[topology]["rated"] += 1
            if efficacy.get("useful"):
                topology_stats[topology]["useful"] += 1
            if efficacy.get("surprising"):
                topology_stats[topology]["surprising"] += 1

    results = []
    for t_id, stats in topology_stats.items():
        if stats["rated"] > 0:
            useful_rate = stats["useful"] / stats["rated"]
            surprising_rate = stats["surprising"] / stats["rated"]
        else:
            useful_rate = 0
            surprising_rate = 0

        avg_agents = stats["avg_agents"] / stats["total"] if stats["total"] > 0 else 0
        top_constraints = stats["constraints_used"].most_common(5)

        results.append({
            "topology": t_id,
            "total_sessions": stats["total"],
            "rated_sessions": stats["rated"],
            "useful_rate": round(useful_rate, 2),
            "surprising_rate": round(surprising_rate, 2),
            "avg_agents": round(avg_agents, 1),
            "top_constraints": [{"constraint": c, "count": n} for c, n in top_constraints],
        })

    results.sort(key=lambda x: x["total_sessions"], reverse=True)

    return {
        "total_sessions": len(sessions),
        "topologies": results,
    }


def pattern_mining() -> dict:
    """Find constraint combinations that frequently appear in successful sessions.

    Looks for pairs and triples of constraints that co-occur in useful+surprising sessions.
    """
    sessions = _load_sessions()

    if not sessions:
        return {"message": "Nessuna sessione disponibile.", "patterns": []}

    # Track co-occurrences in successful sessions
    successful_pairs: Counter = Counter()
    successful_triples: Counter = Counter()
    all_pairs: Counter = Counter()

    for session in sessions:
        constraints = sorted(set(session.get("constraints_used", [])))
        efficacy = session.get("efficacy", {})
        is_successful = efficacy.get("useful") or efficacy.get("surprising")

        # Generate pairs
        for i in range(len(constraints)):
            for j in range(i + 1, len(constraints)):
                pair = (constraints[i], constraints[j])
                all_pairs[pair] += 1
                if is_successful:
                    successful_pairs[pair] += 1

        # Generate triples
        for i in range(len(constraints)):
            for j in range(i + 1, len(constraints)):
                for k in range(j + 1, len(constraints)):
                    triple = (constraints[i], constraints[j], constraints[k])
                    if is_successful:
                        successful_triples[triple] += 1

    # Build results
    pair_patterns = []
    for pair, success_count in successful_pairs.most_common(10):
        total = all_pairs[pair]
        pair_patterns.append({
            "constraints": list(pair),
            "successful_sessions": success_count,
            "total_sessions": total,
            "success_rate": round(success_count / total, 2) if total > 0 else 0,
        })

    triple_patterns = []
    for triple, success_count in successful_triples.most_common(5):
        triple_patterns.append({
            "constraints": list(triple),
            "successful_sessions": success_count,
        })

    return {
        "total_sessions": len(sessions),
        "successful_pairs": pair_patterns,
        "successful_triples": triple_patterns,
    }


def suggest_from_history(
    topic: str,
    goal: Optional[str] = None,
    max_suggestions: int = 4,
) -> list[dict]:
    """Suggest constraints based on session history.

    Strategy:
    1. Find sessions with similar topics (keyword overlap)
    2. Weight by efficacy (useful/surprising)
    3. Prefer constraints from successful sessions
    4. Diversify: don't repeat same category too much

    Returns list of constraint suggestions with confidence and evidence.
    """
    sessions = _load_sessions()

    if not sessions:
        return []

    # Simple keyword extraction from topic
    topic_words = set(
        w.lower().strip("\"'.,;:!?()[]")
        for w in topic.split()
        if len(w) > 3
    )
    if goal:
        topic_words |= set(
            w.lower().strip("\"'.,;:!?()[]")
            for w in goal.split()
            if len(w) > 3
        )

    # Score each session by topic similarity + efficacy
    constraint_scores: dict[str, dict] = defaultdict(
        lambda: {"score": 0.0, "evidence": [], "count": 0}
    )

    for session in sessions:
        session_topic = session.get("topic", "")
        session_words = set(
            w.lower().strip("\"'.,;:!?()[]")
            for w in session_topic.split()
            if len(w) > 3
        )

        # Topic similarity (Jaccard-like)
        overlap = len(topic_words & session_words)
        if not topic_words:
            similarity = 0.1  # baseline for all sessions
        else:
            similarity = overlap / len(topic_words | session_words) if (topic_words | session_words) else 0
            similarity = max(similarity, 0.1)  # minimum baseline

        # Efficacy multiplier
        efficacy = session.get("efficacy", {})
        efficacy_mult = 1.0
        if efficacy.get("useful"):
            efficacy_mult += 0.5
        if efficacy.get("surprising"):
            efficacy_mult += 0.5

        # Score constraints
        constraints = session.get("constraints_used", [])
        for c in constraints:
            score = similarity * efficacy_mult
            constraint_scores[c]["score"] += score
            constraint_scores[c]["count"] += 1
            if similarity > 0.2:  # only add as evidence if reasonably similar
                constraint_scores[c]["evidence"].append({
                    "topic": session_topic[:80],
                    "topology": session.get("topology"),
                    "useful": efficacy.get("useful"),
                    "surprising": efficacy.get("surprising"),
                })

    if not constraint_scores:
        return []

    # Sort by score and return top suggestions
    ranked = sorted(
        constraint_scores.items(),
        key=lambda x: x[1]["score"],
        reverse=True,
    )

    suggestions = []
    for c_id, data in ranked[:max_suggestions]:
        evidence_summary = []
        for ev in data["evidence"][:2]:
            status = []
            if ev.get("useful"):
                status.append("utile")
            if ev.get("surprising"):
                status.append("sorprendente")
            evidence_summary.append(
                f"{ev['topic']} ({', '.join(status) if status else 'non valutata'})"
            )

        suggestions.append({
            "type": c_id,
            "_reason": f"Usato in {data['count']} sessioni precedenti",
            "_confidence": "data-driven" if data["count"] >= 3 else "limited-data",
            "_evidence": evidence_summary,
        })

    return suggestions


def sequence_efficacy() -> dict:
    """Analyze constraint sequence effectiveness for sequential chain sessions.

    Tracks which orderings of constraints produce the best results.
    A constraint in position 1 may perform differently than in position 3.
    """
    sessions = _load_sessions()
    chain_sessions = [
        s for s in sessions
        if s.get("topology") == "sequential_chain" and s.get("constraint_sequence")
    ]

    if not chain_sessions:
        return {
            "message": "Nessuna sessione sequential_chain disponibile.",
            "sequences": [],
        }

    # Track constraint performance by position
    position_stats: dict[str, dict[int, dict]] = defaultdict(
        lambda: defaultdict(lambda: {"total": 0, "useful": 0, "surprising": 0})
    )

    # Track adjacent pairs
    pair_stats: Counter = Counter()
    successful_pairs: Counter = Counter()

    for session in chain_sessions:
        sequence = session["constraint_sequence"]
        efficacy = session.get("efficacy", {})
        is_successful = efficacy.get("useful") or efficacy.get("surprising")

        for pos, constraint in enumerate(sequence):
            position_stats[constraint][pos]["total"] += 1
            if efficacy.get("useful"):
                position_stats[constraint][pos]["useful"] += 1
            if efficacy.get("surprising"):
                position_stats[constraint][pos]["surprising"] += 1

            # Adjacent pairs
            if pos < len(sequence) - 1:
                pair = (constraint, sequence[pos + 1])
                pair_stats[pair] += 1
                if is_successful:
                    successful_pairs[pair] += 1

    # Build position results
    position_results = {}
    for constraint, positions in position_stats.items():
        position_results[constraint] = {
            str(pos): {
                "total": data["total"],
                "useful_rate": round(data["useful"] / data["total"], 2) if data["total"] > 0 else 0,
                "surprising_rate": round(data["surprising"] / data["total"], 2) if data["total"] > 0 else 0,
            }
            for pos, data in sorted(positions.items())
        }

    # Best adjacent pairs
    best_pairs = []
    for pair, count in successful_pairs.most_common(5):
        total = pair_stats[pair]
        best_pairs.append({
            "sequence": list(pair),
            "successful": count,
            "total": total,
            "success_rate": round(count / total, 2) if total > 0 else 0,
        })

    return {
        "total_chain_sessions": len(chain_sessions),
        "constraint_by_position": position_results,
        "best_adjacent_pairs": best_pairs,
    }


# --- Topology-to-skill mapping for smart defaults ---

TOPOLOGY_TO_SKILL = {
    "cascade": "/lens-adversarial",
    "star": "/lens-focus-group",
    "adversarial_jury": "/lens-adversarial",
    "steelman_chain": "/lens-steelman",
    "socratic_drill": "/lens-assumptions",
    "scenario_matrix": "/lens-scenarios",
    "assumption_inversion": "/lens-assumptions",
    "sequential_chain": "/lens-deep",
    "ring": "/lens",
    "parallel_hats": "/lens",
    "bisociation_engine": "/lens-perspective",
    "wise_mind_topology": "/lens-perspective",
    "scamper_parallel": "/lens",
}

GOAL_PATTERNS = [
    (r"stress|attacca|verifica|testa", {"skill": "/lens-adversarial", "topology": "cascade", "mode": "QUICK"}),
    (r"creativ|innova|ide|nuov", {"skill": "/lens", "topology": "bisociation_engine", "mode": "QUICK"}),
    (r"rischi|premortem|falliment|pericol", {"skill": "/lens-premortem", "topology": "cascade", "mode": "QUICK"}),
    (r"assunzion|assumption|nascost|blind", {"skill": "/lens-assumptions", "topology": "assumption_inversion", "mode": "QUICK"}),
    (r"decision|scelt|dilemma|equilibr", {"skill": "/lens", "topology": "wise_mind_topology", "mode": "QUICK"}),
    (r"argoment|convinc|robust|forte", {"skill": "/lens-steelman", "topology": "steelman_chain", "mode": "QUICK"}),
    (r"scenario|futur|incertezz", {"skill": "/lens-scenarios", "topology": "scenario_matrix", "mode": "DEEP"}),
    (r"approfond|epistemic|ipotesi|coerenz", {"skill": "/lens-deep", "topology": "sequential_chain", "mode": "DEEP"}),
    (r"focus.?group|persona|stakeholder|audience", {"skill": "/lens-focus-group", "topology": "star", "mode": "DEEP"}),
]


def smart_defaults(
    topic: str,
    goal: Optional[str] = None,
) -> dict:
    """Generate smart default configuration for a Lens session.

    Analyzes session history to suggest the best configuration based on
    what worked for similar topics. Falls back to heuristics.
    """
    sessions = _load_sessions()
    combined_text = (topic + " " + (goal or "")).lower()

    # Try data-driven first (need >= 3 similar sessions)
    if sessions:
        data_suggestions = suggest_from_history(topic, goal, max_suggestions=4)
        similar_sessions = [
            s for s in sessions
            if _topic_similarity(topic, s.get("topic", "")) > 0.2
        ]

        if len(similar_sessions) >= 3:
            # Find best topology from similar successful sessions
            topo_counter: Counter = Counter()
            intensity_sum = 0
            intensity_count = 0

            for s in similar_sessions:
                eff = s.get("efficacy", {})
                if eff.get("useful") or eff.get("surprising"):
                    topo_counter[s.get("topology", "unknown")] += 1

                # Estimate intensity from constraint count
                n_constraints = len(s.get("constraints_used", []))
                if n_constraints > 0:
                    intensity_sum += min(n_constraints, 5)
                    intensity_count += 1

            best_topology = topo_counter.most_common(1)[0][0] if topo_counter else None
            avg_intensity = round(intensity_sum / intensity_count) if intensity_count > 0 else 3

            if best_topology:
                skill = TOPOLOGY_TO_SKILL.get(best_topology, "/lens")
                constraints = data_suggestions[:4] if data_suggestions else []

                return {
                    "recommendation": {
                        "skill": skill,
                        "topology": best_topology,
                        "constraints": constraints,
                        "intensity": avg_intensity,
                        "mode": "DEEP" if best_topology in ("star", "adversarial_jury", "scenario_matrix", "sequential_chain", "ring", "scamper_parallel") else "QUICK",
                    },
                    "confidence": "data-driven",
                    "reasoning": f"Basato su {len(similar_sessions)} sessioni simili. "
                                 f"{best_topology} ha prodotto i migliori risultati.",
                    "alternatives": _generate_alternatives(combined_text, best_topology),
                }

    # Heuristic fallback
    for pattern, defaults in GOAL_PATTERNS:
        if re.search(pattern, combined_text):
            from constraints.composer import suggest_constraints as heuristic_suggest
            constraints = heuristic_suggest(topic, goal or "", max_constraints=4)

            return {
                "recommendation": {
                    "skill": defaults["skill"],
                    "topology": defaults["topology"],
                    "constraints": constraints,
                    "intensity": 3,
                    "mode": defaults["mode"],
                },
                "confidence": "heuristic",
                "reasoning": f"Basato su euristica goal-matching. "
                             f"Pattern riconosciuto nel topic/goal.",
                "alternatives": _generate_alternatives(combined_text, defaults["topology"]),
            }

    # Ultimate fallback
    from constraints.composer import suggest_constraints as heuristic_suggest
    constraints = heuristic_suggest(topic, goal or "", max_constraints=3)

    return {
        "recommendation": {
            "skill": "/lens-adversarial",
            "topology": "cascade",
            "constraints": constraints,
            "intensity": 3,
            "mode": "QUICK",
        },
        "confidence": "fallback",
        "reasoning": "Nessun pattern riconosciuto. Cascade adversariale come default sicuro.",
        "alternatives": [
            {"skill": "/lens-assumptions", "when": "Se vuoi scavare nelle assunzioni"},
            {"skill": "/lens-deep", "when": "Se vuoi un'analisi profonda e coerente"},
            {"skill": "/lens-perspective", "when": "Se vuoi una singola prospettiva rapida"},
        ],
    }


def _topic_similarity(topic_a: str, topic_b: str) -> float:
    """Simple Jaccard similarity between topic word sets."""
    words_a = set(w.lower().strip("\"'.,;:!?()[]") for w in topic_a.split() if len(w) > 3)
    words_b = set(w.lower().strip("\"'.,;:!?()[]") for w in topic_b.split() if len(w) > 3)
    if not words_a or not words_b:
        return 0.0
    union = words_a | words_b
    return len(words_a & words_b) / len(union) if union else 0.0


def _generate_alternatives(text: str, current_topology: str) -> list[dict]:
    """Generate alternative skill suggestions excluding current."""
    alternatives = []
    for pattern, defaults in GOAL_PATTERNS:
        if defaults["topology"] != current_topology:
            alternatives.append({
                "skill": defaults["skill"],
                "when": f"Se preferisci {defaults['topology']}",
            })
            if len(alternatives) >= 2:
                break

    if not alternatives:
        alternatives = [
            {"skill": "/lens-deep", "when": "Se vuoi approfondimento sequenziale"},
            {"skill": "/lens-perspective", "when": "Se vuoi una prospettiva rapida"},
        ]

    return alternatives


def implementation_rate() -> dict:
    """Calculate the rate of sessions where insights were actually implemented.

    This is the key non-circular metric: not 'was it useful?' (subjective)
    but 'was it used?' (objective, verifiable).
    """
    sessions = _load_sessions()

    if not sessions:
        return {"message": "Nessuna sessione disponibile.", "implementation_rate": 0}

    total = len(sessions)
    implemented_count = 0
    by_topology: dict[str, dict] = defaultdict(
        lambda: {"total": 0, "implemented": 0}
    )
    by_constraint: dict[str, dict] = defaultdict(
        lambda: {"total": 0, "implemented": 0}
    )
    recent_implementations = []

    for session in sessions:
        topology = session.get("topology", "unknown")
        efficacy = session.get("efficacy", {})
        constraints = session.get("constraints_used", [])
        is_implemented = efficacy.get("implemented", False)

        by_topology[topology]["total"] += 1

        for c in constraints:
            by_constraint[c]["total"] += 1

        if is_implemented:
            implemented_count += 1
            by_topology[topology]["implemented"] += 1
            for c in constraints:
                by_constraint[c]["implemented"] += 1
            recent_implementations.append({
                "session_id": session.get("session_id"),
                "topic": session.get("topic", "")[:80],
                "note": efficacy.get("implementation_note", ""),
            })

    # Calculate rates
    topology_rates = {}
    for t_id, stats in by_topology.items():
        topology_rates[t_id] = {
            "total": stats["total"],
            "implemented": stats["implemented"],
            "rate": round(stats["implemented"] / stats["total"], 2) if stats["total"] > 0 else 0,
        }

    constraint_rates = sorted(
        [
            {
                "constraint": c_id,
                "total": stats["total"],
                "implemented": stats["implemented"],
                "rate": round(stats["implemented"] / stats["total"], 2) if stats["total"] > 0 else 0,
            }
            for c_id, stats in by_constraint.items()
        ],
        key=lambda x: x["rate"],
        reverse=True,
    )

    return {
        "total_sessions": total,
        "implemented_sessions": implemented_count,
        "implementation_rate": round(implemented_count / total, 2) if total > 0 else 0,
        "by_topology": topology_rates,
        "top_constraints": constraint_rates[:10],
        "recent_implementations": recent_implementations[:5],
    }


def roi_estimate() -> dict:
    """Estimate ROI of Lens usage based on implementation data."""
    sessions = _load_sessions()

    if not sessions:
        return {"message": "Nessuna sessione disponibile."}

    total = len(sessions)
    implemented = sum(
        1 for s in sessions
        if s.get("efficacy", {}).get("implemented")
    )
    useful = sum(
        1 for s in sessions
        if s.get("efficacy", {}).get("useful")
    )

    # Find most productive topology and constraints
    topo_impl: Counter = Counter()
    constraint_impl: Counter = Counter()

    for s in sessions:
        if s.get("efficacy", {}).get("implemented"):
            topo_impl[s.get("topology", "unknown")] += 1
            for c in s.get("constraints_used", []):
                constraint_impl[c] += 1

    most_productive_topology = topo_impl.most_common(1)[0][0] if topo_impl else None
    most_productive_constraints = [c for c, _ in constraint_impl.most_common(3)]

    recommendation = ""
    if most_productive_topology:
        recommendation = (
            f"Concentrati su {most_productive_topology} "
            f"con {', '.join(most_productive_constraints[:2])} per il massimo ROI."
        )

    return {
        "sessions_total": total,
        "sessions_useful": useful,
        "sessions_implemented": implemented,
        "implementation_rate": round(implemented / total, 2) if total > 0 else 0,
        "useful_rate": round(useful / total, 2) if total > 0 else 0,
        "most_productive_topology": most_productive_topology,
        "most_productive_constraints": most_productive_constraints,
        "recommendation": recommendation,
    }

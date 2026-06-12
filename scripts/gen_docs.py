"""Generate human-readable reference docs from the Lens data files.

Run from the repo root:

    python scripts/gen_docs.py

Writes docs/CONSTRAINTS.md and docs/TOPOLOGIES.md from constraints/library.json
and topologies/definitions.json. These files are generated — do not edit them by
hand; change the JSON and re-run this script (CI checks they are in sync).
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
LIBRARY = ROOT / "constraints" / "library.json"
TOPOLOGIES = ROOT / "topologies" / "definitions.json"
DOCS = ROOT / "docs"

GENERATED_NOTE = (
    "<!-- GENERATED FILE — do not edit by hand. "
    "Run `python scripts/gen_docs.py` after changing the JSON. -->\n\n"
)

CATEGORY_ORDER = [
    "structural",
    "temporal",
    "semantic",
    "modal",
    "creative",
    "analytical",
    "baseline_breaking",
]

CATEGORY_BLURB = {
    "structural": "Reshape the structure of the reasoning itself.",
    "temporal": "Shift the time vantage point.",
    "semantic": "Constrain the language and concepts allowed.",
    "modal": "Switch the mode of cognition.",
    "creative": "Force unusual combinations and fresh framings.",
    "analytical": "Tighten the rigor of explanation and argument.",
    "baseline_breaking": "Push output away from the safe center of the distribution.",
}


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def gen_constraints():
    lib = _load(LIBRARY)
    constraints = lib["constraints"]
    by_cat = {}
    for c in constraints:
        by_cat.setdefault(c["category"], []).append(c)

    out = [GENERATED_NOTE]
    out.append("# Constraint Reference\n")
    out.append(
        f"The {len(constraints)} cognitive constraints that make up the Lens library, "
        f"grouped into {len(by_cat)} categories. Each constraint is a structural rule that "
        "forces a specific thinking pattern.\n"
    )

    # Index
    out.append("## Index\n")
    for cat in CATEGORY_ORDER:
        items = by_cat.get(cat, [])
        if not items:
            continue
        names = ", ".join(f"[`{c['id']}`](#{c['id']})" for c in items)
        out.append(f"- **{cat}** ({len(items)}): {names}")
    out.append("")

    # Per category
    for cat in CATEGORY_ORDER:
        items = by_cat.get(cat, [])
        if not items:
            continue
        out.append(f"## {cat}\n")
        out.append(f"_{CATEGORY_BLURB.get(cat, '')}_\n")
        for c in items:
            out.append(f'### {c["id"]}\n')
            out.append(f'**{c.get("name", c["id"])}** — {c.get("description", "")}\n')
            if c.get("theory"):
                out.append(f'> Theory: {c["theory"]}\n')
            levels = c.get("intensity_levels", {})
            if levels:
                out.append("Intensity:\n")
                for lvl in sorted(levels):
                    out.append(f"- **{lvl}** — {levels[lvl]}")
                out.append("")
            compat = c.get("compatible_with", [])
            incompat = c.get("incompatible_with", [])
            if compat:
                out.append(f"Compatible with: {', '.join(f'`{x}`' for x in compat)}")
            if incompat:
                out.append(f"Incompatible with: {', '.join(f'`{x}`' for x in incompat)}")
            if compat or incompat:
                out.append("")
            examples = c.get("examples", [])
            if examples:
                out.append("Examples:")
                for ex in examples:
                    out.append(f"- {ex}")
                out.append("")
    return "\n".join(out).rstrip() + "\n"


def _range(d):
    lo, hi = d.get("min"), d.get("max")
    return f"{lo}" if lo == hi else f"{lo}-{hi}"


def gen_topologies():
    data = _load(TOPOLOGIES)
    topologies = data["topologies"]

    out = [GENERATED_NOTE]
    out.append("# Topology Reference\n")
    out.append(
        f"The {len(topologies)} topologies that define how constrained agents interact. "
        "Pick one by what you need; `/lens` can also suggest one for you.\n"
    )

    # Summary table
    out.append("## At a glance\n")
    out.append("| Topology | Mode | Agents | Rounds | Best for |")
    out.append("|----------|------|--------|--------|----------|")
    for t in topologies:
        out.append(
            f'| [`{t["id"]}`](#{t["id"]}) | {t.get("mode", "")} '
            f'| {_range(t.get("agent_count", {}))} | {_range(t.get("rounds", {}))} '
            f'| {t.get("best_for", "")} |'
        )
    out.append("")

    # Per topology
    for t in topologies:
        out.append(f'## {t["id"]}\n')
        out.append(f'**{t.get("name", t["id"])}** — {t.get("description", "")}\n')
        if t.get("theory"):
            out.append(f'> Theory: {t["theory"]}\n')
        meta = [
            f'Mode: **{t.get("mode", "")}**',
            f'Agents: {_range(t.get("agent_count", {}))}',
            f'Rounds: {_range(t.get("rounds", {}))}',
            f'Interaction: {t.get("interaction_pattern", "")}',
            f'Output: `{t.get("output_format", "")}`',
        ]
        out.append(" · ".join(meta) + "\n")
        if t.get("best_for"):
            out.append(f'**Best for:** {t["best_for"]}\n')
        rec = t.get("recommended_constraints", [])
        if rec:
            out.append(
                "Recommended constraints: "
                + ", ".join(f"[`{x}`](CONSTRAINTS.md#{x})" for x in rec)
                + "\n"
            )
        wf = t.get("workflow", {})
        if wf.get("description"):
            out.append(f'Workflow: {wf["description"]}\n')
    return "\n".join(out).rstrip() + "\n"


def main():
    DOCS.mkdir(exist_ok=True)
    (DOCS / "CONSTRAINTS.md").write_text(gen_constraints(), encoding="utf-8")
    (DOCS / "TOPOLOGIES.md").write_text(gen_topologies(), encoding="utf-8")
    print("Generated docs/CONSTRAINTS.md and docs/TOPOLOGIES.md")


if __name__ == "__main__":
    main()

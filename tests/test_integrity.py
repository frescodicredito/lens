"""Integrity tests for the Lens data graph.

These tests guard the core invariant of Lens: the references between
constraints, topologies and personas must stay consistent. They are the
safety net that lets contributors add constraints/topologies without
silently breaking the graph.

Run standalone:   python tests/test_integrity.py
Run with pytest:  pytest tests/test_integrity.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
LIBRARY_PATH = ROOT / "constraints" / "library.json"
TOPOLOGIES_PATH = ROOT / "topologies" / "definitions.json"
PERSONAS_DIR = ROOT / "personas" / "templates"


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _constraint_ids():
    library = _load(LIBRARY_PATH)
    return {c["id"] for c in library["constraints"]}


def test_headline_counts():
    """The numbers advertised in the README must match reality."""
    library = _load(LIBRARY_PATH)
    constraints = library["constraints"]
    categories = {c["category"] for c in constraints}
    topologies = _load(TOPOLOGIES_PATH)["topologies"]
    personas = list(PERSONAS_DIR.glob("*.json"))

    assert len(constraints) == 25, f"expected 25 constraints, got {len(constraints)}"
    assert len(categories) == 7, f"expected 7 categories, got {len(categories)}: {sorted(categories)}"
    assert len(topologies) == 13, f"expected 13 topologies, got {len(topologies)}"
    assert len(personas) == 5, f"expected 5 persona templates, got {len(personas)}"


def test_unique_constraint_ids():
    library = _load(LIBRARY_PATH)
    ids = [c["id"] for c in library["constraints"]]
    assert len(ids) == len(set(ids)), "duplicate constraint ids in library.json"


def test_required_constraint_fields():
    library = _load(LIBRARY_PATH)
    for c in library["constraints"]:
        for field in ("id", "name", "category", "prompt_template"):
            assert field in c, f"constraint '{c.get('id', '?')}' missing required field '{field}'"


def test_compatibility_refs_resolve():
    """Every compatible_with / incompatible_with id must exist."""
    library = _load(LIBRARY_PATH)
    ids = _constraint_ids()
    for c in library["constraints"]:
        for field in ("compatible_with", "incompatible_with"):
            for ref in c.get(field, []):
                assert ref in ids, f"constraint '{c['id']}'.{field} references unknown id '{ref}'"


def test_topology_constraint_refs_resolve():
    """Every constraint id recommended by a topology must exist."""
    ids = _constraint_ids()
    topologies = _load(TOPOLOGIES_PATH)["topologies"]
    for topo in topologies:
        topo_id = topo.get("id", "?")
        for ref in topo.get("recommended_constraints", []):
            assert ref in ids, f"topology '{topo_id}' references unknown constraint '{ref}'"


def test_persona_constraint_types_resolve():
    """Every constraint type used by a persona must exist in the library."""
    ids = _constraint_ids()
    for path in PERSONAS_DIR.glob("*.json"):
        persona = _load(path)
        for c in persona.get("constraints", []):
            ctype = c.get("type")
            assert ctype in ids, f"persona '{path.name}' uses unknown constraint type '{ctype}'"


def test_sub_type_tables_present():
    """Constraints with parametric sub-types must ship their lookup table."""
    library = _load(LIBRARY_PATH)
    by_id = {c["id"]: c for c in library["constraints"]}
    expectations = {
        "scamper": "scamper_operations",
        "elm_route": "elm_routes",
        "concept_fan": "abstraction_levels",
        "wise_mind": "mind_types",
    }
    for cid, table in expectations.items():
        if cid in by_id:
            assert table in by_id[cid], f"constraint '{cid}' missing sub-type table '{table}'"


def _run_all():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for t in tests:
        try:
            t()
            print(f"PASS {t.__name__}")
        except AssertionError as e:
            failures += 1
            print(f"FAIL {t.__name__}: {e}")
    print(f"\n{len(tests) - failures}/{len(tests)} passed")
    return failures


if __name__ == "__main__":
    import sys
    sys.exit(1 if _run_all() else 0)

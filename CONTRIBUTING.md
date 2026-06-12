# Contributing to Lens

Lens is built on a simple primitive: the **cognitive constraint**. The easiest and
most valuable way to contribute is to add new constraints, topologies, or personas.
Because everything is data-driven, you rarely need to touch Python.

## Setup

```bash
git clone https://github.com/frescodicredito/lens.git
cd lens
uv sync
python tests/test_integrity.py   # should print "7/7 passed"
python examples/quickstart.py     # see a composed prompt end-to-end
```

## Adding a constraint

Constraints live in [`constraints/library.json`](constraints/library.json). Add an
object to the `constraints` array:

```json
{
  "id": "my_constraint",
  "name": "Human-readable name",
  "category": "structural | temporal | semantic | modal | creative | analytical | baseline_breaking",
  "theory": "Short attribution to the theory/author it draws on",
  "prompt_template": "The instruction injected into the agent. Use {placeholders} for config.",
  "intensity_levels": {
    "1": "Mild version of the constraint",
    "3": "Default version",
    "5": "Maximal, uncompromising version"
  },
  "compatible_with": ["other_constraint_id"],
  "incompatible_with": ["conflicting_constraint_id"]
}
```

Rules of thumb:
- `id` must be unique and snake_case.
- Every id in `compatible_with` / `incompatible_with` must exist in the library.
- If your constraint has parametric sub-types (like `scamper`, `elm_route`), ship the
  lookup table alongside it (see `scamper_operations` in the library for the pattern).
- Keep incompatibility symmetric where it makes sense.

## Adding a topology

Topologies live in [`topologies/definitions.json`](topologies/definitions.json). Every
id in `recommended_constraints` must exist in the library.

## Adding a persona

Personas are constraint bundles in [`personas/templates/`](personas/templates/). Every
constraint `type` you use must exist in the library.

## Before opening a PR

Always run the integrity tests — they are the contract that keeps the constraint graph
consistent:

```bash
python tests/test_integrity.py
```

If you add or change Python code, also confirm it compiles and the quickstart still runs:

```bash
python -m py_compile server.py constraints/composer.py meta/analytics.py
python examples/quickstart.py
```

## Scope

Lens produces *ways of looking at problems*, not content. Proposals that turn Lens into
a content generator, or that hardcode a single "best answer" path, are out of scope.
See the design principles in the README and `LENS.md`.

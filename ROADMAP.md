# Roadmap

Lens evolves by applying its own method to itself (assumption inversion, premortem,
steelman). This is the public-facing direction; it is intentionally high-level.

## Done

- **Single-agent deep chains** — `sequential_chain` topology + `/lens-deep` skill.
- **Adaptive configuration** — `lens_quick_start` and data-driven `suggest_constraints`.
- **Portable output** — Decision Brief and Executive Extract formats for handoff.
- **Anti-baseline constraints** — the `baseline_breaking` category, to push output away
  from the safe center of the distribution.
- **Non-circular metrics** — implementation-rate and ROI tracking, so efficacy is
  measured by "was the insight actually used?" rather than self-report alone.

## Next

- **Contextual triggers** — surface the right topology automatically from the shape of a
  problem, instead of relying on the user to pick one.
- **Constraint authoring guide** — richer human-readable docs per constraint and topology
  (auto-generated from the JSON), so the library is browsable, not just machine-readable.
- **Broader integrations** — adapters that turn external structured data into grounded
  personas (the Miner adapter is the first example of this pattern).

## Out of scope

Lens produces ways of looking at problems, not content. Features that turn it into a
content generator, or that collapse it to a single "best answer" path, are out of scope.

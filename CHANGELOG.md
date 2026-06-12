# Changelog

All notable changes to Lens are documented here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/); this project uses
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- MIT `LICENSE`.
- `tests/test_integrity.py` — validates the constraint/topology/persona reference graph.
- `examples/quickstart.py` — compose a constrained prompt without any MCP setup.
- `CONTRIBUTING.md` and this `CHANGELOG.md`.
- Claude Code skills are now bundled in `skills/` (previously a separate plugin repo).

### Changed
- Generalized branding from "Brain ecosystem" to "LLM reasoning" across server, README,
  and skills — Lens is now self-contained and provider-agnostic.
- `pyproject.toml`: version aligned to 0.2.0, added license/authors/keywords metadata,
  pinned `fastmcp>=3.0.0,<4.0.0`.

### Security
- Fixed path traversal in tools that build file paths from caller-supplied ids.
  `session_id`, `persona_id`, and Miner persona names are now validated/sanitized so a
  value like `../../etc/x` can no longer read or overwrite files outside the intended
  directory. Added `tests/test_security.py` as a regression guard (run in CI).
- Error messages and tool return values no longer leak absolute filesystem paths.

### Fixed
- Session JSON I/O is now corruption-resistant: reads skip malformed files instead of
  crashing all analytics; writes are atomic (temp file + replace).
- `compose_prompt` now surfaces unknown constraint ids as warnings instead of silently
  dropping them.
- `intensity` is clamped to the documented 1–5 range across all compose functions.
- `miner.py` reads loosely-typed fields defensively (no crash on null/non-string input).
- Removed the never-populated `unique_insights` efficacy field and an unused `topic`
  parameter in the Miner integration.

## [0.2.0] — Evolution Plan

### Added
- 5 new constraints (anchor_break + 4 baseline-breaking: anti_sycophancy,
  anti_completeness, anti_coherence, raw_signal) → 25 total across 7 categories.
- `sequential_chain` topology → 13 total.
- Meta-Lens analytics: constraint/topology/sequence efficacy, pattern mining,
  implementation-rate and ROI metrics, data-driven suggestions.
- Miner integration: transform audience personas into Lens cognitive templates.
- `/lens-deep` skill (single-agent sequential chain).

## [0.1.0] — Initial

### Added
- FastMCP server, 20 constraints in 6 categories, 12 topologies, 5 persona templates,
  composer, output formatter, 8 orchestration skills.

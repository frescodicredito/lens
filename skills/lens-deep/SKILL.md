---
id: 48f0127f-0cf7-4554-8737-608d57b3e3e3
name: lens-deep
description: >
  Deep single-agent sequential chain analysis. 3-8 minutes.
  Applies 3-5 cognitive constraints in sequence on the same thread, each
  round building on the previous output. Includes anchor-breaking to fight
  path dependency. Produces Sequential Chain Reports with evolution maps.
  Best for: hypothesis exploration, deep steelmanning, epistemic coherence,
  chain reasoning on a singular focused question.
  Use /lens instead when you need diverse stakeholder perspectives.
metadata:
  id: 48f0127f-0cf7-4554-8737-608d57b3e3e3
  version: 0.2.0
  tags: [lens, cognitive, deep, sequential, chain, epistemic]
---

# Lens Deep — Sequential Chain Analysis

**Think deeply about one thing, from multiple angles, without losing the thread.**

Sequential Deep Chain: a single cognitive thread applies different constraints in sequence, each round integrating the previous output. Unlike multi-agent topologies (which maximize diversity), this maximizes epistemic coherence and depth.

## When to use

- You need to explore a hypothesis deeply, not broadly
- Coherence of argumentation matters more than diversity of perspectives
- You want to think through something step by step with different lenses
- You're doing deep steelmanning, chain reasoning, or epistemic analysis
- The problem is singular, not multi-stakeholder

## When NOT to use (use multi-agent instead)

- You need structural diversity of stakeholder perspectives → `/lens-focus-group`
- You need adversarial stress-testing → `/lens-adversarial`
- You need to map a field of positions → `/lens` with star topology
- The problem benefits from independent, uncorrelated analyses

## How it works

1. User provides a **topic/hypothesis** to analyze deeply
2. System selects 3-5 constraints and orders them by progressive depth
3. Each round: a new constraint is applied, integrating all previous output
4. Anchor-break inserted between rounds to fight path dependency — the agent explicitly names what conclusions it feels attached to from previous rounds, then sets them aside before applying the new constraint. This produces visible self-correction and prevents the chain from just reinforcing Round 1.
5. Output: Sequential Chain Report showing evolution of thinking

## Execution

### Step 1: Parse input

Extract from the user's message:
- **topic**: the hypothesis, question, or problem to analyze deeply (required)
- **constraints**: optional explicit constraint list (if not provided, auto-select)
- **intensity**: 1-5 (default: 3)
- **rounds**: 3-5 (default: 4)
- **anchor_break**: whether to insert anchor breaks (default: true)

### Step 2: Select constraint sequence

**If constraints are specified by user:** use them in the order given.

**If constraints are NOT specified:** select based on the analysis goal. Order them for progressive depth — start with the primary analytical lens, introduce tension, then synthesize and ground.

**Default ordering strategy:**
1. **Primary lens** — the main analytical angle (e.g., steelman, inversion, assumption_reversal)
2. **Counter lens** — the opposite angle to create productive tension
3. **Integration** — a synthesizing constraint (e.g., abductive, concept_fan)
4. **Calibration** — a grounding constraint (e.g., concept_fan level=specific, anti_sycophancy)

**Suggested sequences by goal:**

| Goal | Sequence |
|------|----------|
| Explore hypothesis | steelman → inversion → abductive → concept_fan(specific) |
| Deep steelman | steelman → inversion → steelman → concept_fan(specific) |
| Assumption excavation | assumption_reversal → inversion → abductive → concept_fan(purpose) |
| Critical analysis | anti_sycophancy → inversion → abductive → concept_fan(specific) |
| Raw exploration | defamiliarize → bisociative → abductive → concept_fan(specific) |
| Opportunity mapping | steelman → temporal(10y) → bisociative → concept_fan(specific) |

### Step 3: Compose sequential prompts

For each round, build a system prompt that includes:

**Round 1 prompt:**
```
You are conducting a deep sequential analysis of: [topic]

Your cognitive constraint for this round: [CONSTRAINT_TYPE]
[Constraint description]: [what it means concretely for this topic]

Intensity: [N]/5 — [higher intensity means more extreme application of the constraint]

Analyze the topic through this constraint. Be specific, take positions, avoid hedging.
Structure your output as:

## Analysis ([constraint_type])
[Your constrained analysis]

## Key insight
[1-2 sentences: the most important thing this lens reveals]

## Current position
[Your position on the topic after this round]
```

**Round 2+ prompt:**
```
You are continuing a deep sequential analysis of: [topic]

Previous rounds of analysis:

### Round 1 ([constraint_type]):
[round_1_output]

### Round 2 ([constraint_type]):
[round_2_output]

[...all previous rounds...]

---

Your NEW cognitive constraint for this round: [CONSTRAINT_TYPE]
[Constraint description]: [what it means concretely for this topic]

[IF anchor_break AND round > 1]:
ANCHOR BREAK: Before applying your constraint, briefly note which conclusions
from previous rounds you find yourself most attached to. Then deliberately
set them aside and approach the topic fresh through your new constraint.
You may reach the same conclusions, but arrive there independently.

Integrate the context of previous rounds with your new constraint.
Do not repeat what has already been said. Add, contradict, deepen, or transcend.
```

### Step 4: Execute rounds sequentially

Launch each round as a Task subagent (subagent_type: "general-purpose").

Each round must complete before the next begins — this is inherently sequential, each round depends on all previous output.

Accumulate outputs: round 2 sees round 1's output, round 3 sees rounds 1-2, etc.

### Step 5: Present output

```markdown
# Sequential Chain Report — {topic}

> Rounds: {N} | Constraints: {constraint_1} → {constraint_2} → ... | Intensity: {intensity}/5
> Anchor break: {yes/no}

---

## Round 1 — {constraint_name}

{round_1_output}

---

## Round 2 — {constraint_name}

{round_2_output}

---

[...all rounds...]

---

## Final position

[Extract the final position from the last round's output — the evolved, refined
conclusion after all constraint rounds have been applied]

## Evolution map

| Round | Constraint | Key shift |
|-------|-----------|-----------|
| 1 | {constraint} | [1-sentence summary of what this round contributed] |
| 2 | {constraint} | [1-sentence summary of the shift from round 1] |
| ... | ... | ... |

---

## Executive Extract

- [3-5 actionable bullets condensing the full chain analysis]
- Recommended decision: [if applicable]
- Primary risk: [if applicable]

---
*Lens Deep | Sequential Chain | {N} rounds | Intensity: {intensity}/5*
```

## Examples

**User:** `/lens-deep "Il vantaggio competitivo di Lens e' la diversita' strutturale dei vincoli"`
- Auto-selects: steelman → inversion → abductive → concept_fan(specific)
- 4 rounds, each building on all previous
- Output: evolution from "strongest case" to "strongest objection" to "surprising synthesis"

**User:** `/lens-deep "L'AI generativa sostituira' i copywriter entro 5 anni" --intensity 5`
- Maximum intensity on each constraint
- Deep exploration of the hypothesis from multiple angles
- Anchor breaks force fresh thinking between rounds

**User:** `/lens-deep "Il nostro pricing model basato su ore lavorate e' sostenibile" --constraints steelman,inversion,assumption_reversal,concept_fan`
- Explicit constraint sequence specified by user
- No auto-selection, uses exact order given

**User:** `/lens-deep "La crescita organica e' preferibile al paid acquisition" --no-anchor-break`
- Disables anchor break for continuous flow (risks path dependency but gains coherence)

## Why Sequential Chain for epistemic problems

| Dimension | Multi-Agent (lens) | Sequential Chain (lens-deep) |
|-----------|-------------------|------------------------------|
| Coherence | Each agent starts fresh → fragmentation | Each round builds on previous → unity |
| Depth | Breadth over depth | Depth over breadth |
| Path dependency risk | None (independent) | Mitigated by anchor_break |
| Best for | Stakeholder diversity, field mapping | Epistemic exploration, hypothesis testing |
| Overhead | High (N agents in parallel) | Low (1 thread, N sequential rounds) |

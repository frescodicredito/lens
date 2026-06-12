---
id: 350c44d2-559a-46d4-820f-9b2671ee1c5b
name: lens-assumptions
description: >
  Uncover and invert hidden assumptions in any strategy, plan, or belief.
  Supports QUICK mode (fast assumption surfacing) and DEEP mode (full inversion exploration).
  Combines Socratic Drill and Assumption Inversion topologies.
version: 0.1.0
tags: [lens, cognitive, assumptions, socratic, inversion, quick, deep]
---

# Lens Assumptions — QUICK/DEEP Mode

**Find the assumptions you don't know you're making. Then invert them.**

Combines Socratic Drill (surface hidden assumptions) and Assumption Inversion (systematically explore what happens when each assumption is false). Based on Mason & Mitroff's SAST and CIA's Key Assumptions Check.

## When to use

- You suspect your strategy rests on unexamined assumptions
- You want to find the "taken for granted" beliefs that could be wrong
- You need to identify which assumptions, if wrong, would be catastrophic
- You want to explore "what if the opposite is true?"

## How it works

### QUICK mode (default, 2-3 minutes)
1. User provides a **strategy/plan/belief**
2. Agent 1 (Socratic): surfaces 5-8 hidden assumptions via questioning
3. Agent 2 (Classifier): ranks by importance x certainty
4. Agent 3 (Inverter): inverts the top 3-4 assumptions and explores implications
5. Output: assumption map + inversion insights

### DEEP mode (5-10 minutes, with --deep flag)
1. Same as QUICK, but...
2. After classification, user chooses which assumptions to invert
3. Each selected assumption gets a dedicated inversion agent
4. Cross-analysis of inversions
5. Output: full assumption map + detailed inversion exploration

## Execution

### Step 1: Parse input

Extract from the user's message:
- **subject**: the strategy, plan, belief, or decision to examine (required)
- **mode**: QUICK (default) or DEEP (if --deep flag)
- **intensity**: 1-5 (default: 3)
- **focus**: optional focus area (e.g., "focus on market assumptions", "focus on technical assumptions")

### Step 2: Agent 1 — Socratic Drill (surface assumptions)

```
lens_compose_prompt(
  topic=subject,
  constraints=[
    {"type": "abductive"},
    {"type": "modal", "mode": "only questions and hidden assumptions, no answers or solutions"}
  ],
  output_format="raw",
  intensity=intensity,
  extra_instructions="Your task is to DIG down to the foundational assumptions. For every implicit claim in the strategy, ask: 'Why do we assume this is true?' List ALL the assumptions you find, even the ones that seem obvious. The most dangerous assumptions are the ones no one questions."
)
```

**Agent 1 prompt:**
```
{system_prompt}

STRATEGY/PLAN TO EXAMINE:
{subject}

Identify ALL the hidden assumptions. For each:
1. **Assumption**: what is taken to be true without verifying it
2. **Why it's hidden**: why no one questions it
3. **Evidence**: what evidence supports (or fails to support) this assumption

Goal: find at least 6-8 assumptions, from the most obvious to the deepest.
```

### Step 3: Agent 2 — Classifier (rank by impact x certainty)

**Agent 2 prompt:**
```
You are a strategic risk analyst. You have received a list of hidden assumptions for: "{subject}"

## Identified assumptions
{Agent 1 output}

Classify each assumption along two dimensions:

**IMPORTANCE** (if this assumption is wrong, how much impact does it have?):
- CRITICAL: the plan/strategy collapses entirely
- HIGH: requires significant changes
- MEDIUM: requires adjustments
- LOW: marginal impact

**CERTAINTY** (how sure are we that it's true?):
- VERIFIED: solid data confirms it
- PROBABLE: reasonably sure but not verified
- UNCERTAIN: could go either way
- FRAGILE: based on hope more than on evidence

## Required output

### ASSUMPTIONS MATRIX

| # | Assumption | Importance | Certainty | Inversion priority |
|---|-----------|-----------|---------|---------------------|
| 1 | ... | CRITICAL | FRAGILE | MAXIMUM |
| ... | ... | ... | ... | ... |

### TOP 3-4 FOR INVERSION
[The assumptions combining CRITICAL/HIGH importance + UNCERTAIN/FRAGILE certainty — these are the most dangerous and should be inverted first]
```

**In QUICK mode:** launch Agents 1 and 2 sequentially, then proceed to Step 4.

**In DEEP mode:** after Agent 2, show the matrix to the user and ask:
```
Here is the assumptions map. Which ones do you want to invert?
The top {N} by risk are marked. Do you want to proceed with these or choose others?
```

### Step 4: Agent 3 — Inverter (explore what if assumptions are false)

**QUICK mode: single inverter for top 3-4 assumptions**

```
lens_compose_prompt(
  topic=subject,
  constraints=[
    {"type": "assumption_reversal", "assumption": "[top assumption]", "reversed": "[inverted version]"},
    {"type": "inversion"}
  ],
  output_format="raw",
  intensity=intensity
)
```

**Agent 3 prompt:**
```
{system_prompt}

ORIGINAL STRATEGY: {subject}

ASSUMPTIONS TO INVERT (from the most dangerous):

{For each top assumption from Agent 2:}
### Assumption {N}: {assumption}
**Inversion**: {what if the opposite is true?}

For EACH inversion, explore:
1. **Scenario**: if this assumption is FALSE, what happens to the strategy?
2. **Signals**: what signals would we already see TODAY if the inversion were true?
3. **Adaptation**: how should we modify the strategy to be robust in this case too?
4. **Opportunity**: does the inversion open unexpected opportunities?
```

**DEEP mode: one agent per assumption (parallel)**

For each selected assumption, launch a dedicated agent with `assumption_reversal` constraint set to that specific assumption. Launch all in parallel. Then a synthesizer cross-analyzes.

**DEEP mode synthesizer prompt:**
```
You are the synthesizer of an Assumption Inversion Lens. You have seen {N} independent inversions for: "{subject}"

{For each inversion agent output}

## Cross-inversion analysis

### PATTERNS
[What patterns emerge from the inversions? Are there correlated assumptions that collapse together?]

### MOST DANGEROUS ASSUMPTION
[Which single assumption, if false, causes the greatest damage? Why?]

### VERIFICATION PLAN
[For each critical assumption: what to do CONCRETELY to verify it in the next 30 days?]

### ROBUST STRATEGY
[How to modify the strategy to be less dependent on the most fragile assumptions?]
```

### Step 5: Present output

```markdown
# Assumption Map — {subject}

> Mode: {QUICK/DEEP} | Assumptions found: {N} | Inverted: {M} | Intensity: {intensity}/5

## Assumptions matrix

{Agent 2 matrix}

## Inversions

{Agent 3 output (QUICK) or Synthesizer output (DEEP)}

---

### Assumptions detail

<details>
<summary>Full assumptions list (Agent 1)</summary>
{Agent 1 full output}
</details>

<details>
<summary>Classification (Agent 2)</summary>
{Agent 2 full output}
</details>

---
*Lens Assumptions | {QUICK/DEEP} | {N} assumptions | Intensity: {intensity}/5*
```

### Step 6: Save session

```
lens_session_save(topology="assumption_inversion", topic=subject, agents_count=3 or more, rounds_count=1 or 2, output=full_report)
```

## Examples

**User:** `/lens-assumptions "Our growth strategy relies on acquiring 3 enterprise clients at 100k+/year"`
- QUICK mode: surfaces assumptions, classifies, inverts top 3
- Might find: "assumes the enterprise market is accessible without a dedicated sales team"

**User:** `/lens-assumptions "We're betting everything on the Italian market for the next 2 years" --deep`
- DEEP mode: full exploration, user chooses which assumptions to invert
- Dedicated agent per assumption, cross-analysis

**User:** `/lens-assumptions "Our competitive advantage is service quality" --intensity 5 --focus "market assumptions"`
- Maximum intensity, focused on market-related assumptions
- Will be relentless in surfacing uncomfortable truths

## The Importance-Certainty matrix

```
                    CERTAINTY
                FRAGILE ←——→ VERIFIED
    CRITICAL |  DANGER!  |  PILLAR    |
IMPORTANCE   |  Invert    |  Monitor   |
             |  now       |            |
    LOW      |  NOISE    |  NON-ISSUE |
             |  Ignore    |  Ignore    |
```

The top-left (CRITICAL + FRAGILE) quadrant contains the assumptions that can kill your strategy. These get inverted first.

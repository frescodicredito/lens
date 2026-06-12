---
id: c66a95b8-932b-4151-a65d-38bd5b13775a
name: lens-steelman
description: >
  Build the strongest possible version of any argument, then stress-test it.
  QUICK mode: 2-4 minutes.
  Steelman Chain: 3 agents progressively strengthen the argument,
  then 1-2 adversarial agents attack the strongest version.
version: 0.1.0
tags: [lens, cognitive, steelman, chain, quick]
---

# Lens Steelman — QUICK Mode

**Build the strongest version of any argument, then find what still breaks.**

Steelman Chain topology: multiple agents progressively strengthen an argument, then adversarial agents attack the fortified version. What survives the strongest attack on the strongest defense is genuinely robust.

## When to use

- You need to build the most convincing case for a position
- You want to prepare for objections by finding them first
- You need to present an argument that can withstand hostile scrutiny
- You want to separate "strong on the surface" from "genuinely robust"

## How it works

1. User provides an **argument or position** to strengthen
2. Phase 1 (Build): 2-3 agents progressively strengthen the argument
3. Phase 2 (Test): 1-2 agents attack the strongest version
4. Output: the fortified argument + surviving objections

## Execution

### Step 1: Parse input

Extract from the user's message:
- **argument**: the position, claim, or proposal to steelman (required)
- **intensity**: 1-5, how hard the adversarial phase pushes (default: 4)
- **build_depth**: 2-3, number of strengthening rounds (default: 2)
- **focus**: optional focus area (e.g., "focus on data and evidence", "focus on emotional appeal")

### Step 2: Phase 1 — Build (sequential strengthening)

Each agent receives the previous output and makes it stronger.

**Agent 1 — Foundation Builder:**
```
lens_compose_prompt(
  topic=argument,
  constraints=[
    {"type": "steelman"},
    {"type": "limit", "constraint": "at most 5 arguments, each with a concrete data point or a specific example"}
  ],
  output_format="perspective_card",
  intensity=intensity
)
```

Launch Agent 1 as Task subagent (subagent_type: "general-purpose").

**Agent 1 prompt:**
```
{system_prompt from lens_compose_prompt}

ARGUMENT TO STRENGTHEN:
{argument}

Build the strongest possible version of this argument. Every point must be supported by concrete evidence, data, or rigorous logical reasoning.
```

Wait for Agent 1 output, then...

**Agent 2 — Reinforcer:**
```
lens_compose_prompt(
  topic="[Agent 1 output will be inserted]",
  constraints=[
    {"type": "steelman"},
    {"type": "elm_route", "route": "central", "focus": "logical rigor and evidence quality"}
  ],
  output_format="raw",
  intensity=intensity,
  extra_instructions="You have received an already-built defense. Your task: (1) find the weakest points and STRENGTHEN them, (2) add missing evidence, (3) anticipate objections and include preemptive counter-arguments, (4) make the argumentative structure unassailable."
)
```

**Agent 2 prompt:**
```
{system_prompt}

DEFENSE TO STRENGTHEN:
---
{Agent 1's output}
---

Improve this defense. Don't repeat: strengthen the weak points, add evidence, anticipate objections.
```

Wait for Agent 2 output.

**Agent 3 — Final Strengthener (if build_depth=3):**
Same pattern, focusing on rhetorical coherence and closing any remaining gaps. Use constraints: `steelman` + `modal` with mode "only strengthening, zero concessions".

### Step 3: Phase 2 — Test (adversarial attack on strongest version)

**Agent A — Primary Attacker:**
```
lens_compose_prompt(
  topic="[Strongest version from Phase 1]",
  constraints=[
    {"type": "inversion"},
    {"type": "abductive"}
  ],
  output_format="raw",
  intensity=intensity,
  extra_instructions="This is the STRONGEST version of the argument, already reinforced by 2 experts. Your task: find flaws even in the fortified version. Look for: undeclared assumptions, cherry-picked evidence, masked logical leaps, scenarios where the argument collapses."
)
```

**Agent A prompt:**
```
{system_prompt}

FORTIFIED ARGUMENT (version reinforced by {build_depth} experts):
---
{Final Phase 1 output}
---

This argument has already been strengthened to the maximum. Find the flaws anyway.
```

Wait for Agent A output.

**Agent B — Final Verdict (optional, when intensity >= 4):**

A judge that evaluates what survived the attack on the steelmanned version.

**Agent B prompt:**
```
You are an impartial judge. You have seen an argument built in its strongest version and then attacked by a hostile critic.

ORIGINAL ARGUMENT: {argument}

STRENGTHENED VERSION:
---
{Final Phase 1 output}
---

ATTACK ON THE STRENGTHENED VERSION:
---
{Agent A's output}
---

Produce your verdict:

## FORTIFIED ARGUMENT
[The final version of the argument, incorporating the defenses that withstood the attack]

## RESIDUAL VULNERABLE POINTS
[Weaknesses that remain even in the strongest version]

## OBJECTIONS TO PREPARE FOR
[The 3-5 most likely objections someone will raise, with suggested responses]

## CONFIDENCE
[How robust is this argument after the process? High/Medium/Low, with explanation]
```

### Step 4: Present output

```markdown
# Steelman Chain — {argument}

> Build depth: {build_depth} | Attack intensity: {intensity}/5

## Fortified argument
{Final strengthened version or Agent B's "FORTIFIED ARGUMENT" section}

## Residual vulnerable points
{From Agent A attack or Agent B verdict}

## Objections to prepare for
{From Agent B if present, or extracted from Agent A's attack}

---

### Process

<details>
<summary>Phase 1 — Build ({build_depth} rounds)</summary>

**Round 1 — Foundation:**
{Agent 1 output}

**Round 2 — Reinforcement:**
{Agent 2 output}

</details>

<details>
<summary>Phase 2 — Stress test</summary>

**Attack:**
{Agent A output}

**Verdict:** (if present)
{Agent B output}

</details>

---
*Lens Steelman | Chain depth: {build_depth} + attack | Intensity: {intensity}/5*
```

### Step 5: Save session

```
lens_session_save(topology="steelman_chain", topic=argument, agents_count=build_depth+1 or +2, rounds_count=2, output=full_report)
```

## Examples

**User:** `/lens-steelman "Generative AI is a sustainable competitive advantage for creative agencies"`
- Build depth 2, intensity 4 (default)
- 2 agents strengthen, 1 attacks, 1 judges

**User:** `/lens-steelman "We should turn down clients below 50k/year" --intensity 5`
- Maximum attack intensity on the fortified version
- 4 agents total: 2 build + 1 attack + 1 judge

**User:** `/lens-steelman "Remote-first beats the office for productivity" --build-depth 3 --focus "data and research"`
- 3 strengthening rounds focused on empirical evidence
- Then adversarial test

## Why Steelman Chain > Simple Steelman

A single steelman agent builds a decent case. But it misses:
- **Weak spots it doesn't see**: a second agent catches what the first missed
- **Anticipation of attacks**: the reinforcer thinks adversarially while building
- **Genuine robustness**: only tested arguments survive the final attack

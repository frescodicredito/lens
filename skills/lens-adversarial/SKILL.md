---
id: aa9f8992-d9a8-47cf-b788-50009385a387
name: lens-adversarial
description: >
  Stress-test a claim through adversarial cascade. QUICK mode: 1-3 minutes.
  Each agent attacks the output of the previous one, progressively stripping away
  weak arguments until only the surviving core remains.
version: 0.1.0
tags: [lens, cognitive, adversarial, cascade, stress-test, quick]
---

# Lens Adversarial — QUICK Mode

**Stress-test any claim** through an adversarial cascade. Each agent attacks the previous one's output. What survives is the robust core.

## When to use

- You have a claim, strategy, or decision you want to stress-test
- You want to find the weaknesses in an argument before presenting it
- You need a devil's advocate that actually pushes back hard
- You want to separate conviction from confidence

## How it works

1. The user provides a **claim** to stress-test
2. Agent 1 (Thesis): articulates and defends the claim
3. Agent 2 (Antithesis): attacks Agent 1's defense with maximum force
4. Agent 3 (Synthesis): evaluates what survived, what fell, and what the surviving core is
5. Optional: deeper cascades (4+ agents) for more thorough stress-testing

## Execution

### Step 1: Parse input

Extract from the user's message:
- **claim**: the statement, strategy, or decision to stress-test (required)
- **intensity**: 1-5, how aggressive the attack (default: 3)
- **depth**: 2-4, number of cascade agents (default: 3 = thesis + antithesis + synthesis)
- **focus**: optional attack angle (e.g., "focus on financial viability", "focus on technical feasibility")

### Step 2: Compose prompts for each agent

Use the Lens MCP server to compose prompts for each cascade stage:

**Agent 1 — Thesis (Defender):**
```
lens_compose_prompt(
  topic=claim,
  constraints=[{"type": "steelman"}],
  output_format="perspective_card",
  intensity=intensity
)
```

**Agent 2 — Antithesis (Attacker):**
```
lens_compose_prompt(
  topic="[Agent 1's output will be inserted here]",
  constraints=[
    {"type": "inversion"},
    {"type": "abductive"}
  ],
  output_format="perspective_card",
  intensity=intensity,
  extra_instructions="Attack EVERY point of the previous defense. Find logical flaws, missing evidence, undeclared assumptions. Concede nothing."
)
```

**Agent 3 — Synthesis (Judge):**
```
lens_compose_prompt(
  topic="[All previous outputs will be inserted here]",
  constraints=[
    {"type": "elm_route", "route": "central", "focus": "logical quality of the arguments"}
  ],
  output_format="raw",
  intensity=3,
  extra_instructions="Evaluate the debate. Identify: (1) points of the thesis that survived the attack, (2) demolished points, (3) the surviving core, (4) the unresolved objections."
)
```

**Optional Agent 4 — Deep Attack (depth=4):**
A second attacker that targets the synthesis itself, looking for confirmation bias in the judge.

### Step 3: Execute cascade sequentially

Launch agents in sequence using the Task tool (subagent_type: "general-purpose").

**CRITICAL**: Each agent receives the output of the previous one. This is a sequential cascade, NOT parallel.

**Agent 1 prompt:**
```
{system_prompt from Step 2, Agent 1}

CLAIM TO DEFEND:
{claim}
```

Wait for Agent 1 output, then...

**Agent 2 prompt:**
```
{system_prompt from Step 2, Agent 2}

DEFENSE TO ATTACK:
---
{Agent 1's full output}
---

Attack every point. Make no concessions.
```

Wait for Agent 2 output, then...

**Agent 3 prompt:**
```
You are an impartial judge. Evaluate the following debate with logical rigor.

ORIGINAL CLAIM: {claim}

DEFENSE (Agent 1):
---
{Agent 1's output}
---

ATTACK (Agent 2):
---
{Agent 2's output}
---

Produce your verdict in the following format:

## SURVIVING CORE
[What of the original thesis withstood the attack? Why?]

## DEMOLISHED POINTS
[What fell under the attack? Why?]

## UNRESOLVED OBJECTIONS
[Which of the attacker's critiques remain unanswered?]

## VERDICT
[Is the original claim robust / partially robust / fragile?]
[1-2 sentences with the overall assessment]
```

### Step 4: Present output

Present a structured **Cascade Report** showing:

```markdown
# Adversarial Cascade — {claim}

> Intensity: {intensity}/5 | Depth: {depth} agents

---

## Round 1 — Defense
{Agent 1 output}

---

## Round 2 — Attack
{Agent 2 output}

---

## Verdict
{Agent 3 output}

---
*Lens Adversarial | Cascade depth: {depth} | Intensity: {intensity}/5*
```

### Step 5: Save session

```
lens_session_save(topology="cascade", topic=claim, agents_count=depth, rounds_count=1, output=full_report)
```

## Examples

**User:** `/lens-adversarial "Generative AI will make creative agencies obsolete within 3 years"`
- Depth 3, intensity 3 (default)
- Agent 1 defends, Agent 2 attacks, Agent 3 judges

**User:** `/lens-adversarial "We should invest 500k in a rebrand" --intensity 5`
- Maximum attack intensity
- Agent 2 will be merciless

**User:** `/lens-adversarial "Our competitive advantage is customer service" --depth 4 --focus "long-term sustainability"`
- 4 agents, focused attack on long-term sustainability
- Agent 4 attacks the judge's synthesis

## Intensity guide

- **1**: Constructive criticism, raises reasonable doubts
- **2**: Firm pushback, challenges evidence quality
- **3**: Aggressive attack, no concessions (default)
- **4**: Hostile cross-examination, assumes bad faith
- **5**: Demolition mode, searches for fatal flaws with maximum force

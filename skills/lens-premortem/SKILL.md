---
id: 415fea2c-2d56-401f-9330-f76afde229aa
name: lens-premortem
description: >
  Structured premortem analysis on any project or decision.
  QUICK mode: 1-3 minutes.
  Multiple agents with different failure lenses produce independent failure scenarios,
  then a synthesizer builds a risk map.
version: 0.1.0
tags: [lens, cognitive, premortem, risk, quick]
---

# Lens Premortem — QUICK Mode

**It's 2028. Your project failed. Reconstruct why.**

Structured premortem using Gary Klein's Prospective Hindsight technique, enhanced with diverse cognitive constraints so each agent sees different failure modes.

## When to use

- Before committing to a major decision or investment
- To stress-test a project plan or strategy
- When you suspect optimism bias is hiding risks
- Before a launch, pivot, or major resource allocation

## How it works

1. User provides a **project/decision** to premortem
2. 3-4 agents independently imagine the project has FAILED, each with different failure lenses
3. A synthesizer aggregates into a risk map
4. Output: failure scenarios + risk map + blind spots

## Execution

### Step 1: Parse input

Extract from the user's message:
- **project**: the project, decision, or strategy to premortem (required)
- **horizon**: how far in the future (default: "2028")
- **intensity**: 1-5 (default: 4 — premortem should push hard)

### Step 2: Configure 3-4 failure agents

Each agent gets the same premortem temporal constraint PLUS a different failure lens:

**Agent 1 — Execution Failure:**
```json
[
  {"type": "premortem", "date": "{horizon}"},
  {"type": "modal", "mode": "only execution failures: delays, incompetence, insufficient resources, technical errors"}
]
```

**Agent 2 — Market/External Failure:**
```json
[
  {"type": "premortem", "date": "{horizon}"},
  {"type": "modal", "mode": "only external failures: shifted market, competitors, regulation, economic shocks"}
]
```

**Agent 3 — Strategic Failure:**
```json
[
  {"type": "premortem", "date": "{horizon}"},
  {"type": "assumption_reversal", "assumption": "[key project assumption]", "reversed": "[inversion]"}
]
```

**Agent 4 (optional) — Human/Organizational Failure:**
```json
[
  {"type": "premortem", "date": "{horizon}"},
  {"type": "modal", "mode": "only human and organizational failures: conflicts, turnover, burnout, cultural misalignment, internal politics"}
]
```

### Step 3: Compose and launch agents in parallel

For each agent, call `lens_compose_prompt` with the respective constraints, topic=project, output_format="perspective_card", intensity=4.

Launch ALL agents in parallel using the Task tool (subagent_type: "general-purpose"). They are independent — this is a Star topology, Round 1 must be independent (Surowiecki).

**Each agent prompt:**
```
{system_prompt from lens_compose_prompt}
```

### Step 4: Synthesize into Risk Map

After all agents return, launch a final synthesizer agent with this prompt:

```
You are the synthesizer of a structured premortem. You have received {N} independent failure scenarios for the project: "{project}".

## Scenarios received

### Scenario 1 — Execution failure
{Agent 1 output}

### Scenario 2 — External failure
{Agent 2 output}

### Scenario 3 — Strategic failure
{Agent 3 output}

### Scenario 4 — Organizational failure
{Agent 4 output, if used}

## Your task

Produce a RISK MAP in the following format:

### CONVERGENT RISKS
[Risks that emerge in 2+ scenarios — these are the most likely]

### CATASTROPHIC RISKS
[Risks that appear in only one scenario but would have devastating impact]

### MAIN CAUSAL CHAIN
[The most plausible sequence of events leading to failure]

### EARLY WARNING SIGNALS
[What to monitor in the next 3-6 months to intercept these risks]

### PREVENTIVE ACTIONS
[3-5 concrete actions to take NOW to reduce the identified risks]
```

### Step 5: Present output

```markdown
# Premortem — {project}

> Horizon: {horizon} | Agents: {N} | Intensity: {intensity}/5

{Synthesizer output}

---

### Individual scenarios

<details>
<summary>Scenario 1 — Execution failure</summary>
{Agent 1 output}
</details>

<details>
<summary>Scenario 2 — External failure</summary>
{Agent 2 output}
</details>

<details>
<summary>Scenario 3 — Strategic failure</summary>
{Agent 3 output}
</details>

---
*Lens Premortem | {N} agents | Intensity: {intensity}/5*
```

### Step 6: Save session

```
lens_session_save(topology="star", topic=project, agents_count=N+1, rounds_count=1, output=full_report)
```

## Examples

**User:** `/lens-premortem "Launch of the new B2B SaaS product in March"`
- 4 agents: execution, market, strategic, organizational
- Horizon: 2028 (default)

**User:** `/lens-premortem "Migration to microservices" --horizon 2027`
- Custom horizon
- Agent 3 inverts the assumption "microservices improve velocity"

**User:** `/lens-premortem "Hiring 20 people in the next 6 months" --intensity 5`
- Maximum intensity
- Agents will be merciless in finding failure modes

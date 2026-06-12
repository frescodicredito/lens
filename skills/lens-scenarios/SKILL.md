---
id: 6b388e82-9538-449c-89d0-8f2f72697225
name: lens-scenarios
description: >
  Strategic scenario planning using Scenario Matrix topology.
  DEEP mode: 5-15 minutes, interactive.
  2 critical uncertainties generate 4 quadrants, each explored by a dedicated agent.
  Synthesizer identifies robust strategies that work across scenarios.
version: 0.1.0
tags: [lens, cognitive, scenarios, matrix, strategic-planning, deep]
---

# Lens Scenarios — DEEP Mode

**Explore 4 possible futures. Find strategies that work in all of them.**

Scenario Matrix topology: identify 2 critical uncertainties, generate 4 quadrants, assign an agent to each scenario. A synthesizer identifies strategies robust across all scenarios.

Based on Shell/Schwartz Scenario Planning and CIA Quadrant Crunching.

## When to use

- You face a strategic decision with significant uncertainty
- You want to plan for multiple possible futures
- You need to find strategies that are robust regardless of what happens
- You want to stress-test a plan against different market/tech/regulatory scenarios

## How it works

1. User provides a **strategic question** and optionally the **2 key uncertainties**
2. If uncertainties not provided, Lens identifies them
3. 2 axes x 2 poles = 4 scenarios (quadrants)
4. Round 1: 4 agents explore one scenario each, independently
5. Round 2: synthesizer identifies cross-scenario patterns and robust strategies
6. Output: scenario descriptions + robust strategies + early signals

## Execution

### Step 1: Parse input and identify uncertainties

Extract from the user's message:
- **question**: the strategic question or decision (required)
- **uncertainty_1**: first critical uncertainty axis (optional)
- **uncertainty_2**: second critical uncertainty axis (optional)
- **horizon**: time horizon for scenarios (default: "3-5 years")
- **intensity**: 1-5 (default: 3)

**If uncertainties are NOT provided**, identify them:

Present to the user:
```
To build the scenario matrix, we need 2 critical uncertainties.

I suggest:
1. **{uncertainty_1}**: {pole_a} vs {pole_b}
2. **{uncertainty_2}**: {pole_a} vs {pole_b}

This generates 4 scenarios:
- Q1: {u1_pole_a} + {u2_pole_a}
- Q2: {u1_pole_a} + {u2_pole_b}
- Q3: {u1_pole_b} + {u2_pole_a}
- Q4: {u1_pole_b} + {u2_pole_b}

Shall I proceed with these uncertainties or do you want to change them?
```

**Selection criteria for good uncertainties:**
- High impact on the decision
- Genuinely uncertain (not predictable)
- Independent from each other (not correlated)
- Binary or at least bipolar (clear extremes)

### Step 2: Define the 4 scenarios

Name each quadrant with an evocative name that captures its essence:

| | {Uncertainty 2: Pole A} | {Uncertainty 2: Pole B} |
|---|---|---|
| **{Uncertainty 1: Pole A}** | Q1: {evocative_name} | Q2: {evocative_name} |
| **{Uncertainty 1: Pole B}** | Q3: {evocative_name} | Q4: {evocative_name} |

### Step 3: Round 1 — Explore scenarios independently

For each scenario, compose a dedicated agent prompt:

**Agent Q1:**
```
lens_compose_prompt(
  topic=question,
  constraints=[
    {"type": "temporal", "value": "{horizon from now}"},
    {"type": "assumption_reversal", "assumption": "[current baseline]", "reversed": "[Q1 conditions]"},
    {"type": "modal", "mode": "only consequences of this scenario, no alternatives"}
  ],
  output_format="perspective_card",
  intensity=intensity
)
```

**Each agent prompt:**
```
{system_prompt from lens_compose_prompt}

## Scenario: {quadrant_name}

It's {horizon}. The following conditions have occurred:
- {Uncertainty 1}: {pole for this quadrant}
- {Uncertainty 2}: {pole for this quadrant}

In this world:
1. How did the situation evolve?
2. Which decisions turned out to be winners?
3. Which decisions turned out to be disastrous?
4. Which early signals (visible ALREADY TODAY) would have predicted this scenario?
5. What is the optimal strategy in this world?
```

Launch ALL 4 agents **in parallel** using the Task tool (subagent_type: "general-purpose").

**CRITICAL — INDEPENDENCE**: In Round 1, each agent explores ONLY its own scenario. No agent sees other scenarios. This ensures genuine diversity.

Show Round 1 results to user with the matrix layout. Ask: "Do you want to proceed with the cross-scenario synthesis or do you have questions about a specific scenario?"

### Step 4: Round 2 — Cross-scenario synthesis

Launch a synthesizer agent:

```
You are the synthesizer of a Scenario Matrix Lens. You have received 4 independent scenarios for the strategic question: "{question}"

## Matrix

| | {U2 Pole A} | {U2 Pole B} |
|---|---|---|
| **{U1 Pole A}** | Q1: {name} | Q2: {name} |
| **{U1 Pole B}** | Q3: {name} | Q4: {name} |

## Scenario Q1 — {name}
{Agent Q1 output}

## Scenario Q2 — {name}
{Agent Q2 output}

## Scenario Q3 — {name}
{Agent Q3 output}

## Scenario Q4 — {name}
{Agent Q4 output}

## Your task

Produce a CROSS-SCENARIO ANALYSIS in the following format:

### ROBUST STRATEGIES
[Actions/decisions that work in 3+ scenarios out of 4. These are the safe bets.]

### ASYMMETRIC BETS
[Actions with limited downside but enormous upside in 1-2 specific scenarios. Worth the risk?]

### STRATEGIES TO AVOID
[Actions that look good but fail in 2+ scenarios. These are traps.]

### EARLY SIGNALS
[For each scenario, which indicators to monitor in the next 6-12 months to understand which quadrant we're heading toward?]

### ADAPTIVE PLAN
[A strategy that starts with the robust actions and includes triggers to pivot toward scenario-specific strategies when the signals become clear.]
```

### Step 5: Present output

```markdown
# Scenario Matrix — {question}

> Horizon: {horizon} | Uncertainties: {u1} x {u2} | Intensity: {intensity}/5

## The Matrix

| | {U2 Pole A} | {U2 Pole B} |
|---|---|---|
| **{U1 Pole A}** | **Q1: {name}** | **Q2: {name}** |
| **{U1 Pole B}** | **Q3: {name}** | **Q4: {name}** |

---

## Cross-scenario analysis

{Synthesizer output}

---

## Individual scenarios

### Q1 — {name}
{Q1 agent output}

### Q2 — {name}
{Q2 agent output}

### Q3 — {name}
{Q3 agent output}

### Q4 — {name}
{Q4 agent output}

---
*Lens Scenarios | Scenario Matrix | 4 + 1 agents | Intensity: {intensity}/5*
```

### Step 6: Save session

```
lens_session_save(topology="scenario_matrix", topic=question, agents_count=5, rounds_count=2, output=full_report)
```

## Examples

**User:** `/lens-scenarios "Should we invest in a proprietary AI product or resell third-party solutions?"`
- Auto-identify uncertainties (e.g., "speed of AI commoditization" x "market willingness-to-pay")
- 4 scenarios + cross-scenario analysis

**User:** `/lens-scenarios "Expansion into Germany over the next 2 years" --uncertainty1 "European economy: growth vs recession" --uncertainty2 "AI regulation: permissive vs restrictive"`
- Explicit uncertainties provided
- 4 scenarios explore combinations

**User:** `/lens-scenarios "Which pricing model to adopt for the new SaaS?" --horizon "2028" --intensity 4`
- Custom horizon
- Higher intensity means more extreme scenario exploration

## Good vs Bad uncertainties

**Good uncertainties:**
- "Commoditized AI vs differentiating AI" — genuinely uncertain, high impact
- "Growing vs contracting market" — independent from AI, high impact
- "Tight regulation vs laissez-faire" — genuinely uncertain

**Bad uncertainties:**
- "The sun rises tomorrow vs it doesn't" — not uncertain
- "Competitor enters vs doesn't enter" — too binary/simplistic
- "AI improves vs AI worsens" — correlated with everything, not independent

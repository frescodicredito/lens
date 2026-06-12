---
id: 694c9eee-29eb-4af8-8fea-3c4c048f77bc
name: lens
description: >
  Main Lens skill — cognitive infrastructure for LLM reasoning.
  Multi-agent structured analysis: suggests topology, configures agents with
  cognitive constraints, runs QUICK (parallel/sequential) or DEEP (multi-round
  interactive) sessions. Entry point for the full Lens system.
  Produces Field Maps, Cascade Reports, and Perspective Cards.
  Best for: multi-perspective decisions, stress-testing ideas, stakeholder
  simulation, strategic exploration, creative ideation.
  When unsure which Lens topology to use, start here.
metadata:
  id: 694c9eee-29eb-4af8-8fea-3c4c048f77bc
  version: 0.2.0
  tags: [lens, cognitive, constraints, multi-agent, deep, interactive]
---

# Lens — Main Interactive Skill

**The entry point for Lens cognitive infrastructure.**

Lens navigates the tails of the LLM distribution through structural constraints. This skill is the orchestrator: it understands your problem, suggests the right topology, configures agents with constraints, and runs the session.

## When to use

- `/lens` for the full interactive experience (topic → topology suggestion → execution → output)
- `/lens` when you don't know which topology fits or want guidance
- Delegate to specific skills when the user already knows what they want:
  - `/lens-perspective` — single constrained perspective (30-60 sec)
  - `/lens-adversarial` — stress-test a claim through cascading attacks
  - `/lens-premortem` — what could go wrong analysis
  - `/lens-focus-group` — simulated stakeholder discussion
  - `/lens-deep` — deep sequential chain on a single hypothesis
  - `/lens-steelman` — build and then attack the strongest argument
  - `/lens-assumptions` — uncover and invert hidden assumptions
  - `/lens-scenarios` — strategic scenario planning

## How it works

1. User provides a **topic** (or Lens asks for it)
2. Lens analyzes the topic and suggests the best topology
3. User confirms or adjusts
4. Lens configures agents with constraints
5. Execution: QUICK (Task subagents in parallel/sequence) or DEEP (interactive rounds)
6. Output: structured format (Perspective Card, Field Map, Cascade Report)

## Execution

### Step 1: Understand the topic

If the user provides a clear topic, proceed. If vague, ask:
- "What is the topic or decision to analyze?"
- "What do you want to achieve? (stress-test an idea, explore perspectives, analyze risks, generate creative ideas, find blind spots)"

### Step 2: Suggest topology

Based on the topic and goal, suggest 1-2 topologies from the mapping below:

| Goal | Topology | Mode | Agents |
|------|----------|------|--------|
| Stress-test a claim | `cascade` | QUICK | 2-4 |
| Multiple perspectives | `star` | DEEP | 3-6 |
| Risk analysis / premortem | `premortem` | QUICK | 3-4 |
| Find weaknesses | `adversarial_jury` | DEEP | 5 |
| Creative ideas / innovation | `bisociation_engine` or `ring` | QUICK/DEEP | 3-4 |
| Build strongest argument | `steelman_chain` | QUICK | 3-5 |
| Uncover assumptions | `socratic_drill` or `assumption_inversion` | QUICK | 2-4 |
| Explore future scenarios | `scenario_matrix` | DEEP | 4-5 |
| Balance emotion and logic | `wise_mind` | QUICK | 3 |
| Systematic ideation | `scamper_parallel` | DEEP | 7 |
| Full structured analysis | `parallel_hats` | QUICK | 4-6 |
| Focus group simulation | `star` with personas | DEEP | 4-6 |

Present the suggestion briefly:
```
For this topic I suggest the **[name]** topology: [1-line description].
[N] agents, [mode]. Shall I proceed?
```

If the user wants something different, adjust.

### Step 3: Configure agents

For each agent in the topology, compose a system prompt that includes:

1. **Role assignment** — what this agent's perspective is
2. **Constraints** (2-3 per agent) — structural thinking constraints from the library below
3. **Output format** — what structure the agent should produce

**Constraint selection guidelines:**
- Each agent should have 2-3 constraints (not more — diminishing returns)
- Maximize cognitive diversity between agents (different constraint types)
- At least one agent should have `inversion` or `abductive` (to challenge the obvious)
- For persona-based topologies, define the persona's background, expertise, and cognitive biases

**Agent prompt template:**
```
You are [role] analyzing: [topic]

Your cognitive constraints for this analysis:
- [constraint 1]: [what it means CONCRETELY for this specific topic]
- [constraint 2]: [what it means CONCRETELY for this specific topic]

Produce your analysis as a Perspective Card:
1. Your constrained analysis (be specific, use numbers and examples where possible)
2. **Key insight:** [1-sentence core insight that this constraint uniquely reveals]
3. **Confidence:** [high/medium/low]

Take a clear position. Do not hedge. If your constraint forces an uncomfortable
conclusion, state it directly.
```

The key to good Lens output is making constraints CONCRETE to the topic. "Argue the
opposite" is weak. "Argue that in-housing marketing destroys more value than it creates
because [specific mechanism]" is strong. Always translate abstract constraints into
specific analytical tasks for the topic at hand.

### Step 4: Execute

**QUICK mode** (cascade, steelman_chain, parallel_hats, wise_mind, bisociation_engine, socratic_drill, assumption_inversion, premortem):
- Launch agents as Task subagents (subagent_type: "general-purpose")
- Sequential topologies (cascade, steelman_chain): launch in sequence, each receives previous output
- Parallel topologies (parallel_hats, scamper_parallel): launch all in parallel, then synthesize

**DEEP mode** (star, adversarial_jury, scenario_matrix, ring, scamper_parallel):
- Round 1: launch all agents in parallel (independence mandatory — no agent sees others' output)
- Show Round 1 results to user
- Ask if they want to continue to Round 2 (cross-pollination)
- Round 2 (cross-pollination): each agent receives ALL Round 1 outputs and writes a brief response — agreeing, disagreeing, or building on others' points. This is where the real value emerges: agents challenge each other's assumptions and generate insights that no single perspective could produce alone.
- Synthesizer: a final agent reads all rounds and produces the Field Map

### Step 5: Format and present output

Based on the topology, use the appropriate output format:

**Perspective Card** (single agent or simple topologies):
```markdown
## Perspective Card — [constraint/role]

**Topic:** [topic]
**Constraint:** [constraint type]

[Analysis content]

**Key insight:** [1-sentence core insight]
**Confidence:** [high/medium/low]
```

**Field Map** (multi-agent parallel topologies — star, parallel_hats):
```markdown
# Field Map — [topic]

## Convergences
[Points where multiple agents agree]

## Divergences
[Points of genuine disagreement between agents]

## Outliers
[Surprising or unique insights from individual agents]

## Synthesis
[Integration of the field — what the collective analysis reveals]
```

**Cascade Report** (sequential/adversarial topologies):
```markdown
# Cascade Report — [topic]

## Round 1 — [agent/constraint]
[Output]

## Round 2 — [agent/constraint]
[Output, building on or attacking Round 1]

[...all rounds...]

## Surviving Core
[What remains standing after all rounds of analysis]
```

Always add footer:
```
---
*Lens | Topology: {name} | Agents: {N} | Intensity: {intensity}/5*
```

## Constraint library — Quick reference

> **Authoritative source:** call `lens_list_constraints()` for the full, current list (25 constraints across 7 categories) and `lens_get_constraint(constraint_id)` for the complete definition of any one. The table below is a non-exhaustive subset for quick orientation — do not treat it as the canonical inventory.

A few representative constraints (each forces a specific thinking pattern):

| Constraint | Effect | Example use |
|-----------|--------|-------------|
| `inversion` | Argue the opposite of the obvious position | Challenge conventional wisdom |
| `temporal` | Analyze from a different time perspective (5y ago, 10y future) | Strategic foresight |
| `exclusion` | Ban specific words/concepts to force fresh language | Avoid jargon, find new frames |
| `bisociative` | Force collision with an alien domain | Innovation, creative connections |
| `defamiliarize` | Describe as if seeing for the first time | Uncover hidden assumptions |
| `abductive` | Only non-obvious explanations allowed | Root cause analysis |
| `premortem` | It already failed — explain why | Risk identification |
| `steelman` | Build the strongest possible version of the argument | Rigorous argumentation |
| `assumption_reversal` | Invert a key assumption and explore consequences | Challenge the status quo |
| `role` | Specific professional role with cognitive biases | Stakeholder simulation |
| `anti_sycophancy` | Actively resist agreeable/confirming responses | Honest critical assessment |
| `concept_fan` | De Bono's concept fan: purpose → concepts → specific ideas | Structured ideation |

## Examples

**User:** `/lens "Should we adopt AI for customer support?"`
- Lens suggests: Star/Delphi (multi-perspective, DEEP)
- 4 agents: CTO (technical feasibility + steelman), Customer (defamiliarize + role), CFO (inversion + temporal), Competitor analyst (abductive + bisociative)
- 2 rounds → Field Map

**User:** `/lens "Our positioning is 'AI infrastructure for creative agencies'" --quick`
- Lens suggests: Cascade (stress-test, QUICK)
- 3 agents: steelman → inversion attack → synthesis
- Sequential cascade → Cascade Report with surviving core

**User:** `/lens "Which feature should we build in Q2?" --topology scamper_parallel`
- User specifies topology
- 7 agents, one per SCAMPER operation (Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse)
- Moderator synthesizes best ideas → Field Map

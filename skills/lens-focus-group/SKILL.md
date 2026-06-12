---
id: 08d9a7bc-ad09-4270-980d-664e08ce1980
name: lens-focus-group
description: >
  Simulated cognitive focus group using Lens persona templates.
  DEEP mode: 5-15 minutes, interactive.
  Star/Delphi topology with independent Round 1 (Surowiecki), then cross-pollination,
  then moderator synthesis into Field Map.
version: 0.1.0
tags: [lens, cognitive, focus-group, personas, deep, multi-agent]
---

# Lens Focus Group — DEEP Mode

**Simulate how different cognitive profiles react to your topic.**

Star/Delphi topology: N personas respond independently (Round 1), see each other's responses and revise (Round 2), then a moderator synthesizes into a Field Map.

## When to use

- You want to understand how different stakeholder types react to an idea
- You need a multi-perspective analysis before a decision
- You want to stress-test a pitch, product, or strategy from multiple angles
- You want a Field Map showing convergences, divergences, and outliers

## How it works

1. User provides **topic** + optionally specifies **personas** (or auto-select)
2. Round 1: each persona responds independently (NO cross-talk — Surowiecki condition)
3. Round 2: each persona sees all Round 1 outputs, can revise their position
4. Round 3: moderator synthesizes into a Field Map
5. Output: Field Map (convergences, divergences, outliers, synthesis)

## Execution

### Step 1: Parse input and select personas

Extract:
- **topic**: what to analyze (required)
- **personas**: list of persona_ids (optional, default: auto-select 3-4)
- **intensity**: 1-5 (default: 3)

**Auto-selection logic** (if no personas specified):
- Use `lens_list_personas()` to show available personas
- Select 3-4 that provide maximum cognitive diversity for the topic
- Good defaults: `cto-skeptic` + `early-adopter` + `critical-journalist` + `end-user`
- Tell the user which personas you selected and why

### Step 2: Round 1 — Independent perspectives

For each persona, call `lens_compose_persona(persona_id, topic, output_format="perspective_card", intensity)`.

Launch ALL persona agents **in parallel** using the Task tool (subagent_type: "general-purpose").

**CRITICAL — INDEPENDENCE**: In Round 1, each agent receives ONLY its own persona prompt and the topic. No agent sees any other agent's output. This is the Surowiecki condition — independence in Round 1 is mandatory for collective intelligence.

**Each agent prompt:**
```
{system_prompt from lens_compose_persona}
```

Wait for all agents to complete.

**Show Round 1 results to user:**
Present each persona's Perspective Card. Ask: "Do you want to proceed with Round 2 (cross-pollination) or do you have questions about these results?"

### Step 3: Round 2 — Cross-pollination (optional but recommended)

For each persona, compose a new prompt that includes all Round 1 outputs:

```
You are {persona_name}. You have already expressed your position on the topic.
Now you have read the positions of the other focus group participants.

## Your original positions (Round 1)
{This persona's Round 1 output}

## Other participants' positions

### {Persona 2 name}
{Persona 2 Round 1 output}

### {Persona 3 name}
{Persona 3 Round 1 output}

[...for each persona...]

## Your task

In light of the others' positions:
1. What do you CONFIRM of your original position?
2. What do you REVISE or NUANCE?
3. What NEW aspects emerge from the comparison that you hadn't considered?
4. Where do you STRONGLY DISAGREE with the other participants?

Maintain your role and your biases. Do not seek artificial consensus.
```

Launch all in parallel. Show Round 2 results to user.

### Step 4: Round 3 — Moderator synthesis

Launch a final moderator agent:

```
You are the moderator of a Lens cognitive focus group. Your task is to produce a Field Map that synthesizes the perspectives without forcing consensus.

## Topic
{topic}

## Participants and their positions

{For each persona: name + Round 1 + Round 2 (if done)}

## Produce the Field Map

### CONVERGENCES
[What do 3+ participants agree on? Why is it significant?]

### DIVERGENCES
[Where is disagreement substantial and irreducible? What are the positions?]

### OUTLIERS
[Surprising insights raised by a SINGLE participant but potentially valuable]

### PRODUCTIVE TENSIONS
[Where does disagreement generate insight that no single perspective would have produced?]

### COLLECTIVE BLIND SPOT
[What did NO participant mention that might be relevant?]

### SYNTHESIS
[An integration that honors the divergences without forcing consensus. Not an average: a map of the territory.]
```

### Step 5: Present output

```markdown
# Focus Group — {topic}

> Participants: {persona_names} | Rounds: {2 or 3} | Intensity: {intensity}/5

## Field Map

{Moderator output}

---

## Individual perspectives

### {Persona 1 name}
**Round 1:** {output}
**Round 2:** {revision, if done}

### {Persona 2 name}
[...]

---
*Lens Focus Group | Star/Delphi | {N} personas | {rounds} rounds*
```

### Step 6: Save session

```
lens_session_save(topology="star", topic, agents_count=N+1, rounds_count=rounds, output=full_report)
```

## Examples

**User:** `/lens-focus-group "Should we launch an enterprise plan at 50k/year?"`
- Auto-select: cto-skeptic, early-adopter, regulator, end-user
- 3 rounds (independent → cross-pollination → synthesis)

**User:** `/lens-focus-group "Complete company rebrand" --personas cto-skeptic,critical-journalist`
- Only 2 specific personas
- Focused contrast between skeptic and investigator

**User:** `/lens-focus-group "New AI feature in the product" --intensity 5`
- Maximum intensity: personas will be extreme in their positions

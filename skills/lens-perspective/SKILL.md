---
id: f2971214-f849-4b2a-83af-6d1f60ab734a
name: lens-perspective
description: >
  Generate a single constrained perspective on any topic using Lens cognitive constraints.
  QUICK mode: fire and forget, 30-60 seconds.
  Uses structural constraints to navigate the tails of the LLM distribution,
  producing insights that would not emerge from a standard prompt.
version: 0.1.0
tags: [lens, cognitive, constraints, perspective, quick]
---

# Lens Perspective — QUICK Mode

Generate a **Perspective Card** on any topic using structural cognitive constraints.

## When to use

- You need a fresh, non-obvious perspective on a topic
- You want to stress-test an assumption or claim
- You want to see a topic through a specific cognitive lens
- You want to simulate a specific persona's reaction

## How it works

1. The user provides a **topic** and optionally specifies **constraints** or a **persona**
2. Lens composes a structured prompt with rigid cognitive constraints
3. A single subagent runs with those constraints
4. Output: a **Perspective Card** (claim, supporto, blind spot, confidenza)

## Execution

### Step 1: Parse input

Extract from the user's message:
- **topic**: the subject to analyze (required)
- **constraints**: specific constraint types to apply (optional)
- **persona_id**: a persona template to use instead of raw constraints (optional)
- **intensity**: 1-5, how rigid the constraints are (default: 3)

If the user provides neither constraints nor persona, use `lens_suggest_constraints` to suggest optimal constraints based on the topic.

### Step 2: Compose the prompt

Use the Lens MCP server tools:

**If persona_id is provided:**
```
lens_compose_persona(persona_id, topic, output_format="perspective_card", intensity)
```

**If constraints are provided:**
```
lens_compose_prompt(topic, constraints_json, output_format="perspective_card", intensity)
```

**If neither is provided:**
1. Call `lens_suggest_constraints(topic, goal)` to get suggested constraints
2. Show the suggestions to the user briefly
3. Call `lens_compose_prompt` with the suggested constraints

The tool returns a JSON with `system_prompt` (the structured prompt) and `warnings` (compatibility issues).

### Step 3: Launch subagent

Launch a **single Task subagent** (subagent_type: "general-purpose") with:
- The `system_prompt` from Step 2 as the task prompt
- Let the agent respond freely within the constraints

**IMPORTANT**: The subagent's prompt should be:
```
{system_prompt from lens_compose_prompt}
```

The subagent will produce a Perspective Card following the embedded schema.

### Step 4: Present output

Present the subagent's output directly to the user. It should already be a Perspective Card with:
- **CLAIM**: the main position
- **SUPPORTO**: evidence and reasoning
- **BLIND SPOT**: what this perspective might miss
- **CONFIDENZA**: high/medium/low with explanation

Add a brief footer:
```
---
*Lens Perspective | Vincoli: [list] | Intensita': [N]/5*
```

### Step 5: Save session (optional)

If the output was valuable, save it:
```
lens_session_save(topology="single_perspective", topic, agents_count=1, rounds_count=1, output)
```

## Examples

**User:** `/lens-perspective L'AI sostituira' i copywriter entro 5 anni`
- Suggest constraints: `inversion` + `temporal(2030)`
- Generate perspective card with opposite+future view

**User:** `/lens-perspective "Il nostro pricing e' troppo alto" --persona cto-scettico`
- Load CTO scettico persona
- Generate perspective card from CTO's viewpoint

**User:** `/lens-perspective "Dovremmo adottare microservizi" --constraints inversion,abductive`
- Compose prompt with inversion + abductive constraints
- Generate perspective card with contrarian + non-obvious view

## Constraints reference

Quick reference for common constraint types:
- `inversion` — argue the opposite
- `temporal` — perspective from future/past (add `value: "2030"`)
- `exclusion` — ban specific words (add `words: [...]`)
- `bisociative` — force collision with alien domain (add `domain_forced: "..."`)
- `defamiliarize` — describe as if never seen before
- `abductive` — only non-obvious explanations
- `premortem` — it already failed, reconstruct why (add `date: "2028"`)
- `steelman` — build the strongest version
- `provocation` — start from impossible statement (add `po_statement: "..."`)

Use `lens_list_constraints()` for the full library.

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
  extra_instructions="Attacca OGNI punto della difesa precedente. Trova falle logiche, evidenze mancanti, assunzioni non dichiarate. Non concedere nulla."
)
```

**Agent 3 — Synthesis (Judge):**
```
lens_compose_prompt(
  topic="[All previous outputs will be inserted here]",
  constraints=[
    {"type": "elm_route", "route": "central", "focus": "qualita' logica degli argomenti"}
  ],
  output_format="raw",
  intensity=3,
  extra_instructions="Valuta il dibattito. Identifica: (1) punti della tesi che sono sopravvissuti all'attacco, (2) punti demoliti, (3) il nucleo sopravvissuto, (4) le obiezioni irrisolte."
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

CLAIM DA DIFENDERE:
{claim}
```

Wait for Agent 1 output, then...

**Agent 2 prompt:**
```
{system_prompt from Step 2, Agent 2}

DIFESA DA ATTACCARE:
---
{Agent 1's full output}
---

Attacca ogni punto. Non fare concessioni.
```

Wait for Agent 2 output, then...

**Agent 3 prompt:**
```
Sei un giudice imparziale. Valuta il seguente dibattito con rigore logico.

CLAIM ORIGINALE: {claim}

DIFESA (Agente 1):
---
{Agent 1's output}
---

ATTACCO (Agente 2):
---
{Agent 2's output}
---

Produci il tuo verdetto nel seguente formato:

## NUCLEO SOPRAVVISSUTO
[Cosa della tesi originale ha resistito all'attacco? Perche'?]

## PUNTI DEMOLITI
[Cosa e' caduto sotto l'attacco? Perche'?]

## OBIEZIONI IRRISOLTE
[Quali critiche dell'attaccante restano senza risposta?]

## VERDETTO
[Il claim originale e' robusto / parzialmente robusto / fragile?]
[1-2 frasi con la valutazione complessiva]
```

### Step 4: Present output

Present a structured **Cascade Report** showing:

```markdown
# Adversarial Cascade — {claim}

> Intensita': {intensity}/5 | Profondita': {depth} agenti

---

## Round 1 — Difesa
{Agent 1 output}

---

## Round 2 — Attacco
{Agent 2 output}

---

## Verdetto
{Agent 3 output}

---
*Lens Adversarial | Cascade depth: {depth} | Intensita': {intensity}/5*
```

### Step 5: Save session

```
lens_session_save(topology="cascade", topic=claim, agents_count=depth, rounds_count=1, output=full_report)
```

## Examples

**User:** `/lens-adversarial "L'AI generativa rendera' obsolete le agenzie creative entro 3 anni"`
- Depth 3, intensity 3 (default)
- Agent 1 defends, Agent 2 attacks, Agent 3 judges

**User:** `/lens-adversarial "Dovremmo investire 500k in un rebrand" --intensity 5`
- Maximum attack intensity
- Agent 2 will be merciless

**User:** `/lens-adversarial "Il nostro vantaggio competitivo e' il servizio clienti" --depth 4 --focus "sostenibilita' nel tempo"`
- 4 agents, focused attack on long-term sustainability
- Agent 4 attacks the judge's synthesis

## Intensity guide

- **1**: Constructive criticism, raises reasonable doubts
- **2**: Firm pushback, challenges evidence quality
- **3**: Aggressive attack, no concessions (default)
- **4**: Hostile cross-examination, assumes bad faith
- **5**: Demolition mode, searches for fatal flaws with maximum force

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
  {"type": "modal", "mode": "solo fallimenti di esecuzione: ritardi, incompetenza, risorse insufficienti, errori tecnici"}
]
```

**Agent 2 — Market/External Failure:**
```json
[
  {"type": "premortem", "date": "{horizon}"},
  {"type": "modal", "mode": "solo fallimenti esterni: mercato cambiato, competitor, regolamentazione, shock economici"}
]
```

**Agent 3 — Strategic Failure:**
```json
[
  {"type": "premortem", "date": "{horizon}"},
  {"type": "assumption_reversal", "assumption": "[assunzione chiave del progetto]", "reversed": "[inversione]"}
]
```

**Agent 4 (optional) — Human/Organizational Failure:**
```json
[
  {"type": "premortem", "date": "{horizon}"},
  {"type": "modal", "mode": "solo fallimenti umani e organizzativi: conflitti, turnover, burnout, disallineamento culturale, politica interna"}
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
Sei il sintetizzatore di un premortem strutturato. Hai ricevuto {N} scenari di fallimento indipendenti per il progetto: "{project}".

## Scenari ricevuti

### Scenario 1 — Fallimento esecutivo
{Agent 1 output}

### Scenario 2 — Fallimento esterno
{Agent 2 output}

### Scenario 3 — Fallimento strategico
{Agent 3 output}

### Scenario 4 — Fallimento organizzativo
{Agent 4 output, if used}

## Il tuo compito

Produci una MAPPA DEI RISCHI nel seguente formato:

### RISCHI CONVERGENTI
[Rischi che emergono in 2+ scenari — sono i piu' probabili]

### RISCHI CATASTROFICI
[Rischi che appaiono in un solo scenario ma avrebbero impatto devastante]

### CATENA CAUSALE PRINCIPALE
[La sequenza di eventi piu' plausibile che porta al fallimento]

### SEGNALI DI ALLARME PRECOCI
[Cosa monitorare nei prossimi 3-6 mesi per intercettare questi rischi]

### AZIONI PREVENTIVE
[3-5 azioni concrete da fare ORA per ridurre i rischi identificati]
```

### Step 5: Present output

```markdown
# Premortem — {project}

> Orizzonte: {horizon} | Agenti: {N} | Intensita': {intensity}/5

{Synthesizer output}

---

### Scenari individuali

<details>
<summary>Scenario 1 — Fallimento esecutivo</summary>
{Agent 1 output}
</details>

<details>
<summary>Scenario 2 — Fallimento esterno</summary>
{Agent 2 output}
</details>

<details>
<summary>Scenario 3 — Fallimento strategico</summary>
{Agent 3 output}
</details>

---
*Lens Premortem | {N} agenti | Intensita': {intensity}/5*
```

### Step 6: Save session

```
lens_session_save(topology="star", topic=project, agents_count=N+1, rounds_count=1, output=full_report)
```

## Examples

**User:** `/lens-premortem "Lancio del nuovo prodotto SaaS B2B a marzo"`
- 4 agents: execution, market, strategic, organizational
- Horizon: 2028 (default)

**User:** `/lens-premortem "Migrazione a microservizi" --horizon 2027`
- Custom horizon
- Agent 3 inverts assumption "microservizi migliorano la velocity"

**User:** `/lens-premortem "Assunzione di 20 persone nei prossimi 6 mesi" --intensity 5`
- Maximum intensity
- Agents will be merciless in finding failure modes

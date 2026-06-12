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
    {"type": "limit", "constraint": "massimo 5 argomenti, ognuno con un dato concreto o un esempio specifico"}
  ],
  output_format="perspective_card",
  intensity=intensity
)
```

Launch Agent 1 as Task subagent (subagent_type: "general-purpose").

**Agent 1 prompt:**
```
{system_prompt from lens_compose_prompt}

ARGOMENTO DA RAFFORZARE:
{argument}

Costruisci la versione piu' forte possibile di questo argomento. Ogni punto deve essere supportato da evidenze concrete, dati o ragionamenti logici stringenti.
```

Wait for Agent 1 output, then...

**Agent 2 — Reinforcer:**
```
lens_compose_prompt(
  topic="[Agent 1 output will be inserted]",
  constraints=[
    {"type": "steelman"},
    {"type": "elm_route", "route": "central", "focus": "rigore logico e qualita' delle evidenze"}
  ],
  output_format="raw",
  intensity=intensity,
  extra_instructions="Hai ricevuto una difesa gia' costruita. Il tuo compito: (1) trovare i punti piu' deboli e RAFFORZARLI, (2) aggiungere evidenze mancanti, (3) anticipare obiezioni e includere contro-argomenti preventivi, (4) rendere la struttura argomentativa inattaccabile."
)
```

**Agent 2 prompt:**
```
{system_prompt}

DIFESA DA RAFFORZARE:
---
{Agent 1's output}
---

Migliora questa difesa. Non ripetere: rafforza i punti deboli, aggiungi evidenze, anticipa obiezioni.
```

Wait for Agent 2 output.

**Agent 3 — Final Strengthener (if build_depth=3):**
Same pattern, focusing on rhetorical coherence and closing any remaining gaps. Use constraints: `steelman` + `modal` with mode "solo rafforzamento, zero concessioni".

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
  extra_instructions="Questa e' la versione PIU' FORTE dell'argomento, gia' rafforzata da 2 esperti. Il tuo compito: trovare falle anche nella versione blindata. Cerca: assunzioni non dichiarate, evidenze cherry-picked, salti logici mascherati, scenari dove l'argomento crolla."
)
```

**Agent A prompt:**
```
{system_prompt}

ARGOMENTO BLINDATO (versione rafforzata da {build_depth} esperti):
---
{Final Phase 1 output}
---

Questo argomento e' gia' stato rafforzato al massimo. Trova comunque le falle.
```

Wait for Agent A output.

**Agent B — Final Verdict (optional, when intensity >= 4):**

A judge that evaluates what survived the attack on the steelmanned version.

**Agent B prompt:**
```
Sei un giudice imparziale. Hai visto un argomento costruito nella sua versione piu' forte e poi attaccato da un critico ostile.

ARGOMENTO ORIGINALE: {argument}

VERSIONE RAFFORZATA:
---
{Final Phase 1 output}
---

ATTACCO ALLA VERSIONE RAFFORZATA:
---
{Agent A's output}
---

Produci il tuo verdetto:

## ARGOMENTO BLINDATO
[La versione finale dell'argomento, incorporando le difese che hanno resistito all'attacco]

## PUNTI VULNERABILI RESIDUI
[Debolezze che restano anche nella versione piu' forte]

## OBIEZIONI DA PREPARARE
[Le 3-5 obiezioni piu' probabili che qualcuno fara', con le risposte suggerite]

## CONFIDENZA
[Quanto e' robusto questo argomento dopo il processo? Alta/Media/Bassa, con spiegazione]
```

### Step 4: Present output

```markdown
# Steelman Chain — {argument}

> Build depth: {build_depth} | Intensita' attacco: {intensity}/5

## Argomento blindato
{Final strengthened version or Agent B's "ARGOMENTO BLINDATO" section}

## Punti vulnerabili residui
{From Agent A attack or Agent B verdict}

## Obiezioni da preparare
{From Agent B if present, or extracted from Agent A's attack}

---

### Processo

<details>
<summary>Fase 1 — Costruzione ({build_depth} round)</summary>

**Round 1 — Foundation:**
{Agent 1 output}

**Round 2 — Reinforcement:**
{Agent 2 output}

</details>

<details>
<summary>Fase 2 — Stress test</summary>

**Attacco:**
{Agent A output}

**Verdetto:** (if present)
{Agent B output}

</details>

---
*Lens Steelman | Chain depth: {build_depth} + attack | Intensita': {intensity}/5*
```

### Step 5: Save session

```
lens_session_save(topology="steelman_chain", topic=argument, agents_count=build_depth+1 or +2, rounds_count=2, output=full_report)
```

## Examples

**User:** `/lens-steelman "L'AI generativa e' un vantaggio competitivo sostenibile per le agenzie creative"`
- Build depth 2, intensity 4 (default)
- 2 agents strengthen, 1 attacks, 1 judges

**User:** `/lens-steelman "Dovremmo rifiutare clienti sotto i 50k/anno" --intensity 5`
- Maximum attack intensity on the fortified version
- 4 agents total: 2 build + 1 attack + 1 judge

**User:** `/lens-steelman "Il remote-first e' migliore dell'ufficio per la produttivita'" --build-depth 3 --focus "dati e ricerche"`
- 3 strengthening rounds focused on empirical evidence
- Then adversarial test

## Why Steelman Chain > Simple Steelman

A single steelman agent builds a decent case. But it misses:
- **Weak spots it doesn't see**: a second agent catches what the first missed
- **Anticipation of attacks**: the reinforcer thinks adversarially while building
- **Genuine robustness**: only tested arguments survive the final attack

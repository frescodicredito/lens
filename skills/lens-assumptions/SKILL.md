---
id: 350c44d2-559a-46d4-820f-9b2671ee1c5b
name: lens-assumptions
description: >
  Uncover and invert hidden assumptions in any strategy, plan, or belief.
  Supports QUICK mode (fast assumption surfacing) and DEEP mode (full inversion exploration).
  Combines Socratic Drill and Assumption Inversion topologies.
version: 0.1.0
tags: [lens, cognitive, assumptions, socratic, inversion, quick, deep]
---

# Lens Assumptions — QUICK/DEEP Mode

**Find the assumptions you don't know you're making. Then invert them.**

Combines Socratic Drill (surface hidden assumptions) and Assumption Inversion (systematically explore what happens when each assumption is false). Based on Mason & Mitroff's SAST and CIA's Key Assumptions Check.

## When to use

- You suspect your strategy rests on unexamined assumptions
- You want to find the "taken for granted" beliefs that could be wrong
- You need to identify which assumptions, if wrong, would be catastrophic
- You want to explore "what if the opposite is true?"

## How it works

### QUICK mode (default, 2-3 minutes)
1. User provides a **strategy/plan/belief**
2. Agent 1 (Socratic): surfaces 5-8 hidden assumptions via questioning
3. Agent 2 (Classifier): ranks by importance x certainty
4. Agent 3 (Inverter): inverts the top 3-4 assumptions and explores implications
5. Output: assumption map + inversion insights

### DEEP mode (5-10 minutes, with --deep flag)
1. Same as QUICK, but...
2. After classification, user chooses which assumptions to invert
3. Each selected assumption gets a dedicated inversion agent
4. Cross-analysis of inversions
5. Output: full assumption map + detailed inversion exploration

## Execution

### Step 1: Parse input

Extract from the user's message:
- **subject**: the strategy, plan, belief, or decision to examine (required)
- **mode**: QUICK (default) or DEEP (if --deep flag)
- **intensity**: 1-5 (default: 3)
- **focus**: optional focus area (e.g., "focus on market assumptions", "focus on technical assumptions")

### Step 2: Agent 1 — Socratic Drill (surface assumptions)

```
lens_compose_prompt(
  topic=subject,
  constraints=[
    {"type": "abductive"},
    {"type": "modal", "mode": "solo domande e assunzioni nascoste, nessuna risposta o soluzione"}
  ],
  output_format="raw",
  intensity=intensity,
  extra_instructions="Il tuo compito e' SCAVARE fino alle assunzioni fondamentali. Per ogni affermazione implicita nella strategia, chiedi: 'Perche' assumiamo che sia vero?' Elenca TUTTE le assunzioni che trovi, anche quelle che sembrano ovvie. Le assunzioni piu' pericolose sono quelle che nessuno mette in discussione."
)
```

**Agent 1 prompt:**
```
{system_prompt}

STRATEGIA/PIANO DA ESAMINARE:
{subject}

Identifica TUTTE le assunzioni nascoste. Per ciascuna:
1. **Assunzione**: cosa si assume sia vero senza verificarlo
2. **Perche' e' nascosta**: perche' nessuno la mette in discussione
3. **Evidenza**: quale evidenza supporta (o non supporta) questa assunzione

Obiettivo: trovare almeno 6-8 assunzioni, dalle piu' ovvie alle piu' profonde.
```

### Step 3: Agent 2 — Classifier (rank by impact x certainty)

**Agent 2 prompt:**
```
Sei un analista di rischio strategico. Hai ricevuto una lista di assunzioni nascoste per: "{subject}"

## Assunzioni identificate
{Agent 1 output}

Classifica ogni assunzione su due dimensioni:

**IMPORTANZA** (se questa assunzione e' sbagliata, quanto impatta?):
- CRITICA: il piano/strategia crolla completamente
- ALTA: richiede modifiche significative
- MEDIA: richiede aggiustamenti
- BASSA: impatto marginale

**CERTEZZA** (quanto siamo sicuri che sia vera?):
- VERIFICATA: dati solidi la confermano
- PROBABILE: ragionevolmente sicura ma non verificata
- INCERTA: potrebbe andare in entrambe le direzioni
- FRAGILE: basata su speranze piu' che su evidenze

## Output richiesto

### MATRICE ASSUNZIONI

| # | Assunzione | Importanza | Certezza | Priorita' inversione |
|---|-----------|-----------|---------|---------------------|
| 1 | ... | CRITICA | FRAGILE | MASSIMA |
| ... | ... | ... | ... | ... |

### TOP 3-4 PER INVERSIONE
[Le assunzioni con combinazione CRITICA/ALTA importanza + INCERTA/FRAGILE certezza — queste sono le piu' pericolose e vanno invertite per prime]
```

**In QUICK mode:** launch Agents 1 and 2 sequentially, then proceed to Step 4.

**In DEEP mode:** after Agent 2, show the matrix to the user and ask:
```
Ecco la mappa delle assunzioni. Quali vuoi invertire?
Le top {N} per rischio sono segnate. Vuoi procedere con queste o sceglierne altre?
```

### Step 4: Agent 3 — Inverter (explore what if assumptions are false)

**QUICK mode: single inverter for top 3-4 assumptions**

```
lens_compose_prompt(
  topic=subject,
  constraints=[
    {"type": "assumption_reversal", "assumption": "[top assumption]", "reversed": "[inverted version]"},
    {"type": "inversion"}
  ],
  output_format="raw",
  intensity=intensity
)
```

**Agent 3 prompt:**
```
{system_prompt}

STRATEGIA ORIGINALE: {subject}

ASSUNZIONI DA INVERTIRE (dalla piu' pericolosa):

{For each top assumption from Agent 2:}
### Assunzione {N}: {assumption}
**Inversione**: {what if the opposite is true?}

Per OGNI inversione, esplora:
1. **Scenario**: se questa assunzione e' FALSA, cosa succede alla strategia?
2. **Segnali**: quali segnali vedremmo GIA' OGGI se l'inversione fosse vera?
3. **Adattamento**: come dovremmo modificare la strategia per essere robusti anche in questo caso?
4. **Opportunita'**: l'inversione apre opportunita' inaspettate?
```

**DEEP mode: one agent per assumption (parallel)**

For each selected assumption, launch a dedicated agent with `assumption_reversal` constraint set to that specific assumption. Launch all in parallel. Then a synthesizer cross-analyzes.

**DEEP mode synthesizer prompt:**
```
Sei il sintetizzatore di una Assumption Inversion Lens. Hai visto {N} inversioni indipendenti per: "{subject}"

{For each inversion agent output}

## Analisi cross-inversione

### PATTERN
[Quali pattern emergono dalle inversioni? Ci sono assunzioni correlate che crollano insieme?]

### ASSUNZIONE PIU' PERICOLOSA
[Quale singola assunzione, se falsa, causa il danno maggiore? Perche'?]

### PIANO DI VERIFICA
[Per ogni assunzione critica: cosa fare CONCRETAMENTE per verificarla nei prossimi 30 giorni?]

### STRATEGIA ROBUSTA
[Come modificare la strategia per essere meno dipendente dalle assunzioni piu' fragili?]
```

### Step 5: Present output

```markdown
# Assumption Map — {subject}

> Modo: {QUICK/DEEP} | Assunzioni trovate: {N} | Invertite: {M} | Intensita': {intensity}/5

## Matrice assunzioni

{Agent 2 matrix}

## Inversioni

{Agent 3 output (QUICK) or Synthesizer output (DEEP)}

---

### Dettaglio assunzioni

<details>
<summary>Lista completa assunzioni (Agent 1)</summary>
{Agent 1 full output}
</details>

<details>
<summary>Classificazione (Agent 2)</summary>
{Agent 2 full output}
</details>

---
*Lens Assumptions | {QUICK/DEEP} | {N} assunzioni | Intensita': {intensity}/5*
```

### Step 6: Save session

```
lens_session_save(topology="assumption_inversion", topic=subject, agents_count=3 or more, rounds_count=1 or 2, output=full_report)
```

## Examples

**User:** `/lens-assumptions "La nostra strategia di crescita si basa sull'acquisizione di 3 clienti enterprise da 100k+/anno"`
- QUICK mode: surfaces assumptions, classifies, inverts top 3
- Might find: "assume che il mercato enterprise sia accessibile senza sales team dedicato"

**User:** `/lens-assumptions "Puntiamo tutto sul mercato italiano per i prossimi 2 anni" --deep`
- DEEP mode: full exploration, user chooses which assumptions to invert
- Dedicated agent per assumption, cross-analysis

**User:** `/lens-assumptions "Il nostro vantaggio competitivo e' la qualita' del servizio" --intensity 5 --focus "market assumptions"`
- Maximum intensity, focused on market-related assumptions
- Will be relentless in surfacing uncomfortable truths

## The Importance-Certainty matrix

```
                    CERTEZZA
                FRAGILE ←——→ VERIFICATA
    CRITICA  |  DANGER!  |  PILASTRO  |
IMPORTANZA   |  Invertire |  Monitorare |
             |  subito    |            |
    BASSA    |  RUMORE   |  NON-ISSUE |
             |  Ignorare  |  Ignorare  |
```

The top-right (CRITICA + FRAGILE) quadrant contains the assumptions that can kill your strategy. These get inverted first.

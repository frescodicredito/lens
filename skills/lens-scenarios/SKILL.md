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
- **horizon**: time horizon for scenarios (default: "3-5 anni")
- **intensity**: 1-5 (default: 3)

**If uncertainties are NOT provided**, identify them:

Present to the user:
```
Per costruire la matrice scenari, servono 2 incertezze critiche.

Suggerisco:
1. **{uncertainty_1}**: {pole_a} vs {pole_b}
2. **{uncertainty_2}**: {pole_a} vs {pole_b}

Questo genera 4 scenari:
- Q1: {u1_pole_a} + {u2_pole_a}
- Q2: {u1_pole_a} + {u2_pole_b}
- Q3: {u1_pole_b} + {u2_pole_a}
- Q4: {u1_pole_b} + {u2_pole_b}

Procedo con queste incertezze o vuoi modificarle?
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
    {"type": "modal", "mode": "solo conseguenze di questo scenario, nessuna alternativa"}
  ],
  output_format="perspective_card",
  intensity=intensity
)
```

**Each agent prompt:**
```
{system_prompt from lens_compose_prompt}

## Scenario: {quadrant_name}

Siamo nel {horizon}. Le seguenti condizioni si sono verificate:
- {Uncertainty 1}: {pole for this quadrant}
- {Uncertainty 2}: {pole for this quadrant}

In questo mondo:
1. Come si e' evoluta la situazione?
2. Quali decisioni si sono rivelate vincenti?
3. Quali decisioni si sono rivelate disastrose?
4. Quali segnali precoci (visibili GIA' OGGI) avrebbero predetto questo scenario?
5. Qual e' la strategia ottimale in questo mondo?
```

Launch ALL 4 agents **in parallel** using the Task tool (subagent_type: "general-purpose").

**CRITICAL — INDEPENDENCE**: In Round 1, each agent explores ONLY its own scenario. No agent sees other scenarios. This ensures genuine diversity.

Show Round 1 results to user with the matrix layout. Ask: "Vuoi procedere con la sintesi cross-scenario o hai domande su uno scenario specifico?"

### Step 4: Round 2 — Cross-scenario synthesis

Launch a synthesizer agent:

```
Sei il sintetizzatore di una Scenario Matrix Lens. Hai ricevuto 4 scenari indipendenti per la domanda strategica: "{question}"

## Matrice

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

## Il tuo compito

Produci una ANALISI CROSS-SCENARIO nel seguente formato:

### STRATEGIE ROBUSTE
[Azioni/decisioni che funzionano in 3+ scenari su 4. Queste sono le scommesse sicure.]

### SCOMMESSE ASIMMETRICHE
[Azioni con downside limitato ma upside enorme in 1-2 scenari specifici. Vale la pena rischiare?]

### STRATEGIE DA EVITARE
[Azioni che sembrano buone ma falliscono in 2+ scenari. Sono trappole.]

### SEGNALI PRECOCI
[Per ogni scenario, quali indicatori monitorare nei prossimi 6-12 mesi per capire verso quale quadrante stiamo andando?]

### PIANO ADATTIVO
[Una strategia che inizia con le azioni robuste e include trigger per pivotare verso strategie scenario-specifiche quando i segnali diventano chiari.]
```

### Step 5: Present output

```markdown
# Scenario Matrix — {question}

> Orizzonte: {horizon} | Incertezze: {u1} x {u2} | Intensita': {intensity}/5

## La Matrice

| | {U2 Pole A} | {U2 Pole B} |
|---|---|---|
| **{U1 Pole A}** | **Q1: {name}** | **Q2: {name}** |
| **{U1 Pole B}** | **Q3: {name}** | **Q4: {name}** |

---

## Analisi cross-scenario

{Synthesizer output}

---

## Scenari individuali

### Q1 — {name}
{Q1 agent output}

### Q2 — {name}
{Q2 agent output}

### Q3 — {name}
{Q3 agent output}

### Q4 — {name}
{Q4 agent output}

---
*Lens Scenarios | Scenario Matrix | 4 + 1 agenti | Intensita': {intensity}/5*
```

### Step 6: Save session

```
lens_session_save(topology="scenario_matrix", topic=question, agents_count=5, rounds_count=2, output=full_report)
```

## Examples

**User:** `/lens-scenarios "Dovremmo investire in un prodotto AI proprietario o rivendere soluzioni terze?"`
- Auto-identify uncertainties (e.g., "velocita' commoditizzazione AI" x "willingness-to-pay del mercato")
- 4 scenarios + cross-scenario analysis

**User:** `/lens-scenarios "Espansione in Germania nei prossimi 2 anni" --uncertainty1 "economia europea: crescita vs recessione" --uncertainty2 "regolamentazione AI: permissiva vs restrittiva"`
- Explicit uncertainties provided
- 4 scenarios explore combinations

**User:** `/lens-scenarios "Quale modello di pricing adottare per il nuovo SaaS?" --horizon "2028" --intensity 4`
- Custom horizon
- Higher intensity means more extreme scenario exploration

## Good vs Bad uncertainties

**Good uncertainties:**
- "AI commoditizzata vs AI differenziante" — genuinely uncertain, high impact
- "Mercato in crescita vs contrazione" — independent from AI, high impact
- "Regolamentazione stretta vs laissez-faire" — genuinely uncertain

**Bad uncertainties:**
- "Il sole sorge domani vs non sorge" — not uncertain
- "Competitor entra vs non entra" — too binary/simplistic
- "AI migliora vs AI peggiora" — correlated with everything, not independent

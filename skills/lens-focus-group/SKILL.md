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
5. Output: Field Map (convergenze, divergenze, outlier, sintesi)

## Execution

### Step 1: Parse input and select personas

Extract:
- **topic**: what to analyze (required)
- **personas**: list of persona_ids (optional, default: auto-select 3-4)
- **intensity**: 1-5 (default: 3)

**Auto-selection logic** (if no personas specified):
- Use `lens_list_personas()` to show available personas
- Select 3-4 that provide maximum cognitive diversity for the topic
- Good defaults: `cto-scettico` + `early-adopter` + `giornalista-critico` + `utente-finale`
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
Present each persona's Perspective Card. Ask: "Vuoi procedere con il Round 2 (cross-pollination) o hai domande su questi risultati?"

### Step 3: Round 2 — Cross-pollination (optional but recommended)

For each persona, compose a new prompt that includes all Round 1 outputs:

```
Sei {persona_name}. Hai gia' espresso la tua posizione sul topic.
Ora hai letto le posizioni degli altri partecipanti al focus group.

## Le tue posizioni originali (Round 1)
{This persona's Round 1 output}

## Posizioni degli altri partecipanti

### {Persona 2 name}
{Persona 2 Round 1 output}

### {Persona 3 name}
{Persona 3 Round 1 output}

[...for each persona...]

## Il tuo compito

Alla luce delle posizioni degli altri:
1. Cosa CONFERMI della tua posizione originale?
2. Cosa RIVEDI o SFUMI?
3. Quali NUOVI aspetti emergono dal confronto che non avevi considerato?
4. Su cosa sei in DISACCORDO FORTE con gli altri partecipanti?

Mantieni il tuo ruolo e i tuoi bias. Non cercare consenso artificiale.
```

Launch all in parallel. Show Round 2 results to user.

### Step 4: Round 3 — Moderator synthesis

Launch a final moderator agent:

```
Sei il moderatore di un focus group cognitivo Lens. Il tuo compito e' produrre una Field Map che sintetizzi le prospettive senza forzare consenso.

## Topic
{topic}

## Partecipanti e loro posizioni

{For each persona: name + Round 1 + Round 2 (if done)}

## Produci la Field Map

### CONVERGENZE
[Su cosa concordano 3+ partecipanti? Perche' e' significativo?]

### DIVERGENZE
[Dove il disaccordo e' sostanziale e irreducibile? Quali sono le posizioni?]

### OUTLIER
[Insight sorprendenti emersi da UN solo partecipante ma potenzialmente preziosi]

### TENSIONI PRODUTTIVE
[Dove il disaccordo genera insight che nessuna singola prospettiva avrebbe prodotto?]

### BLIND SPOT COLLETTIVO
[Cosa NESSUN partecipante ha menzionato ma potrebbe essere rilevante?]

### SINTESI
[Integrazione che onora le divergenze senza forzare consenso. Non una media: una mappa del territorio.]
```

### Step 5: Present output

```markdown
# Focus Group — {topic}

> Partecipanti: {persona_names} | Round: {2 or 3} | Intensita': {intensity}/5

## Field Map

{Moderator output}

---

## Prospettive individuali

### {Persona 1 name}
**Round 1:** {output}
**Round 2:** {revision, if done}

### {Persona 2 name}
[...]

---
*Lens Focus Group | Star/Delphi | {N} persona | {rounds} round*
```

### Step 6: Save session

```
lens_session_save(topology="star", topic, agents_count=N+1, rounds_count=rounds, output=full_report)
```

## Examples

**User:** `/lens-focus-group "Dovremmo lanciare un piano enterprise a 50k/anno?"`
- Auto-select: cto-scettico, early-adopter, regolatore, utente-finale
- 3 rounds (independent → cross-pollination → synthesis)

**User:** `/lens-focus-group "Rebrand completo dell'azienda" --personas cto-scettico,giornalista-critico`
- Only 2 specific personas
- Focused contrast between skeptic and investigator

**User:** `/lens-focus-group "Nuova feature AI nel prodotto" --intensity 5`
- Maximum intensity: personas will be extreme in their positions

<!-- GENERATED FILE — do not edit by hand. Run `python scripts/gen_docs.py` after changing the JSON. -->


# Topology Reference

The 13 topologies that define how constrained agents interact. Pick one by what you need; `/lens` can also suggest one for you.

## At a glance

| Topology | Mode | Agents | Rounds | Best for |
|----------|------|--------|--------|----------|
| [`cascade`](#cascade) | QUICK | 2-4 | 1 | ['stress-testing claims', 'argomenti controversi', 'decisioni binarie'] |
| [`star`](#star) | DEEP | 3-6 | 2-3 | ['multi-prospettiva', 'focus group', 'analisi strategica'] |
| [`adversarial_jury`](#adversarial_jury) | DEEP | 5 | 2-3 | ['decisioni ad alto impatto', 'valutazione imparziale', 'controversie'] |
| [`ring`](#ring) | DEEP | 3-5 | 1-2 | ['generazione creativa', 'connessioni inedite', 'innovazione radicale'] |
| [`parallel_hats`](#parallel_hats) | QUICK | 4-6 | 1-2 | ['analisi completa', 'decisioni strutturate', 'evitare groupthink'] |
| [`steelman_chain`](#steelman_chain) | QUICK | 3-5 | 2 | ['costruire argomenti robusti', 'trovare debolezze nascoste', 'preparazione a obiezioni'] |
| [`socratic_drill`](#socratic_drill) | QUICK | 2-3 | 3-5 | ['scoprire assunzioni nascoste', 'chiarezza concettuale', 'validazione logica'] |
| [`scenario_matrix`](#scenario_matrix) | DEEP | 4-5 | 1-2 | ['pianificazione strategica', 'scenari futuri', 'decisioni in incertezza'] |
| [`bisociation_engine`](#bisociation_engine) | QUICK | 3-4 | 1-2 | ['innovazione radicale', 'connessioni inedite', 'pensiero laterale'] |
| [`wise_mind_topology`](#wise_mind_topology) | QUICK | 3 | 1 | ['decisioni personali', 'equilibrio emozione-logica', 'dilemmi etici'] |
| [`scamper_parallel`](#scamper_parallel) | DEEP | 7 | 1 | ['ideazione prodotto', 'innovazione sistematica', 'brainstorming strutturato'] |
| [`assumption_inversion`](#assumption_inversion) | QUICK | 2-4 | 2-3 | ['sfidare lo status quo', 'trovare blind spot strategici', 'innovazione di processo'] |
| [`sequential_chain`](#sequential_chain) | DEEP | 1 | 3-6 | ['approfondimento ipotesi', 'coerenza argomentativa', 'chain epistemica', 'steelmanning profondo'] |

## cascade

**Cascade (Dialettica Hegeliana)** — Sequenza dialettica: ogni agente attacca o raffina l'output del precedente. Tesi -> Antitesi -> Sintesi iterata.

> Theory: Hegel, Boosting cognitivo (ensemble), Devil's Advocacy (CIA/IC)

Mode: **QUICK** · Agents: 2-4 · Rounds: 1 · Interaction: sequential · Output: `perspective_card`

**Best for:** ['stress-testing claims', 'argomenti controversi', 'decisioni binarie']

Recommended constraints: [`inversion`](CONSTRAINTS.md#inversion), [`steelman`](CONSTRAINTS.md#steelman), [`limit`](CONSTRAINTS.md#limit)

Workflow: Agente 1 produce output -> Agente 2 riceve output e attacca/raffina -> Agente 3 sintetizza

## star

**Star / Delphi** — Moderatore + N agenti indipendenti. Round 1 indipendente (no cross-talk), poi sintesi. Bagging cognitivo.

> Theory: Wisdom of Crowds (Surowiecki), Delphi (RAND), Bagging (ensemble)

Mode: **DEEP** · Agents: 3-6 · Rounds: 2-3 · Interaction: parallel_then_aggregate · Output: `field_map`

**Best for:** ['multi-prospettiva', 'focus group', 'analisi strategica']

Recommended constraints: [`role`](CONSTRAINTS.md#role), [`modal`](CONSTRAINTS.md#modal), [`elm_route`](CONSTRAINTS.md#elm_route), [`concept_fan`](CONSTRAINTS.md#concept_fan)

Workflow: Round 1: N agenti rispondono indipendentemente. Round 2: agenti vedono output altrui, rivedono posizioni. Moderatore sintetizza.

## adversarial_jury

**Adversarial + Jury** — 2 agenti dibattono, 3 giurati valutano indipendentemente. Separa argomentazione da giudizio.

> Theory: Adversarial Collaboration, ACH (CIA), Argumentative Theory (Mercier-Sperber)

Mode: **DEEP** · Agents: 5 · Rounds: 2-3 · Interaction: adversarial_then_judge · Output: `field_map`

**Best for:** ['decisioni ad alto impatto', 'valutazione imparziale', 'controversie']

Recommended constraints: [`inversion`](CONSTRAINTS.md#inversion), [`steelman`](CONSTRAINTS.md#steelman), [`elm_route`](CONSTRAINTS.md#elm_route)

Workflow: 2 avvocati dibattono per N round, poi 3 giurati con vincoli diversi valutano indipendentemente.

## ring

**Ring (Bisociazione Iterata)** — Catena circolare: ogni agente trasforma l'output nel proprio frame, l'ultimo riporta al primo.

> Theory: Bisociazione (Koestler), Ring topology

Mode: **DEEP** · Agents: 3-5 · Rounds: 1-2 · Interaction: circular_handoff · Output: `field_map`

**Best for:** ['generazione creativa', 'connessioni inedite', 'innovazione radicale']

Recommended constraints: [`bisociative`](CONSTRAINTS.md#bisociative), [`defamiliarize`](CONSTRAINTS.md#defamiliarize), [`synectics`](CONSTRAINTS.md#synectics)

Workflow: Agente 1 -> Agente 2 -> ... -> Agente N -> Agente 1. Ogni passaggio forza re-interpretazione nel frame dell'agente.

## parallel_hats

**Parallel Hats (De Bono)** — N agenti, ognuno vincolato a una modalita' cognitiva diversa, operano in parallelo.

> Theory: Six Thinking Hats (De Bono), Cognitive Diversity (Ashby)

Mode: **QUICK** · Agents: 4-6 · Rounds: 1-2 · Interaction: parallel_independent · Output: `field_map`

**Best for:** ['analisi completa', 'decisioni strutturate', 'evitare groupthink']

Recommended constraints: [`modal`](CONSTRAINTS.md#modal), [`exclusion`](CONSTRAINTS.md#exclusion)

Workflow: Ogni agente opera in una modalita' cognitiva esclusiva. Output aggregato senza contaminazione.

## steelman_chain

**Steelman Chain** — 3 round di rafforzamento progressivo, poi 1-2 round adversariali sulla versione piu' forte.

> Theory: Steelmanning, Principle of Charity + Adversarial Collaboration

Mode: **QUICK** · Agents: 3-5 · Rounds: 2 · Interaction: strengthen_then_attack · Output: `perspective_card`

**Best for:** ['costruire argomenti robusti', 'trovare debolezze nascoste', 'preparazione a obiezioni']

Recommended constraints: [`steelman`](CONSTRAINTS.md#steelman), [`inversion`](CONSTRAINTS.md#inversion), [`limit`](CONSTRAINTS.md#limit)

Workflow: Fase 1: N agenti rafforzano l'argomento in sequenza. Fase 2: 1-2 agenti attaccano la versione piu' forte.

## socratic_drill

**Socratic Drill** — Catena di domande che scavano fino alle assunzioni fondamentali.

> Theory: Metodo Socratico / Elenchus, Key Assumptions Check (CIA)

Mode: **QUICK** · Agents: 2-3 · Rounds: 3-5 · Interaction: iterative_questioning · Output: `perspective_card`

**Best for:** ['scoprire assunzioni nascoste', 'chiarezza concettuale', 'validazione logica']

Recommended constraints: [`abductive`](CONSTRAINTS.md#abductive), [`assumption_reversal`](CONSTRAINTS.md#assumption_reversal)

Workflow: Agente interrogatore chiede 'perche'?'. Agente rispondente difende. L'interrogatore scava fino alle assunzioni non dichiarate.

## scenario_matrix

**Scenario Matrix** — 2 incertezze critiche generano 4 quadranti. 4 agenti esplorano uno scenario ciascuno.

> Theory: Scenario Planning (Shell/Schwartz), Quadrant Crunching (CIA)

Mode: **DEEP** · Agents: 4-5 · Rounds: 1-2 · Interaction: parallel_independent · Output: `field_map`

**Best for:** ['pianificazione strategica', 'scenari futuri', 'decisioni in incertezza']

Recommended constraints: [`temporal`](CONSTRAINTS.md#temporal), [`role`](CONSTRAINTS.md#role), [`assumption_reversal`](CONSTRAINTS.md#assumption_reversal)

Workflow: 2 assi di incertezza -> 4 scenari. Ogni agente esplora uno scenario assumendolo come realta'. Poi confronto.

## bisociation_engine

**Bisociation Engine** — Collisione forzata tra domini incompatibili per generare connessioni inedite.

> Theory: Bisociazione (Koestler), Synectics (Gordon)

Mode: **QUICK** · Agents: 3-4 · Rounds: 1-2 · Interaction: collision · Output: `perspective_card`

**Best for:** ['innovazione radicale', 'connessioni inedite', 'pensiero laterale']

Recommended constraints: [`bisociative`](CONSTRAINTS.md#bisociative), [`synectics`](CONSTRAINTS.md#synectics), [`defamiliarize`](CONSTRAINTS.md#defamiliarize)

Workflow: Ogni agente analizza il topic dal suo dominio forzato. Un sintetizzatore trova le connessioni strutturali.

## wise_mind_topology

**Wise Mind** — Emotional Mind + Rational Mind -> Wise Mind synthesis. Non dialettica ma integrazione.

> Theory: DBT Wise Mind (Linehan, 1993), Dual Process Theory

Mode: **QUICK** · Agents: 3 · Rounds: 1 · Interaction: parallel_then_integrate · Output: `perspective_card`

**Best for:** ['decisioni personali', 'equilibrio emozione-logica', 'dilemmi etici']

Recommended constraints: [`wise_mind`](CONSTRAINTS.md#wise_mind), [`modal`](CONSTRAINTS.md#modal)

Workflow: Agente emotional produce prospettiva emotiva. Agente rational produce prospettiva razionale. Agente wise integra.

## scamper_parallel

**SCAMPER Parallel** — 7 agenti, ognuno vincolato a una operazione SCAMPER diversa.

> Theory: SCAMPER (Eberle/Osborn)

Mode: **DEEP** · Agents: 7 · Rounds: 1 · Interaction: parallel_independent · Output: `field_map`

**Best for:** ['ideazione prodotto', 'innovazione sistematica', 'brainstorming strutturato']

Recommended constraints: [`scamper`](CONSTRAINTS.md#scamper), [`limit`](CONSTRAINTS.md#limit)

Workflow: 7 agenti applicano S-C-A-M-P-E-R in parallelo. Moderatore sintetizza le migliori idee.

## assumption_inversion

**Assumption Inversion** — Identifica assunzioni, le inverte sistematicamente, esplora le implicazioni.

> Theory: SAST (Mason & Mitroff), Assumption Reversal

Mode: **QUICK** · Agents: 2-4 · Rounds: 2-3 · Interaction: sequential · Output: `perspective_card`

**Best for:** ['sfidare lo status quo', 'trovare blind spot strategici', 'innovazione di processo']

Recommended constraints: [`assumption_reversal`](CONSTRAINTS.md#assumption_reversal), [`abductive`](CONSTRAINTS.md#abductive), [`inversion`](CONSTRAINTS.md#inversion)

Workflow: Fase 1: Socratic Drill per elencare assunzioni. Fase 2: classificazione importanza/certezza. Fase 3: inversione top-K assunzioni.

## sequential_chain

**Sequential Deep Chain** — Vincoli concatenati in sequenza sullo stesso thread cognitivo. Ogni round riceve l'output di tutti i precedenti e lo integra con un nuovo vincolo.

> Theory: Chain-of-Thought (Wei et al. 2022), Self-Consistency (Wang et al. 2023), Deliberative Alignment

Mode: **DEEP** · Agents: 1 · Rounds: 3-6 · Interaction: sequential_self · Output: `chain_output`

**Best for:** ['approfondimento ipotesi', 'coerenza argomentativa', 'chain epistemica', 'steelmanning profondo']

Recommended constraints: [`inversion`](CONSTRAINTS.md#inversion), [`steelman`](CONSTRAINTS.md#steelman), [`abductive`](CONSTRAINTS.md#abductive), [`assumption_reversal`](CONSTRAINTS.md#assumption_reversal), [`anchor_break`](CONSTRAINTS.md#anchor_break)

Workflow: Ogni round applica un vincolo diverso allo stesso problema. L'agente integra l'output dei round precedenti come contesto.

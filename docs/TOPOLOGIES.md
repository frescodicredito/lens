<!-- GENERATED FILE — do not edit by hand. Run `python scripts/gen_docs.py` after changing the JSON. -->


# Topology Reference

The 13 topologies that define how constrained agents interact. Pick one by what you need; `/lens` can also suggest one for you.

## At a glance

| Topology | Mode | Agents | Rounds | Best for |
|----------|------|--------|--------|----------|
| [`cascade`](#cascade) | QUICK | 2-4 | 1 | ['stress-testing claims', 'controversial arguments', 'binary decisions'] |
| [`star`](#star) | DEEP | 3-6 | 2-3 | ['multi-perspective', 'focus group', 'strategic analysis'] |
| [`adversarial_jury`](#adversarial_jury) | DEEP | 5 | 2-3 | ['high-impact decisions', 'impartial evaluation', 'controversies'] |
| [`ring`](#ring) | DEEP | 3-5 | 1-2 | ['creative generation', 'novel connections', 'radical innovation'] |
| [`parallel_hats`](#parallel_hats) | QUICK | 4-6 | 1-2 | ['comprehensive analysis', 'structured decisions', 'avoiding groupthink'] |
| [`steelman_chain`](#steelman_chain) | QUICK | 3-5 | 2 | ['building robust arguments', 'finding hidden weaknesses', 'preparing for objections'] |
| [`socratic_drill`](#socratic_drill) | QUICK | 2-3 | 3-5 | ['uncovering hidden assumptions', 'conceptual clarity', 'logical validation'] |
| [`scenario_matrix`](#scenario_matrix) | DEEP | 4-5 | 1-2 | ['strategic planning', 'future scenarios', 'decisions under uncertainty'] |
| [`bisociation_engine`](#bisociation_engine) | QUICK | 3-4 | 1-2 | ['radical innovation', 'novel connections', 'lateral thinking'] |
| [`wise_mind_topology`](#wise_mind_topology) | QUICK | 3 | 1 | ['personal decisions', 'emotion-logic balance', 'ethical dilemmas'] |
| [`scamper_parallel`](#scamper_parallel) | DEEP | 7 | 1 | ['product ideation', 'systematic innovation', 'structured brainstorming'] |
| [`assumption_inversion`](#assumption_inversion) | QUICK | 2-4 | 2-3 | ['challenging the status quo', 'finding strategic blind spots', 'process innovation'] |
| [`sequential_chain`](#sequential_chain) | DEEP | 1 | 3-6 | ['deepening hypotheses', 'argumentative coherence', 'epistemic chain', 'deep steelmanning'] |

## cascade

**Cascade (Hegelian Dialectic)** — Dialectical sequence: each agent attacks or refines the previous one's output. Thesis -> Antithesis -> iterated Synthesis.

> Theory: Hegel, Boosting cognitivo (ensemble), Devil's Advocacy (CIA/IC)

Mode: **QUICK** · Agents: 2-4 · Rounds: 1 · Interaction: sequential · Output: `perspective_card`

**Best for:** ['stress-testing claims', 'controversial arguments', 'binary decisions']

Recommended constraints: [`inversion`](CONSTRAINTS.md#inversion), [`steelman`](CONSTRAINTS.md#steelman), [`limit`](CONSTRAINTS.md#limit)

Workflow: Agent 1 produces output -> Agent 2 receives it and attacks/refines -> Agent 3 synthesizes

## star

**Star / Delphi** — Moderator + N independent agents. Independent Round 1 (no cross-talk), then synthesis. Cognitive bagging.

> Theory: Wisdom of Crowds (Surowiecki), Delphi (RAND), Bagging (ensemble)

Mode: **DEEP** · Agents: 3-6 · Rounds: 2-3 · Interaction: parallel_then_aggregate · Output: `field_map`

**Best for:** ['multi-perspective', 'focus group', 'strategic analysis']

Recommended constraints: [`role`](CONSTRAINTS.md#role), [`modal`](CONSTRAINTS.md#modal), [`elm_route`](CONSTRAINTS.md#elm_route), [`concept_fan`](CONSTRAINTS.md#concept_fan)

Workflow: Round 1: N agents respond independently. Round 2: agents see each other's output and revise their positions. The moderator synthesizes.

## adversarial_jury

**Adversarial + Jury** — 2 agents debate, 3 jurors evaluate independently. Separates argumentation from judgment.

> Theory: Adversarial Collaboration, ACH (CIA), Argumentative Theory (Mercier-Sperber)

Mode: **DEEP** · Agents: 5 · Rounds: 2-3 · Interaction: adversarial_then_judge · Output: `field_map`

**Best for:** ['high-impact decisions', 'impartial evaluation', 'controversies']

Recommended constraints: [`inversion`](CONSTRAINTS.md#inversion), [`steelman`](CONSTRAINTS.md#steelman), [`elm_route`](CONSTRAINTS.md#elm_route)

Workflow: 2 advocates debate for N rounds, then 3 jurors with different constraints evaluate independently.

## ring

**Ring (Iterated Bisociation)** — Circular chain: each agent transforms the output into its own frame, and the last one passes it back to the first.

> Theory: Bisociazione (Koestler), Ring topology

Mode: **DEEP** · Agents: 3-5 · Rounds: 1-2 · Interaction: circular_handoff · Output: `field_map`

**Best for:** ['creative generation', 'novel connections', 'radical innovation']

Recommended constraints: [`bisociative`](CONSTRAINTS.md#bisociative), [`defamiliarize`](CONSTRAINTS.md#defamiliarize), [`synectics`](CONSTRAINTS.md#synectics)

Workflow: Agent 1 -> Agent 2 -> ... -> Agent N -> Agent 1. Each handoff forces a re-interpretation within the agent's frame.

## parallel_hats

**Parallel Hats (De Bono)** — N agents, each constrained to a different cognitive mode, operating in parallel.

> Theory: Six Thinking Hats (De Bono), Cognitive Diversity (Ashby)

Mode: **QUICK** · Agents: 4-6 · Rounds: 1-2 · Interaction: parallel_independent · Output: `field_map`

**Best for:** ['comprehensive analysis', 'structured decisions', 'avoiding groupthink']

Recommended constraints: [`modal`](CONSTRAINTS.md#modal), [`exclusion`](CONSTRAINTS.md#exclusion)

Workflow: Each agent operates in an exclusive cognitive mode. Output is aggregated without contamination.

## steelman_chain

**Steelman Chain** — 3 rounds of progressive strengthening, then 1-2 adversarial rounds against the strongest version.

> Theory: Steelmanning, Principle of Charity + Adversarial Collaboration

Mode: **QUICK** · Agents: 3-5 · Rounds: 2 · Interaction: strengthen_then_attack · Output: `perspective_card`

**Best for:** ['building robust arguments', 'finding hidden weaknesses', 'preparing for objections']

Recommended constraints: [`steelman`](CONSTRAINTS.md#steelman), [`inversion`](CONSTRAINTS.md#inversion), [`limit`](CONSTRAINTS.md#limit)

Workflow: Phase 1: N agents strengthen the argument in sequence. Phase 2: 1-2 agents attack the strongest version.

## socratic_drill

**Socratic Drill** — A chain of questions that digs down to the fundamental assumptions.

> Theory: Metodo Socratico / Elenchus, Key Assumptions Check (CIA)

Mode: **QUICK** · Agents: 2-3 · Rounds: 3-5 · Interaction: iterative_questioning · Output: `perspective_card`

**Best for:** ['uncovering hidden assumptions', 'conceptual clarity', 'logical validation']

Recommended constraints: [`abductive`](CONSTRAINTS.md#abductive), [`assumption_reversal`](CONSTRAINTS.md#assumption_reversal)

Workflow: The interrogator agent asks 'why?'. The responding agent defends. The interrogator digs down to the undeclared assumptions.

## scenario_matrix

**Scenario Matrix** — 2 critical uncertainties generate 4 quadrants. 4 agents each explore one scenario.

> Theory: Scenario Planning (Shell/Schwartz), Quadrant Crunching (CIA)

Mode: **DEEP** · Agents: 4-5 · Rounds: 1-2 · Interaction: parallel_independent · Output: `field_map`

**Best for:** ['strategic planning', 'future scenarios', 'decisions under uncertainty']

Recommended constraints: [`temporal`](CONSTRAINTS.md#temporal), [`role`](CONSTRAINTS.md#role), [`assumption_reversal`](CONSTRAINTS.md#assumption_reversal)

Workflow: 2 axes of uncertainty -> 4 scenarios. Each agent explores one scenario, assuming it as reality. Then comparison.

## bisociation_engine

**Bisociation Engine** — Forced collision between incompatible domains to generate novel connections.

> Theory: Bisociazione (Koestler), Synectics (Gordon)

Mode: **QUICK** · Agents: 3-4 · Rounds: 1-2 · Interaction: collision · Output: `perspective_card`

**Best for:** ['radical innovation', 'novel connections', 'lateral thinking']

Recommended constraints: [`bisociative`](CONSTRAINTS.md#bisociative), [`synectics`](CONSTRAINTS.md#synectics), [`defamiliarize`](CONSTRAINTS.md#defamiliarize)

Workflow: Each agent analyzes the topic from its forced domain. A synthesizer finds the structural connections.

## wise_mind_topology

**Wise Mind** — Emotional Mind + Rational Mind -> Wise Mind synthesis. Not dialectic but integration.

> Theory: DBT Wise Mind (Linehan, 1993), Dual Process Theory

Mode: **QUICK** · Agents: 3 · Rounds: 1 · Interaction: parallel_then_integrate · Output: `perspective_card`

**Best for:** ['personal decisions', 'emotion-logic balance', 'ethical dilemmas']

Recommended constraints: [`wise_mind`](CONSTRAINTS.md#wise_mind), [`modal`](CONSTRAINTS.md#modal)

Workflow: The emotional agent produces an emotional perspective. The rational agent produces a rational perspective. The wise agent integrates.

## scamper_parallel

**SCAMPER Parallel** — 7 agents, each constrained to a different SCAMPER operation.

> Theory: SCAMPER (Eberle/Osborn)

Mode: **DEEP** · Agents: 7 · Rounds: 1 · Interaction: parallel_independent · Output: `field_map`

**Best for:** ['product ideation', 'systematic innovation', 'structured brainstorming']

Recommended constraints: [`scamper`](CONSTRAINTS.md#scamper), [`limit`](CONSTRAINTS.md#limit)

Workflow: 7 agents apply S-C-A-M-P-E-R in parallel. The moderator synthesizes the best ideas.

## assumption_inversion

**Assumption Inversion** — Identifies assumptions, inverts them systematically, and explores the implications.

> Theory: SAST (Mason & Mitroff), Assumption Reversal

Mode: **QUICK** · Agents: 2-4 · Rounds: 2-3 · Interaction: sequential · Output: `perspective_card`

**Best for:** ['challenging the status quo', 'finding strategic blind spots', 'process innovation']

Recommended constraints: [`assumption_reversal`](CONSTRAINTS.md#assumption_reversal), [`abductive`](CONSTRAINTS.md#abductive), [`inversion`](CONSTRAINTS.md#inversion)

Workflow: Phase 1: Socratic Drill to list the assumptions. Phase 2: classification by importance/certainty. Phase 3: inversion of the top-K assumptions.

## sequential_chain

**Sequential Deep Chain** — Constraints chained in sequence on the same cognitive thread. Each round receives the output of all previous ones and integrates it with a new constraint.

> Theory: Chain-of-Thought (Wei et al. 2022), Self-Consistency (Wang et al. 2023), Deliberative Alignment

Mode: **DEEP** · Agents: 1 · Rounds: 3-6 · Interaction: sequential_self · Output: `chain_output`

**Best for:** ['deepening hypotheses', 'argumentative coherence', 'epistemic chain', 'deep steelmanning']

Recommended constraints: [`inversion`](CONSTRAINTS.md#inversion), [`steelman`](CONSTRAINTS.md#steelman), [`abductive`](CONSTRAINTS.md#abductive), [`assumption_reversal`](CONSTRAINTS.md#assumption_reversal), [`anchor_break`](CONSTRAINTS.md#anchor_break)

Workflow: Each round applies a different constraint to the same problem. The agent integrates the output of the previous rounds as context.

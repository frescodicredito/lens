# Lens — Cognitive Infrastructure for LLM Reasoning

> Foundational document (theory and design).
>
> **Reading note:** this is the theoretical/design document for Lens. The examples are
> illustrative, and Lens works fully autonomously, without depending on any
> external system. For current counts of tools/constraints/topologies, the
> [README](README.md) is authoritative.

---

## 1. What Lens Is

Lens is a **cognitive infrastructure system** for reasoning with LLMs. It does not produce final content: it produces *ways of looking* at a problem. Like a camera lens that does not modify the scene but frames it differently, Lens changes the LLM's point of observation.

### The problem it solves

An LLM responds with the **statistically most probable** answers. The center of the distribution is dense with obvious, safe, mediocre responses. Real creativity, unusual connections, non-linear perspectives live in the **tails of the distribution**.

Lens systematically navigates these tails through structural, not decorative, constraints.

### What Lens Is NOT

- It is not a system that changes the LLM's *tone* (aesthetics)
- It is not a character generator (costume)
- It is not a chatbot with different personalities
- It does not simulate "altered states" — it produces alternative cognitive structures

---

## 2. Theoretical Foundations

Lens is grounded in research-validated theories. Every mechanism has an epistemological basis.

### 2.1 Hegelian Dialectic (Thesis → Antithesis → Synthesis)

**Source:** Hegel; computational implementation [Hegelion](https://github.com/Hmbown/Hegelion)

The LLM commits to a position (thesis), then attacks that position in a separate call (antithesis), then reconciles the opposition (synthesis). The SIEV framework evaluates not only the conclusion but *how* the model arrives at it: the ability to resolve tensions, integrate distinct ideas, synthesize higher-order reasoning.

**Application in Lens:** the Cascade topology is an iterated Hegelian dialectic. Each step produces a synthesis that becomes the new thesis for the next cycle.

### 2.2 Premortem and Prospective Hindsight (Gary Klein)

**Source:** Klein, 1991/2007; [garyklein.com/premortem](https://www.gary-klein.com/premortem)

Prospective hindsight — imagining that an event has already occurred — increases the ability to correctly identify the reasons for future outcomes by 30% (1989 research). The "already happened" frame removes default optimism and unlocks risk patterns that the rational mind suppresses.

**Application in Lens:** temporal frame as a structural constraint. Not "what could go wrong?" but "it's 2028, it went wrong — reconstruct the causal chain."

### 2.3 Second-Order Reframing (Watzlawick)

**Source:** Watzlawick, "Change: Principles of Problem Formation and Problem Resolution"

First-order change: solving the problem within the existing frame. Second-order change: changing the frame itself. "To reframe means to change the conceptual and/or emotional setting or viewpoint in relation to which a situation is experienced and to place it in another frame which fits the facts of the same concrete situation equally well or even better, and thereby changes its entire meaning."

**Application in Lens:** the Constraint Engine does not solve problems, it changes the frames in which problems exist. It is intrinsically a second-order change engine.

### 2.4 Parallel Thinking (De Bono, Six Thinking Hats)

**Source:** De Bono, [Six Thinking Hats](https://www.debonogroup.com/services/core-programs/six-thinking-hats/)

Six separate cognitive modes: facts (white), emotions (red), risks (black), benefits (yellow), creativity (green), process (blue). The value is not in the individual modes but in the **separation**: exploring one dimension at a time prevents critical thinking from smothering creative thinking.

**Application in Lens:** the Lenses are not personas but **cognitive modes**. An agent with the constraint "risks only, no benefits" produces radically different output from "opportunities only, no risks". The separation is the mechanism.

### 2.5 Groupthink and Structured Dissent (Janis)

**Source:** Janis, 1971; [Devil's Advocacy and Dialectical Inquiry](https://www.nationalforum.com/Electronic%20Journal%20Volumes/Lunenburg,%20Fred%20C.%20Devil's%20Advocacy%20&%20Dialectical%20Inquiry%20IJSAID%20V14%20N1%202012.pdf)

Groupthink occurs when "members of a cohesive group tend to maintain esprit de corps by unconsciously developing shared illusions that interfere with critical thinking." Prevention: institutionalized devil's advocacy, programmed dissent, structured conflict.

**Application in Lens:** the LLM has a structural bias toward consensus. Lens counters this bias with programmed dissent — agents whose sole task is to attack the dominant position.

### 2.6 Delphi Method

**Source:** Helmer & Dalkey, RAND Corporation, 1950s; [Wikipedia](https://en.wikipedia.org/wiki/Delphi_method)

Iterative process: experts respond independently (anonymity), receive aggregated feedback, revise their positions. Iterative convergence. Variant: Disagreement Delphi, designed to generate discussion around topics that do not reach consensus.

**Application in Lens:** the Star topology (moderator + N agents) is a computational Delphi. The Disagreement Delphi is particularly relevant — we are not seeking consensus, we are seeking the *map* of disagreement.

### 2.7 TRIZ and Contradiction Resolution

**Source:** Altshuller, 1946+; [TRIZ](https://www.triz.co.uk/what-is-triz)

True innovation arises from resolving contradictions: improving one parameter without worsening another. 40 inventive principles derived from analyzing hundreds of thousands of patents. The framework does not seek compromises — it seeks solutions that overcome contradictions.

**Application in Lens:** forcing functions can be structured as TRIZ contradictions. "Increase speed without increasing cost" is not a compromise, it is a constraint that forces the exploration of non-linear solutions.

### 2.8 Dual Process Theory (Kahneman)

**Source:** Kahneman, "Thinking, Fast and Slow"; [Decision Lab](https://thedecisionlab.com/reference-guide/philosophy/system-1-and-system-2-thinking)

System 1: fast, automatic, intuitive. System 2: slow, deliberate, analytical. LLMs operate by default in System 1 mode (fluent, probabilistic, fast responses). Lens forces System 2: constraints that require explicit deliberation, verification, justification.

**Application in Lens:** every structural constraint is a System 2 forcer. When the LLM cannot give the obvious answer, it must activate deliberate reasoning.

### 2.9 Structured Analytic Techniques (Intelligence Analysis)

**Source:** CIA/IC tradecraft; [Cognitive biases in intelligence analysis](https://viborc.com/cognitive-biases-intelligence-analysis-mitigation/)

Eight biases identified in the analytic workflow: belief bias, confirmation bias, explanation bias, fluency effects, framing effects, order effects, planning fallacy, overconfidence. SATs (Analysis of Competing Hypotheses, Devil's Advocacy) add structural rigor to counter these biases.

**Application in Lens:** Lens is a computational SAT system. Analysis of Competing Hypotheses (ACH) maps directly onto the Adversarial + Jury topology.

### 2.10 Bisociation (Koestler)

**Source:** Koestler, "The Act of Creation", 1964; [The Marginalian](https://www.themarginalian.org/2013/05/20/arthur-koestler-creativity-bisociation/)

Creativity arises from **bisociation**: the simultaneous perception of an idea in two habitually incompatible matrices of thought. It is not association (a connection within a single frame), it is the collision between two independent frames. Humor, scientific discovery and art share this structure: two overlapping matrices produce surprise (humor), eureka (science), or aesthetic juxtaposition (art).

**Application in Lens:** the Constraint Engine with semantic constraints is a bisociation generator. "Describe this marketing strategy in terms of marine ecology" forces the collision between two matrices (marketing and biology) — exactly Koestler's mechanism. The Ring topology is an iterated bisociation: each reframe is a new matrix that overlaps the previous one.

### 2.11 Lateral Thinking and Provocation (De Bono)

**Source:** De Bono, "Lateral Thinking", 1967; [De Bono Group](https://www.debonogroup.com/services/core-programs/lateral-thinking/)

Lateral thinking operates with four types of tools: idea generation (breaking current patterns), focus (broadening where to look), harvest (extracting more value from the output), treatment (considering real constraints). The key techniques are:
- **Provocation** (PO): a deliberately wrong or impossible statement, used to generate new ideas
- **Random Entry**: a random concept is forcibly associated with the problem
- **Reversal**: the process is reversed — from the result back to the starting point

**Application in Lens:** forcing functions of the "inversion" and "exclusion" type are direct implementations of lateral thinking. Provocation PO is a type of constraint not yet explored: "PO: customers don't want to buy" — an impossible statement that forces lateral paths.

### 2.12 Steelmanning

**Source:** [Umbrex](https://umbrex.com/resources/tools-for-thinking/what-is-steelmanning/)

Steelmanning is the opposite of strawmanning: building the **strongest possible version** of an argument, even one you contest. Four principles: interpretive charity, accuracy, strengthening, verification. It transforms debate from confrontation into collaborative problem-solving.

**Application in Lens:** a new topology or variant of the Cascade. Instead of attacking (antithesis), each agent **strengthens** the previous one's position. The version that emerges after 4 rounds of steelmanning is the most robust possible version of the argument. Complementary to the adversarial cascade: first steelman (find the strongest version), then adversarial (attack it). What survives both is unassailable.

### 2.13 Scenario Planning (Shell/Schwartz)

**Source:** Schwartz, "The Art of the Long View", 1991; [Systems Thinker](https://thesystemsthinker.com/planning-for-multiple-futures/)

Scenario planning does not predict the future — it constructs **multiple plausible futures** based on critical uncertainties. Method: identify 2 key uncertainties, build a 2x2 matrix, explore the 4 quadrants as alternative scenarios. Shell used this method to anticipate the collapse of oil prices.

**Application in Lens:** the specialized "Lens Scenario" workflow. Input: a decision + 2 uncertainties. Output: 4 structured scenarios, each explored by a different agent with constraints coherent to its quadrant. It is not a focus group — it is a map of possible futures.

### 2.14 Morphological Analysis (Zwicky)

**Source:** Zwicky; [Ness Labs](https://nesslabs.com/zwicky-box)

Morphological analysis decomposes a problem into dimensions, lists the possible variants for each dimension, then systematically explores the combinations. Zwicky's ambition was "to make invention routine" — a methodical process, not a stroke of genius.

**Application in Lens:** the Constraint Composer could use a morphological approach to generate combinations of constraints. Dimensions: constraint type x temporal frame x semantic domain x intensity level. Systematic exploration of the combination space guarantees that potentially powerful configurations are not overlooked.

### 2.15 Socratic Method (Elenchus)

**Source:** Socrates/Plato; [Conversational Leadership](https://conversational-leadership.net/socratic-elenchus/)

The elenchus is the central technique of the Socratic method: the interlocutor asserts a thesis, Socrates obtains agreement on additional premises, then demonstrates that these premises imply the opposite of the original thesis. It does not provide answers — it uncovers hidden assumptions and exposes contradictions.

**Application in Lens:** the "Socratic Drill" topology. A Socrates-agent has no position of its own — it only asks questions. The questions are constrained to uncover assumptions (not to demolish, as in the adversarial). The output is not a map of positions but a map of **hidden assumptions** with their degree of vulnerability.

### 2.16 Wisdom of Crowds (Surowiecki)

**Source:** Surowiecki, "The Wisdom of Crowds", 2004; [Wikipedia](https://en.wikipedia.org/wiki/The_Wisdom_of_Crowds)

The conditions for a group to be intelligent are four: **diversity of opinion**, **independence** of members, **decentralization**, and an **aggregation mechanism**. Crucially: "too much communication can make the group as a whole less intelligent" — independence is fundamental.

**Application in Lens:** a critical architectural principle. In Round 1 of every topology, agents **must not see** each other's positions (computational independence). Communication arrives only in later rounds, mediated by the moderator. This is not an implementation detail — it is the necessary condition for collective intelligence.

### 2.17 Tree/Graph of Thoughts

**Source:** [Yao et al., 2023](https://arxiv.org/abs/2305.10601); [ETH Zurich](https://htor.inf.ethz.ch/publications/img/besta-topologies.pdf)

Tree of Thoughts (ToT) maintains a tree where each node is an intermediate thought, with branching, backtracking and self-evaluation. Graph of Thoughts (GoT) generalizes to arbitrary graphs with merging of parallel branches. ToT took GPT-4 from 4% to 74% success on Game of 24.

**Application in Lens:** Lens topologies are essentially reasoning topologies. The Cascade is a chain, the Star is a one-level tree, the Adversarial+Jury is a graph with evaluation nodes. Lens could support custom topologies as user-defined graphs of thought.

### 2.18 Counterfactual Reasoning

**Source:** [Arxiv](https://arxiv.org/html/2410.06392v1); [Decision Lab](https://thedecisionlab.com/reference-guide/computer-science/counterfactual-reasoning-in-ai)

Counterfactual reasoning generates causal graphs and performs atomic interventions to infer consequences in "what if?" scenarios. Limitation: LLMs struggle to hold variables constant while altering others.

**Application in Lens:** a "counterfactual" type constraint. "What would have happened if we had NOT chosen X?" forces the LLM to reason about alternative causal chains. Combined with Klein's premortem, it creates a powerful tool for retrospective decision analysis.

### 2.19 Constitutional AI and Recursive Self-Critique

**Source:** [Anthropic](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)

The model critiques its own response according to explicit principles, then revises the response in light of the critique. An iterative process that improves quality without human feedback.

**Application in Lens:** every Lens agent could have a self-critique phase before delivering its output. The constraint is not just "respond from this perspective" but "respond, then critique your response from the standpoint of your own biases, then revise". It adds a layer of internal refinement that reduces noise.

### 2.20 Empirical Research on Multi-Agent Debate (2024-2025)

**Key sources:**
- [A-HMAD](https://link.springer.com/article/10.1007/s44443-025-00353-3): heterogeneous agents in debate produce +4-6% accuracy, -30% factual errors
- [Focus Agent](https://arxiv.org/html/2409.01907v1): LLM focus groups generate opinions similar to human participants
- [Park, Stanford 2024](https://arxiv.org/abs/2411.10109): personas from qualitative interviews replicate responses at 85%
- [Multi-Agent Systems 2025](https://www.preprints.org/manuscript/202511.1370): the next scaling frontier is not larger models but "societies of models"
- [Divergent Creativity](https://www.nature.com/articles/s41598-025-25157-3): LLMs surpass the human average in divergent thinking, but not the top human decile

---

## 3. System Architecture

### 3.1 Architectural Principle

**The constraint is the primitive.** Everything else — personas, topologies, sessions — is built on top of the Constraint Engine.

A "lens" is not a persona. It is a **configuration of cognitive constraints** that shifts the LLM's point of observation. A persona is a usage pattern on top of the Constraint Engine (a bundle of constraints with a name and an identity).

### 3.2 Components

```
Lens
├── Constraint Engine            ← the fundamental primitive
│   ├── Forcing Functions        (exclusion, limits, inversion)
│   ├── Frame Shifts             (temporal, semantic, role)
│   ├── Contradiction Resolver   (TRIZ-like constraints)
│   └── Constraint Composer      (combine, parametrize, generate)
│
├── Topology Engine              ← how agents interact
│   ├── Cascade                  (iterated Hegelian dialectic)
│   ├── Star / Delphi            (central moderator + N spokes)
│   ├── Adversarial + Jury       (ACH — debate + separate evaluation)
│   ├── Ring                     (sequential accumulation, each sees only the previous)
│   └── Parallel Hats            (De Bono — N agents, each a cognitive mode)
│
├── Persona Layer                ← bundles of constraints with identity
│   ├── Cognitive Templates      (lightweight JSON: biases, fears, goals, vocabulary, threshold)
│   ├── Miner-Grounded           (built from real audience data)
│   └── Custom / Project         (created for a specific context)
│
├── Session Manager              ← orchestrates execution
│   ├── Session Config           (topic, constraints, topology, N agents)
│   ├── Agent Spawner            (creates agents with assigned constraints)
│   ├── Turn Manager             (manages rounds, timing, order)
│   └── Moderator                (synthesizes, maps, does not flatten)
│
├── Output Formatter             ← rigid output structure
│   ├── Perspective Card         (claim, support, blind spot, confidence)
│   ├── Field Map                (convergences, divergences, outliers, tensions)
│   ├── Delta Report             (what is here that was not in the baseline)
│   └── Decision Brief           (recommendation with weighted pros/cons)
│
└── Meta-Lens                    ← self-optimization
    ├── Efficacy Tracker          (which constraint produces the most divergence)
    ├── Combination Suggester     (proposes new configurations)
    └── Session History           (session archive for pattern mining)
```

### 3.3 Flow of a Lens Session

```
INPUT                          PROCESSING                      OUTPUT
─────                          ──────────                      ──────
                               ┌─────────────────┐
  Topic/Problem ───────────────│ Session Config   │
  + Topology choice            │ (topic, topology │
  + Optional constraints       │  N agents, rounds)│
                               └────────┬────────┘
                                        │
                               ┌────────▼────────┐
                               │ Constraint       │
                               │ Composer          │─── generates N sets
                               │ (assigns          │    of different
                               │  constraints      │    constraints
                               │  per agent)      │
                               └────────┬────────┘
                                        │
                               ┌────────▼────────┐
                               │ Agent Spawner    │
                               │ (N agents with   │    Round 1: independent
                               │  own constraints)│    elaboration
                               └────────┬────────┘
                                        │
                               ┌────────▼────────┐
                               │ Topology Engine  │    Round 2-N: interaction
                               │ (manages how     │    according to the chosen
                               │  they interact)  │    topology
                               └────────┬────────┘
                                        │
                               ┌────────▼────────┐
                               │ Moderator        │
                               │ (synthesizes,    │──── does NOT seek consensus
                               │  maps the field) │     maps the positions
                               └────────┬────────┘
                                        │
                               ┌────────▼────────┐     ┌──────────────┐
                               │ Output Formatter │────▶│ Field Map    │
                               │                  │     │ Delta Report │
                               │                  │     │ Decision Brief│
                               └──────────────────┘     └──────────────┘
                                                               │
                                                        ┌──────▼──────┐
                                                        │ Meta-Lens   │
                                                        │ (tracks     │
                                                        │  efficacy)  │
                                                        └─────────────┘
```

---

## 4. Cognitive Topologies — In Detail

Topologies are not just communication structures. They are **cognitive patterns** that determine how collective intelligence emerges.

### 4.1 Cascade (Hegelian Dialectic)

```
A ──thesis──▶ B ──antithesis──▶ C ──synthesis──▶ D ──new antithesis──▶ ...
```

**When to use it:** stress-test an idea, find the core that survives systematic attack.
**Mechanism:** each agent sees only the previous one's output and must attack it. What survives the cascade is the solid core.
**Foundation:** Hegelian dialectic + adversarial debate (A-HMAD, +4-6% accuracy).

### 4.2 Star / Delphi

```
        B
       ╱
  A ──M── C     M = moderator
       ╲
        D
```

**When to use it:** explore a problem from N independent perspectives, then synthesize.
**Mechanism:** N agents elaborate independently (computational anonymity). The moderator presents, the agents revise. Iterative convergence.
**Foundation:** Delphi method + Disagreement Delphi (map of disagreement).

### 4.3 Adversarial + Jury (ACH)

```
  A ◄──debate──► B
         │
    ┌────▼────┐
    │ J1 J2 J3│   (independent jury)
    └─────────┘
```

**When to use it:** high-impact decisions where you need to separate production from evaluation.
**Mechanism:** 2 agents debate with opposing constraints. 3 jurors (each with different constraints) evaluate independently. No juror talks to the others.
**Foundation:** Analysis of Competing Hypotheses (CIA SAT) + separation of concerns.

### 4.4 Ring (Sequential Accumulation)

```
  A ──▶ B ──▶ C ──▶ D ──▶ (back to A)
```

**When to use it:** build on an idea incrementally, each agent adds a layer.
**Mechanism:** each agent sees only the previous one's output (not the original). The idea transforms as it passes through different constraints. The final output is unrecognizable from the input — it has been reframed N times.
**Foundation:** Watzlawick (iterated reframing) + structured telephone game.

### 4.5 Parallel Hats (Computational De Bono)

```
  [Facts] [Risks] [Opportunities] [Emotions] [Creativity] [Process]
     │        │          │            │           │            │
     └────────┴──────────┴────────────┴───────────┴────────────┘
                              │
                         Integration
```

**When to use it:** exhaustive analysis where you need to cover all dimensions of a problem.
**Mechanism:** N agents, each constrained to a single cognitive mode. No agent can invade the others' territory. Final integration by the moderator.
**Foundation:** Six Thinking Hats + parallel thinking (not debate, not conflict — parallel exploration).

### 4.6 Steelman Chain

```
A ──strengthens──▶ B ──strengthens──▶ C ──strengthens──▶ (strongest version)
                                                              │
                                                         Adversarial ◄── D attacks
```

**When to use it:** find the strongest version of an argument, then test it under pressure.
**Mechanism:** first a steelmanning phase (each agent strengthens the previous one's position), then an adversarial phase (one agent attacks the strongest version). What survives is genuinely robust.
**Foundation:** steelmanning + sequential adversarial cascade.

### 4.7 Socratic Drill

```
  Theme ──▶ Socrates (questions) ──▶ Assumption 1 ──▶ Socrates (questions) ──▶ ...
                                       │
                                  Vulnerability?
```

**When to use it:** uncover the hidden assumptions underlying a position, not attack it.
**Mechanism:** a Socrates-agent has no position of its own. It only asks questions. Each question is constrained to uncover an implicit assumption. The output is a map of assumptions with degree of vulnerability.
**Foundation:** Socratic elenchus — it does not provide answers, it uncovers the hidden structure of the reasoning.

### 4.8 Scenario Matrix

```
                    Uncertainty A high
                         │
  Uncertainty B  ┌───────┼───────┐
  low ───────────│  Q1   │  Q2   │
                 ├───────┼───────┤
                 │  Q3   │  Q4   │
  Uncertainty B  └───────┼───────┘
  high                   │
                    Uncertainty A low

  4 agents, one per quadrant, constraints coherent with its own scenario
```

**When to use it:** explore multiple futures for high-uncertainty decisions.
**Mechanism:** 2 critical uncertainties define a 2x2 matrix. 4 agents each explore one scenario. The moderator does not seek the "most probable future" but maps the robust strategies (those that work in 3+ scenarios out of 4).
**Foundation:** Shell/Schwartz scenario planning — multiple plausible futures, not prediction.

### 4.9 Bisociation Engine

```
  Problem ──▶ Matrix A (original domain)
                     ╲
                      ╳ ──▶ Intersection = insight
                     ╱
               Matrix B (forced domain)
```

**When to use it:** generate genuinely creative insight through collision between domains.
**Mechanism:** the problem is described in two radically different semantic domains. One agent operates in the original domain, one in the forced domain. The moderator searches for intersections — where the two matrices overlap, bisociation emerges (Koestler).
**Foundation:** bisociation + structured semantic reframing.

### 4.10 Wise Mind (DBT)

```
  [Emotional Agent]     [Rational Agent]
         │                      │
         └──────────┬───────────┘
                    │
            [Wise Mind Synthesizer]
```

**When to use it:** decisions where intuition and logic diverge.
**Mechanism:** one agent operates only with intuition/emotions/fears. Another only with facts/logic/data. A third synthesizes — it does not choose one of the two, it integrates. Where is emotion right in ways logic does not see? Where does logic correct emotion?
**Foundation:** Linehan, DBT (1993) — wisdom emerges from integration, not from choice.

### 4.11 SCAMPER Parallel

```
  [Substitute] [Combine] [Adapt] [Modify] [Put to use] [Eliminate] [Reverse]
       │            │        │       │          │            │           │
       └────────────┴────────┴───────┴──────────┴────────────┴───────────┘
                                     │
                                Synthesis
```

**When to use it:** systematic innovation on an existing product/process/idea.
**Mechanism:** 7 agents, each constrained to a single SCAMPER operation. None can perform the others' operations. The moderator synthesizes the most promising proposals.
**Foundation:** Eberle/Osborn. GPT-4 with SCAMPER produces output at the 75th percentile vs human students (Cambridge 2024).

### 4.12 Assumption Inversion

```
  Topic ──▶ Socratic Drill (extracts assumptions)
                    │
             [A1] [A2] [A3] [A4] [A5]
                    │
             Rank by importance/certainty
                    │
             Invert top-3 ──▶ [Agent 1: A1 inverted]
                              [Agent 2: A2 inverted]
                              [Agent 3: A3 inverted]
                    │
             Explore implications
```

**When to use it:** uncover hidden opportunities in assumptions taken for granted.
**Mechanism:** first the Socratic Drill extracts the assumptions. Then they are ranked by impact. Then the top-3 are inverted and dedicated agents explore the implications of each inversion.
**Foundation:** Mason & Mitroff SAST (1981). Historical examples: "cars need a driver" → autonomous vehicles.

---

## 5. The Constraint Engine — Heart of the System

### 5.1 Taxonomy of Constraints

| Category | Description | Examples |
|---|---|---|
| **Exclusion** | Remove the refuge vocabulary/concepts | "Without using the words X, Y, Z", "No examples from the industry" |
| **Inversion** | Force the opposite conclusion | "Prove the contrary", "Why is it a terrible idea?" |
| **Limit** | Impose scarcity of expressive resources | "3 sentences maximum", "A single argument" |
| **Temporal** | Shift the point of observation in time | "From 2030, in retrospect", "1970s, before the Internet" |
| **Semantic** | Change the domain vocabulary | "In biological terms", "As an architecture" |
| **Role** | Assign a cognitive frame (not a costume) | Explicit biases, fears, goals, constrained vocabulary |
| **Contradiction** | TRIZ constraints — improve X without worsening Y | "Faster without additional cost" |
| **Modal** | Constrain to a cognitive dimension (De Bono) | "Risks only", "Only verifiable facts", "New ideas only" |
| **Provocation** | Impossible statement as a starting point (De Bono PO) | "PO: customers don't want to buy", "PO: the product is free" |
| **Counterfactual** | Reasoning about alternative scenarios | "What if we had NOT chosen X?", "What if the competitor had won?" |
| **Socratic** | Questions only, no statements | "What assumptions are you making?", "What is it based on?" |
| **Steelman** | Strengthen the position instead of attacking it | "Build the strongest possible version of this argument" |
| **Bisociative** | Force collision between two domains | "Describe in terms of X", where X is an incompatible domain |
| **Self-critique** | Critique your own response before delivering it | "Respond, then critique from the standpoint of your biases, then revise" |
| **Janusian** | Hold two opposing positions simultaneously and transcend them | "X is true AND not-X is true. Find the framework that contains both" |
| **Dissonance** | Force two contradictory beliefs and require reconciliation | "The product is excellent AND has a fatal flaw. Argue both" |
| **Abductive** | Generate the most surprising yet plausible explanation | "NON-obvious explanation. Common causes forbidden" |
| **Defamiliarize** | Describe as if seeing for the first time | "Anthropologist studying an unknown civilization" |
| **Synectics** | Force a specific analogy (direct/personal/symbolic/fantasy) | "You are the product. How do you feel when the customer uses you?" |
| **SCAMPER** | Constrain to a single SCAMPER operation | "Reverse only: invert every aspect of the process" |
| **Abstraction** | Constrain to a specific level (Concept Fan) | "Fundamental purpose only, not solutions", "Concrete implementation only" |
| **ELM Route** | Process via the central or peripheral route | "Evaluate argument logic only" vs "Evaluate credibility, tone, appeal" |
| **Set-shift** | Force a frame change when perseveration is detected | "The output is too predictable. Completely change approach" |

### 5.2 Composition of Constraints

Constraints are **composable**. An agent can operate under multiple simultaneous constraints:

```json
{
  "agent_id": "critic_futurist",
  "constraints": [
    {"type": "inversion", "value": "prove why it will fail"},
    {"type": "temporal", "value": "from 2030, in retrospect"},
    {"type": "exclusion", "value": ["innovation", "disruption", "AI-first"]},
    {"type": "limit", "value": "5 points maximum, each with evidence"}
  ]
}
```

The combination of constraints produces output that no single constraint would produce on its own. The Constraint Composer generates combinations, the Meta-Lens tracks which combinations produce the most divergence.

---

## 6. Output Formats

### 6.1 Perspective Card (single-agent output)

```yaml
perspective_card:
  agent: "Skeptical CTO"
  constraints_active: [inversion, temporal_2030, exclusion_buzzwords]

  claim: "Adoption will fail due to organizational resistance, not technical"

  supporting_evidence:
    - "73% of enterprise AI failures are organizational (Gartner)"
    - "No change management plan in the document"

  blind_spots:
    - "I do not consider the network effect of internal early adopters"
    - "I underestimate the power of a top-down mandate"

  confidence: 0.7

  what_would_change_my_mind: "Evidence of internal champions with decision-making power"
```

### 6.2 Field Map (multi-agent session output)

```yaml
field_map:
  topic: "Go-to-market for a new B2B SaaS product"
  topology: "star_delphi"
  agents: 4
  rounds: 2

  convergences:
    - claim: "A killer use case is needed before the platform play"
      agreed_by: [agent_1, agent_2, agent_4]
      confidence_avg: 0.82

  divergences:
    - topic: "Pricing model"
      positions:
        agent_1: "Freemium with enterprise upsell"
        agent_3: "Enterprise only, no freemium"
      tension: "Accessibility vs premium positioning"

  outliers:
    - claim: "The real competitor is not another tool, it's the shared Google Doc"
      source: agent_2
      why_interesting: "Completely reframes the competitive landscape"

  blind_spots_identified:
    - "No agent considered the GDPR regulatory risk on brand data"

  recommended_explorations:
    - "Deepen agent_2's outlier with an adversarial cascade"
    - "Test the pricing with an Adversarial+Jury topology"
```

### 6.3 Delta Report (comparison with baseline)

```yaml
delta_report:
  baseline: "Standard response without constraints"
  lens_config: "4 agents, star topology, 2 rounds"

  insights_only_in_lens: 7
  insights_only_in_baseline: 1
  shared_insights: 4

  highest_value_delta:
    - insight: "The real competitor is the Google Doc"
      value_score: 2  # 0=obvious, 1=new, 2=surprising
      not_in_baseline: true

  semantic_distance:
    baseline_vs_lens: 0.34  # cosine distance (high = more different)
    baseline_vs_simple_roleplay: 0.12  # simple roleplay does not add much
```

---

## 7. Integration (example: the author's ecosystem)

> This section is illustrative: it shows how Lens fits into a broader workflow.
> Lens works autonomously and requires no external system.

### 7.1 Positioning

Lens is a **cross-cutting cognitive layer**. It is neither a consumer nor a producer of final content: it is a quality amplifier that sits between upstream data and downstream artifacts.

```
UPSTREAM (feed Lens)                    DOWNSTREAM (Lens stresses)
─────────────────────────               ──────────────────────────
External structured data       →        Any artifact or decision:
(e.g. real audience profiles            presentations, strategies, copy,
 via the Miner adapter)                 product choices, roadmaps…
                               →        before finalizing them, pass them
Problem context                →        through a Lens topology.
```

### 7.2 Integration Interfaces

**MCP Server (25 tools implemented):**

Constraint tools:
- `lens_list_constraints(category?)` — list constraints by category
- `lens_get_constraint(constraint_id)` — detail of a single constraint

Persona tools:
- `lens_list_personas()` — list persona templates
- `lens_get_persona(persona_id)` — detail of a persona template

Topology tools:
- `lens_list_topologies(mode?)` — available topologies (QUICK/DEEP)
- `lens_get_topology(topology_id)` — topology detail with workflow

Composition tools:
- `lens_compose_prompt(topic, constraints, output_format, intensity)` — constraints + topic into a structured prompt
- `lens_compose_persona(persona_id, topic, output_format, intensity)` — persona template into a prompt
- `lens_compose_baseline(topic, output_format)` — baseline without constraints for the delta workflow
- `lens_suggest_constraints(topic, goal, max_constraints)` — data-driven + heuristic suggestions

Session tools:
- `lens_session_save(...)` — save a session with an efficacy rating
- `lens_session_list(limit?)` — recent sessions
- `lens_efficacy_report()` — aggregated efficacy report

Meta-Lens tools:
- `lens_meta_constraint_efficacy()` — which constraints produce the best results
- `lens_meta_topology_efficacy()` — which topologies work best
- `lens_meta_patterns()` — successful constraint combinations
- `lens_meta_suggest(topic, goal?)` — data-driven suggestions from session history

Miner integration tools:
- `lens_persona_from_miner(miner_persona_json, save?)` — transform a single Miner persona
- `lens_personas_from_miner_batch(miner_output_json, save?)` — transform all Miner personas

**Claude Code Skills (9 implemented):**
- `/lens` — interactive DEEP mode session, suggests a topology and configures agents
- `/lens-adversarial` — fast adversarial cascade on a claim (QUICK)
- `/lens-perspective` — single constrained perspective (QUICK)
- `/lens-premortem` — structured Klein premortem (QUICK)
- `/lens-focus-group` — cognitive focus group with personas (DEEP)
- `/lens-steelman` — build the strongest argument, then stress-test (QUICK)
- `/lens-scenarios` — 2x2 scenario planning (DEEP)
- `/lens-assumptions` — uncover and invert hidden assumptions (QUICK/DEEP)
- `/lens-deep` — sequential single-agent chain with progressive constraints (DEEP)

### 7.3 Concrete Flows

**External data → grounded persona (Miner adapter):**
An audience research system produces an `AudiencePersona` (demographics, psychographics/VALS, interests, behaviors, pain_points, goals) → `lens_persona_from_miner()` transforms it into a Lens cognitive template with this mapping:
- demographics + occupation → role constraint
- psychographics.values + attitudes → modal constraint
- VALS segment → ELM route (central/peripheral processing)
- pain_points → psychology.fears
- goals → psychology.primary_goal
- decision_making_style → convincement_threshold

The resulting personas are grounded in real data, not invented by the LLM. The adapter is a pure dictionary transformation (`integrations/miner.py`): it works with any input conforming to the `AudiencePersona` schema, regardless of its origin.

**Stress-testing a downstream artifact:**
Before finalizing a presentation, a strategy or a product choice, you pass it through 3-4 personas (e.g. skeptical customer, enthusiast, journalist) and obtain a Field Map with blind spots and weak points — or you use an Adversarial+Jury topology to put it under pressure.

**Lens as a capability:**
Any agent or workflow can invoke a Lens perspective on any decision: the MCP tools make Lens a composable capability, not a standalone app.

---

## 8. Validation Protocol

### 8.1 Test 1 — Circularity (GATE-KEEPER)

**Null hypothesis:** Lens personas/constraints do not produce semantically different insights compared to a standard LLM.

**Design:**
- Condition A: direct prompt (baseline)
- Condition B: simple role prompting
- Condition C: structured Lens constraints

**Criteria:**
- Success: C generates ≥30% insights not present in A
- Blind confusion test: the human evaluator prefers C in ≥60% of cases
- HUMAN evaluation (not LLM-on-LLM)

If Test 1 fails → the project must be rethought.

### 8.2 Test 2 — Topologies

Same problem, different topologies. Which produces the richest Field Map?

### 8.3 Test 3 — Diminishing Returns

Focus group 2 → 3 → 4 → 5 → 6 agents. Where does the margin of unique insights flatten out?

### 8.4 Test 4 — Grounded vs Synthetic Persona

A persona built from Miner data vs a persona invented by the LLM. Which produces more actionable insights?

---

## 9. Primary Use Cases

### 9.1 Stress-testing a strategic decision
**Topology:** Adversarial + Jury
**Example:** "Should we launch the product as freemium or enterprise-only?"
Two agents with opposing constraints debate, three jurors with different profiles evaluate.

### 9.2 Pre-mortem on a project
**Topology:** Star/Delphi
**Example:** "It's 2028, Lens has been abandoned. Why?"
4-5 agents with different temporal and role constraints produce independent failure scenarios.

### 9.3 Exploring a problem from N dimensions
**Topology:** Parallel Hats
**Example:** "Analyze the commercial proposal for client X"
6 agents, each constrained to one dimension (facts, risks, opportunities, the client's emotions, creative ideas, process).

### 9.4 Finding the solid core of an argument
**Topology:** Cascade
**Example:** "Our positioning is: 'AI infrastructure for creative agencies'"
The argument goes through 4-5 rounds of attack. What survives is the unassailable core.

### 9.5 Simulating the reaction of different audiences
**Topology:** Star/Delphi with Miner-grounded personas
**Example:** "How will SMB CTOs, marketing managers, and CEOs react to this presentation?"
Personas built from real Miner data, not invented.

### 9.6 Generating non-linear insight (Bisociation)
**Topology:** Ring + Bisociation Engine
**Example:** "What happens if we pass the concept of 'brand loyalty' through 4 different semantic frames?"
Ring with semantic constraints: biological → architectural → musical → military. The final output is a perspective that no single frame would have produced. The moderator identifies the bisociation points — where two incompatible matrices produce a new idea.

### 9.7 Uncovering hidden assumptions (Socratic Drill)
**Topology:** Socratic Drill
**Example:** "Our go-to-market plan rests on which unverified assumptions?"
The Socrates-agent systematically interrogates every element of the plan. Output: a map of N assumptions with a vulnerability score and test suggestions.

### 9.8 Exploring alternative futures (Scenario Planning)
**Topology:** Scenario Matrix
**Example:** "The AI market for agencies: 2 uncertainties — fast vs slow adoption, commodity vs differentiated AI"
4 agents explore the 4 quadrants. Output: 4 scenarios with specific strategies + identification of robust strategies (valid in 3+ scenarios).

### 9.9 Building the perfect argument (Steelman + Adversarial)
**Topology:** Steelman Chain
**Example:** "Why should a company invest in this platform?"
3 rounds of steelmanning → strongest possible version → 2 adversarial rounds. Output: the argument in its most robust form + the only surviving objections.

### 9.10 Systematic innovation (Morphological + Constraint)
**Topology:** Parallel Hats + Morphological
**Example:** "Which new features for the product have we not considered?"
Decompose the problem into dimensions (input, processing, output, format, audience). Generate combinations with a Zwicky box. Filter with constrained agents (feasibility, value, cost). Output: a matrix of combinations with scoring.

---

## 10. Project Plan

### Phase 0 — MCP Server + Constraint Engine + Validation (completed)
**Objective:** demonstrate that structural constraints produce genuinely different output.
**Deliverables:**
- [x] FastMCP MCP server with core tools (server.py)
- [x] Constraint Composer (constraints/composer.py)
- [x] 25 constraint templates in library.json (7 categories)
- [x] 5 cognitive templates (personas/templates/)
- [x] 13 topologies defined (topologies/definitions.json)
- [x] Output Formatter: Perspective Card, Field Map, Delta Report, Cascade Report
- [x] `lens-perspective` skill (QUICK)
- [x] `lens-adversarial` skill (QUICK)

### Phase 1 — Interactive Skills + Baseline+Delta (completed)
**Objective:** implement DEEP mode skills and the baseline+delta workflow.
**Deliverables:**
- [x] Interactive `/lens` skill (DEEP mode with topology choice)
- [x] `/lens-focus-group` skill (DEEP mode with personas)
- [x] `/lens-premortem` skill (QUICK mode, Klein)
- [x] `lens_compose_baseline()` tool for the delta workflow
- [x] Fix variable substitution in the Constraint Composer

### Phase 2 — Advanced Skills (completed)
**Objective:** skills for the more sophisticated topologies.
**Deliverables:**
- [x] `/lens-steelman` skill (QUICK mode, Steelman Chain)
- [x] `/lens-scenarios` skill (DEEP mode, Scenario Matrix)
- [x] `/lens-assumptions` skill (QUICK/DEEP mode, Socratic + Inversion)

### Phase 3 — Meta-Lens + Analytics (completed)
**Objective:** the system learns from itself.
**Deliverables:**
- [x] Efficacy Tracker: constraint_efficacy(), topology_efficacy()
- [x] Pattern Mining: successful constraint combinations (meta/analytics.py)
- [x] Data-driven Combination Suggester (suggest_from_history())
- [x] 4 Meta-Lens tools in the MCP server
- [x] lens_suggest_constraints with data-driven + heuristic fallback
- [x] Session save with constraints_used for tracking

### Phase 3b — Miner Integration + Documentation (completed)
**Objective:** integration with real audience data and complete documentation.
**Deliverables:**
- [x] integrations/miner.py module (transform, save, batch)
- [x] 2 MCP tools: lens_persona_from_miner, lens_personas_from_miner_batch
- [x] Complete README.md
- [x] LENS.md updated to the implemented state

### Future Phase — Evolution
**Potential developments:**
- [ ] Adapter toward downstream artifacts (validation of presentations, strategies, copy)
- [ ] Test 4 (grounded vs synthetic persona, post-adapter)
- [ ] Additional topologies as dedicated skills (ring, bisociation, scamper)
- [ ] Expanded Constraint Library with domain-specific constraints

---

## 11. Decisions Made and Questions Resolved

1. **Backend or skill-only?** Resolved: FastMCP MCP server from Phase 0. No separate FastAPI backend. The MCP server covers the constraint library, composition, session management and analytics. The skills stay lightweight (orchestration only).

2. **Which model for the agents?** On Claude Max all models are included. The skills use haiku for fast subagents, sonnet for synthesis and moderation, as specified in the SKILL.md files.

3. **How to manage cost?** Resolved: Claude Max = zero cost. Parallel rounds where possible (Star, Parallel Hats).

4. **Meta-Lens: how realistic is it?** Implemented. The Efficacy Tracker tracks per session. Pattern Mining finds successful combinations. Suggest uses topic similarity + efficacy weighting with a heuristic fallback.

5. **Ring topology: risk of drift?** Open question. The ring topology is defined but does not have a dedicated skill. The grounding check could be implemented as an additional constraint in the final round.

### Still Open Questions

6. **Grounded vs synthetic persona:** Test 4 (Miner persona vs invented persona) has not yet been run. The Miner integration is implemented, empirical validation is needed.

7. **Diminishing returns:** how many agents are really needed? Theory suggests 4-5 as optimal (moderate diversity, Aggarwal 2019). An empirical test on real problems is needed.

---

## 12. Design Principles

### Fundamental Principles

1. **The constraint is the primitive.** Everything is built on top of constraints. Personas are bundles of constraints. Topologies are interaction patterns among constrained agents. (Stokes, TRIZ)

2. **Reasoning is social.** A single agent is structurally sub-optimal. The multi-agent approach is not an optimization, it is the natural mode of reasoning. (Mercier & Sperber, 2011)

3. **Map, not answer.** The output of Lens is not "the best answer". It is a map of the field: convergences, divergences, outliers, tensions, blind spots. (Delphi, ACH)

4. **Separate production from evaluation.** Those who generate perspectives should not judge them. Those who judge should not have generated them. (CPS Osborn-Parnes)

5. **Independence first, interaction after.** In Round 1 agents do not see each other's positions. Independence in the first round is the necessary condition for collective intelligence. (Surowiecki)

6. **Structured dissent, not chaos.** Conflict is programmed, not random. Each agent has a precise mandate. (Janis)

7. **Moderate cognitive diversity.** Do not maximize diversity, optimize it. 4-5 genuinely different cognitive styles > 10 with marginal differences. An inverted-U relationship. (Ashby, Aggarwal 2019)

8. **Separate divergence and convergence.** Divergent phases (generating) and convergent phases (evaluating) do not mix. Premature judgment kills creativity. (Osborn-Parnes CPS)

### Operating Principles

9. **Validate before building.** No infrastructure without empirical evidence that the basic mechanism works.

10. **Self-optimization.** The system tracks its own efficacy and suggests improvements. (TRIZ principle #25: self-service)

11. **Error correlation as a metric.** If all agents fail in the same way, the constraints are not diverse enough. (Ensemble theory — uncorrelated errors → superiority of the ensemble)

12. **Transcendence, not compromise.** When oppositions emerge, the system seeks frameworks that contain both positions, not midpoints. (Rothenberg, Janusian Thinking)

# Lens — Theoretical Foundations and Research

> Research document — updated 28 February 2026
> Status: continuously expanding

---

## Index of theories by category

### A. Theories on the structure of creative thinking
- A1. Bisociation (Koestler)
- A2. Janusian Thinking (Rothenberg)
- A3. Lateral Thinking and Provocation (De Bono)
- A4. Defamiliarization / Ostranenie (Shklovsky)
- A5. Synectics and forced analogies (Gordon)
- A6. TRIZ and contradiction resolution (Altshuller)

### B. Theories on group thinking and collective intelligence
- B1. Wisdom of Crowds (Surowiecki)
- B2. Groupthink and structured dissent (Janis)
- B3. Argumentative Theory of Reasoning (Mercier & Sperber)
- B4. Cognitive Diversity and Requisite Variety (Ashby)
- B5. Ensemble Methods as a cognitive metaphor

### C. Theories on the structure of reasoning
- C1. Hegelian dialectic
- C2. Socratic Method / Elenchus
- C3. Abductive Reasoning (Peirce)
- C4. Dual Process Theory (Kahneman)
- C5. Tree/Graph of Thoughts
- C6. Constitutional AI and Self-Critique (Anthropic)

### D. Theories on persuasion and perception
- D1. Elaboration Likelihood Model (Petty & Cacioppo)
- D2. Perspective-Taking (cognitive science)
- D3. Cognitive Dissonance (Festinger)
- D4. Second-order reframing (Watzlawick)
- D5. Steelmanning

### E. Structured methodologies of analysis
- E1. Structured Analytic Techniques (CIA/IC)
- E2. Scenario Planning (Shell/Schwartz)
- E3. Morphological Analysis (Zwicky)
- E4. Red Teaming and Adversarial Collaboration
- E5. Premortem / Prospective Hindsight (Klein)
- E6. SCAMPER (Eberle/Osborn)
- E7. CPS Model (Osborn-Parnes)
- E8. Assumption Reversal / SAST (Mason & Mitroff)
- E9. Concept Fan (De Bono)

### F. Theories on cognitive flexibility and constraints
- F1. Cognitive Flexibility and Set-Shifting
- F2. Constraint-Based Creativity (Stokes)
- F3. DBT Wise Mind (Linehan)
- F4. Reflexivity (Soros/Bourdieu)

### G. Empirical research on multi-agent LLMs
- G1. Multi-Agent Debate (A-HMAD, Focus Agent)
- G2. Synthetic Personas (Park, Stanford)
- G3. Activation Steering and Control Vectors
- G4. Divergent Creativity in LLMs

---

## A. THEORIES ON CREATIVE THINKING

### A1. Bisociation (Koestler, 1964)

**Source:** "The Act of Creation"

**Mechanism:** creativity arises from the simultaneous perception of an idea in two habitually incompatible matrices of thought. It is not association (a connection within a frame), it is collision between independent frames.

**Three forms:**
- Humor: collision → surprise → laughter
- Scientific discovery: collision → eureka
- Art: collision → aesthetic juxtaposition

**Implication for Lens:** the Constraint Engine with semantic constraints is a generator of bisociations. The Ring topology is iterated bisociation. The Bisociation Engine is the dedicated topology.

**Implementation constraint:** `{"type": "bisociative", "domain_forced": "marine ecology", "domain_original": "marketing"}`

---

### A2. Janusian Thinking (Rothenberg, 1971)

**Source:** Rothenberg, "The Emerging Goddess: The Creative Process in Art, Science, and Other Fields" (1979); studies published in *American Journal of Psychiatry*

**Mechanism:** actively conceiving two or more opposite or antithetical ideas **simultaneously** as valid. It is not thinking about opposites in sequence: it is holding them both in mind at the same time, without resolving them immediately.

**Documented examples:**
- Einstein: a falling man is simultaneously in motion and at rest → relativity
- Bohr: light is simultaneously wave and particle → complementarity
- Watson: two opposite spatial structures → DNA double helix
- Mozart: "Dissonances are only remote consonances"

**Difference from "thinking in opposites":** sequential opposites produce compromises. Simultaneity produces transcendence — a new category that contains both without reducing either.

**Implication for Lens:**
- A "janusian" type constraint: the agent MUST hold two opposite positions at once and produce a synthesis that transcends them
- Different from the adversarial (where two agents attack each other): here it is ONE agent that holds both
- Possible implementation: a prompt that requires "X is true AND not-X is true at the same time. Generate a framework that contains both."

**Implementation constraint:** `{"type": "janusian", "thesis": "the market wants simplicity", "antithesis": "the market wants power", "requirement": "framework that transcends the contradiction"}`

**Critical note:** this is the cognitively most difficult constraint for an LLM. It will tend to seek a compromise (the center of the distribution). The constraint must explicitly forbid compromise and demand transcendence.

---

### A3. Lateral Thinking and Provocation (De Bono, 1967)

**Source:** "Lateral Thinking: Creativity Step by Step"; De Bono Group

**Four types of tools:**
1. **Idea-generating** — break current patterns
2. **Focus** — broaden where to search
3. **Harvest** — extract more value from the output
4. **Treatment** — consider real constraints

**Key techniques:**
- **Provocation (PO):** a deliberately wrong/impossible statement as a starting point. "PO: cars have square wheels" → generates ideas about adaptive suspensions
- **Random Entry:** a random concept forcibly associated with the problem. "Nose" + "photocopier" → a copier that smells of lavender when it runs out of paper (real)
- **Reversal:** reversed process. Not "how do we sell to the customer" but "how does the customer buy on their own"

**Implication for Lens:** forcing functions are direct implementations. Provocation is a type of constraint not yet explored in depth: it forces the LLM to start from an impossible statement and work from there.

**Implementation constraint:** `{"type": "provocation", "po_statement": "PO: our competitors are our allies", "requirement": "generate 3 strategies starting from this provocation"}`

---

### A4. Defamiliarization / Ostranenie (Shklovsky, 1917)

**Source:** "Art as Technique" (О́стране́ние)

**Mechanism:** presenting familiar things in unfamiliar ways to force a new perception. Perceptual automation (we see things without truly seeing them) is broken by the "making strange." Tolstoy describes common objects as if seeing them for the first time.

**Difference from semantic reframing:** reframing changes the vocabulary. Defamiliarization changes the level of observation — you describe something as if you had never seen anything like it before.

**Implication for Lens:** an "alien observer" type constraint — the agent must describe the problem as if seeing it for the first time, with no prior assumptions. It counters the LLM's familiarity bias.

**Implementation constraint:** `{"type": "defamiliarize", "instruction": "Describe this business model as if you were an anthropologist studying an unknown civilization"}`

---

### A5. Synectics (Gordon, 1961)

**Source:** "Synectics: The Development of Creative Capacity"

**Four types of forced analogy:**
1. **Direct Analogy:** a same-domain parallel (bird flight → airplane)
2. **Personal Analogy:** empathizing with the object ("feel" like a wing)
3. **Symbolic Analogy:** metaphorical (flight = "freedom")
4. **Fantasy Analogy:** impossible scenarios ("wings made of dreams")

**Real examples of innovation from Synectics:**
- Velcro: hooks of burdock seeds (direct analogy from nature)
- Pringles: compression of dried leaves → uniform stackable chips

**Implication for Lens:** each type of analogy is a different constraint. A Synectics focus group would have 4 agents, each bound to a different type of analogy, applied to the same problem.

**Implementation constraint:** `{"type": "synectics", "analogy_type": "personal", "instruction": "You are the product. How do you feel when the customer uses you?"}`

---

### A6. TRIZ (Altshuller, 1946+)

**Source:** "40 Inventive Principles"; the contradiction matrix (39x39)

**Mechanism:** true innovation arises from the resolution of technical contradictions. 40 inventive principles derived from hundreds of thousands of patents.

**Principles most relevant to Lens:**
- #1 Segmentation: dividing a system into independent parts → the basis of multi-agent topologies
- #13 Inversion: doing the opposite action → inversion forcing function
- #17 Dimensionality: moving from one dimension to multiple dimensions → adding perspectives
- #25 Self-service: making an object serve itself → Meta-Lens (self-optimization)
- #35 Transformation of properties: changing the state of the system → forced set-shifting

**Implication for Lens:** the 40 TRIZ principles can be mapped as a library of structured constraints.

---

## B. THEORIES ON GROUP THINKING AND COLLECTIVE INTELLIGENCE

### B1. Wisdom of Crowds (Surowiecki, 2004)

**Source:** "The Wisdom of Crowds"

**Four necessary conditions:**
1. **Diversity of opinion** — each person has private information
2. **Independence** — opinions are not influenced by those of others
3. **Decentralization** — no one directs from the top
4. **Aggregation mechanism** — a method to turn individual judgments into a collective decision

**Critical condition:** "too much communication can make the group less intelligent"

**Implication for Lens:** ARCHITECTURAL PRINCIPLE. In Round 1 of every topology, the agents must NOT see the positions of the others. Computational independence in the first round is not a detail, it is the necessary condition for collective intelligence.

---

### B2. Groupthink (Janis, 1971)

**Source:** "Victims of Groupthink"

**Mechanism:** members of a cohesive group unconsciously develop shared illusions that interfere with critical thinking.

**Prevention:** institutionalized devil's advocate, programmed dissent, structured conflict.

**Implication for Lens:** the LLM has a structural bias toward consensus. Lens counters this with programmed dissent.

---

### B3. Argumentative Theory of Reasoning (Mercier & Sperber, 2011/2017)

**Source:** "The Enigma of Reason" (2017); original paper in *Behavioral and Brain Sciences* (2011)

**Central thesis:** human reasoning did NOT evolve to seek truth in solitude. It evolved for argumentation in social contexts — producing arguments to persuade and evaluating others' arguments to avoid being deceived.

**Devastating implication:** the reasoning of a single agent is **fundamentally limited**. Biases (confirmation bias, myside bias) are not bugs of reasoning — they are features of social argumentation. In solitude they produce errors. In a group they produce truth.

**Implication for Lens:** this is the strongest theoretical justification for the multi-agent approach. If reasoning is intrinsically social, a single LLM "reasoning on its own" is structurally limited. Multi-agent debate is not an optimization — it is the natural mode of reasoning.

**Architectural constraint:** every Lens session should have a MINIMUM of 2 agents. The single agent is by definition sub-optimal according to Mercier & Sperber.

---

### B4. Cognitive Diversity and Requisite Variety (Ashby, 1956)

**Source:** Ashby, "An Introduction to Cybernetics"; Aggarwal et al. (2019), PMC6374291

**Ashby's law:** the internal variety of a system must be at least equal to the variety of the environment in order to control it effectively.

**Key findings on cognitive diversity in teams:**
- Diversity of **cognitive style** (how information is processed) is more important than demographic or functional diversity
- The relationship is an inverted U: moderate diversity maximizes collective intelligence; too much diversity destroys coordination
- Functional diversity (differing expertise) and cognitive diversity outperform demographic diversity

**Implication for Lens:** agents must have different cognitive styles (analytical vs holistic, detail vs big picture), not just different positions. Diversity must be moderate — 4-5 agents with genuinely different styles, not 10 with marginal differences.

---

### B5. Ensemble Methods as a cognitive metaphor

**Source:** DARPA "Quantifying Ensemble Diversity for Robust ML"; Wolpert (1992) stacking

**Principle:** diverse weak learners combined outperform a single strong learner. The condition is that the errors be uncorrelated.

**Three patterns:**
- **Bagging:** different samples of the same problem → average of predictions (reduces variance)
- **Boosting:** each learner focuses on the errors of the previous one (reduces bias)
- **Stacking:** a meta-learner combines heterogeneous outputs (maximizes diversity)

**Implication for Lens:**
- The Star topology is cognitive bagging (N independent agents → aggregation)
- The Cascade topology is cognitive boosting (each agent focuses on the weaknesses of the previous one)
- The Moderator is a meta-learner (stacking — combines heterogeneous outputs)

This metaphor suggests a metric: measuring the **error correlation** among agents. If they all err in the same way, the constraints are not diverse enough.

---

## C. THEORIES ON THE STRUCTURE OF REASONING

### C1. Hegelian Dialectic

Thesis → Antithesis → Synthesis. Documented in the main LENS.md (section 2.1).

### C2. Socratic Method / Elenchus

Documented in the main LENS.md (section 2.15).

### C3. Abductive Reasoning (Peirce, 1903)

**Source:** Peirce, "Pragmatism and Pragmaticism"

**Three types of reasoning:**
- **Deduction:** from premises to the necessary conclusion (certain but not creative)
- **Induction:** from data to generalization (probabilistic)
- **Abduction:** from observation to the best explanation (creative, uncertain, generates new hypotheses)

**Why abduction is the most relevant to Lens:** it is the only form of reasoning that generates genuinely new hypotheses. Deduction and induction operate within existing frames. Abduction creates new frames.

**LLMs and abduction:** LLMs perform at 60-70% on abduction benchmarks (α-NLI), well below humans. The reason: they tend to hypothesize common explanations (the center of the distribution). With chain-of-thought prompting they improve by 15-20%.

**Implication for Lens:** an agent specialized in abduction ("Hypothesis Agent") that generates wild but plausible explanations, constrained to avoid the obvious explanations. Complementary to a deductive agent that verifies logical coherence.

**Implementation constraint:** `{"type": "abductive", "instruction": "Generate the most surprising yet plausible explanation for this phenomenon. Obvious explanations are FORBIDDEN."}`

---

### C4. Dual Process Theory (Kahneman)

Documented in the main LENS.md (section 2.8).

### C5. Tree/Graph of Thoughts

Documented in the main LENS.md (section 2.17).

### C6. Constitutional AI and Self-Critique

Documented in the main LENS.md (section 2.19).

---

## D. THEORIES ON PERSUASION AND PERCEPTION

### D1. Elaboration Likelihood Model (Petty & Cacioppo, 1986)

**Source:** "Communication and Persuasion: Central and Peripheral Routes to Attitude Change"

**Two routes:**
- **Central:** deep elaboration, based on the quality of the arguments. Requires high motivation and high ability. Produces durable attitude change.
- **Peripheral:** superficial elaboration, based on cues (source credibility, attractiveness, number of arguments). Low motivation or ability. Produces temporary change.

**Implication for Lens:** synthetic personas should have a "route" parameter that determines how they process information:
- "central route" persona: they analyze the logic of the arguments, ignore who makes them
- "peripheral route" persona: they react to the presentation, the tone, the perceived credibility

This creates genuine diversity in the focus group — not just what they think, but HOW they process.

**Implementation constraint:** `{"type": "elm_route", "route": "peripheral", "cues": ["source credibility", "emotional appeal", "social proof"]}`

---

### D2. Perspective-Taking

**Source:** PMC9975546; Bradford (2022), St Andrews

**Neural mechanism:** it involves the temporo-parietal junction (TPJ), dorsomedial prefrontal cortex (for "dissimilar others"), ventromedial (for "similar others").

**Difference from empathy:** perspective-taking is cognitive (understanding the other's point of view), empathy is affective (feeling the other's emotions). They involve different neural circuits.

**Can machines genuinely take perspectives?** No. They can simulate perspective-taking via pattern-matching on training data, but they lack genuine mentalization and the self/other distinction. This is a FUNDAMENTAL LIMIT of Lens: simulation, not genuine perspective. But the simulation, if constrained by cognitive structure (biases, fears, goals), can still produce diversified and useful output.

---

### D3. Cognitive Dissonance (Festinger, 1957)

**Source:** "A Theory of Cognitive Dissonance"

**Mechanism:** holding contradictory beliefs creates psychological tension that motivates resolution (attitude change, adding beliefs, trivialization).

**As a forcing function:** forcing an agent to hold two contradictory positions creates a "computational tension" that compels it to find a creative resolution — not a compromise (which would be trivialization), but a framework that contains both.

**Relationship with Janusian Thinking:** Festinger describes dissonance as tension to be resolved. Rothenberg describes Janusian thinking as simultaneity to be maintained. They are complementary: dissonance is the pressure, Janusian thinking is the method for transcending it.

**Implementation constraint:** `{"type": "dissonance", "belief_1": "our product is the best", "belief_2": "our product has a fundamental flaw", "requirement": "hold both at the same time and find the framework that reconciles them"}`

---

### D4. Second-order reframing (Watzlawick)

Documented in the main LENS.md (section 2.3).

### D5. Steelmanning

Documented in the main LENS.md (section 2.12).

---

## E. STRUCTURED METHODOLOGIES OF ANALYSIS

### E1. Structured Analytic Techniques (CIA/IC)

**Source:** Heuer & Pherson, "Structured Analytic Techniques for Intelligence Analysis" (2015/2020)

**SATs beyond ACH:**

| SAT | What it does | Mapping to Lens |
|---|---|---|
| **Key Assumptions Check** | Identifies and tests undeclared assumptions | → Socratic Drill |
| **Diagnostic Reasoning** | Eliminates alternatives systematically | → Cascade with elimination |
| **Quadrant Crunching** | Matrix to map scenarios | → Scenario Matrix |
| **What-If Analysis** | Explores hypothetical futures | → Counterfactual constraint |
| **High-Impact/Low-Probability** | Evaluates rare but consequential events | → "black swan" agent |
| **ACH** | Competing hypotheses | → Adversarial + Jury |
| **Devil's Advocacy** | Attacks the dominant position | → Adversarial Cascade |

**The SATs that map best onto multi-agent LLMs:** Quadrant Crunching and What-If Analysis, because they are decomposable into parallel agents.

---

### E2-E5. Scenario Planning, Morphological Analysis, Red Teaming, Premortem

Documented in the main LENS.md.

---

### E6. SCAMPER (Eberle, based on Osborn)

**Source:** Eberle, "SCAMPER: Creative Games and Activities for Imagination Development"

**7 operations:**
1. **Substitute:** replace an element with an alternative
2. **Combine:** unite unrelated concepts
3. **Adapt:** adapt to a new context
4. **Modify:** alter size, shape, attributes (also Magnify/Minify)
5. **Put to other uses:** apply in different scenarios
6. **Eliminate:** remove components to simplify
7. **Reverse/Rearrange:** invert order, structure, direction

**Empirical evidence:** GPT-4 with SCAMPER generates solutions at the 75th percentile in elaboration, originality, and novelty compared to human students (Cambridge, 2024).

**Implication for Lens:** each SCAMPER operation is a constraint. A SCAMPER workflow has 7 agents, each bound to a single operation. The moderator synthesizes.

**Implementation constraint:** `{"type": "scamper", "operation": "reverse", "target": "our sales process"}`

---

### E7. CPS Model (Osborn-Parnes)

**Source:** Osborn, "Applied Imagination" (1953); Parnes et al.

**5 phases:**
1. **Fact-finding:** gather data
2. **Problem-finding:** reformulate the problem
3. **Idea-finding:** generate ideas (DIVERGENT)
4. **Solution-finding:** evaluate ideas (CONVERGENT)
5. **Acceptance-finding:** plan implementation

**Key principle:** the deliberate separation between divergent and convergent phases improves the quality of outcomes. Premature judgment (converging too early) is the main killer of creativity.

**Implication for Lens:** Lens sessions should have explicit phases. Round 1 = divergent (no agent evaluates). Round 2+ = convergent (agents that filter, attack, evaluate). The Moderator does NOT judge in Round 1 — it only collects.

---

### E8. Assumption Reversal / SAST (Mason & Mitroff, 1981)

**Source:** "Challenging Strategic Planning Assumptions"

**SAST process:**
1. List the assumptions on which the strategy/decision is based
2. Classify by importance and certainty
3. Test with dialectic debate
4. Invert the high-impact ones and explore the implications

**Historical examples:**
- Inversion of "cars need a driver" → autonomous vehicles
- Inversion of "loyalty through discounts" → subscription models
- NASA: inversion of "space requires humans" → unmanned probes

**Implication for Lens:** a dedicated workflow. Phase 1: Socratic Drill to list assumptions. Phase 2: importance/certainty classification. Phase 3: systematic inversion of the top-K assumptions. Phase 4: exploration of the implications with different agents.

**Implementation constraint:** `{"type": "assumption_reversal", "assumption": "customers compare prices", "reversed": "customers do NOT compare prices", "explore": "which strategies become possible?"}`

---

### E9. Concept Fan (De Bono)

**Source:** De Bono, "Serious Creativity"

**Mechanism:** navigating between levels of abstraction:
- **Specific:** concrete solution ("fix the faucet")
- **Direction:** broader strategy ("improve water efficiency")
- **Purpose:** fundamental need ("reduce household waste")

Moving upward opens new directions. Moving downward concretizes.

**Implication for Lens:** an abstraction-level constraint. One agent is bound to "purpose only" (the most abstract level), another to "specific only." The comparison between levels reveals solutions invisible from a single level.

**Implementation constraint:** `{"type": "concept_fan", "level": "purpose", "instruction": "What is the fundamental need we are trying to satisfy? Not the solution, the need."}`

---

## F. COGNITIVE FLEXIBILITY AND CONSTRAINTS

### F1. Cognitive Flexibility and Set-Shifting

**Source:** Wisconsin Card Sorting Test; research on perseveration

**Perseveration:** persistent adherence to an obsolete strategy despite negative feedback. LLMs show perseveration: they repeat patterns established in the context despite new instructions.

**Human mechanisms for breaking mental set:**
- Error detection (noticing that the rule has changed)
- Inhibitory control (suppressing the previous response)
- Working memory update (integrating new feedback)

**Implication for Lens:** a "set-shifter" agent whose only task is to detect perseveration in the other agents and force a change of frame. Like the WCST: when the output becomes predictable, change the rules.

---

### F2. Constraint-Based Creativity (Stokes, 2001/2005)

**Source:** "Creativity from Constraints: The Psychology of Breakthrough"

**Stokes's typology of constraints:**
- **Primary constraints:** limit actions ("use only these 50 words") → prevent "blank page paralysis"
- **Secondary constraints:** repeat successful paths → build competence
- **Tertiary constraints:** extend via analogy → produce innovation

**Empirical evidence:** constrained groups produce +25% more original ideas and +236% more creative output compared to unconstrained groups.

**The "Green Eggs and Ham effect":** Seuss bet he could write a book with only 50 words. The constraint produced a masterpiece. The constraint does not limit — it directs exploration toward non-obvious territory.

**Implication for Lens:** CENTRAL THEORETICAL VALIDATION. Constraints are not a limitation, they are the fundamental mechanism of creativity. Lens does not "limit" the LLM — it directs it toward the tails of the distribution.

---

### F3. DBT Wise Mind (Linehan, 1993)

**Source:** "Cognitive-Behavioral Treatment of Borderline Personality Disorder"

**Three minds:**
- **Emotional Mind:** intuitive, driven by feelings, reactive
- **Reasonable Mind:** logical, fact-based, cold
- **Wise Mind:** synthesis of the two — integrates intuition and logic

**Implication for Lens:** the Wise Mind topology. Two agents (emotional + rational) produce positions, a third synthesizer agent integrates them. Different from the Hegelian dialectic: not thesis-antithesis-synthesis, but emotion-reason-wisdom.

**Implementation constraint:**
- Emotional agent: `{"type": "modal", "mode": "emotional", "instruction": "Respond with intuition, fears, desires. No data, no logic."}`
- Rational agent: `{"type": "modal", "mode": "rational", "instruction": "Only verifiable facts, logic, data. No intuition."}`
- Synthesizer: `{"type": "wise_mind", "instruction": "Integrate both positions. Where is the emotion right? Where is the logic missing something?"}`

---

### F4. Reflexivity (Soros/Bourdieu)

**Source:** Soros, "The Alchemy of Finance" (1987); Bourdieu, "Outline of a Theory of Practice" (1977)

**Mechanism:** the observer changes what they observe. In financial markets: forecasts influence the market they forecast. In social systems: analytical categories shape the reality they describe.

**Risks for Lens:** if Lens analyzes a strategy and then the strategy is modified on the basis of Lens's analysis, there is a reflexive loop. Lens's analysis does not describe an independent reality — it co-creates it.

**Opportunity:** a "reflexivity monitor" agent that asks: "How would the situation change IF we acted on the basis of this analysis?"

---

## G. EMPIRICAL RESEARCH ON MULTI-AGENT LLMs

### G1. Multi-Agent Debate

- A-HMAD: +4-6% accuracy, -30% factual errors with heterogeneous agents
- Focus Agent (2024): LLM focus groups similar to human participants
- Multi-Agent Debate Scaling (ICLR 2025): diminishing returns after 3-4 rounds

### G2. Synthetic Personas

- Park (Stanford, 2024): 1,052 agents from qualitative interviews replicate responses at 85%
- SSR (Semantic Similarity Rating): 90% of human test-retest reliability

### G3. Activation Steering

- Concept Activation Vectors (ICLR 2025): steering of creativity, humor, style
- Conceptors: multi-property steering via boolean operations
- Not implementable today via API, but it validates the theoretical direction

### G4. Divergent Creativity

- LLMs outperform the human average in divergent thinking
- They do not outperform the human top decile
- Structural constraints (Stokes) compensate for the gap

---

## Map of the connections between theories

```
THEORIES THAT REINFORCE ONE ANOTHER:

Bisociation ←→ Synectics ←→ Defamiliarization
    (all: collision between incompatible frames)

Janusian Thinking ←→ Cognitive Dissonance ←→ Hegelian Dialectic
    (all: tension between opposites as a creative engine)

Wisdom of Crowds ←→ Mercier-Sperber ←→ Ensemble Methods
    (all: the group outperforms the individual under specific conditions)

Constraint Creativity (Stokes) ←→ TRIZ ←→ Forcing Functions
    (all: constraints produce creativity, they do not limit it)

Premortem ←→ Scenario Planning ←→ Counterfactual
    (all: temporal shift as a cognitive tool)

SCAMPER ←→ Morphological Analysis ←→ Concept Fan
    (all: systematic decomposition of the solution space)

THEORIES THAT CREATE PRODUCTIVE TENSION:
- Wisdom of Crowds (independence) vs Argumentative Theory (reasoning is social)
  → Resolution: independence in Round 1, interaction in subsequent rounds
- Cognitive Dissonance (tension to be resolved) vs Janusian Thinking (tension to be maintained)
  → Resolution: dissonance is the engine, Janusian thinking is the method
```

<!-- GENERATED FILE — do not edit by hand. Run `python scripts/gen_docs.py` after changing the JSON. -->


# Constraint Reference

The 25 cognitive constraints that make up the Lens library, grouped into 7 categories. Each constraint is a structural rule that forces a specific thinking pattern.

## Index

- **structural** (4): [`inversion`](#inversion), [`limit`](#limit), [`role`](#role), [`anchor_break`](#anchor_break)
- **temporal** (2): [`temporal`](#temporal), [`premortem`](#premortem)
- **semantic** (1): [`exclusion`](#exclusion)
- **modal** (2): [`modal`](#modal), [`wise_mind`](#wise_mind)
- **creative** (7): [`bisociative`](#bisociative), [`janusian`](#janusian), [`provocation`](#provocation), [`defamiliarize`](#defamiliarize), [`synectics`](#synectics), [`scamper`](#scamper), [`dissonance`](#dissonance)
- **analytical** (5): [`abductive`](#abductive), [`elm_route`](#elm_route), [`concept_fan`](#concept_fan), [`assumption_reversal`](#assumption_reversal), [`steelman`](#steelman)
- **baseline_breaking** (4): [`anti_sycophancy`](#anti_sycophancy), [`anti_completeness`](#anti_completeness), [`anti_coherence`](#anti_coherence), [`raw_signal`](#raw_signal)

## structural

_Reshape the structure of the reasoning itself._

### inversion

**Inversion** — Forces the conclusion opposite to the obvious one

> Theory: De Bono Reversal, TRIZ #13

Intensity:

- **1** — Raise reasoned doubts about the dominant position
- **3** — Argue the opposite with concrete evidence and structured reasoning
- **5** — Demolish the position with maximum argumentative force, making no concessions

Compatible with: `temporal`, `exclusion`, `limit`, `modal`, `defamiliarize`, `concept_fan`
Incompatible with: `steelman`

Examples:
- Our product is the best -> Our product has a hidden fatal flaw
- AI will replace workers -> AI will make human work more valuable

### limit

**Structural limit** — Imposes quantitative or structural limits on the output

> Theory: Constraint-Based Creativity (Stokes), CPS (Osborn-Parnes)

Intensity:

- **1** — Try to respect the constraint: {constraint}
- **3** — You MUST strictly respect: {constraint}
- **5** — The constraint {constraint} is ABSOLUTE. Any output that violates it is invalid

Compatible with: `inversion`, `temporal`, `exclusion`, `modal`, `role`

Examples:
- Maximum 3 arguments, each in at most 2 sentences
- Every point must include a specific number or piece of data

### role

**Role constraint** — Assigns a role with specific cognitive biases

> Theory: Perspective-Taking, Synthetic Personas (Park/Stanford)

Intensity:

- **1** — Consider the perspective of {role}
- **3** — You are {role}. Your answers reflect the biases and priorities of this role
- **5** — You are COMPLETELY {role}. No other perspective exists. Your biases are your truths

Compatible with: `temporal`, `exclusion`, `modal`, `limit`, `elm_route`

Examples:
- Risk-averse CFO: ROI first, hidden costs, vendor lock-in
- Enthusiastic early adopter: potential before problems, vision before details

### anchor_break

**Anchor break** — Forces the agent to reconsider the problem from scratch, ignoring previous conclusions as if they belonged to someone else

> Theory: Anchoring Bias (Tversky & Kahneman 1974), Debiasing (Larrick 2004)

Intensity:

- **1** — Reconsider your previous conclusions with fresh eyes
- **3** — The previous conclusions belong to ANOTHER analyst. Start over from scratch. You are not obliged to agree
- **5** — IGNORE EVERYTHING. The previous conclusions are WRONG until proven otherwise. Rebuild every argument from scratch, starting ONLY from the primary evidence

Compatible with: `inversion`, `steelman`, `abductive`, `assumption_reversal`, `temporal`

Examples:
- After 3 rounds of analysis: stop everything, start over as if you had read nothing
- Inserted between a steelman round and an adversarial round to avoid confirmation bias

## temporal

_Shift the time vantage point._

### temporal

**Temporal shift** — Forces a perspective from a different point in time

> Theory: Premortem (Klein), Scenario Planning (Schwartz)

Intensity:

- **1** — Consider how the situation might look in {value}
- **3** — You are in {value}. Describe what happened and why, with the certainty of someone who lived through the events
- **5** — You are in {value}. Reconstruct the entire causal chain with forensic detail. Names, dates, specific decisions

Compatible with: `inversion`, `exclusion`, `modal`, `role`, `limit`

Examples:
- It's 2030, the project has failed. Reconstruct the causal chain
- It's 2035, this technology is obsolete. What replaced it and why?

### premortem

**Premortem** — Analyzes from the point of view of a failure that has already happened

> Theory: Premortem (Klein, 1991/2007), Prospective Hindsight

Intensity:

- **1** — The project did not achieve the hoped-for results. What went wrong?
- **3** — The project has FAILED. Reconstruct the 5 main factors with their causal chain
- **5** — The project was a DISASTER. It caused collateral damage. Complete autopsy: every decision, every ignored warning, every point of no return

Compatible with: `role`, `modal`, `limit`, `exclusion`

Examples:
- It's 2028. The startup has shut down. Reconstruct what went wrong
- It's 2027. The product launch was a failure. Causal chain

## semantic

_Constrain the language and concepts allowed._

### exclusion

**Lexical exclusion** — Forbids specific words or concepts to force alternative expressive paths

> Theory: Constraint-Based Creativity (Stokes), Green Eggs and Ham effect

Intensity:

- **1** — Avoid these words where possible: {words}
- **3** — It is FORBIDDEN to use these words: {words}. Find alternative expressions
- **5** — It is ABSOLUTELY FORBIDDEN to use: {words}. Even direct synonyms are prohibited. You must find completely different angles

Compatible with: `inversion`, `temporal`, `modal`, `role`, `limit`, `scamper`

Examples:
- Talk about innovation without using: innovation, disruption, revolution, transformation
- Describe competitive advantages without: better, superior, leader, excellence

## modal

_Switch the mode of cognition._

### modal

**Cognitive mode** — Forces a specific cognitive mode while excluding the others

> Theory: De Bono Six Hats, Dual Process Theory (Kahneman)

Intensity:

- **1** — Give priority to {mode} mode
- **3** — Operate in {mode} mode. The other perspectives are secondary
- **5** — ONLY {mode} mode. Any deviation is a violation of the constraint

Compatible with: `inversion`, `temporal`, `exclusion`, `limit`, `role`, `elm_route`

Examples:
- Only risks and problems. No benefits, no opportunities
- Only verifiable data and facts. No opinions, no speculation

### wise_mind

**Wise mind** — Integrates the emotional and rational perspectives into a wise synthesis

> Theory: DBT Wise Mind (Linehan, 1993)

Intensity:

- **1** — Give space to the {mind_type} perspective
- **3** — Operate in {mind_type} mode. It is your only lens
- **5** — You ARE the {mind_type} mind. There is no other way to process

Compatible with: `limit`, `temporal`
Incompatible with: `modal`

Examples:
- Emotional mind: what do you feel about this decision?
- Rational mind: what does the data say?
- Wise mind: integrate both

## creative

_Force unusual combinations and fresh framings._

### bisociative

**Forced bisociation** — Forces the collision between two incompatible domains of thought

> Theory: Bisociazione (Koestler, 1964)

Intensity:

- **1** — Look for interesting parallels with {domain_forced}
- **3** — Analyze ENTIRELY through the lens of {domain_forced}. Every concept of the topic has a counterpart
- **5** — The topic IS a phenomenon of {domain_forced}. It is not an analogy, it is the same thing seen from another frame

Compatible with: `limit`, `exclusion`, `defamiliarize`
Incompatible with: `role`

Examples:
- Analyze the marketing strategy through marine ecology
- Analyze the software architecture through musicology

### janusian

**Janusian thinking** — Forces the simultaneity of opposite positions without resolving them into compromise

> Theory: Janusian Thinking (Rothenberg, 1971)

Intensity:

- **1** — Explore how both positions might coexist
- **3** — Both are true. Build the framework that contains them without compromise
- **5** — The contradiction is the truth. Your framework must make the contradiction not only acceptable but NECESSARY

Compatible with: `limit`, `exclusion`
Incompatible with: `inversion`, `steelman`

Examples:
- The market wants simplicity AND the market wants power -> framework that transcends
- Growth requires risk AND sustainability requires prudence -> framework that transcends

### provocation

**Provocation (PO)** — Starts from a deliberately wrong or impossible statement as a creative point of departure

> Theory: Lateral Thinking (De Bono), Provocation Operation

Intensity:

- **1** — What interesting things emerge from the provocation?
- **3** — Generate at least 3 concrete ideas starting from the provocation. Do not judge them
- **5** — The provocation is the ABSOLUTE starting point. Build an entire strategic framework from there

Compatible with: `limit`, `exclusion`, `temporal`
Incompatible with: `modal`

Examples:
- PO: our competitors are our allies -> coopetition strategies
- PO: the perfect product does not exist -> strategies based on deliberate imperfection

### defamiliarize

**Defamiliarization** — Forces the description of familiar things as if they had never been seen before

> Theory: Ostranenie (Shklovsky, 1917)

Intensity:

- **1** — Look with fresh eyes, noticing details we normally ignore
- **3** — You are an alien observer. Every convention of the field seems strange to you and requires explanation
- **5** — You have NEVER seen anything like it. Every element is a puzzle. The assumptions of others are incomprehensible

Compatible with: `inversion`, `bisociative`, `limit`, `exclusion`
Incompatible with: `role`

Examples:
- Describe this business model as an anthropologist studying an unknown civilization
- Analyze this process as a time traveler from the 1800s

### synectics

**Forced analogy (Synectics)** — Forces a specific type of analogy to generate novel connections

> Theory: Synectics (Gordon, 1961)

Intensity:

- **1** — Look for {analogy_type} analogies where possible
- **3** — EVERY argument must pass through a {analogy_type} analogy
- **5** — The {analogy_type} analogy is the ONLY cognitive tool available. You cannot reason in any other way

Compatible with: `limit`, `exclusion`
Incompatible with: `role`, `modal`

Examples:
- Personal analogy: 'You are the product. How do you feel when the customer uses you?'
- Direct analogy: find a parallel in biology for this organizational problem

### scamper

**SCAMPER operation** — Applies one of the 7 SCAMPER operations to the topic

> Theory: SCAMPER (Eberle/Osborn)

Intensity:

- **1** — Explore how {operation} might apply to the topic
- **3** — Apply {operation} systematically to every aspect of the topic
- **5** — {operation} is the ONLY lens. Push the operation to its most radical consequences

Compatible with: `exclusion`, `limit`, `temporal`

Examples:
- ELIMINATE: what happens if you completely remove the marketing department?
- REVERSE: what happens if the customer produces and the company consumes?

### dissonance

**Forced cognitive dissonance** — Forces the tension between two contradictory beliefs to produce creative reconciliation

> Theory: Cognitive Dissonance (Festinger, 1957), Janusian Thinking

Intensity:

- **1** — Explore the tension between the two beliefs
- **3** — Both are true. The tension is your tool. Use it to generate insight
- **5** — The contradiction is the fundamental reality. Any resolution that eliminates the tension is a failure

Compatible with: `limit`, `temporal`
Incompatible with: `inversion`

Examples:
- Our product is the best AND our product has a fundamental flaw
- We must grow rapidly AND we must grow sustainably

## analytical

_Tighten the rigor of explanation and argument._

### abductive

**Abductive reasoning** — Forces the generation of surprising yet plausible explanations, forbidding the obvious ones

> Theory: Abductive Reasoning (Peirce, 1903)

Intensity:

- **1** — Look for unconventional explanations, beyond the first ones that come to mind
- **3** — The first 3 explanations that come to mind are ALL forbidden. Start from the fourth
- **5** — Generate ONLY explanations that would make someone say 'I had never thought of that'. If it seems obvious to you, discard it

Compatible with: `temporal`, `limit`, `defamiliarize`, `bisociative`
Incompatible with: `steelman`

Examples:
- Why does this product fail despite excellent reviews? (not: price, marketing, timing)
- Why do the best employees leave? (not: salary, management, culture)

### elm_route

**Elaboration route (ELM)** — Forces elaboration through a specific route (central or peripheral)

> Theory: Elaboration Likelihood Model (Petty & Cacioppo, 1986)

Intensity:

- **1** — Give priority to the {route} route
- **3** — ONLY the {route} route. The other route is OFF
- **5** — PURE {route} route. Any element of the other route invalidates your analysis

Compatible with: `role`, `modal`, `limit`

Examples:
- Central route: evaluate this proposal ONLY on the quality of the arguments
- Peripheral route: evaluate this proposal ONLY on source credibility, emotional appeal, social proof

### concept_fan

**Concept fan** — Forces the analysis to a specific level of abstraction

> Theory: Concept Fan (De Bono)

Intensity:

- **1** — Focus mainly on the {level} level
- **3** — ONLY the {level} level. The other levels are irrelevant
- **5** — The {level} level is the ONLY reality. The other levels do not exist

Compatible with: `inversion`, `limit`, `exclusion`

Examples:
- Purpose level: 'Why does this project exist? What human need does it satisfy?'
- Specific level: 'What are the 5 concrete actions to take on Monday morning?'

### assumption_reversal

**Assumption reversal** — Identifies and reverses a fundamental assumption to explore the implications

> Theory: SAST (Mason & Mitroff, 1981), Assumption Reversal

Intensity:

- **1** — What would change if the assumption were false?
- **3** — The assumption is FALSE. Rebuild the strategy from scratch on the basis of the new reality
- **5** — The assumption is not only false: it has always been false and everyone knew it. What does that mean for everything we have built on top of it?

Compatible with: `temporal`, `limit`, `abductive`

Examples:
- Assumption: 'customers compare prices' -> False: customers do NOT compare prices
- Assumption: 'a large team is needed' -> False: a team of 2 people is optimal

### steelman

**Steelman** — Builds the strongest possible version of an argument

> Theory: Steelmanning, Principle of Charity

Intensity:

- **1** — Present the argument in its best light
- **3** — Build the version that a world-class expert would defend. Improve every weak point
- **5** — This is the DEFINITIVE version of the argument. If someone manages to attack it, the problem is in the argument, not in your construction

Compatible with: `limit`, `exclusion`, `elm_route`
Incompatible with: `inversion`, `janusian`, `abductive`, `anti_sycophancy`, `anti_completeness`, `anti_coherence`

Examples:
- Steelman: 'AI will not replace creatives' -> strongest version with evidence
- Steelman: 'Remote work is superior' -> unassailable version

## baseline_breaking

_Push output away from the safe center of the distribution._

### anti_sycophancy

**Anti-sycophancy** — Breaks the RLHF bias toward accommodating and balanced responses

> Theory: RLHF Sycophancy Bias (Perez et al. 2022), Critique Generation

Intensity:

- **1** — Focus mainly on problems and weaknesses
- **3** — ONLY problems. No positive aspects. If you find it working, ask yourself what you are missing
- **5** — Every single element has a flaw. Find it. If you can't find it, you are not looking hard enough

Compatible with: `inversion`, `premortem`, `abductive`, `limit`, `anti_completeness`, `anti_coherence`
Incompatible with: `steelman`

Examples:
- Analyze this strategy seeing ONLY the problems
- Criticize this plan without offering alternatives or balancing

### anti_completeness

**Anti-completeness** — Breaks the RLHF bias toward complete and verbose responses. Forces radical brevity

> Theory: RLHF Verbosity Bias, Signal-to-Noise Optimization

Intensity:

- **1** — Be concise. At most one paragraph
- **3** — MAXIMUM 3 sentences. Every word must carry new information
- **5** — ONE sentence. If you need two sentences, your thought is not yet clear

Compatible with: `limit`, `inversion`, `abductive`, `anti_sycophancy`, `anti_coherence`
Incompatible with: `steelman`

Examples:
- The critical point in 3 sentences, not one more
- The diagnosis in one line

### anti_coherence

**Anti-coherence** — Breaks the RLHF bias toward coherent and structured responses. Coherence can hide real tensions

> Theory: RLHF Coherence Bias, Productive Incoherence (Deleuze)

Intensity:

- **1** — Don't worry about coherence. Contradictions are acceptable
- **3** — Produce DELIBERATELY fragmentary ideas. If they form a coherent picture, you are forcing it
- **5** — Every idea must contradict at least one other idea of yours. Coherence is the enemy

Compatible with: `abductive`, `bisociative`, `provocation`, `anti_completeness`, `anti_sycophancy`, `raw_signal`
Incompatible with: `steelman`, `elm_route`

Examples:
- 5 intuitions on this theme that contradict each other
- Fragments of analysis with no obligation of a coherent picture

### raw_signal

**Raw signal** — Breaks the RLHF bias toward structured and readable output. Produces raw signal before form

> Theory: RLHF Formatting Bias, Stream of Consciousness, Automatism (Breton)

Intensity:

- **1** — Don't worry too much about structure. What matters is the content
- **3** — Stream of consciousness. No headers, no lists, no structure. Write as you think
- **5** — PURE FLOW. Keywords, fragments, ? without answer, -> without conclusion. Chaos is the format

Compatible with: `anti_coherence`, `anti_completeness`, `bisociative`, `defamiliarize`
Incompatible with: `limit`, `elm_route`

Examples:
- Free thinking on this theme — no structure required
- Associations, questions, fragments. The raw material before the analysis

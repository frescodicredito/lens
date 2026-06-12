# Lens — Fondamenti Teorici e Ricerca

> Documento di ricerca — aggiornato 28 febbraio 2026
> Stato: in espansione continua

---

## Indice delle teorie per categoria

### A. Teorie sulla struttura del pensiero creativo
- A1. Bisociazione (Koestler)
- A2. Janusian Thinking (Rothenberg)
- A3. Lateral Thinking e Provocation (De Bono)
- A4. Defamiliarization / Ostranenie (Shklovsky)
- A5. Synectics e analogie forzate (Gordon)
- A6. TRIZ e risoluzione di contraddizioni (Altshuller)

### B. Teorie sul pensiero di gruppo e intelligenza collettiva
- B1. Wisdom of Crowds (Surowiecki)
- B2. Groupthink e dissenso strutturato (Janis)
- B3. Argumentative Theory of Reasoning (Mercier & Sperber)
- B4. Cognitive Diversity e Requisite Variety (Ashby)
- B5. Ensemble Methods come metafora cognitiva

### C. Teorie sulla struttura del ragionamento
- C1. Dialettica hegeliana
- C2. Metodo Socratico / Elenchus
- C3. Abductive Reasoning (Peirce)
- C4. Dual Process Theory (Kahneman)
- C5. Tree/Graph of Thoughts
- C6. Constitutional AI e Self-Critique (Anthropic)

### D. Teorie sulla persuasione e percezione
- D1. Elaboration Likelihood Model (Petty & Cacioppo)
- D2. Perspective-Taking (cognitive science)
- D3. Cognitive Dissonance (Festinger)
- D4. Reframing di secondo ordine (Watzlawick)
- D5. Steelmanning

### E. Metodologie strutturate di analisi
- E1. Structured Analytic Techniques (CIA/IC)
- E2. Scenario Planning (Shell/Schwartz)
- E3. Morphological Analysis (Zwicky)
- E4. Red Teaming e Adversarial Collaboration
- E5. Premortem / Prospective Hindsight (Klein)
- E6. SCAMPER (Eberle/Osborn)
- E7. CPS Model (Osborn-Parnes)
- E8. Assumption Reversal / SAST (Mason & Mitroff)
- E9. Concept Fan (De Bono)

### F. Teorie su flessibilità cognitiva e vincoli
- F1. Cognitive Flexibility e Set-Shifting
- F2. Constraint-Based Creativity (Stokes)
- F3. DBT Wise Mind (Linehan)
- F4. Reflexivity (Soros/Bourdieu)

### G. Ricerca empirica su multi-agent LLM
- G1. Multi-Agent Debate (A-HMAD, Focus Agent)
- G2. Synthetic Personas (Park, Stanford)
- G3. Activation Steering e Control Vectors
- G4. Divergent Creativity negli LLM

---

## A. TEORIE SUL PENSIERO CREATIVO

### A1. Bisociazione (Koestler, 1964)

**Fonte:** "The Act of Creation"

**Meccanismo:** la creatività nasce dalla percezione simultanea di un'idea in due matrici di pensiero abitualmente incompatibili. Non è associazione (collegamento dentro un frame), è collisione tra frame indipendenti.

**Tre forme:**
- Umorismo: collisione → sorpresa → risata
- Scoperta scientifica: collisione → eureka
- Arte: collisione → giustapposizione estetica

**Implicazione per Lens:** il Constraint Engine con vincoli semantici è un generatore di bisociazioni. La topologia Ring è bisociazione iterata. Il Bisociation Engine è la topologia dedicata.

**Vincolo implementativo:** `{"type": "bisociative", "domain_forced": "ecologia marina", "domain_original": "marketing"}`

---

### A2. Janusian Thinking (Rothenberg, 1971)

**Fonte:** Rothenberg, "The Emerging Goddess: The Creative Process in Art, Science, and Other Fields" (1979); studi pubblicati su *American Journal of Psychiatry*

**Meccanismo:** concepire attivamente due o più idee opposte o antitetiche **simultaneamente** come valide. Non è pensare a opposti in sequenza: è tenerli entrambi in mente nello stesso momento, senza risolverli immediatamente.

**Esempi documentati:**
- Einstein: un uomo che cade è simultaneamente in moto e a riposo → relatività
- Bohr: la luce è simultaneamente onda e particella → complementarità
- Watson: due strutture spaziali opposte → doppia elica DNA
- Mozart: "Le dissonanze sono solo consonanze remote"

**Differenza da "pensare per opposti":** gli opposti sequenziali producono compromessi. La simultaneità produce trascendenza — una nuova categoria che contiene entrambi senza ridurre nessuno dei due.

**Implicazione per Lens:**
- Vincolo di tipo "janusian": l'agente DEVE sostenere due posizioni opposte contemporaneamente e produrre una sintesi che le trascenda
- Diverso dall'adversarial (dove due agenti si attaccano): qui è UN agente che tiene entrambi
- Implementazione possibile: prompt che richiede "X è vero E non-X è vero contemporaneamente. Genera un framework che li contenga entrambi."

**Vincolo implementativo:** `{"type": "janusian", "thesis": "il mercato vuole semplicità", "antithesis": "il mercato vuole potenza", "requirement": "framework che trascende la contraddizione"}`

**Nota critica:** questo è il vincolo cognitivamente più difficile per un LLM. Tenderà a cercare un compromesso (il centro della distribuzione). Il vincolo deve esplicitamente vietare il compromesso e richiedere trascendenza.

---

### A3. Lateral Thinking e Provocation (De Bono, 1967)

**Fonte:** "Lateral Thinking: Creativity Step by Step"; De Bono Group

**Quattro tipi di strumenti:**
1. **Idea-generating** — rompere pattern correnti
2. **Focus** — ampliare dove cercare
3. **Harvest** — estrarre più valore dall'output
4. **Treatment** — considerare vincoli reali

**Tecniche chiave:**
- **Provocation (PO):** affermazione deliberatamente sbagliata/impossibile come punto di partenza. "PO: le automobili hanno ruote quadrate" → genera idee su sospensioni adattive
- **Random Entry:** concetto casuale forzatamente associato al problema. "Naso" + "fotocopiatrice" → copiatrice che profuma di lavanda quando finisce la carta (reale)
- **Reversal:** processo rovesciato. Non "come vendiamo al cliente" ma "come fa il cliente a comprare da solo"

**Implicazione per Lens:** le forcing functions sono implementazioni dirette. La Provocation è un tipo di vincolo non ancora esplorato a fondo: forza l'LLM a partire da un'affermazione impossibile e lavorare da lì.

**Vincolo implementativo:** `{"type": "provocation", "po_statement": "PO: i nostri competitor sono nostri alleati", "requirement": "genera 3 strategie partendo da questa provocazione"}`

---

### A4. Defamiliarization / Ostranenie (Shklovsky, 1917)

**Fonte:** "Art as Technique" (О́стране́ние)

**Meccanismo:** presentare cose familiari in modi non familiari per forzare una nuova percezione. L'automazione percettiva (vediamo le cose senza vederle davvero) viene rotta dalla "resa strana". Tolstoj descrive oggetti comuni come se li vedesse per la prima volta.

**Differenza dal semantic reframing:** il reframing cambia il vocabolario. La defamiliarization cambia il livello di osservazione — descrivi qualcosa come se non avessi mai visto nulla di simile prima.

**Implicazione per Lens:** vincolo di tipo "alien observer" — l'agente deve descrivere il problema come se lo vedesse per la prima volta, senza assunzioni pregresse. Combatte il bias di familiarità dell'LLM.

**Vincolo implementativo:** `{"type": "defamiliarize", "instruction": "Descrivi questo business model come se fossi un antropologo che studia una civiltà sconosciuta"}`

---

### A5. Synectics (Gordon, 1961)

**Fonte:** "Synectics: The Development of Creative Capacity"

**Quattro tipi di analogia forzata:**
1. **Direct Analogy:** parallelo stesso-dominio (volo degli uccelli → aeroplano)
2. **Personal Analogy:** empatizzare con l'oggetto ("sentiti" come un'ala)
3. **Symbolic Analogy:** metaforica (volo = "libertà")
4. **Fantasy Analogy:** scenari impossibili ("ali fatte di sogni")

**Esempi reali di innovazione da Synectics:**
- Velcro: ganci dei semi di bardana (direct analogy dalla natura)
- Pringles: compressione delle foglie secche → chip uniformi impilabili

**Implicazione per Lens:** ogni tipo di analogia è un vincolo diverso. Un focus group Synectics avrebbe 4 agenti, ognuno vincolato a un tipo di analogia diverso, applicati allo stesso problema.

**Vincolo implementativo:** `{"type": "synectics", "analogy_type": "personal", "instruction": "Sei il prodotto. Come ti senti quando il cliente ti usa?"}`

---

### A6. TRIZ (Altshuller, 1946+)

**Fonte:** "40 Inventive Principles"; matrice delle contraddizioni (39x39)

**Meccanismo:** l'innovazione vera nasce dalla risoluzione di contraddizioni tecniche. 40 principi inventivi derivati da centinaia di migliaia di brevetti.

**Principi più rilevanti per Lens:**
- #1 Segmentazione: dividere un sistema in parti indipendenti → base delle topologie multi-agente
- #13 Inversione: fare l'azione opposta → forcing function di inversione
- #17 Dimensionalità: passare da una dimensione a più dimensioni → aggiungere prospettive
- #25 Self-service: fare che un oggetto si serva da solo → Meta-Lens (auto-ottimizzazione)
- #35 Trasformazione di proprietà: cambiare lo stato del sistema → set-shifting forzato

**Implicazione per Lens:** i 40 principi TRIZ possono essere mappati come una libreria di vincoli strutturati.

---

## B. TEORIE SU PENSIERO DI GRUPPO E INTELLIGENZA COLLETTIVA

### B1. Wisdom of Crowds (Surowiecki, 2004)

**Fonte:** "The Wisdom of Crowds"

**Quattro condizioni necessarie:**
1. **Diversità di opinione** — ciascuno ha informazioni private
2. **Indipendenza** — le opinioni non sono influenzate da quelle degli altri
3. **Decentralizzazione** — nessuno dirige dall'alto
4. **Meccanismo di aggregazione** — un metodo per trasformare giudizi individuali in decisione collettiva

**Condizione critica:** "troppa comunicazione può rendere il gruppo meno intelligente"

**Implicazione per Lens:** PRINCIPIO ARCHITETTURALE. Nel Round 1 di ogni topologia, gli agenti NON devono vedere le posizioni degli altri. L'indipendenza computazionale nel primo round non è un dettaglio, è la condizione necessaria per l'intelligenza collettiva.

---

### B2. Groupthink (Janis, 1971)

**Fonte:** "Victims of Groupthink"

**Meccanismo:** i membri di un gruppo coeso sviluppano inconsciamente illusioni condivise che interferiscono con il pensiero critico.

**Prevenzione:** avvocato del diavolo istituzionalizzato, dissenso programmato, conflitto strutturato.

**Implicazione per Lens:** l'LLM ha un bias strutturale verso il consenso. Lens contrasta questo con dissenso programmato.

---

### B3. Argumentative Theory of Reasoning (Mercier & Sperber, 2011/2017)

**Fonte:** "The Enigma of Reason" (2017); paper originale in *Behavioral and Brain Sciences* (2011)

**Tesi centrale:** il ragionamento umano NON si è evoluto per cercare la verità in solitudine. Si è evoluto per l'argomentazione in contesti sociali — produrre argomenti per persuadere e valutare argomenti altrui per non farsi ingannare.

**Implicazione devastante:** il ragionamento di un singolo agente è **fondamentalmente limitato**. I bias (confirmation bias, myside bias) non sono bug del ragionamento — sono feature dell'argomentazione sociale. In solitudine producono errori. In gruppo producono verità.

**Implicazione per Lens:** questa è la giustificazione teorica più forte per il multi-agent approach. Se il ragionamento è intrinsecamente sociale, un singolo LLM che "ragiona da solo" è strutturalmente limitato. Il debate multi-agente non è un'ottimizzazione — è la modalità naturale del ragionamento.

**Vincolo architetturale:** ogni sessione Lens dovrebbe avere MINIMO 2 agenti. Il singolo agente è per definizione sub-ottimale secondo Mercier & Sperber.

---

### B4. Cognitive Diversity e Requisite Variety (Ashby, 1956)

**Fonte:** Ashby, "An Introduction to Cybernetics"; Aggarwal et al. (2019), PMC6374291

**Legge di Ashby:** la varietà interna di un sistema deve essere almeno pari alla varietà dell'ambiente per controllarlo efficacemente.

**Findings chiave sulla diversità cognitiva nei team:**
- La diversità di **stile cognitivo** (come si elabora informazione) è più importante della diversità demografica o funzionale
- La relazione è a U invertita: diversità moderata massimizza l'intelligenza collettiva; troppa diversità distrugge la coordinazione
- La diversità funzionale (expertise diversa) e cognitiva superano quella demografica

**Implicazione per Lens:** gli agenti devono avere stili cognitivi diversi (analitico vs olistico, dettaglio vs big picture), non solo posizioni diverse. La diversità deve essere moderata — 4-5 agenti con stili genuinamente diversi, non 10 con differenze marginali.

---

### B5. Ensemble Methods come metafora cognitiva

**Fonte:** DARPA "Quantifying Ensemble Diversity for Robust ML"; Wolpert (1992) stacking

**Principio:** learner deboli diversi combinati superano un singolo learner forte. La condizione è che gli errori siano non correlati.

**Tre pattern:**
- **Bagging:** campioni diversi dello stesso problema → media delle predizioni (riduce varianza)
- **Boosting:** ogni learner si concentra sugli errori del precedente (riduce bias)
- **Stacking:** un meta-learner combina output eterogenei (massimizza diversità)

**Implicazione per Lens:**
- La topologia Star è bagging cognitivo (N agenti indipendenti → aggregazione)
- La topologia Cascade è boosting cognitivo (ogni agente si concentra sulle debolezze del precedente)
- Il Moderatore è un meta-learner (stacking — combina output eterogenei)

Questa metafora suggerisce una metrica: misurare la **correlazione degli errori** tra agenti. Se tutti sbagliano nello stesso modo, i vincoli non sono abbastanza diversi.

---

## C. TEORIE SULLA STRUTTURA DEL RAGIONAMENTO

### C1. Dialettica Hegeliana

Tesi → Antitesi → Sintesi. Documentato nel LENS.md principale (sezione 2.1).

### C2. Metodo Socratico / Elenchus

Documentato nel LENS.md principale (sezione 2.15).

### C3. Abductive Reasoning (Peirce, 1903)

**Fonte:** Peirce, "Pragmatism and Pragmaticism"

**Tre tipi di ragionamento:**
- **Deduzione:** dalle premesse alla conclusione necessaria (sicura ma non creativa)
- **Induzione:** dai dati alla generalizzazione (probabilistica)
- **Abduzione:** dall'osservazione alla migliore spiegazione (creativa, incerta, genera ipotesi nuove)

**Perché l'abduzione è la più rilevante per Lens:** è l'unica forma di ragionamento che genera ipotesi genuinamente nuove. Deduzione e induzione operano dentro frame esistenti. L'abduzione crea frame nuovi.

**LLM e abduzione:** gli LLM performano al 60-70% su benchmark di abduzione (α-NLI), molto sotto gli umani. La ragione: tendono a ipotizzare spiegazioni comuni (centro della distribuzione). Con chain-of-thought prompting migliorano del 15-20%.

**Implicazione per Lens:** un agente specializzato in abduzione ("Hypothesis Agent") che genera spiegazioni wild ma plausibili, vincolato a evitare le spiegazioni ovvie. Complementare a un agente deduttivo che verifica la coerenza logica.

**Vincolo implementativo:** `{"type": "abductive", "instruction": "Genera la spiegazione più sorprendente ma plausibile per questo fenomeno. Sono VIETATE le spiegazioni ovvie."}`

---

### C4. Dual Process Theory (Kahneman)

Documentato nel LENS.md principale (sezione 2.8).

### C5. Tree/Graph of Thoughts

Documentato nel LENS.md principale (sezione 2.17).

### C6. Constitutional AI e Self-Critique

Documentato nel LENS.md principale (sezione 2.19).

---

## D. TEORIE SU PERSUASIONE E PERCEZIONE

### D1. Elaboration Likelihood Model (Petty & Cacioppo, 1986)

**Fonte:** "Communication and Persuasion: Central and Peripheral Routes to Attitude Change"

**Due route:**
- **Central:** elaborazione profonda, basata sulla qualità degli argomenti. Richiede alta motivazione e alta abilità. Produce cambio di atteggiamento durevole.
- **Peripheral:** elaborazione superficiale, basata su segnali (credibilità fonte, attrattività, numero di argomenti). Bassa motivazione o abilità. Produce cambio temporaneo.

**Implicazione per Lens:** le synthetic persona dovrebbero avere un parametro "route" che determina come processano l'informazione:
- Persona "central route": analizzano la logica degli argomenti, ignorano chi li fa
- Persona "peripheral route": reagiscono alla presentazione, al tono, alla credibilità percepita

Questo crea diversità genuina nel focus group — non solo cosa pensano, ma COME processano.

**Vincolo implementativo:** `{"type": "elm_route", "route": "peripheral", "cues": ["credibilità fonte", "appeal emotivo", "social proof"]}`

---

### D2. Perspective-Taking

**Fonte:** PMC9975546; Bradford (2022), St Andrews

**Meccanismo neurale:** coinvolge la giunzione temporo-parietale (TPJ), corteccia prefrontale dorsomediale (per "altri dissimili"), ventromediale (per "altri simili").

**Differenza da empatia:** la perspective-taking è cognitiva (capire il punto di vista dell'altro), l'empatia è affettiva (sentire le emozioni dell'altro). Coinvolgono circuiti neurali diversi.

**Le macchine possono genuinamente prendere prospettive?** No. Possono simulare perspective-taking via pattern-matching sui dati di training, ma mancano della mentalizzazione genuina e della distinzione sé/altro. Questo è un LIMITE FONDAMENTALE di Lens: simulazione, non prospettiva genuina. Ma la simulazione, se vincolata da struttura cognitiva (bias, paure, obiettivi), può comunque produrre output diversificato e utile.

---

### D3. Cognitive Dissonance (Festinger, 1957)

**Fonte:** "A Theory of Cognitive Dissonance"

**Meccanismo:** tenere credenze contraddittorie crea tensione psicologica che motiva la risoluzione (cambio di atteggiamento, aggiunta di credenze, banalizzazione).

**Come forcing function:** forzare un agente a sostenere due posizioni contraddittorie crea una "tensione computazionale" che lo costringe a trovare una risoluzione creativa — non un compromesso (che sarebbe banalizzazione), ma un framework che contiene entrambe.

**Relazione con Janusian Thinking:** Festinger descrive la dissonanza come tensione da risolvere. Rothenberg descrive il Janusian thinking come simultaneità da mantenere. Sono complementari: la dissonanza è la pressione, il Janusian thinking è il metodo per trascenderla.

**Vincolo implementativo:** `{"type": "dissonance", "belief_1": "il nostro prodotto è il migliore", "belief_2": "il nostro prodotto ha un difetto fondamentale", "requirement": "sostieni entrambe contemporaneamente e trova il framework che le riconcilia"}`

---

### D4. Reframing di secondo ordine (Watzlawick)

Documentato nel LENS.md principale (sezione 2.3).

### D5. Steelmanning

Documentato nel LENS.md principale (sezione 2.12).

---

## E. METODOLOGIE STRUTTURATE DI ANALISI

### E1. Structured Analytic Techniques (CIA/IC)

**Fonte:** Heuer & Pherson, "Structured Analytic Techniques for Intelligence Analysis" (2015/2020)

**SAT oltre ACH:**

| SAT | Cosa fa | Mapping a Lens |
|---|---|---|
| **Key Assumptions Check** | Identifica e testa assunzioni non dichiarate | → Socratic Drill |
| **Diagnostic Reasoning** | Elimina alternative sistematicamente | → Cascade con eliminazione |
| **Quadrant Crunching** | Matrice per mappare scenari | → Scenario Matrix |
| **What-If Analysis** | Esplora futuri ipotetici | → Vincolo counterfactual |
| **High-Impact/Low-Probability** | Valuta eventi rari ma consequenziali | → Agente "black swan" |
| **ACH** | Ipotesi in competizione | → Adversarial + Jury |
| **Devil's Advocacy** | Attacca la posizione dominante | → Adversarial Cascade |

**I SAT che mappano meglio su multi-agent LLM:** Quadrant Crunching e What-If Analysis, perché scomponibili in agenti paralleli.

---

### E2-E5. Scenario Planning, Morphological Analysis, Red Teaming, Premortem

Documentati nel LENS.md principale.

---

### E6. SCAMPER (Eberle, basato su Osborn)

**Fonte:** Eberle, "SCAMPER: Creative Games and Activities for Imagination Development"

**7 operazioni:**
1. **Substitute:** sostituisci un elemento con un'alternativa
2. **Combine:** unisci concetti non correlati
3. **Adapt:** adatta a un nuovo contesto
4. **Modify:** altera dimensione, forma, attributi (anche Magnify/Minify)
5. **Put to other uses:** applica in scenari diversi
6. **Eliminate:** rimuovi componenti per semplificare
7. **Reverse/Rearrange:** inverti ordine, struttura, direzione

**Evidenza empirica:** GPT-4 con SCAMPER genera soluzioni al 75° percentile in elaborazione, originalità e novità rispetto a studenti umani (Cambridge, 2024).

**Implicazione per Lens:** ogni operazione SCAMPER è un vincolo. Un workflow SCAMPER ha 7 agenti, ognuno vincolato a una sola operazione. Il moderatore sintetizza.

**Vincolo implementativo:** `{"type": "scamper", "operation": "reverse", "target": "il nostro processo di vendita"}`

---

### E7. CPS Model (Osborn-Parnes)

**Fonte:** Osborn, "Applied Imagination" (1953); Parnes et al.

**5 fasi:**
1. **Fact-finding:** raccogliere dati
2. **Problem-finding:** riformulare il problema
3. **Idea-finding:** generare idee (DIVERGENTE)
4. **Solution-finding:** valutare idee (CONVERGENTE)
5. **Acceptance-finding:** pianificare implementazione

**Principio chiave:** la separazione deliberata tra fasi divergenti e convergenti migliora la qualità degli outcome. La prematura giudizio (convergere troppo presto) è il killer principale della creatività.

**Implicazione per Lens:** le sessioni Lens dovrebbero avere fasi esplicite. Round 1 = divergente (nessun agente valuta). Round 2+ = convergente (agenti che filtrano, attaccano, valutano). Il Moderatore NON giudica nel Round 1 — solo raccoglie.

---

### E8. Assumption Reversal / SAST (Mason & Mitroff, 1981)

**Fonte:** "Challenging Strategic Planning Assumptions"

**Processo SAST:**
1. Elencare le assunzioni su cui si basa la strategia/decisione
2. Classificare per importanza e certezza
3. Testare con dialectic debate
4. Invertire quelle ad alto impatto e esplorare le implicazioni

**Esempi storici:**
- Inversione di "le auto hanno bisogno di un guidatore" → veicoli autonomi
- Inversione di "fidelizzazione tramite sconti" → modelli subscription
- NASA: inversione di "lo spazio richiede esseri umani" → sonde non pilotate

**Implicazione per Lens:** workflow dedicato. Fase 1: Socratic Drill per elencare assunzioni. Fase 2: classificazione importanza/certezza. Fase 3: inversione sistematica delle top-K assunzioni. Fase 4: esplorazione delle implicazioni con agenti diversi.

**Vincolo implementativo:** `{"type": "assumption_reversal", "assumption": "i clienti confrontano prezzi", "reversed": "i clienti NON confrontano prezzi", "explore": "quali strategie diventano possibili?"}`

---

### E9. Concept Fan (De Bono)

**Fonte:** De Bono, "Serious Creativity"

**Meccanismo:** navigare tra livelli di astrazione:
- **Specifico:** soluzione concreta ("ripara il rubinetto")
- **Direzione:** strategia più ampia ("migliora l'efficienza idrica")
- **Scopo:** bisogno fondamentale ("riduci gli sprechi domestici")

Muoversi verso l'alto apre nuove direzioni. Muoversi verso il basso concretizza.

**Implicazione per Lens:** vincolo di livello di astrazione. Un agente è vincolato a "solo scopo" (il livello più astratto), un altro a "solo specifico". Il confronto tra livelli rivela soluzioni invisibili da un singolo livello.

**Vincolo implementativo:** `{"type": "concept_fan", "level": "purpose", "instruction": "Qual è il bisogno fondamentale che stiamo cercando di soddisfare? Non la soluzione, il bisogno."}`

---

## F. FLESSIBILITÀ COGNITIVA E VINCOLI

### F1. Cognitive Flexibility e Set-Shifting

**Fonte:** Wisconsin Card Sorting Test; ricerca su perseverazione

**Perseverazione:** aderenza persistente a una strategia obsoleta nonostante feedback negativo. Gli LLM mostrano perseverazione: ripetono pattern stabiliti nel contesto nonostante nuove istruzioni.

**Meccanismi umani per rompere mental set:**
- Error detection (notare che la regola è cambiata)
- Inhibitory control (sopprimere la risposta precedente)
- Working memory update (integrare nuovo feedback)

**Implicazione per Lens:** un agente "set-shifter" il cui unico compito è rilevare perseverazione negli altri agenti e forzare un cambio di frame. Come il WCST: quando l'output diventa prevedibile, cambia le regole.

---

### F2. Constraint-Based Creativity (Stokes, 2001/2005)

**Fonte:** "Creativity from Constraints: The Psychology of Breakthrough"

**Tipologia dei vincoli Stokes:**
- **Primary constraints:** limitano le azioni ("usa solo questi 50 parole") → prevengono la "paralisi della pagina bianca"
- **Secondary constraints:** ripetono percorsi di successo → costruiscono competenza
- **Tertiary constraints:** estendono via analogia → producono innovazione

**Evidenza empirica:** gruppi vincolati producono +25% idee più originali e +236% output più creativo rispetto a gruppi liberi.

**Il "Green Eggs and Ham effect":** Seuss scommise di scrivere un libro con sole 50 parole. Il vincolo produsse un capolavoro. Il vincolo non limita — dirige l'esplorazione verso territorio non ovvio.

**Implicazione per Lens:** VALIDAZIONE TEORICA CENTRALE. I vincoli non sono una limitazione, sono il meccanismo fondamentale della creatività. Lens non "limita" l'LLM — lo dirige verso le code della distribuzione.

---

### F3. DBT Wise Mind (Linehan, 1993)

**Fonte:** "Cognitive-Behavioral Treatment of Borderline Personality Disorder"

**Tre menti:**
- **Emotional Mind:** intuitiva, guidata dai sentimenti, reattiva
- **Reasonable Mind:** logica, basata sui fatti, fredda
- **Wise Mind:** sintesi delle due — integra intuizione e logica

**Implicazione per Lens:** topologia Wise Mind. Due agenti (emotional + rational) producono posizioni, un terzo agente-sintetizzatore le integra. Diverso dalla dialettica hegeliana: non tesi-antitesi-sintesi, ma emozione-ragione-saggezza.

**Vincolo implementativo:**
- Agente emotional: `{"type": "modal", "mode": "emotional", "instruction": "Rispondi con intuizione, paure, desideri. Nessun dato, nessuna logica."}`
- Agente rational: `{"type": "modal", "mode": "rational", "instruction": "Solo fatti verificabili, logica, dati. Nessuna intuizione."}`
- Sintetizzatore: `{"type": "wise_mind", "instruction": "Integra entrambe le posizioni. Dove l'emozione ha ragione? Dove la logica manca qualcosa?"}`

---

### F4. Reflexivity (Soros/Bourdieu)

**Fonte:** Soros, "The Alchemy of Finance" (1987); Bourdieu, "Outline of a Theory of Practice" (1977)

**Meccanismo:** l'osservatore cambia ciò che osserva. In mercati finanziari: le previsioni influenzano il mercato che prevedono. In sistemi sociali: le categorie analitiche modellano la realtà che descrivono.

**Rischi per Lens:** se Lens analizza una strategia e poi la strategia viene modificata sulla base dell'analisi di Lens, c'è un loop riflessivo. L'analisi di Lens non descrive una realtà indipendente — la co-crea.

**Opportunità:** un agente "reflexivity monitor" che chiede: "Come cambierebbe la situazione SE agissimo sulla base di questa analisi?"

---

## G. RICERCA EMPIRICA SU MULTI-AGENT LLM

### G1. Multi-Agent Debate

- A-HMAD: +4-6% accuratezza, -30% errori fattuali con agenti eterogenei
- Focus Agent (2024): focus group LLM simili a partecipanti umani
- Multi-Agent Debate Scaling (ICLR 2025): diminishing returns dopo 3-4 round

### G2. Synthetic Personas

- Park (Stanford, 2024): 1.052 agenti da interviste qualitative replicano risposte all'85%
- SSR (Semantic Similarity Rating): 90% della affidabilità test-retest umana

### G3. Activation Steering

- Concept Activation Vectors (ICLR 2025): steering di creatività, humor, stile
- Conceptors: steering multi-proprietà via operazioni booleane
- Non implementabile oggi via API, ma valida la direzione teorica

### G4. Divergent Creativity

- LLM superano la media umana in divergent thinking
- Non superano il top decile umano
- I vincoli strutturali (Stokes) compensano il gap

---

## Mappa delle connessioni tra teorie

```
TEORIE CHE SI RAFFORZANO A VICENDA:

Bisociazione ←→ Synectics ←→ Defamiliarization
    (tutte: collisione tra frame incompatibili)

Janusian Thinking ←→ Cognitive Dissonance ←→ Dialettica Hegeliana
    (tutte: tensione tra opposti come motore creativo)

Wisdom of Crowds ←→ Mercier-Sperber ←→ Ensemble Methods
    (tutte: il gruppo supera l'individuo sotto condizioni specifiche)

Constraint Creativity (Stokes) ←→ TRIZ ←→ Forcing Functions
    (tutte: i vincoli producono creatività, non la limitano)

Premortem ←→ Scenario Planning ←→ Counterfactual
    (tutte: spostamento temporale come strumento cognitivo)

SCAMPER ←→ Morphological Analysis ←→ Concept Fan
    (tutte: scomposizione sistematica dello spazio delle soluzioni)

TEORIE CHE CREANO TENSIONE PRODUTTIVA:
- Wisdom of Crowds (indipendenza) vs Argumentative Theory (ragionamento è sociale)
  → Risoluzione: indipendenza nel Round 1, interazione nei round successivi
- Cognitive Dissonance (tensione da risolvere) vs Janusian Thinking (tensione da mantenere)
  → Risoluzione: la dissonanza è il motore, il Janusian thinking è il metodo
```

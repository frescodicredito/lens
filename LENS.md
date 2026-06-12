# Lens — Cognitive Infrastructure for LLM Reasoning

> Documento fondativo (teoria e design).
>
> **Nota di lettura:** questo è il documento teorico/di design di Lens. Gli esempi sono
> illustrativi e Lens funziona in modo completamente autonomo, senza dipendere da alcun
> sistema esterno. Per i conteggi correnti di tool/vincoli/topologie fa fede il
> [README](README.md).

---

## 1. Cos'è Lens

Lens è un **sistema di infrastruttura cognitiva** per il ragionamento con LLM. Non produce contenuti finali: produce *modi di guardare* un problema. Come un obiettivo fotografico che non modifica la scena ma la inquadra diversamente, Lens cambia il punto di osservazione dell'LLM.

### Il problema che risolve

Un LLM risponde con le risposte **statisticamente più probabili**. Il centro della distribuzione è denso di risposte ovvie, sicure, mediocri. La creatività reale, le connessioni insolite, le prospettive non-lineari vivono nelle **code della distribuzione**.

Lens naviga sistematicamente queste code attraverso vincoli strutturali, non decorativi.

### Cosa NON è Lens

- Non è un sistema che cambia il *tono* dell'LLM (estetica)
- Non è un generatore di personaggi (costume)
- Non è un chatbot con personalità diverse
- Non simula "stati alterati" — produce strutture cognitive alternative

---

## 2. Fondamenti teorici

Lens si basa su teorie validate dalla ricerca. Ogni meccanismo ha una base epistemologica.

### 2.1 Dialectica hegeliana (Tesi → Antitesi → Sintesi)

**Fonte:** Hegel; implementazione computazionale [Hegelion](https://github.com/Hmbown/Hegelion)

L'LLM si impegna su una posizione (tesi), poi attacca quella posizione in una chiamata separata (antitesi), poi riconcilia l'opposizione (sintesi). Il framework SIEV valuta non solo la conclusione ma *come* il modello ci arriva: la capacità di risolvere tensioni, integrare idee distinte, sintetizzare ragionamento di ordine superiore.

**Applicazione in Lens:** la topologia Cascade è una dialettica hegeliana iterata. Ogni passaggio produce una sintesi che diventa la nuova tesi per il ciclo successivo.

### 2.2 Premortem e Prospective Hindsight (Gary Klein)

**Fonte:** Klein, 1991/2007; [garyklein.com/premortem](https://www.gary-klein.com/premortem)

L'hindsight prospettico — immaginare che un evento sia già accaduto — aumenta del 30% la capacità di identificare correttamente le ragioni di esiti futuri (ricerca 1989). Il frame del "già successo" rimuove l'ottimismo di default e sblocca pattern di rischio che la mente razionale sopprime.

**Applicazione in Lens:** frame temporale come vincolo strutturale. Non "cosa potrebbe andare male?" ma "è il 2028, è andato male — ricostruisci la catena causale."

### 2.3 Reframing di secondo ordine (Watzlawick)

**Fonte:** Watzlawick, "Change: Principles of Problem Formation and Problem Resolution"

Cambiamento di primo ordine: risolvere il problema dentro il frame esistente. Cambiamento di secondo ordine: cambiare il frame stesso. "Reframing significa cambiare il contesto concettuale e/o emotivo in cui una situazione è esperita, collocandola in un altro frame che si adatta ai fatti altrettanto bene o meglio, cambiandone l'intero significato."

**Applicazione in Lens:** il Constraint Engine non risolve problemi, cambia i frame in cui i problemi esistono. È intrinsecamente un motore di cambiamento di secondo ordine.

### 2.4 Pensiero parallelo (De Bono, Six Thinking Hats)

**Fonte:** De Bono, [Six Thinking Hats](https://www.debonogroup.com/services/core-programs/six-thinking-hats/)

Sei modalità cognitive separate: fatti (bianco), emozioni (rosso), rischi (nero), benefici (giallo), creatività (verde), processo (blu). Il valore non è nelle singole modalità ma nella **separazione**: esplorare una dimensione alla volta evita che il pensiero critico soffochi quello creativo.

**Applicazione in Lens:** le Lens non sono persona ma **modalità cognitive**. Un agente con vincolo "solo rischi, nessun beneficio" produce output radicalmente diverso da "solo opportunità, nessun rischio". La separazione è il meccanismo.

### 2.5 Groupthink e dissenso strutturato (Janis)

**Fonte:** Janis, 1971; [Devil's Advocacy and Dialectical Inquiry](https://www.nationalforum.com/Electronic%20Journal%20Volumes/Lunenburg,%20Fred%20C.%20Devil's%20Advocacy%20&%20Dialectical%20Inquiry%20IJSAID%20V14%20N1%202012.pdf)

Il groupthink si verifica quando "i membri di un gruppo coeso tendono a mantenere l'esprit de corps sviluppando inconsciamente illusioni condivise che interferiscono con il pensiero critico." Prevenzione: avvocato del diavolo istituzionalizzato, dissenso programmato, conflitto strutturato.

**Applicazione in Lens:** l'LLM ha un bias strutturale verso il consenso. Lens contrasta questo bias con dissenso programmato — agenti il cui unico compito è attaccare la posizione dominante.

### 2.6 Metodo Delphi

**Fonte:** Helmer & Dalkey, RAND Corporation, 1950s; [Wikipedia](https://en.wikipedia.org/wiki/Delphi_method)

Processo iterativo: esperti rispondono indipendentemente (anonimato), ricevono feedback aggregato, rivedono le posizioni. Convergenza iterativa. Variante: Disagreement Delphi, progettato per generare discussione intorno a topic che non raggiungono consenso.

**Applicazione in Lens:** la topologia Star (moderatore + N agenti) è un Delphi computazionale. Il Disagreement Delphi è particolarmente rilevante — non cerchiamo consenso, cerchiamo la *mappa* del disaccordo.

### 2.7 TRIZ e risoluzione di contraddizioni

**Fonte:** Altshuller, 1946+; [TRIZ](https://www.triz.co.uk/what-is-triz)

L'innovazione vera nasce dalla risoluzione di contraddizioni: migliorare un parametro senza peggiorarne un altro. 40 principi inventivi derivati dall'analisi di centinaia di migliaia di brevetti. Il framework non cerca compromessi — cerca soluzioni che superano le contraddizioni.

**Applicazione in Lens:** le forcing functions possono essere strutturate come contraddizioni TRIZ. "Aumenta la velocità senza aumentare il costo" non è un compromesso, è un vincolo che forza l'esplorazione di soluzioni non-lineari.

### 2.8 Dual Process Theory (Kahneman)

**Fonte:** Kahneman, "Thinking, Fast and Slow"; [Decision Lab](https://thedecisionlab.com/reference-guide/philosophy/system-1-and-system-2-thinking)

Sistema 1: veloce, automatico, intuitivo. Sistema 2: lento, deliberato, analitico. Gli LLM operano di default in modalità Sistema 1 (risposte fluide, probabilistiche, veloci). Lens forza il Sistema 2: vincoli che richiedono deliberazione esplicita, verifica, giustificazione.

**Applicazione in Lens:** ogni vincolo strutturale è un forzante di Sistema 2. Quando l'LLM non può dare la risposta ovvia, deve attivare ragionamento deliberato.

### 2.9 Structured Analytic Techniques (Intelligence Analysis)

**Fonte:** CIA/IC tradecraft; [Cognitive biases in intelligence analysis](https://viborc.com/cognitive-biases-intelligence-analysis-mitigation/)

Otto bias identificati nel workflow analitico: belief bias, confirmation bias, explanation bias, fluency effects, framing effects, order effects, planning fallacy, overconfidence. Le SAT (Analysis of Competing Hypotheses, Devil's Advocacy) aggiungono rigore strutturale per contrastare questi bias.

**Applicazione in Lens:** Lens è un sistema SAT computazionale. L'Analysis of Competing Hypotheses (ACH) mappa direttamente sulla topologia Adversarial + Jury.

### 2.10 Bisociazione (Koestler)

**Fonte:** Koestler, "The Act of Creation", 1964; [The Marginalian](https://www.themarginalian.org/2013/05/20/arthur-koestler-creativity-bisociation/)

La creatività nasce dalla **bisociazione**: la percezione simultanea di un'idea in due matrici di pensiero abitualmente incompatibili. Non è associazione (collegamento dentro un singolo frame), è la collisione tra due frame indipendenti. L'umorismo, la scoperta scientifica e l'arte condividono questa struttura: due matrici sovrapposte producono sorpresa (umorismo), eureka (scienza), o giustapposizione estetica (arte).

**Applicazione in Lens:** il Constraint Engine con vincoli semantici è un generatore di bisociazioni. "Descrivi questa strategia di marketing in termini di ecologia marina" forza la collisione tra due matrici (marketing e biologia) — esattamente il meccanismo di Koestler. La topologia Ring è una bisociazione iterata: ogni reframe è una nuova matrice che si sovrappone alla precedente.

### 2.11 Lateral Thinking e Provocation (De Bono)

**Fonte:** De Bono, "Lateral Thinking", 1967; [De Bono Group](https://www.debonogroup.com/services/core-programs/lateral-thinking/)

Il lateral thinking opera con quattro tipi di strumenti: generazione di idee (rompere pattern correnti), focus (ampliare dove cercare), harvest (estrarre più valore dall'output), treatment (considerare vincoli reali). Le tecniche chiave sono:
- **Provocation** (PO): affermazione deliberatamente sbagliata o impossibile, usata per generare idee nuove
- **Random Entry**: un concetto casuale viene forzatamente associato al problema
- **Reversal**: il processo viene rovesciato — dal risultato al punto di partenza

**Applicazione in Lens:** le forcing functions di tipo "inversione" e "esclusione" sono implementazioni dirette del lateral thinking. La Provocation PO è un tipo di vincolo ancora non esplorato: "PO: i clienti non vogliono comprare" — un'affermazione impossibile che forza percorsi laterali.

### 2.12 Steelmanning

**Fonte:** [Umbrex](https://umbrex.com/resources/tools-for-thinking/what-is-steelmanning/)

Lo steelmanning è il contrario dello strawman: costruire la **versione più forte possibile** di un argomento, anche se lo si contesta. Quattro principi: carità interpretativa, accuratezza, rafforzamento, verifica. Trasforma il debate da confronto a problem-solving collaborativo.

**Applicazione in Lens:** nuova topologia o variante della Cascade. Invece di attaccare (antitesi), ogni agente **rafforza** la posizione del precedente. La versione che emerge dopo 4 round di steelmanning è la versione più robusta possibile dell'argomento. Complementare all'adversarial cascade: prima steelman (trova la versione più forte), poi adversarial (attaccala). Quello che sopravvive a entrambi è inattaccabile.

### 2.13 Scenario Planning (Shell/Schwartz)

**Fonte:** Schwartz, "The Art of the Long View", 1991; [Systems Thinker](https://thesystemsthinker.com/planning-for-multiple-futures/)

Lo scenario planning non predice il futuro — costruisce **futuri multipli plausibili** basati su incertezze critiche. Metodo: identifica 2 incertezze chiave, costruisci una matrice 2x2, esplora i 4 quadranti come scenari alternativi. Shell usò questo metodo per anticipare la caduta dei prezzi del petrolio.

**Applicazione in Lens:** workflow specializzato "Lens Scenario". Input: una decisione + 2 incertezze. Output: 4 scenari strutturati, ognuno esplorato da un agente diverso con vincoli coerenti al suo quadrante. Non è un focus group — è una mappa di futuri possibili.

### 2.14 Morphological Analysis (Zwicky)

**Fonte:** Zwicky; [Ness Labs](https://nesslabs.com/zwicky-box)

L'analisi morfologica scompone un problema in dimensioni, elenca le varianti possibili per ogni dimensione, poi esplora sistematicamente le combinazioni. L'ambizione di Zwicky era "rendere l'invenzione routinizzabile" — un processo metodico, non un colpo di genio.

**Applicazione in Lens:** il Constraint Composer potrebbe usare un approccio morfologico per generare combinazioni di vincoli. Dimensioni: tipo di vincolo x frame temporale x dominio semantico x livello di intensità. L'esplorazione sistematica dello spazio delle combinazioni garantisce di non tralasciare configurazioni potenzialmente potenti.

### 2.15 Metodo Socratico (Elenchus)

**Fonte:** Socrate/Platone; [Conversational Leadership](https://conversational-leadership.net/socratic-elenchus/)

L'elenchus è la tecnica centrale del metodo socratico: l'interlocutore asserisce una tesi, Socrate ottiene l'accordo su premesse aggiuntive, poi dimostra che queste premesse implicano il contrario della tesi originale. Non fornisce risposte — scopre assunzioni nascoste e espone contraddizioni.

**Applicazione in Lens:** topologia "Socratic Drill". Un agente-Socrate non ha una posizione propria — fa solo domande. Le domande sono vincolate a scoprire assunzioni (non a demolire, come nell'adversarial). L'output non è una mappa di posizioni ma una mappa di **assunzioni nascoste** con il loro grado di vulnerabilità.

### 2.16 Wisdom of Crowds (Surowiecki)

**Fonte:** Surowiecki, "The Wisdom of Crowds", 2004; [Wikipedia](https://en.wikipedia.org/wiki/The_Wisdom_of_Crowds)

Le condizioni perché un gruppo sia intelligente sono quattro: **diversità di opinione**, **indipendenza** dei membri, **decentralizzazione**, e **meccanismo di aggregazione**. Cruciale: "troppa comunicazione può rendere il gruppo meno intelligente" — l'indipendenza è fondamentale.

**Applicazione in Lens:** principio architetturale critico. Nel Round 1 di ogni topologia, gli agenti **non devono vedere** le posizioni degli altri (indipendenza computazionale). La comunicazione arriva solo nei round successivi, mediata dal moderatore. Questo non è un dettaglio implementativo — è la condizione necessaria per l'intelligenza collettiva.

### 2.17 Tree/Graph of Thoughts

**Fonte:** [Yao et al., 2023](https://arxiv.org/abs/2305.10601); [ETH Zurich](https://htor.inf.ethz.ch/publications/img/besta-topologies.pdf)

Tree of Thoughts (ToT) mantiene un albero dove ogni nodo è un pensiero intermedio, con branching, backtracking e self-evaluation. Graph of Thoughts (GoT) generalizza a grafi arbitrari con merge di rami paralleli. ToT ha portato GPT-4 dal 4% al 74% di successo su Game of 24.

**Applicazione in Lens:** le topologie Lens sono essenzialmente topologie di reasoning. La Cascade è una catena, la Star è un albero a un livello, l'Adversarial+Jury è un grafo con nodi di valutazione. Lens potrebbe supportare topologie custom come grafi di pensiero definiti dall'utente.

### 2.18 Counterfactual Reasoning

**Fonte:** [Arxiv](https://arxiv.org/html/2410.06392v1); [Decision Lab](https://thedecisionlab.com/reference-guide/computer-science/counterfactual-reasoning-in-ai)

Il ragionamento controfattuale genera grafi causali e esegue interventi atomici per inferire conseguenze in scenari "what if?". Limitazione: gli LLM faticano a mantenere variabili costanti mentre ne alterano altre.

**Applicazione in Lens:** vincolo di tipo "counterfactual". "Cosa sarebbe successo se NON avessimo scelto X?" costringe l'LLM a ragionare su catene causali alternative. Combinato con il premortem di Klein, crea uno strumento potente per l'analisi decisionale retrospettiva.

### 2.19 Constitutional AI e Self-Critique ricorsiva

**Fonte:** [Anthropic](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)

Il modello critica la propria risposta secondo principi espliciti, poi rivede la risposta alla luce della critica. Processo iterativo che migliora la qualità senza feedback umano.

**Applicazione in Lens:** ogni agente Lens potrebbe avere una fase di self-critique prima di consegnare l'output. Il vincolo non è solo "rispondi da questa prospettiva" ma "rispondi, poi critica la tua risposta dal punto di vista dei tuoi stessi bias, poi rivedi". Aggiunge un layer di raffinamento interno che riduce il rumore.

### 2.20 Ricerca empirica su Multi-Agent Debate (2024-2025)

**Fonti chiave:**
- [A-HMAD](https://link.springer.com/article/10.1007/s44443-025-00353-3): agenti eterogenei in debate producono +4-6% accuratezza, -30% errori fattuali
- [Focus Agent](https://arxiv.org/html/2409.01907v1): focus group LLM generano opinioni simili a partecipanti umani
- [Park, Stanford 2024](https://arxiv.org/abs/2411.10109): persona da interviste qualitative replicano risposte all'85%
- [Multi-Agent Systems 2025](https://www.preprints.org/manuscript/202511.1370): il prossimo scaling frontier non è modelli più grandi ma "societies of models"
- [Divergent Creativity](https://www.nature.com/articles/s41598-025-25157-3): LLM superano media umana in divergent thinking, ma non il top decile umano

---

## 3. Architettura del sistema

### 3.1 Principio architetturale

**Il vincolo è il primitivo.** Tutto il resto — persona, topologie, sessioni — è costruito sopra il Constraint Engine.

Una "lente" non è una persona. È una **configurazione di vincoli cognitivi** che sposta il punto di osservazione dell'LLM. Una persona è un pattern d'uso sopra il Constraint Engine (un bundle di vincoli con un nome e un'identità).

### 3.2 Componenti

```
Lens
├── Constraint Engine            ← il primitivo fondamentale
│   ├── Forcing Functions        (esclusione, limiti, inversione)
│   ├── Frame Shifts             (temporale, semantico, di ruolo)
│   ├── Contradiction Resolver   (vincoli TRIZ-like)
│   └── Constraint Composer      (combina, parametrizza, genera)
│
├── Topology Engine              ← come gli agenti interagiscono
│   ├── Cascade                  (dialettica hegeliana iterata)
│   ├── Star / Delphi            (moderatore centrale + N raggi)
│   ├── Adversarial + Jury       (ACH — debate + valutazione separata)
│   ├── Ring                     (accumulo sequenziale, ciascuno vede solo il precedente)
│   └── Parallel Hats            (De Bono — N agenti, ognuno una modalità cognitiva)
│
├── Persona Layer                ← bundle di vincoli con identità
│   ├── Cognitive Templates      (JSON leggero: bias, paure, obiettivi, vocabolario, soglia)
│   ├── Miner-Grounded           (costruite da dati audience reali)
│   └── Custom / Progetto        (create per contesto specifico)
│
├── Session Manager              ← orchestra l'esecuzione
│   ├── Session Config           (topic, vincoli, topologia, N agenti)
│   ├── Agent Spawner            (crea agenti con vincoli assegnati)
│   ├── Turn Manager             (gestisce round, timing, ordine)
│   └── Moderator                (sintetizza, mappa, non appiattisce)
│
├── Output Formatter             ← struttura rigida dell'output
│   ├── Perspective Card         (claim, supporto, blind spot, confidenza)
│   ├── Field Map                (convergenze, divergenze, outlier, tensioni)
│   ├── Delta Report             (cosa c'è qui che non c'era nella baseline)
│   └── Decision Brief           (raccomandazione con pro/contro pesati)
│
└── Meta-Lens                    ← auto-ottimizzazione
    ├── Efficacy Tracker          (quale vincolo produce più divergenza)
    ├── Combination Suggester     (propone configurazioni nuove)
    └── Session History           (archivio sessioni per pattern mining)
```

### 3.3 Flusso di una sessione Lens

```
INPUT                          PROCESSING                      OUTPUT
─────                          ──────────                      ──────
                               ┌─────────────────┐
  Topic/Problema ──────────────│ Session Config   │
  + Scelta topologia           │ (topic, topologia│
  + Vincoli opzionali          │  N agenti, round)│
                               └────────┬────────┘
                                        │
                               ┌────────▼────────┐
                               │ Constraint       │
                               │ Composer          │─── genera N set
                               │ (assegna vincoli │    di vincoli
                               │  per agente)     │    diversi
                               └────────┬────────┘
                                        │
                               ┌────────▼────────┐
                               │ Agent Spawner    │
                               │ (N agenti con    │    Round 1: elaborazione
                               │  vincoli propri) │    indipendente
                               └────────┬────────┘
                                        │
                               ┌────────▼────────┐
                               │ Topology Engine  │    Round 2-N: interazione
                               │ (gestisce come   │    secondo la topologia
                               │  interagiscono)  │    scelta
                               └────────┬────────┘
                                        │
                               ┌────────▼────────┐
                               │ Moderator        │
                               │ (sintetizza,     │──── NON cerca consenso
                               │  mappa il campo) │     mappa le posizioni
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
                                                        │ (traccia    │
                                                        │  efficacia) │
                                                        └─────────────┘
```

---

## 4. Topologie cognitive — dettaglio

Le topologie non sono solo strutture di comunicazione. Sono **pattern cognitivi** che determinano come emerge l'intelligenza collettiva.

### 4.1 Cascade (Dialettica Hegeliana)

```
A ──tesi──▶ B ──antitesi──▶ C ──sintesi──▶ D ──nuova antitesi──▶ ...
```

**Quando usarla:** stressare un'idea, trovare il nucleo che sopravvive all'attacco sistematico.
**Meccanismo:** ogni agente vede solo l'output del precedente e deve attaccarlo. Quello che sopravvive alla cascata è il nucleo solido.
**Fondamento:** dialettica hegeliana + adversarial debate (A-HMAD, +4-6% accuratezza).

### 4.2 Star / Delphi

```
        B
       ╱
  A ──M── C     M = moderatore
       ╲
        D
```

**Quando usarla:** esplorare un problema da N prospettive indipendenti, poi sintetizzare.
**Meccanismo:** N agenti elaborano indipendentemente (anonimato computazionale). Il moderatore espone, gli agenti rivedono. Convergenza iterativa.
**Fondamento:** metodo Delphi + Disagreement Delphi (mappa del disaccordo).

### 4.3 Adversarial + Jury (ACH)

```
  A ◄──debate──► B
         │
    ┌────▼────┐
    │ J1 J2 J3│   (giuria indipendente)
    └─────────┘
```

**Quando usarla:** decisioni ad alto impatto dove serve separare produzione da valutazione.
**Meccanismo:** 2 agenti dibattono con vincoli opposti. 3 giurati (con vincoli diversi tra loro) valutano indipendentemente. Nessun giurato parla con gli altri.
**Fondamento:** Analysis of Competing Hypotheses (CIA SAT) + separation of concerns.

### 4.4 Ring (Accumulo sequenziale)

```
  A ──▶ B ──▶ C ──▶ D ──▶ (torna ad A)
```

**Quando usarla:** costruire su un'idea in modo incrementale, ogni agente aggiunge un layer.
**Meccanismo:** ogni agente vede solo l'output del precedente (non l'originale). L'idea si trasforma passando attraverso vincoli diversi. L'output finale è irreconoscibile dall'input — è stato reframato N volte.
**Fondamento:** Watzlawick (reframing iterato) + telephone game strutturato.

### 4.5 Parallel Hats (De Bono computazionale)

```
  [Fatti] [Rischi] [Opportunità] [Emozioni] [Creatività] [Processo]
     │        │          │            │           │            │
     └────────┴──────────┴────────────┴───────────┴────────────┘
                              │
                         Integrazione
```

**Quando usarla:** analisi esaustiva dove serve coprire tutte le dimensioni di un problema.
**Meccanismo:** N agenti, ognuno vincolato a una singola modalità cognitiva. Nessun agente può invadere il territorio degli altri. Integrazione finale del moderatore.
**Fondamento:** Six Thinking Hats + parallel thinking (non debate, non conflitto — esplorazione parallela).

### 4.6 Steelman Chain

```
A ──rafforza──▶ B ──rafforza──▶ C ──rafforza──▶ (versione più forte)
                                                       │
                                                  Adversarial ◄── D attacca
```

**Quando usarla:** trovare la versione più forte di un argomento, poi testarla sotto pressione.
**Meccanismo:** prima fase steelmanning (ogni agente rafforza la posizione del precedente), poi fase adversariale (un agente attacca la versione più forte). Quello che sopravvive è genuinamente robusto.
**Fondamento:** steelmanning + adversarial cascade sequenziale.

### 4.7 Socratic Drill

```
  Tema ──▶ Socrate (domande) ──▶ Assunzione 1 ──▶ Socrate (domande) ──▶ ...
                                    │
                               Vulnerabilità?
```

**Quando usarla:** scoprire le assunzioni nascoste sotto una posizione, non attaccarla.
**Meccanismo:** un agente-Socrate non ha posizione propria. Fa solo domande. Ogni domanda è vincolata a scoprire un'assunzione implicita. L'output è una mappa di assunzioni con grado di vulnerabilità.
**Fondamento:** elenchus socratico — non fornisce risposte, scopre la struttura nascosta del ragionamento.

### 4.8 Scenario Matrix

```
                    Incertezza A alta
                         │
  Incertezza B   ┌───────┼───────┐
  bassa ─────────│  Q1   │  Q2   │
                 ├───────┼───────┤
                 │  Q3   │  Q4   │
  Incertezza B   └───────┼───────┘
  alta                   │
                    Incertezza A bassa

  4 agenti, uno per quadrante, vincoli coerenti con il proprio scenario
```

**Quando usarla:** esplorare futuri multipli per decisioni ad alta incertezza.
**Meccanismo:** 2 incertezze critiche definiscono una matrice 2x2. 4 agenti esplorano ciascuno uno scenario. Il moderatore non cerca il "futuro più probabile" ma mappa le strategie robuste (che funzionano in 3+ scenari su 4).
**Fondamento:** scenario planning Shell/Schwartz — futuri multipli plausibili, non predizione.

### 4.9 Bisociation Engine

```
  Problema ──▶ Matrice A (dominio originale)
                     ╲
                      ╳ ──▶ Intersezione = insight
                     ╱
               Matrice B (dominio forzato)
```

**Quando usarla:** generare insight genuinamente creativi per collisione tra domini.
**Meccanismo:** il problema viene descritto in due domini semantici radicalmente diversi. Un agente opera nel dominio originale, uno nel dominio forzato. Il moderatore cerca le intersezioni — dove le due matrici si sovrappongono emerge la bisociazione (Koestler).
**Fondamento:** bisociazione + semantic reframing strutturato.

### 4.10 Wise Mind (DBT)

```
  [Emotional Agent]     [Rational Agent]
         │                      │
         └──────────┬───────────┘
                    │
            [Wise Mind Synthesizer]
```

**Quando usarla:** decisioni dove l'intuizione e la logica divergono.
**Meccanismo:** un agente opera solo con intuizione/emozioni/paure. Un altro solo con fatti/logica/dati. Un terzo sintetizza — non sceglie uno dei due, integra. Dove l'emozione ha ragione che la logica non vede? Dove la logica corregge l'emozione?
**Fondamento:** Linehan, DBT (1993) — la saggezza emerge dall'integrazione, non dalla scelta.

### 4.11 SCAMPER Parallel

```
  [Substitute] [Combine] [Adapt] [Modify] [Put to use] [Eliminate] [Reverse]
       │            │        │       │          │            │           │
       └────────────┴────────┴───────┴──────────┴────────────┴───────────┘
                                     │
                                Sintesi
```

**Quando usarla:** innovazione sistematica su un prodotto/processo/idea esistente.
**Meccanismo:** 7 agenti, ognuno vincolato a una sola operazione SCAMPER. Nessuno può fare operazioni degli altri. Il moderatore sintetizza le proposte più promettenti.
**Fondamento:** Eberle/Osborn. GPT-4 con SCAMPER produce output al 75° percentile vs studenti umani (Cambridge 2024).

### 4.12 Assumption Inversion

```
  Topic ──▶ Socratic Drill (estrae assunzioni)
                    │
             [A1] [A2] [A3] [A4] [A5]
                    │
             Classifica importanza/certezza
                    │
             Inverti top-3 ──▶ [Agente 1: A1 invertita]
                              [Agente 2: A2 invertita]
                              [Agente 3: A3 invertita]
                    │
             Esplora implicazioni
```

**Quando usarla:** scoprire opportunità nascoste nelle assunzioni date per scontate.
**Meccanismo:** prima il Socratic Drill estrae le assunzioni. Poi si classificano per impatto. Poi si invertono le top-3 e agenti dedicati esplorano le implicazioni di ciascuna inversione.
**Fondamento:** Mason & Mitroff SAST (1981). Esempi storici: "le auto hanno bisogno di guidatore" → veicoli autonomi.

---

## 5. Il Constraint Engine — cuore del sistema

### 5.1 Tassonomia dei vincoli

| Categoria | Descrizione | Esempi |
|---|---|---|
| **Esclusione** | Rimuovi il vocabolario/concetti rifugio | "Senza usare le parole X, Y, Z", "Nessun esempio del settore" |
| **Inversione** | Forza la conclusione opposta | "Dimostra il contrario", "Perché è una pessima idea?" |
| **Limite** | Imponi scarsità di risorse espressive | "3 frasi massimo", "Un solo argomento" |
| **Temporale** | Sposta il punto di osservazione nel tempo | "Dal 2030, retrospettiva", "Anni '70, prima di Internet" |
| **Semantico** | Cambia il vocabolario di dominio | "In termini biologici", "Come architettura" |
| **Ruolo** | Assegna un frame cognitivo (non un costume) | Bias espliciti, paure, obiettivi, vocabolario vincolato |
| **Contraddizione** | Vincoli TRIZ — migliora X senza peggiorare Y | "Più veloce senza costi aggiuntivi" |
| **Modale** | Vincola a una dimensione cognitiva (De Bono) | "Solo rischi", "Solo fatti verificabili", "Solo idee nuove" |
| **Provocation** | Affermazione impossibile come punto di partenza (De Bono PO) | "PO: i clienti non vogliono comprare", "PO: il prodotto è gratis" |
| **Counterfactual** | Ragionamento su scenari alternativi | "Cosa se NON avessimo scelto X?", "E se il competitor avesse vinto?" |
| **Socratico** | Solo domande, nessuna affermazione | "Quali assunzioni stai facendo?", "Su cosa si basa?" |
| **Steelman** | Rafforza la posizione invece di attaccarla | "Costruisci la versione più forte possibile di questo argomento" |
| **Bisociativo** | Forza collisione tra due domini | "Descrivi in termini di X", dove X è un dominio incompatibile |
| **Self-critique** | Critica la propria risposta prima di consegnarla | "Rispondi, poi critica dal punto di vista dei tuoi bias, poi rivedi" |
| **Janusian** | Tieni due posizioni opposte simultaneamente e trascendile | "X è vero E non-X è vero. Trova il framework che contiene entrambi" |
| **Dissonance** | Forza due credenze contraddittorie e richiedi riconciliazione | "Il prodotto è ottimo E ha un difetto fatale. Sostieni entrambe" |
| **Abductive** | Genera la spiegazione più sorprendente ma plausibile | "Spiegazione NON ovvia. Vietate le cause comuni" |
| **Defamiliarize** | Descrivi come se vedessi per la prima volta | "Antropologo che studia una civiltà sconosciuta" |
| **Synectics** | Forza analogia specifica (direct/personal/symbolic/fantasy) | "Sei il prodotto. Come ti senti quando il cliente ti usa?" |
| **SCAMPER** | Vincola a una singola operazione SCAMPER | "Solo Reverse: inverti ogni aspetto del processo" |
| **Abstraction** | Vincola a un livello specifico (Concept Fan) | "Solo scopo fondamentale, non soluzioni", "Solo implementazione concreta" |
| **ELM Route** | Processa via route centrale o periferica | "Valuta solo logica argomenti" vs "Valuta credibilità, tono, appeal" |
| **Set-shift** | Forza cambio di frame quando rileva perseverazione | "L'output è troppo prevedibile. Cambia completamente approccio" |

### 5.2 Composizione dei vincoli

I vincoli sono **componibili**. Un agente può operare sotto più vincoli simultanei:

```json
{
  "agent_id": "critic_futurist",
  "constraints": [
    {"type": "inversion", "value": "dimostra perché fallirà"},
    {"type": "temporal", "value": "dal 2030, retrospettiva"},
    {"type": "exclusion", "value": ["innovazione", "disruption", "AI-first"]},
    {"type": "limit", "value": "massimo 5 punti, ognuno con evidenza"}
  ]
}
```

La combinazione di vincoli produce output che nessun singolo vincolo produrrebbe da solo. Il Constraint Composer genera combinazioni, il Meta-Lens traccia quali combinazioni producono più divergenza.

---

## 6. Formati di output

### 6.1 Perspective Card (output singolo agente)

```yaml
perspective_card:
  agent: "CTO Scettico"
  constraints_active: [inversion, temporal_2030, exclusion_buzzwords]

  claim: "L'adozione fallirà per resistance organizzativa, non tecnica"

  supporting_evidence:
    - "Il 73% dei fallimenti enterprise AI è organizzativo (Gartner)"
    - "Nessun piano di change management nel documento"

  blind_spots:
    - "Non considero l'effetto network degli early adopter interni"
    - "Sottostimo il potere del mandate top-down"

  confidence: 0.7

  what_would_change_my_mind: "Evidenza di champion interni con potere decisionale"
```

### 6.2 Field Map (output sessione multi-agente)

```yaml
field_map:
  topic: "Go-to-market per un nuovo prodotto SaaS B2B"
  topology: "star_delphi"
  agents: 4
  rounds: 2

  convergences:
    - claim: "Serve un caso d'uso killer prima del platform play"
      agreed_by: [agent_1, agent_2, agent_4]
      confidence_avg: 0.82

  divergences:
    - topic: "Pricing model"
      positions:
        agent_1: "Freemium con upsell enterprise"
        agent_3: "Solo enterprise, no freemium"
      tension: "Accessibilità vs posizionamento premium"

  outliers:
    - claim: "Il vero competitor non è un altro tool, è il Google Doc condiviso"
      source: agent_2
      why_interesting: "Riformula completamente il competitive landscape"

  blind_spots_identified:
    - "Nessun agente ha considerato il rischio regolatorio GDPR su brand data"

  recommended_explorations:
    - "Approfondire l'outlier di agent_2 con una cascade adversariale"
    - "Testare il pricing con topologia Adversarial+Jury"
```

### 6.3 Delta Report (confronto con baseline)

```yaml
delta_report:
  baseline: "Risposta standard senza vincoli"
  lens_config: "4 agenti, star topology, 2 round"

  insights_only_in_lens: 7
  insights_only_in_baseline: 1
  shared_insights: 4

  highest_value_delta:
    - insight: "Il vero competitor è il Google Doc"
      value_score: 2  # 0=ovvio, 1=nuovo, 2=sorprendente
      not_in_baseline: true

  semantic_distance:
    baseline_vs_lens: 0.34  # cosine distance (alto = più diverso)
    baseline_vs_simple_roleplay: 0.12  # roleplay semplice non aggiunge molto
```

---

## 7. Integrazione (esempio: l'ecosistema dell'autore)

> Questa sezione è illustrativa: mostra come Lens si innesta in un flusso di lavoro più
> ampio. Lens funziona in modo autonomo e non richiede nessun sistema esterno.

### 7.1 Posizionamento

Lens è un **layer cognitivo trasversale**. Non è consumatore né produttore di contenuto finale: è un amplificatore di qualità che si interpone tra i dati a monte e gli artefatti a valle.

```
UPSTREAM (alimentano Lens)              DOWNSTREAM (Lens stressa)
─────────────────────────               ──────────────────────────
Dati strutturati esterni       →        Qualsiasi artefatto o decisione:
(es. profili audience reali             presentazioni, strategie, copy,
 via l'adapter Miner)                   scelte di prodotto, roadmap…
                               →        prima di finalizzarli, passali
Contesto del problema          →        attraverso una topologia Lens.
```

### 7.2 Interfacce di integrazione

**MCP Server (25 tool implementati):**

Constraint tools:
- `lens_list_constraints(category?)` — lista vincoli per categoria
- `lens_get_constraint(constraint_id)` — dettaglio singolo vincolo

Persona tools:
- `lens_list_personas()` — lista persona templates
- `lens_get_persona(persona_id)` — dettaglio persona template

Topology tools:
- `lens_list_topologies(mode?)` — topologie disponibili (QUICK/DEEP)
- `lens_get_topology(topology_id)` — dettaglio topologia con workflow

Composition tools:
- `lens_compose_prompt(topic, constraints, output_format, intensity)` — vincoli + topic in prompt strutturato
- `lens_compose_persona(persona_id, topic, output_format, intensity)` — persona template in prompt
- `lens_compose_baseline(topic, output_format)` — baseline senza vincoli per workflow delta
- `lens_suggest_constraints(topic, goal, max_constraints)` — suggerimenti data-driven + euristica

Session tools:
- `lens_session_save(...)` — salva sessione con rating efficacia
- `lens_session_list(limit?)` — sessioni recenti
- `lens_efficacy_report()` — report aggregato efficacia

Meta-Lens tools:
- `lens_meta_constraint_efficacy()` — quali vincoli producono risultati migliori
- `lens_meta_topology_efficacy()` — quali topologie funzionano meglio
- `lens_meta_patterns()` — combinazioni di vincoli di successo
- `lens_meta_suggest(topic, goal?)` — suggerimenti data-driven da storico sessioni

Miner integration tools:
- `lens_persona_from_miner(miner_persona_json, save?)` — trasforma singola persona Miner
- `lens_personas_from_miner_batch(miner_output_json, save?)` — trasforma tutte le persona Miner

**Skill Claude Code (9 implementate):**
- `/lens` — sessione interattiva DEEP mode, suggerisce topologia e configura agenti
- `/lens-adversarial` — cascata adversariale rapida su un claim (QUICK)
- `/lens-perspective` — singola prospettiva vincolata (QUICK)
- `/lens-premortem` — premortem strutturato Klein (QUICK)
- `/lens-focus-group` — focus group cognitivo con persona (DEEP)
- `/lens-steelman` — costruisci argomento piu' forte, poi stress-test (QUICK)
- `/lens-scenarios` — scenario planning 2x2 (DEEP)
- `/lens-assumptions` — scopri e inverti assunzioni nascoste (QUICK/DEEP)
- `/lens-deep` — chain sequenziale single-agent con vincoli progressivi (DEEP)

### 7.3 Flussi concreti

**Dati esterni → persona grounded (adapter Miner):**
Un sistema di audience research produce un `AudiencePersona` (demographics, psychographics/VALS, interests, behaviors, pain_points, goals) → `lens_persona_from_miner()` lo trasforma in un cognitive template Lens con questo mapping:
- demographics + occupation → role constraint
- psychographics.values + attitudes → modal constraint
- VALS segment → ELM route (central/peripheral processing)
- pain_points → psychology.fears
- goals → psychology.primary_goal
- decision_making_style → convincement_threshold

Le persona risultanti sono grounded su dati reali, non inventate dall'LLM. L'adapter è una pura trasformazione di dizionari (`integrations/miner.py`): funziona con qualunque input conforme allo schema `AudiencePersona`, indipendentemente dalla sua origine.

**Stress-test di un artefatto a valle:**
Prima di finalizzare una presentazione, una strategia o una scelta di prodotto, la passi attraverso 3-4 persona (es. cliente scettico, entusiasta, giornalista) e ottieni una Field Map con blind spot e punti deboli — oppure usi una topologia Adversarial+Jury per metterla sotto pressione.

**Lens come capability:**
Qualsiasi agente o workflow può invocare una prospettiva Lens su qualsiasi decisione: i tool MCP rendono Lens una capability componibile, non un'app a sé stante.

---

## 8. Protocollo di validazione

### 8.1 Test 1 — Circolarità (GATE-KEEPER)

**Ipotesi null:** le persona/vincoli Lens non producono insight semanticamente diversi rispetto a un LLM standard.

**Design:**
- Condizione A: prompt diretto (baseline)
- Condizione B: role prompting semplice
- Condizione C: vincoli strutturati Lens

**Criteri:**
- Successo: C genera ≥30% insight non presenti in A
- Confusion test cieco: il valutatore umano preferisce C in ≥60% dei casi
- Valutazione UMANA (non LLM su LLM)

Se Test 1 fallisce → il progetto va ripensato.

### 8.2 Test 2 — Topologie

Stesso problema, topologie diverse. Quale produce la Field Map più ricca?

### 8.3 Test 3 — Diminishing Returns

Focus group 2 → 3 → 4 → 5 → 6 agenti. Dove il margine di insight unici si appiattisce?

### 8.4 Test 4 — Grounded vs Synthetic Persona

Persona costruita da dati Miner vs persona inventata dall'LLM. Quale produce insight più actionable?

---

## 9. Casi d'uso primari

### 9.1 Stressare una decisione strategica
**Topologia:** Adversarial + Jury
**Esempio:** "Dovremmo lanciare il prodotto come freemium o enterprise-only?"
Due agenti con vincoli opposti dibattono, tre giurati con profili diversi valutano.

### 9.2 Pre-mortem su un progetto
**Topologia:** Star/Delphi
**Esempio:** "È il 2028, Lens è stato abbandonato. Perché?"
4-5 agenti con vincoli temporali e di ruolo diversi producono scenari di fallimento indipendenti.

### 9.3 Esplorare un problema da N dimensioni
**Topologia:** Parallel Hats
**Esempio:** "Analizza la proposta commerciale per il cliente X"
6 agenti, ognuno vincolato a una dimensione (fatti, rischi, opportunità, emozioni del cliente, idee creative, processo).

### 9.4 Trovare il nucleo solido di un argomento
**Topologia:** Cascade
**Esempio:** "Il nostro positioning è: 'AI infrastructure for creative agencies'"
L'argomento attraversa 4-5 round di attacco. Quello che sopravvive è il nucleo non-attaccabile.

### 9.5 Simulare la reazione di audience diverse
**Topologia:** Star/Delphi con persona Miner-grounded
**Esempio:** "Come reagiranno CTO PMI, marketing manager, e CEO a questa presentazione?"
Persona costruite da dati Miner reali, non inventate.

### 9.6 Generare insight non-lineari (Bisociazione)
**Topologia:** Ring + Bisociation Engine
**Esempio:** "Cosa succede se passiamo il concetto di 'brand loyalty' attraverso 4 frame semantici diversi?"
Ring con vincoli semantici: biologico → architetturale → musicale → militare. L'output finale è una prospettiva che nessun singolo frame avrebbe prodotto. Il moderatore identifica i punti di bisociazione — dove due matrici incompatibili producono un'idea nuova.

### 9.7 Scoprire assunzioni nascoste (Socratic Drill)
**Topologia:** Socratic Drill
**Esempio:** "Il nostro piano di go-to-market si basa su quali assunzioni non verificate?"
L'agente-Socrate interroga sistematicamente ogni elemento del piano. Output: mappa di N assunzioni con score di vulnerabilità e suggerimenti di test.

### 9.8 Esplorare futuri alternativi (Scenario Planning)
**Topologia:** Scenario Matrix
**Esempio:** "Il mercato AI per agenzie: 2 incertezze — adozione veloce vs lenta, AI commodity vs differenziata"
4 agenti esplorano i 4 quadranti. Output: 4 scenari con strategie specifiche + identificazione delle strategie robuste (valide in 3+ scenari).

### 9.9 Costruire l'argomento perfetto (Steelman + Adversarial)
**Topologia:** Steelman Chain
**Esempio:** "Perché un'azienda dovrebbe investire in questa piattaforma?"
3 round di steelmanning → versione più forte possibile → 2 round adversariali. Output: l'argomento nella sua forma più robusta + le uniche obiezioni sopravvissute.

### 9.10 Innovazione sistematica (Morphological + Constraint)
**Topologia:** Parallel Hats + Morphological
**Esempio:** "Quali nuove feature per il prodotto non abbiamo considerato?"
Scomponi il problema in dimensioni (input, elaborazione, output, formato, audience). Genera combinazioni con Zwicky box. Filtra con agenti vincolati (fattibilità, valore, costo). Output: matrice di combinazioni con scoring.

---

## 10. Piano progettuale

### Fase 0 — MCP Server + Constraint Engine + Validazione (completata)
**Obiettivo:** dimostrare che i vincoli strutturali producono output genuinamente diverso.
**Deliverable:**
- [x] MCP server FastMCP con tool core (server.py)
- [x] Constraint Composer (constraints/composer.py)
- [x] 25 constraint templates in library.json (7 categorie)
- [x] 5 cognitive templates (personas/templates/)
- [x] 13 topologie definite (topologies/definitions.json)
- [x] Output Formatter: Perspective Card, Field Map, Delta Report, Cascade Report
- [x] Skill `lens-perspective` (QUICK)
- [x] Skill `lens-adversarial` (QUICK)

### Fase 1 — Skill interattive + Baseline+Delta (completata)
**Obiettivo:** implementare skill DEEP mode e il workflow baseline+delta.
**Deliverable:**
- [x] Skill `/lens` interattiva (DEEP mode con scelta topologia)
- [x] Skill `/lens-focus-group` (DEEP mode con persona)
- [x] Skill `/lens-premortem` (QUICK mode, Klein)
- [x] Tool `lens_compose_baseline()` per workflow delta
- [x] Fix variable substitution nel Constraint Composer

### Fase 2 — Skill avanzate (completata)
**Obiettivo:** skill per le topologie piu' sofisticate.
**Deliverable:**
- [x] Skill `/lens-steelman` (QUICK mode, Steelman Chain)
- [x] Skill `/lens-scenarios` (DEEP mode, Scenario Matrix)
- [x] Skill `/lens-assumptions` (QUICK/DEEP mode, Socratic + Inversion)

### Fase 3 — Meta-Lens + Analytics (completata)
**Obiettivo:** il sistema impara da se stesso.
**Deliverable:**
- [x] Efficacy Tracker: constraint_efficacy(), topology_efficacy()
- [x] Pattern Mining: combinazioni di vincoli di successo (meta/analytics.py)
- [x] Combination Suggester data-driven (suggest_from_history())
- [x] 4 tool Meta-Lens nel MCP server
- [x] lens_suggest_constraints con fallback data-driven + euristica
- [x] Session save con constraints_used per tracking

### Fase 3b — Miner Integration + Documentazione (completata)
**Obiettivo:** integrazione con dati audience reali e documentazione completa.
**Deliverable:**
- [x] Modulo integrations/miner.py (transform, save, batch)
- [x] 2 tool MCP: lens_persona_from_miner, lens_personas_from_miner_batch
- [x] README.md completo
- [x] LENS.md aggiornato a stato implementato

### Fase futura — Evoluzione
**Potenziali sviluppi:**
- [ ] Adapter verso artefatti a valle (validazione di presentazioni, strategie, copy)
- [ ] Test 4 (grounded vs synthetic persona, post-adapter)
- [ ] Topologie aggiuntive come skill dedicate (ring, bisociation, scamper)
- [ ] Constraint Library espansa con vincoli domain-specific

---

## 11. Decisioni prese e domande risolte

1. **Backend o skill-only?** Risolto: MCP server FastMCP da Fase 0. Niente backend FastAPI separato. Il server MCP copre constraint library, composition, session management e analytics. Le skill restano leggere (solo orchestrazione).

2. **Quale modello per gli agenti?** Su Claude Max tutti i modelli sono inclusi. Le skill usano haiku per subagent veloci, sonnet per sintesi e moderazione, come specificato nei SKILL.md.

3. **Come gestire il costo?** Risolto: Claude Max = costo zero. Round paralleli dove possibile (Star, Parallel Hats).

4. **Meta-Lens: quanto e' realistico?** Implementato. Efficacy Tracker traccia per sessione. Pattern Mining trova combinazioni di successo. Suggest usa topic similarity + efficacy weighting con fallback euristico.

5. **Ring topology: rischio di drift?** Domanda aperta. La topologia ring e' definita ma non ha una skill dedicata. Il grounding check potrebbe essere implementato come vincolo aggiuntivo nel round finale.

### Domande ancora aperte

6. **Grounded vs synthetic persona:** il Test 4 (persona Miner vs persona inventata) non e' ancora stato eseguito. L'integrazione Miner e' implementata, serve validazione empirica.

7. **Diminishing returns:** quanti agenti servono davvero? La teoria suggerisce 4-5 ottimali (diversita' moderata, Aggarwal 2019). Serve test empirico su problemi reali.

---

## 12. Principi di design

### Principi fondamentali

1. **Il vincolo è il primitivo.** Tutto si costruisce sopra i vincoli. Le persona sono bundle di vincoli. Le topologie sono pattern di interazione tra agenti vincolati. (Stokes, TRIZ)

2. **Il ragionamento è sociale.** Un singolo agente è strutturalmente sub-ottimale. Il multi-agent approach non è un'ottimizzazione, è la modalità naturale del ragionamento. (Mercier & Sperber, 2011)

3. **Mappa, non risposta.** L'output di Lens non è "la risposta migliore". È una mappa del campo: convergenze, divergenze, outlier, tensioni, blind spot. (Delphi, ACH)

4. **Separare produzione da valutazione.** Chi genera prospettive non dovrebbe giudicarle. Chi giudica non dovrebbe aver generato. (CPS Osborn-Parnes)

5. **Indipendenza prima, interazione dopo.** Nel Round 1 gli agenti non vedono le posizioni degli altri. L'indipendenza nel primo round è la condizione necessaria per l'intelligenza collettiva. (Surowiecki)

6. **Dissenso strutturato, non caos.** Il conflitto è programmato, non casuale. Ogni agente ha un mandato preciso. (Janis)

7. **Diversità cognitiva moderata.** Non massimizzare la diversità, ottimizzarla. 4-5 stili cognitivi genuinamente diversi > 10 con differenze marginali. Relazione a U invertita. (Ashby, Aggarwal 2019)

8. **Separare divergenza e convergenza.** Fasi divergenti (generare) e convergenti (valutare) non si mescolano. Il giudizio prematuro uccide la creatività. (Osborn-Parnes CPS)

### Principi operativi

9. **Validare prima di costruire.** Nessuna infrastruttura senza evidenza empirica che il meccanismo base funziona.

10. **Auto-ottimizzazione.** Il sistema traccia la propria efficacia e suggerisce miglioramenti. (TRIZ principio #25: self-service)

11. **Correlazione degli errori come metrica.** Se tutti gli agenti sbagliano nello stesso modo, i vincoli non sono abbastanza diversi. (Ensemble theory — errori non correlati → superiorità dell'insieme)

12. **Trascendenza, non compromesso.** Quando emergono opposizioni, il sistema cerca framework che contengano entrambe le posizioni, non punti medi. (Rothenberg, Janusian Thinking)

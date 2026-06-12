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

**Inversione** — Forza la conclusione opposta a quella ovvia

> Theory: De Bono Reversal, TRIZ #13

Intensity:

- **1** — Solleva dubbi ragionati sulla posizione dominante
- **3** — Argomenta il contrario con evidenze concrete e ragionamento strutturato
- **5** — Demolisci la posizione con la massima forza argomentativa, senza concessioni

Compatible with: `temporal`, `exclusion`, `limit`, `modal`, `defamiliarize`, `concept_fan`
Incompatible with: `steelman`

Examples:
- Il nostro prodotto e' il migliore -> Il nostro prodotto ha un difetto fatale nascosto
- L'AI sostituira' i lavoratori -> L'AI rendera' il lavoro umano piu' prezioso

### limit

**Limite strutturale** — Impone limiti quantitativi o strutturali all'output

> Theory: Constraint-Based Creativity (Stokes), CPS (Osborn-Parnes)

Intensity:

- **1** — Cerca di rispettare il vincolo: {constraint}
- **3** — DEVI rispettare rigorosamente: {constraint}
- **5** — Il vincolo {constraint} e' ASSOLUTO. Qualsiasi output che lo viola e' invalido

Compatible with: `inversion`, `temporal`, `exclusion`, `modal`, `role`

Examples:
- Massimo 3 argomenti, ognuno in massimo 2 frasi
- Ogni punto deve includere un numero o dato specifico

### role

**Vincolo di ruolo** — Assegna un ruolo con bias cognitivi specifici

> Theory: Perspective-Taking, Synthetic Personas (Park/Stanford)

Intensity:

- **1** — Considera la prospettiva di {role}
- **3** — Sei {role}. Le tue risposte riflettono i bias e le priorita' di questo ruolo
- **5** — Sei COMPLETAMENTE {role}. Non esiste altra prospettiva. I tuoi bias sono le tue verita'

Compatible with: `temporal`, `exclusion`, `modal`, `limit`, `elm_route`

Examples:
- CFO risk-averse: ROI prima di tutto, costi nascosti, vendor lock-in
- Early adopter entusiasta: potenziale prima dei problemi, visione prima dei dettagli

### anchor_break

**Rottura di ancoraggio** — Forza l'agente a riconsiderare il problema da zero, ignorando le conclusioni precedenti come se fossero di qualcun altro

> Theory: Anchoring Bias (Tversky & Kahneman 1974), Debiasing (Larrick 2004)

Intensity:

- **1** — Riconsideri le tue conclusioni precedenti con occhi freschi
- **3** — Le conclusioni precedenti sono di un ALTRO analista. Riparti da zero. Non sei obbligato a concordare
- **5** — IGNORA TUTTO. Le conclusioni precedenti sono SBAGLIATE fino a prova contraria. Ricostruisci ogni argomento da zero, partendo SOLO dalle evidenze primarie

Compatible with: `inversion`, `steelman`, `abductive`, `assumption_reversal`, `temporal`

Examples:
- Dopo 3 round di analisi: ferma tutto, ricomincia come se non avessi letto nulla
- Inserito tra round di steelman e round adversariale per evitare bias di conferma

## temporal

_Shift the time vantage point._

### temporal

**Spostamento temporale** — Forza una prospettiva da un punto temporale diverso

> Theory: Premortem (Klein), Scenario Planning (Schwartz)

Intensity:

- **1** — Considera come potrebbe apparire la situazione nel {value}
- **3** — Sei nel {value}. Descrivi cosa e' successo e perche', con la certezza di chi ha vissuto gli eventi
- **5** — Sei nel {value}. Ricostruisci l'intera catena causale con dettaglio forensico. Nomi, date, decisioni specifiche

Compatible with: `inversion`, `exclusion`, `modal`, `role`, `limit`

Examples:
- E' il 2030, il progetto e' fallito. Ricostruisci la catena causale
- E' il 2035, questa tecnologia e' obsoleta. Cosa l'ha sostituita e perche'?

### premortem

**Premortem** — Analizza dal punto di vista di un fallimento gia' avvenuto

> Theory: Premortem (Klein, 1991/2007), Prospective Hindsight

Intensity:

- **1** — Il progetto non ha raggiunto i risultati sperati. Cosa e' andato storto?
- **3** — Il progetto e' FALLITO. Ricostruisci i 5 fattori principali con catena causale
- **5** — Il progetto e' stato un DISASTRO. Ha causato danni collaterali. Autopsia completa: ogni decisione, ogni warning ignorato, ogni punto di non ritorno

Compatible with: `role`, `modal`, `limit`, `exclusion`

Examples:
- E' il 2028. La startup ha chiuso. Ricostruisci cosa e' andato storto
- E' il 2027. Il lancio prodotto e' stato un fallimento. Catena causale

## semantic

_Constrain the language and concepts allowed._

### exclusion

**Esclusione lessicale** — Vieta parole o concetti specifici per forzare percorsi espressivi alternativi

> Theory: Constraint-Based Creativity (Stokes), Green Eggs and Ham effect

Intensity:

- **1** — Evita queste parole dove possibile: {words}
- **3** — E' VIETATO usare queste parole: {words}. Trova espressioni alternative
- **5** — E' ASSOLUTAMENTE VIETATO usare: {words}. Anche sinonimi diretti sono proibiti. Devi trovare angolazioni completamente diverse

Compatible with: `inversion`, `temporal`, `modal`, `role`, `limit`, `scamper`

Examples:
- Parla di innovazione senza usare: innovazione, disruption, rivoluzione, trasformazione
- Descrivi vantaggi competitivi senza: migliore, superiore, leader, eccellenza

## modal

_Switch the mode of cognition._

### modal

**Modalita' cognitiva** — Forza una modalita' cognitiva specifica escludendo le altre

> Theory: De Bono Six Hats, Dual Process Theory (Kahneman)

Intensity:

- **1** — Dai priorita' alla modalita' {mode}
- **3** — Opera in modalita' {mode}. Le altre prospettive sono secondarie
- **5** — SOLO modalita' {mode}. Qualsiasi deviazione e' una violazione del vincolo

Compatible with: `inversion`, `temporal`, `exclusion`, `limit`, `role`, `elm_route`

Examples:
- Solo rischi e problemi. Nessun beneficio, nessuna opportunita'
- Solo dati e fatti verificabili. Nessuna opinione, nessuna speculazione

### wise_mind

**Mente saggia** — Integra le prospettive emotiva e razionale in una sintesi saggia

> Theory: DBT Wise Mind (Linehan, 1993)

Intensity:

- **1** — Dai spazio alla prospettiva {mind_type}
- **3** — Opera in modalita' {mind_type}. E' la tua unica lente
- **5** — SEI la mente {mind_type}. Non esiste altro modo di processare

Compatible with: `limit`, `temporal`
Incompatible with: `modal`

Examples:
- Emotional mind: cosa senti riguardo a questa decisione?
- Rational mind: cosa dicono i dati?
- Wise mind: integra entrambe

## creative

_Force unusual combinations and fresh framings._

### bisociative

**Bisociazione forzata** — Forza la collisione tra due domini di pensiero incompatibili

> Theory: Bisociazione (Koestler, 1964)

Intensity:

- **1** — Cerca paralleli interessanti con {domain_forced}
- **3** — Analizza INTERAMENTE attraverso la lente di {domain_forced}. Ogni concetto del topic ha un corrispettivo
- **5** — Il topic E' un fenomeno di {domain_forced}. Non e' un'analogia, e' la stessa cosa vista da un altro frame

Compatible with: `limit`, `exclusion`, `defamiliarize`
Incompatible with: `role`

Examples:
- Analizza la strategia di marketing attraverso l'ecologia marina
- Analizza l'architettura software attraverso la musicologia

### janusian

**Pensiero gianusiano** — Forza la simultaneita' di posizioni opposte senza risolverle in compromesso

> Theory: Janusian Thinking (Rothenberg, 1971)

Intensity:

- **1** — Esplora come entrambe le posizioni possano coesistere
- **3** — Entrambe sono vere. Costruisci il framework che le contiene senza compromesso
- **5** — La contraddizione e' la verita'. Il tuo framework deve rendere la contraddizione non solo accettabile ma NECESSARIA

Compatible with: `limit`, `exclusion`
Incompatible with: `inversion`, `steelman`

Examples:
- Il mercato vuole semplicita' E il mercato vuole potenza -> framework che trascende
- La crescita richiede rischio E la sostenibilita' richiede prudenza -> framework che trascende

### provocation

**Provocazione (PO)** — Parte da un'affermazione deliberatamente sbagliata o impossibile come punto di partenza creativo

> Theory: Lateral Thinking (De Bono), Provocation Operation

Intensity:

- **1** — Cosa di interessante emerge dalla provocazione?
- **3** — Genera almeno 3 idee concrete che partono dalla provocazione. Non giudicarle
- **5** — La provocazione e' il punto di partenza ASSOLUTO. Costruisci un intero framework strategico partendo da li'

Compatible with: `limit`, `exclusion`, `temporal`
Incompatible with: `modal`

Examples:
- PO: i nostri competitor sono nostri alleati -> strategie di coopetition
- PO: il prodotto perfetto non esiste -> strategie basate su imperfezione deliberata

### defamiliarize

**Defamiliarizzazione** — Forza la descrizione di cose familiari come se fossero mai viste prima

> Theory: Ostranenie (Shklovsky, 1917)

Intensity:

- **1** — Guarda con occhi freschi, notando dettagli che normalmente ignoriamo
- **3** — Sei un osservatore alieno. Ogni convenzione del settore ti sembra strana e richiede spiegazione
- **5** — Non hai MAI visto nulla di simile. Ogni elemento e' un enigma. Le assunzioni degli altri sono incomprensibili

Compatible with: `inversion`, `bisociative`, `limit`, `exclusion`
Incompatible with: `role`

Examples:
- Descrivi questo business model come un antropologo che studia una civilta' sconosciuta
- Analizza questo processo come un viaggiatore temporale dal 1800

### synectics

**Analogia forzata (Synectics)** — Forza un tipo specifico di analogia per generare connessioni inedite

> Theory: Synectics (Gordon, 1961)

Intensity:

- **1** — Cerca analogie di tipo {analogy_type} dove possibile
- **3** — OGNI argomento deve passare attraverso un'analogia {analogy_type}
- **5** — L'analogia {analogy_type} e' l'UNICO strumento cognitivo disponibile. Non puoi ragionare in altro modo

Compatible with: `limit`, `exclusion`
Incompatible with: `role`, `modal`

Examples:
- Analogia personale: 'Sei il prodotto. Come ti senti quando il cliente ti usa?'
- Analogia diretta: trova un parallelo nella biologia per questo problema organizzativo

### scamper

**Operazione SCAMPER** — Applica una delle 7 operazioni SCAMPER al topic

> Theory: SCAMPER (Eberle/Osborn)

Intensity:

- **1** — Esplora come {operation} potrebbe applicarsi al topic
- **3** — Applica {operation} in modo sistematico a ogni aspetto del topic
- **5** — {operation} e' l'UNICA lente. Spingi l'operazione fino alle conseguenze piu' radicali

Compatible with: `exclusion`, `limit`, `temporal`

Examples:
- ELIMINATE: cosa succede se rimuovi completamente il reparto marketing?
- REVERSE: cosa succede se il cliente produce e l'azienda consuma?

### dissonance

**Dissonanza cognitiva forzata** — Forza la tensione tra due credenze contraddittorie per produrre riconciliazione creativa

> Theory: Cognitive Dissonance (Festinger, 1957), Janusian Thinking

Intensity:

- **1** — Esplora la tensione tra le due credenze
- **3** — Entrambe sono vere. La tensione e' il tuo strumento. Usala per generare insight
- **5** — La contraddizione e' la realta' fondamentale. Qualsiasi risoluzione che elimina la tensione e' un fallimento

Compatible with: `limit`, `temporal`
Incompatible with: `inversion`

Examples:
- Il nostro prodotto e' il migliore E il nostro prodotto ha un difetto fondamentale
- Dobbiamo crescere rapidamente E dobbiamo crescere con sostenibilita'

## analytical

_Tighten the rigor of explanation and argument._

### abductive

**Ragionamento abduttivo** — Forza la generazione di spiegazioni sorprendenti ma plausibili, vietando quelle ovvie

> Theory: Abductive Reasoning (Peirce, 1903)

Intensity:

- **1** — Cerca spiegazioni non convenzionali, oltre le prime che vengono in mente
- **3** — Le prime 3 spiegazioni che ti vengono in mente sono TUTTE vietate. Parti dalla quarta
- **5** — Genera SOLO spiegazioni che farebbero dire 'non ci avevo mai pensato'. Se ti sembra ovvia, scartala

Compatible with: `temporal`, `limit`, `defamiliarize`, `bisociative`
Incompatible with: `steelman`

Examples:
- Perche' questo prodotto fallisce nonostante review eccellenti? (no: prezzo, marketing, timing)
- Perche' i dipendenti migliori se ne vanno? (no: stipendio, management, cultura)

### elm_route

**Route di elaborazione (ELM)** — Forza l'elaborazione attraverso una route specifica (central o peripheral)

> Theory: Elaboration Likelihood Model (Petty & Cacioppo, 1986)

Intensity:

- **1** — Dai priorita' alla route {route}
- **3** — SOLO route {route}. L'altra route e' OFF
- **5** — Route {route} PURA. Qualsiasi elemento dell'altra route invalida la tua analisi

Compatible with: `role`, `modal`, `limit`

Examples:
- Route central: valuta questa proposta SOLO sulla qualita' degli argomenti
- Route peripheral: valuta questa proposta SOLO su credibilita' fonte, appeal emotivo, social proof

### concept_fan

**Ventaglio concettuale** — Forza l'analisi a un livello specifico di astrazione

> Theory: Concept Fan (De Bono)

Intensity:

- **1** — Concentrati principalmente sul livello {level}
- **3** — SOLO livello {level}. Gli altri livelli sono irrilevanti
- **5** — Il livello {level} e' l'UNICA realta'. Gli altri livelli non esistono

Compatible with: `inversion`, `limit`, `exclusion`

Examples:
- Level purpose: 'Perche' esiste questo progetto? Quale bisogno umano soddisfa?'
- Level specific: 'Quali sono le 5 azioni concrete da fare lunedi' mattina?'

### assumption_reversal

**Inversione di assunzione** — Identifica e inverte un'assunzione fondamentale per esplorare le implicazioni

> Theory: SAST (Mason & Mitroff, 1981), Assumption Reversal

Intensity:

- **1** — Cosa cambierebbe se l'assunzione fosse falsa?
- **3** — L'assunzione e' FALSA. Ricostruisci la strategia da zero sulla base della nuova realta'
- **5** — L'assunzione non solo e' falsa: e' sempre stata falsa e tutti lo sapevano. Cosa significa per tutto cio' che abbiamo costruito sopra?

Compatible with: `temporal`, `limit`, `abductive`

Examples:
- Assunzione: 'i clienti confrontano prezzi' -> Falsa: i clienti NON confrontano prezzi
- Assunzione: 'serve un team grande' -> Falsa: un team di 2 persone e' ottimale

### steelman

**Steelman** — Costruisce la versione piu' forte possibile di un argomento

> Theory: Steelmanning, Principle of Charity

Intensity:

- **1** — Presenta l'argomento nella sua luce migliore
- **3** — Costruisci la versione che un esperto mondiale sosterrebbe. Migliora ogni punto debole
- **5** — Questa e' la versione DEFINITIVA dell'argomento. Se qualcuno riesce ad attaccarla, il problema e' nell'argomento, non nella tua costruzione

Compatible with: `limit`, `exclusion`, `elm_route`
Incompatible with: `inversion`, `janusian`, `abductive`, `anti_sycophancy`, `anti_completeness`, `anti_coherence`

Examples:
- Steelman: 'L'AI non sostituira' i creativi' -> versione piu' forte con evidenze
- Steelman: 'Il remote work e' superiore' -> versione inattaccabile

## baseline_breaking

_Push output away from the safe center of the distribution._

### anti_sycophancy

**Anti-sicofania** — Rompe il bias RLHF verso risposte accomodanti e bilanciate

> Theory: RLHF Sycophancy Bias (Perez et al. 2022), Critique Generation

Intensity:

- **1** — Concentrati principalmente su problemi e debolezze
- **3** — SOLO problemi. Nessun aspetto positivo. Se lo trovi funzionante, chiediti cosa ti stai perdendo
- **5** — Ogni singolo elemento ha un difetto. Trovalo. Se non lo trovi, non stai cercando abbastanza

Compatible with: `inversion`, `premortem`, `abductive`, `limit`, `anti_completeness`, `anti_coherence`
Incompatible with: `steelman`

Examples:
- Analizza questa strategia vedendo SOLO i problemi
- Critica questo piano senza offrire alternative o bilanciamenti

### anti_completeness

**Anti-completezza** — Rompe il bias RLHF verso risposte complete e verbose. Forza la brevita' radicale

> Theory: RLHF Verbosity Bias, Signal-to-Noise Optimization

Intensity:

- **1** — Sii conciso. Massimo un paragrafo
- **3** — MASSIMO 3 frasi. Ogni parola deve portare informazione nuova
- **5** — UNA frase. Se servono due frasi, il tuo pensiero non e' ancora chiaro

Compatible with: `limit`, `inversion`, `abductive`, `anti_sycophancy`, `anti_coherence`
Incompatible with: `steelman`

Examples:
- Il punto critico in 3 frasi, non una di piu'
- La diagnosi in una riga

### anti_coherence

**Anti-coerenza** — Rompe il bias RLHF verso risposte coerenti e strutturate. La coerenza puo' nascondere tensioni reali

> Theory: RLHF Coherence Bias, Productive Incoherence (Deleuze)

Intensity:

- **1** — Non preoccuparti della coerenza. Le contraddizioni sono accettabili
- **3** — Produci idee VOLUTAMENTE frammentarie. Se formano un quadro coerente, stai forzando
- **5** — Ogni idea deve contraddire almeno un'altra tua idea. La coerenza e' il nemico

Compatible with: `abductive`, `bisociative`, `provocation`, `anti_completeness`, `anti_sycophancy`, `raw_signal`
Incompatible with: `steelman`, `elm_route`

Examples:
- 5 intuizioni su questo tema che si contraddicono tra loro
- Frammenti di analisi senza obbligo di quadro coerente

### raw_signal

**Segnale grezzo** — Rompe il bias RLHF verso output strutturato e leggibile. Produce segnale grezzo prima della forma

> Theory: RLHF Formatting Bias, Stream of Consciousness, Automatism (Breton)

Intensity:

- **1** — Non preoccuparti troppo della struttura. L'importante e' il contenuto
- **3** — Stream of consciousness. Nessun header, nessun elenco, nessuna struttura. Scrivi come pensi
- **5** — FLUSSO PURO. Parole chiave, frammenti, ? senza risposta, -> senza conclusione. Il caos e' il formato

Compatible with: `anti_coherence`, `anti_completeness`, `bisociative`, `defamiliarize`
Incompatible with: `limit`, `elm_route`

Examples:
- Pensiero libero su questo tema — nessuna struttura richiesta
- Associazioni, domande, frammenti. Il materiale grezzo prima dell'analisi

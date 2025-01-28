Ohne Improvements:

    - Senti4SD: 
        - F1: 0.45 (macro), 0.45 (weighted)
    - EASTER
        - F1 0.48 (macro), 0.51 (weighted)
    - ChatGPT
        - F1 0.38 (macro), 0.36 (weighted)

1. Shorter than 50 words

src\Improvement_Ideas\less_than_x_words.py
Alle Kommentare die weniger als 50 Worte haben habe ich entfernt.
-> 45 Kommentare übrig


    - Senti4SD: 
        - F1: 0.27 (macro), 0.33 (weighted)
    - EASTER
        - F1 0.57 (macro), \textbf{0.63} (weighted)
    - ChatGPT
        - F1 0.38 (macro), 0.36 (weighted)



2. Only sentences with "Microservices"

    - Senti4SD: 
        - F1: 0.26 (macro), 0.26 (weighted)
    - EASTER
        - F1 0.49 (macro), 0.51 (weighted)
    - ChatGPT
        - F1 0.42 (macro), 0.41 (weighted)


3. ChatGPT Compression

Vorgehensweise siehe chatGPT_summup_prompts.txt

    - Senti4SD: 
        - F1: 0.33 (macro), 0.34 (weighted)
    - EASTER
        - F1 0.26 (macro), 0.25 (weighted)
    - ChatGPT
        - F1 0.37 (macro), 0.38 (weighted)


Schlüsse:

- Baseline: EASTER performt am besten, ChatGPT am schwächsten.
- <50 Worte entfernt: EASTER verbessert sich stark, Senti4SD bricht ein.
- „Microservices“: ChatGPT leicht besser, EASTER und Senti4SD schlechter.
- ChatGPT-Kompression: Senti4SD leicht besser, EASTER deutlich schlechter, ChatGPT konstant.


--> mit EASTER probieren welche Wortlänge welche Ergebnisse erzielt

--> dann mit der guten Wortlänge wieder auf 100 Posts auffüllen


Phase 2:
Wortlänge mit EASTER varieren


25 Words max
 - F1 0.43 (macro), 0.57 (weighted)
 17 Posts
 schlecht weil die Stichprobe zu klein ist
 sagt meistens 0

50 Words max
 - F1 0.57 (macro), 0.63 (weighted)

 100 Words max
 - F1 0.50 (macro), 0.52 (weighted)
 73 Posts

Phase 3:
Manuell auf 100 Posts mit 50 Wörtern auffüllen

 - F1 0.57 (macro), 0.61 (weighted)

Phase 4:

Die positiven Sentiments von ChatGPT übernehmen und dann den Rest nochmal mit EASTER

F1: 0.44


ChatGPT different prompts:
macro avg - Precision: 0.48, Recall: 0.39, F1-Score: 0.35
weighted avg - Precision: 0.51, Recall: 0.42, F1-Score: 0.36


Phase 5:

Kombination aus ChatGPT mit Microservice Sätzen only für positive Sentences
 & EASTER shorter than 50 words für den Rest

 wenn ChatGPT 1 sagt -> ChatGPT glauben

 sonst EASTER glauben
 
 Statistical Metrics:
-1 - Precision: 0.91, Recall: 0.24, F1-Score: 0.38
0 - Precision: 0.77, Recall: 0.93, F1-Score: 0.84
1 - Precision: 0.41, Recall: 0.89, F1-Score: 0.57
macro avg - Precision: 0.70, Recall: 0.69, F1-Score: 0.60
weighted avg - Precision: 0.76, Recall: 0.64, F1-Score: 0.60

besser bei 1, schlechter bei -1

----
wenn EASTER sagt -1 EASTER glauben
else if ChatGPT sagt 1
    ChatGPT glauben
else EASTER glauben

--
if_else
wenn EASTER sagt 1 oder 0 && ChatGPT sagt 1 -> 1
else: das was EASTER sagt.

-- 
if_else 2
wenn easter -1 -> -1
wenn EASTER sagt 1 oder 0 && ChatGPT sagt 1 -> 1
else: das was EASTER sagt.

Kombination aus Senti & EASTER & ChatGPT
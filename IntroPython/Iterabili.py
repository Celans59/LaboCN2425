
# Come visto in ASD, liste e tuple sono ITERABILI
# Un ITERABILE è definito come una variabile composta da "parti più piccole" alle quali è possibile accedervi singolarmente.
# Altri esempi di ITERABILI, oltre a liste e tuple sono: Stringhe, Generatori, Dizionari e Insiemi!

# Alcune delle operazioni che abbiamo visto con liste e tuple sono, in realtà, operazioni su iterabili
# non tutti gli iterabili condivisono le stesse operazioni; alcuni di essi hanno vincoli speciali che non permette ciò

# Ad esempio, lo slicing è applicabile anche alle stringhe
s1: str = "Pippo"
print(s1[2])    # Stampa il secondo carattere della stringa
print(s1[::-1]) # Stampiamo la stringa al contrario
print(len(s1), end="\n\n")  # Stampiamo il numero di caratteri di s1


# DIZIONARI
# Utili per organizzare dati complessi e lavorare con grandi quantità di informazioni in modo efficiente
# Un DIZIONARIO è una tipologia di array i cui valori sono indicizzati da array, invece dalla posizione dell'elemento nell'array
# La stringa che indicizza un valore è detta CHIAVE
# I dizionari sono mutabili, quindi è possibile modificare, aggiungere o eliminare elementi dopo la loro creazione
# Per definire un dizionario si utilizzano le { } all'interno delle quali vengono scritte le loro chiavi
# che vengono associate al rispettivo valore tramite i :
emptyDictionary = { }
studente = {
    "Nome" :  "Andrea",
    "Eta" :   23,
    "Corso" : "Calcolo Numerico",
}
print(studente)
# Posiamo accedere ai suoi singoli elementi utilizzando operazioni già viste...
print(studente["Nome"])
# E possiamo modificarne i valori
studente["Eta"] = 24
print(studente)
# Per aggiungere una chiave basta semplicemente...
studente["Voto"] = 30
print(studente, end="\n\n")

# Tramite determinate operazioni possiamo avere la classe delle chiavi o la classe dei valori o la classe delle coppie chiave-valore
print(studente.keys())      # Stampa tutte le chiavi
print(studente.values())    # Stampa tutti i valori associati alle chiavi
print(studente.items(), end="\n\n") # Stampa tutte le coppie chiavi-valore

# é ovviamente possibile annidare vocabolari dentro un altro vocabolario, per un'organizzazinoe dati ancora più massiccia
classe = {
    "studente1": {
        "Nome" : "Raffaele",
        "Eta" :  "22",
        "Voto" :  25,
    },

    "studente2": {
        "Nome" : "Loris",
        "Eta" :  "23",
        "Voto":   25,
    } 
}
print(classe)



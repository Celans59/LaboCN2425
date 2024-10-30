
'''
Parliamo di PATH RELATIVO e ASSOLUTO e WORKING DIRECTORY
i path sono delle stringhe che indicano l'indirizzo di un file o di una directory all'interno di un computer.
PATH ASSOLUTO: specifica l'intero percorso a partire dalla directory radice.
PATH RELATIVO: specifica il percorso a partire dalla directory corrente in cui ci troviamo.
Directory corrente = working directory. è la directory in cui il programma Python, ovvero la radice del progetto, sta lavorando
è importnte che TUTTI i percorsi dei file (lettura/scrittura), devono essere dati rispetto alla working directory.

Quando si tratta di gestione del path ci sono due librerie built-in molto importanti: OS e GLOB
'''
import os

print(os.getcwd(), end="\n\n") # Visualizza la directory di lavoro corrente

# Posso anche modificare direttamente da codice la directory di lavoro
# os.chdir("/Users/utente/Desktop") --> in questo modo 

'''
La libreria os ha altre funzioni per gestire i path, com:
-> os.path.join(path1, path2, ...) che prende in input una serie di stringhe e ritorna in output il path ottenuto 
    concatenando le stringhe, inserendo automaticamente il separatore corretto in base al sistema operativo.
-> os.listdir(path) dato un path in input, ritorna l’elenco di tutti i files e le directory contenuti in esso, 
    nella forma di una lista.
-> os.path.exists(path) dato un path in input, ritorna True se tale path esiste, False altrimenti.
-> os.makedirs(path, exists_ok=True) preso in input un path, non fa niente se il path richiesto esiste. 
    Crea invece tutte le cartelle necessarie per costruirlo, se tale path non esiste.
'''
data_path = "./data"       # Consideriamo una cartella "data"
file_name = "esempio.txt"  # e supponiamo di avere al suo interno un file "esempio.txt"
path_file = os.path.join(data_path, file_name) # Costruiamo il percorso per il file
print(path_file)

if os.path.exists(data_path):               # Verifica se il path per il file esiste
    os.makedirs(data_path, exist_ok=True)   # altrimenti lo costruiamo!
print(os.path.exists(data_path), end="\n\n") # Vediamo se ora esiste


# La libreria GLOB ha funzionalità simili a quelle di os, ma viene utilizzata principalmente perchè permette
# di selezionare files all'interno di un percorso, filtrandoli rispetto ad alcune proprietà
import glob

data_path = "./data"
file_txt = glob.glob(os.path.join(data_path, "*.txt"))  # Cerca tutti i file.txt nella directory ./data
print(file_txt)

file_python = glob.glob(os.path.join(data_path, "**", "*.txt"), recursive=True) # Oppure in tutte le sue sub-directory
print(file_python)


# I risultati prodotti da script Python spariscono non appena il programma termina!
# Per mantenere salvate delle informazioni (o per leggerne precedentemente salvate), è necessario utilizzare files.

# Ci sono tre diversi standard in Python in cui questa cosa viene fatta, che dipende dal tipo di informazione
# che si vuole memorizzare / leggere:
# file.txt
# file.json
# tramite la libreria pickle

# FILE.TXT
# Usati quando si vogliono salvare informazioni di tipo testuale / numerico. In maniera rapida e non strutturata.
# Per fare ciò è necessario aprire il file tramite la funzione open() e inserirci i valori desiderati all'interno.
# import os
s = "Creiamo una stringa da salvare!"
path = os.path.join("logs", "nome_file.txt") # Definiamo il path
os.makedirs("logs", exist_ok = True)

with open(path, mode = "w") as f:   # All'interno del "with" posso lavorare sul file, chiamato "f"
    f.write(s)
# Fuori dal "with", il file è stato chiuso

'''
Analizziamo il codice:
Come prima cosa abbiamo fatto abbiamo aperto il file con la funzione open()
    che prende in input due argomenti: il path per il file (abbiamo scritto solo il nome del file perchè vogliamo salvarlo
    nella working directory, avremmo inserito il percorso relativo se avessimo voluto salvarlo in una directory specifica)
    e la modalità di apertura.
Ricordiamo le più comunemente utilizzate:
    "w": sola scrittura --> il file viene sovrascritto ogni volta;
    "a": sola scrittura --> il contenuto viene aggiunto al file, senza sovrascrizione;
    "r": sola lettura.
La funzione open è stata inserita all’interno del comando with, che ha lo scopo di tenere aperto il file, solo all’interno del suo corpo. 
    La variabile associata al file verrà chiusa ed eliminata subito dopo.
Nella stessa linea del comando with, abbiamo assegnato al file il nome di una variabile (in questo caso f), 
    che abbiamo poi utilizzato per scrivere al suo interno tramite la funzione f.write().
'''

# Per leggere il contenuto del file è speculare, utilizzando il metodo .read() e assegnandolo ad una stringa.
with open(path, "r") as f:  # Andiamo a leggere il contenuto del file appena creato
    s = f.read()
print(s)


#FILE.JSON
# vengono utilizzati principalmente per salvare informazioni strutturate, come ad esempio dei dizionari,
# con lo scopo di salvarsi dei dati di configurazione.
# Per gestire files .json, è necessario importare la libreria built-in json.
import json
#import os

config = {    # Generiamo un dizionario di esempio
    "nome_algoritmo": "MetodoDiscesa",
    "parametro1": 10,
    "parametro2": 0.01,
}
path = os.path.join("logs", "config.json")  # Definiamo il path (come prima)
with open(path, "w") as f:  # Apriamo un file json in lettura
    json.dump(config, f)

# Similmente possiamo leggere i file".json", convertendoli in dizionari
#import json
#import os

path = os.path.join("logs", "config.json")  # Definiamo il path (come prima)
with open(path, "r") as f:  # Apriamo un file json in lettura
    config = json.load(f)
print(config)


# LIBRERIA PICKLE
# Questo è sicuramente il formato più utilizzato per memorizzare informazioni di output da Python.
# Il suo nome deriva dalla libreria built-in pickle, che fornisce le funzionalità necessarie al suo utilizzo.
# Il vantaggio di pickle è che permette di leggere/scrivere su file ogni oggetto Python, 
# che verrà memorizzato nella forma in cui è, e ricaricato nello stesso modo.
# La sintassi è praticamente la stessa di prima:
import pickle

a = [1, 3, ("c", "i", "a", "o")]    # Definiamo un qualunque oggetto Python (ad esempio, una lista)
path = os.path.join("logs", "file.pickle")  # Definiamo il path

with open(path, "wb") as f: # Salviamo con Pickle
    pickle.dump(a, f)

with open(path, "rb") as f: # Leggiamo il file pickle
    b = pickle.load(f)
print(b)

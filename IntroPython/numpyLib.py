
# NLA o Numerical Linear Algebra è la materia che si occupa di studiare come le operazioni tra matrici e vettori
# possano essere utilizzate all'interno di algoritmi con lo scopo di produrre risposte efficienti e accurate

# è necessario implementare in maniera efficiente operazioni matriciali e vettoriali.
# Nel seguito indicheremo con le maiuscole (A, B, C, ...) le matrici e con le minuscole i vettori.

# Per lavorare con matrici e vettori utilizzeremo la libreria NUMPY.
# in collaborazione con essa utilizzeremo le librerie SCIPY e MATPLOTLIB.


'''
LA LIBRERIA NUMPY
implementa un tipo di dato che estende i classici array, pensato specificatamente per massimizzare l'efficienza di operazioni
di algebra lineare (come la somma elemento per elemento o prodotto riga per colonna, ...), e sono chiamati NDARRAY.
Tramite essi è possibile inizializzare facilmente vettori, metrici, tensori, ..., mantenendo le funzionalità di base degli array
Il loro unico limite è che possono contenere solo numeri.
Il metodo classico per la creazione di un ndarray è quello di castarlo da un’array classico di Python.
Vediamo come creare un vettore...
'''
import numpy as np # se salvo il file numpy.py ci sarà collisione nell'importazione e python importerà il file stesso!! Errore 

a: list[int] = [1, 2, 3]
v: np.ndarray = np.array(a)
print(v)
print(type(v))
print(a)
print(type(a), end="\n\n")

'''
Con la proprietà SHAPE possiamo conoscere la dimesione degli ndarray. Più precisamente:
un VETTORE avrà come shape una tupla contenente un solo numero: la sua lunghezza
una MATRICE avrà come shape una tupla contente due numeri: il numero di righe e colonne.
Per inizializzare una matrice a partire da un'array Python è necessario costruiore un array contenente
altri array: ciascuno dei quali rappresenta una riga della matrice.
'''
w = np.array([1.5, 1, 3, 2])   # vettore w
A = np.array([[1, 1, -1],   # matrice A
              [0, -1, 1]])

print(A)
print(f"La shape di A é: {A.shape}")
print(type(A))
print(w)
print(type(w))
print(f"La shape di w é: {w.shape}\n")

# Un'altra proprietà importante è DTYPE che ci restituisce i tipi differenti di aritmetica floating point per i propri array
# che possono esserea singola precisione(np.float32), doppia(np.float64) o mezza(np.float16).
# Se non diversamente specificato il valore di default assunto è dtype = np.float64 per floating point, np.int64 altrimenti.
print(v.dtype)
print(w.dtype)
x = np.array([1, 4, -2], dtype = np.float32)
print(x.dtype, end="\n\n")

'''
Si può cadere nel problema di dover maneggiare matrici e vettori di dimensioni enormi, ciò non è possibile 
come visto precedentemente. Fortunatamente quando gli array che si vogliono generare hanno dei PATTERN specifici
è possibile inizializzarli tramite una serie di funzioni:

-> np.linspace(a, b, n): Crea un vettore di lunghezza n, con n elementi uniformemente distributi nel’intervallo [a, b] 
    con estremi inclusi.
-> np.arange(inizio, fine, passo): Simile alla funzione Python range. Crea un vettore che contiene tutti i numeri interi 
    a partire da inizio, fino a fine-1, con passo fissato.
-> np.zeros((m, n)): Crea una matrice di dimensione (m, n) di zeri. Chiaramente, per creare un vettore invece 
    che una matrice, si utilizza la funzione np.zeros((m, )).
-> np.ones((m, n)): Come prima, ma crea una matrice (o vettore) di 1.
-> np.zeros_like(a): Crea una matrice o un vettore, della stessa dimensione di un altro array a. 
    è equivalente a np.zeros(a.shape). Esiste l’equivalente np.ones_like(a).
-> np.diag(v): Dato un vettore v di lunghezza n, costruisce una matrice diagonale di dimensione (n, n), la cui diagonale è v.
-> np.random.randn(m, n): Crea una matrice di dimensione (m, n) di numeri casuali distribuiti con distribuzione normale standard.
-> np.random.rand(m, n): Uguale a prima, ma con valori estratti da una distribuzione uniforme nel dominio. 
'''
y = np.random.rand(10)  # Vettore di valori casuali in [0, 1] di shape = 10
print(y, end="\n\n")


# Ora, come li utilizziamo? Vediamo le classiche operazioni svolte elemento per elemento
c = np.array([1, -1, 0])
e = np.linspace(1, 3, 3) # Array (1, 2, 3)

# Eseguiamo operazioni semplici matematiche tra di loro e vediamo la semplicita della cosa!
s = c + e
d = c - e
p = c * e
f = c / e
print(f"c = {c},d = {e}\nSomma = {s}\nDifferenza = {d}\nProdotto = {p}\nDivisione = {f}\n")

x = np.linspace(0, 2 * np.pi, 4)
print(f"L'array x = {x}")
# Calcoliamo i valori trigonometrici
print(f"sin(x) = {np.sin(x)}")
print(f"cos(x) = {np.cos(x)}")
print(f"tan(x) = {np.tan(x)}")
# Calcoliamo esponensiale e logaritmico
print(f"e^x = {np.exp(x)}")
print(f"ln(x) = {np.log(x + 1)}")
print(f"log_10(x) = {np.log10(x + 1)}\n")

'''
Passiamo ad analizzare l'operazione riga per colonna tra matrici e vettori (o anche detto prodotto scalare)
Questa operazione è implementata su numpy tramite l'operatore "@" o, equivalmente, tramite la funzione np.dot(A, x)
'''
B = np.array([[1, 1, 1], [0, -1, 0], [0, 0, 1]]) # Definiamo una matrice B
z = np.array([1, 0, 1])

pr = B @ z   # Prodotto riga per colonna!
print(pr, end="\n\n")

'''
E per quanto riguarda i vettori? Bisogna fare una distinsione tra i tipi di vettori:
-> vettore classico a dimensione singola, la cui shape sarà uguale a qualcosa tipo (n, ) (come già visto prima)
-> vettore colonna, come se fosse una matrice ad una sola colonna e numero di righe pari alla sua lunghezza.
'''




























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
-> vettore colonna, come se fosse una matrice ad una sola colonna e numero di righe pari alla sua lunghezza. shape(n, 1)
-> vettore riga, come se fosse una matrice ad una sola riga e numero di colonne pari alla sua lunchezza. shape(1, n)
Occhio a questa distinsione!! Alcune funzionalità di numpy lavorano diversamente rispetto alla natura del vettore!!
Ad esempio, l’operatore "@" restituirà il prodotto scalare standard tra vettori nel caso in cui i due elementi moltiplicati
siano due vettori classici, restituirà errore nel caso in cui siano due vettori colonna,
e darà il prodotto scalare standard se i vettori saranno il primo un vettore riga, il secondo un vettore colonna.
'''
# Definiamo due vettori classici
m = np.array([1, -1, 1])
n = np.array([0, 1, 1])
print(m.shape, n.shape) # Controlliamo che siano vettori classici
# Calcoliamone il prodotto scalare
print(m @ n)
# Definiamo la loro versione come vettori colonna
m = np.array([[1], [-1], [1]])
n = np.array([[0], [1], [1]])
print(m.shape, n.shape, end="\n\n")
# Calcoliamone il prodotto scalare
# print(m @ n) --> Errore


# è possibile definire degli ndarray che contengono valori booleani (0 per il False e 1 per il True)
# Molto utili per svolgere in maniera efficiente operazioni di filtraggio di contenuti
# Sarà, quindi, possibile eseguire operazioni booleane classiche (AND, OR e NOT) e di confronto (=, !=, ...) 
# tra ndarray booleani, che verranno applicate elemento per elemento

# Definiamo 3 vettori casuali
h = np.random.rand(10)
j = np.random.rand(10)
k = np.random.rand(10)
# Generiamo il vettore booleano 'l' che segue l'operazione booleana >=
l = h >= j
print(l)
# ed il vettore 'o' che segue la stessa logica di prima
o = j >= k
print(o)
# Ed ora li uniamo con un'operazione '&' elemento per elemento!!
print(l & o, end="\n\n")


# SLICING su ndarray
# Su vettori classici funziona esattamente come per liste e tuple, la cui notazione v[inizio:fine] restituisce 
# gli elementi di v da inizio a fine - 1.
aa = np.array([0, 1, -1, 2, 1, -1])
ww = aa[0:3]
print(ww, end="\n\n")

'''
Il vero vantaggio degli ndarray, rispetto a liste e tuple, è la possibilità di utilizzare gli ndarray booleani
per filtrare gli elementi di un altro ndarray. 
Infatti, se all’interno delle parentesi quadre inseriamo un array booleano della stessa dimensione dell’array 
su cui stiamo facendo slicing, questo ci ritornerà tutti gli elementi dell’array che corrispondono alle posizioni dei True.
'''
jj = np.array([0, 1, -1, 2, 1, -1]) # Array di esempio
print(jj)

bb = np.array([True, True, False, True, False, False])  # Vettore booleano
print(bb)

print(jj[bb], end="\n\n") # Slicing

# Questo ci permette di eseguire in maniera estramamente rapida e in un linguaggio molto vicino a quello naturale, 
# operazioni condizionali su vettori.
# Vediamo ad esempio come prendere un vettore casuale, e porre a 0 tutti i suoi valori negativi 
# (operazione, nota come proiezione sull’asse positivo, molto comune in alcuni problemi di algebra lineare).
xx = np.random.randn(8) # cond randN generiamo anche valori negativi!
print(xx)
# Proiettiamo sull'asse positivo!!
xx[xx < 0] = 0
print(xx, end="\n\n")


# SLICING SU MATRICI
# Lo slicing sulle matrici prevede l'inserimento, tra le [ ], di due indici (della forma inizio:fine:step):
# uno per gli indici di riga ed uno per gli indici di colonna
# Vediamo ad esempio come estrarre, da una matrice A di shape (3, 3), la sua sottomatrice principale di ordine 2, 
# ovvero la sottomatrice di dimensione (2, 2) che si trova nell’angolo in alto a sinistra di A.
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Creiamo la matrice
# Slicing
P = M[:2, :2]
print(P, end="\n\n")


'''
Ultima proprietà che vediamo degli ndarray, sono tutte le operazioni comunemente effettuate nell’algebra lineare su di essi, 
come ad esempio il calcolo della norma, dell’inversa, del rango, della trasposta, oltre che di operazioni di utilità 
come la funzione reshape, che modifica la forma di un vettore o matrice, senza cambiarne il contenuto.
Necessario il sottopacchetto di numpy: np.linalg --> implementa varie operazioni dell'algebra lineare

Vediamo alcune operazioni:
-> np.linalg.norm(a, p): Calcola la norma-p di un vettore o di una matrice
-> np.linalg.cond(A, p): Calcola il numero di condizionamento di una matrice in norma p
-> np.linalg.matrix_rank(A): Calcola il rango della matrice A;
-> np.linalg.inv(A): Calcola l’inverso della matrice A, quando esiste. 
    ATTENZIONE: Questa operazione è molto lenta anche per matrici relativamente piccole;
-> np.transpose(A): Calcola la trasposta della matrice A. E’ equivalente a A.T;
-> np.reshape(a, new_shape): Modifica la shape di un ndarray a, nella forma specificata.
'''
gg = np.linspace(1, 9, 9)   # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(gg)
CC = np.reshape(gg, (3, 3)) # Costruiamo la matrice CC di shape 3x3 ottenuta modificando gg
print(CC)

print(np.linalg.matrix_rank(CC))    # Controlliamo se CC è di rango massimo
# E, se non ha rango massimo, calcoliamone l'inversa
if np.linalg.matrix_rank(CC) == CC.shape[0]:
    CC_inv = np.linalg.inv(CC)


'''
EFFICIENZA DI NUMPY
L’obiettivo di questa sezione di approfondimento è verificare in modo empirico quanto numpy 
è più efficiente del Python classico per operazioni su vettori. Per farlo, andremo ad utilizzare la libreria time 
per misurare il tempo richiesto a Python base e numpy per svolgere le stesse operazioni.
In questo esempio, utilizzeremo un vettore di lunghezza 10 milioni, casuale, e proveremo a calcolare la somma 
del valore assoluto dei suoi elementi (operazione nota come norma 1 del vettore, 
e solitamente indicata con ||v||_1, utilizzando Python classico (attraverso due algoritmi differenti) e le funzioni di numpy.
'''
import time
# import numpy as np
import math

v = np.random.randn(10_000_000) # Costruiamo il vettore

# || v ||_1 con Python modo 1
start_time = time.time()
norma_1 = 0
for i in range(len(v)):
    norma_1 = norma_1 + abs(v[i])
end_time = time.time()
print(f"Tempo impiegato con Python modo 1: {end_time - start_time}s")

# || v ||_1 con Python modo 2
start_time = time.time()
norma_1 = sum((abs(i) for i in v)) # list comprehension
end_time = time.time()
print(f"Tempo impiegato con Python modo 2: {end_time - start_time}s")

# || v ||_1 con numpy
start_time = time.time()
norma_1 = np.sum(np.abs(v))
end_time = time.time()
print(f"Tempo impiegato con Numpy: {end_time - start_time}s")

'''
Tempo impiegato con Python modo 1: 2.772596836090088s
Tempo impiegato con Python modo 2: 1.545154094696045s
Tempo impiegato con Numpy: 0.054563045501708984s

Da questo esempio appare chiaro come Numpy, avendo implementato funzione pre-compilate, 
è estremamente più efficiente di Python standard, ed è quindi più preposto a eseguire operazioni di algebra lineare, 
dove l’efficienza è importantissima.
'''


# Discutiamo ora degli Array (variabili che ne contengono altre) in Python
# Esistono due tipologie di array in Python: le LISTE e le TUPLE
# Le LISTE sono mutabili e sono dinamiche: possiamo allungarle e accorciarle a nostro piacimento
# Le TUPLE sono immutabili

# Definiamo tre tipi di lista: numeri, stringhe e mista
a = [1, 5, 3]               # Lista di interi
b = ["C", "i", "a", "o"]    # Lista di Stringhe
c = ["C", 3, True]          # Lista mista
print(a)
print(b)
print(c)
print(type(a), end="\n\n")

# Definiamo, ora, una tupla
d = (3, "Pippo", [1, 2, 3]) 
# Si possono inserire array dentro altri array! Funzione ottima per l'Algebra Lineare per la creazione di matrici
print(d)
print(type(d), end="\n\n")
# è la "," che crea veramente la tupla, infatti le ( ) possono essere omesse!

# Come per le variabili posso esplicitare il tipo degli array, ma è solo formale...
e: list[int] = [1, 2, 3, "Ciao"] 
# Esplicito la lista come una lista di interi, ma in realtà posso inserire ciò che voglio senza incombere in errori


# Lo SLICING è l'operazione, fondamentale, di estrazione di elementi da un array, per farlo basta conoscere 
# la posizione (numericamente parlando) dell'elemento che ci interessa nell'array. Si parte sempre da posizione 0
f = [4, 2, 54, 6, 1]
print(f)
print(f"L'elemento di posto 2 nella lista f è: {f[2]}.\n")

# Si possono anche estrarre sotto-blocchi di elementi e non un singolo elemento. Grazie alla seguente sintassi -->
# inizio:fine:step  dove inizio è compreso, mentre fine è escluso dal sotto-blocco.
# QUetsa sintassi permette di fare svariate operazioni utili con gli array
g: list[int] = [2, 65, 8, 1, -6453, 8, 14, 8]
print(g)
pari = g[0:8:2] # Così facendo estraggo gli elementi di indice pari tra l'indice 0 e 8 (escluso)
print(pari)
print(type(pari))
centrali = g[2:6] # Estraggo gli elementi centrali della lista
print(centrali)
print(f"Il numero di elementi dell'array g è: {len(f)}.") # La funzione len() restituisce il numero degli elementi degli array
# Grazie a len() posso fare riferimento agli elementi grazie a lui
pari2 = g[2:len(g)] # Estraggo elementi dalla lista dalla posizione 2 fino alla fine
print(pari2, end="\n\n")

# Possiamo fare riferimento all'ultimo elemento della lista in vari modi:
print(g[2:len(g)]) # Da 2 fino len(a) - 1, come visto prima.
print(g[2:-1]) # Da 2 fino a -1, dove con -1 Python accederà alla lista al contrario! (-1 = ultimo elemento! quindi escluso)
print(g[2:], end="\n\n") # Da 2 fino in fondo, lasciando vuoto il campo "fine"

# Possiamo anche invertire l'array dando step = -1, che accederà alla lista al contrario.
print(g[::-1], end="\n\n")

# Interessante notare che con step = -1 e indici inizio:fine negativi posso anche prendere sotto-blocchi di array al contrario
print(g[-1:-5:-1], end="\n\n")


# Possiamo modificare gli elementi delle liste!
h = [1, 2, 2]
print(h)
h[2] = 3 # In questo modo modifichiamo l'elemento di posto 2 nella lista h
print(h, end="\n\n")

h.append(4) # In questo modo appendo alla fine della lista il valore 4
print(h)
h.insert(0, 0)  # In questo modo uso la sintassi posizione:valore per inserire il valore 0 nella posizione 0 della lista
print(h, end="\n\n")

# Posso, infine, anche concatenare liste! Seguiranno l'ordine di scrittura dato.
i = [5, 6, 7]
j = h + i   # Concatenazione di liste
print(j, end="\n\n")


# Come detto le TUPLE sono definite, nella realtà, dalle virgole e non dalle parentesi tonde!
# Per lo stesso motivo per dichiarare una tupla con un unci valore non può essere dichiarata con tupla = (3)
# non avendo nessuna virgola non verrà riconosciuta come tuple. Se definissimo tuple = (3, ) --> questa è una tupla
k = (1, 2, 3)
l = 1, 2, 3
print(f"k = {k}.")
print(f"l = {l}.")
print(type(l), end="\n\n")

m = (3)
print(type(m))  # Intero
n = (3, )
print(type(n), end="\n\n")  # Tuple
# Non posso modificare gli elementi della typle! Avrei un errore
# Per il resto le tuple si comportano similmente alle liste: posso, ad esempio, concatenarle.

o = k + l   # Concatenazione di tuple
print(o, end="\n\n")

# Cosa utilizziamo quindi, liste o tuple?
# A livello di memoria: tuple salvate in maniera più efficienti non essendo modificabili.
# A livello sintattico la vera forza delle tuple risiede nell'assegnazione multipla: è possibile distribuire
# i valori di una tupla a più variabili semplicmente utilizzando le tuple stesse.
p = 5, "Difensore"  # Creo una tupla
numero, ruolo = p   # Assegno a due variabili due valori della tupla
print(numero)
print(ruolo, end="\n\n")


# Anche in python si deve stare attenti al Pass-By-References!
# Se creassi una nuov lista A e gli assegnassi suoi valori e, in seguito, facessi la seguente operazione: B = A
# in questo modo non andrei a creare una nuova lista B copiandoci gli elementi di A! Ma, semplicmente, creerei 
# un nuovo riferimento (B) alla lista A!! Quindi modificando A modificherei anche B
q: list[str] = ["Mi", "chiamo", "Andrea"]
print(q)
r = q     # Assegno ad r lo stesso riferimento di q
print(r)  # L'output è lo stesso di print(q)

q[-1] = "Raffaele"  # Modifico l'ultimo elemento di q
print(q)
print(r)    # Ho modificato entrambe le liste!!
# Equivalemnte
q.append("Tamburri")
print(r, end="\n\n")

# Per evitare questa situazione (volendo lavorare sulla copia di una lista) -->
s: list[str] = ["Mi", "chiamo", "Andrea"]
print(s)

t = s[:] # Attenzione ai [:]. In questo modoottengo una copia di s sulla lista t. Perchè?
# Dal risultato di un'operazione ottengo la copia (rislutati dell'operazione) della lista e non un nuovo puntatore!
# Se avessi fatto t = s + ["Tamburri"], avrei ottenuto lo stesso effetto!
print(t)

s[-1] = "Raffaele"
print(s) # Unico modificato
print(t, end ="\n\n") # Non modificato


# L'aggiunta di elementi alla lista vviene con delle ocnseguenze!
# Ad esempio l'operazione ".append()" scatena delle "operazione che non vediamo" --> verrà creata una nuova lista
# che è la copia della precedente, ma con un elemento in più e, infine, viene eliminata la lista precedente 
# (garbage collector). Come risultato la memoria soffre di questa operazione: per un momemnto avremo il doppio 
# della memoria che una lista occupa. Per sviare a questo problema, quando ci si aspetta di dover modificare una ista
# svariate volte si inizializza VUOTA, i cui elementi vengono sostituiti durante l'esecuzione del programma.
# Tutto ciò rende l'uso della lista più efficiente.
u: list[int] = [0] * 4 # Creo una lista vuota lunga 4
u[0] = 5
u[1] = 3
u[2] = -6
u[3] = 9
print(u)

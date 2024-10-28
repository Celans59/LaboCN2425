
# Python non ha bisogno di una tipizazzione esplicita delle variabili!!
a = 3       # Intera
x = 2.1     # Floating 
s1 = "Pippo" # Stringa
b = True    # Booleana

# Per stampare in output si utilizza la funzione print()
print(a)
print(x)
print(s1)
print(b, end="\n\n")

# Per conoscere il tipo di una variabile passiamo come argomento alla funzione print() la funzione type()
print(type(a))
print(type(x))
print(type(s1))
print(type(b), end="\n\n")

# Riassegnazione valore di una variabile in cui si sottolinea la non importanza del tipo di dato
a = 3.6 # a era una variabile intera traspformata automaticamente in float
print(a)
print(type(a), end="\n\n")

# Possiamo utilizzare funzioni semplici per forzare il cambio di un tipo di variabile!
print(a)             # a = 3.6
print(int(a))        # a = 3
print(a, end="\n\n") # a = 3.6 --> non è cambiato il valore della variabile!
int(a)   # Di per se non fa nulla se utilizzata in questa maniera e il valore di a è sempre 3.6

# I nomi di variabili sono CASE-SENSITIVE!

s2 = "Ciao, "
# print(s = s2 + s1) --> Questa riga non ha senso! Devo prima inizializzare la variabile s, non posso usarla direttamente
s = s2 + s1 # Concatenazione di due stringhe
print(s, end="\n\n")

# E come ci si comporta quando si deve concatenare stringhe con valori numerici? Si tuilizza la fuzione str()
t = "Il valore di a è: " + str(a) # 3.6 (valore di a) verrà inserito esattamente alla fine della stirnga
print(t, end="\n\n")
# Questa, però, è una procedura lenta e sconsigliata!

# Per un'ottimizzazione di questo passaggio si utilizzeranno le f-stringhe che, semplicemente,
# vengonpo utilizzate inserendo {variabile} dove essa dovrà essere stampata nell'output
# e non verrà utilizzata la funzione str(). Verrà aggiunta una "f" all'inizio della stringa!
r = f"Il valore di a è: {a}." # IN questo modo è anche più dinamico l'inserimento della variabile
print(r, end="\n\n")    # Python convertirà automaticamente la variabile a in una stringa.

# Ulteriore vantaggio delle f-stringhe è la formattazione dell'output con un'adeguata sintassi
pi = 3.14159265358979323846
print(f"Il valore di pi-greco è: {pi}")         # Possiamo anche stampare direttamente la stringa
print(f"Il valore di pi-greco è: {pi:0.4f}")    # Tutti gli interi e 4 decimali
print(f"Il valore di pi-greco è: {pi:0.7f}\n")     # Tutti gli interi e 7 decimal

# Curiosità Python tra interi e float...
c = 3.0         # Trattata come float anche se, in realtà, è un intero!
print(type(c), end="\n\n")  # Stamperà class: float

d = 3
print(f"Il valore di d é: {d},\nil valore di c è: {c}.\nLe variabili c e d sono uguali?? {c == d}.\n")
# In questa riga di codice stampiamo i valori di c e di d, per poi mettere nell'output
# un valore booleano data dal confornto (e dall'operatore di confronto ==) che ci farà
# notare che per Python 3 e 3.0 sono uiguali anche se uno è un intero e l'altro un float!!

# Vediamo operatori di operazioni numeriche e il comportamento di Phyton con operazioni tra interi e float
j = 5
k = 3.6
l = 2.4
print(f"Il valore di j è: {j}")
print(f"Il valore di k è: {k}")
print(f"Il valore di l è: {l}")
print(f"j + k = {j+k},\nj / k = {j/k},\nj ^ k = {j**k}") # Operatori di somma, divisione e poetnza
print(f"Il valore di k + l = {k+l}\n")
# Il risultato di tali operazioni sarà sempre un float! Sia se faremo: intero +/*-... float
# Sia se sommiamo due float che danno un intero: il risultato sarà sempre float.

# Variabili booleane e conversioni
bool1 = True
bool2 = False
print(bool1)        
print(bool2)        
print(int(bool1))   # Stampa 1
print(int(bool2))   # Stampa 0
bool3 = 5
bool4 = 0
print(bool(bool3))              # Stampa True (sempre se la variabile != 0)
print(bool(bool4), end="\n\n")  # STampa False (False se la variabile == 0)
# Occhio alle lettere maiuscole su True e False

# Esiste, ed è largamente utilizzato, il tipo None. Serve per indicare l'assenza di dati!
# Spesso presente come output nelle funzioni che non devono restituire nulla (simile a VOID)
w = None
x = "Hello!!"
print(w is None)                # output: True
print(x is None, end="\n\n")    # output: False

# Anche se non necessario è buona usanza dichiarare il tipo di dato delle vaiabili
# Anche per migliorare la leggibilità e la portabilità tra programmatori
y: int = 5
# Tutto ciò non vincola la variabile al tipo di dato...
z: int = "é una stringa, non un intero"
print(type(z)) # output ci dirà che z è di tipo STringa e non intero!

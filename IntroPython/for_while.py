
# I cicli sono fondamentali per automatizzare la ripetizioni di istruzioni quando necessario
# Vediamo due tipi di cicli: FOR e WHILE


# La sintassi del ciclo FOR è la seguente:
# for <VARIABILE> in <ITERABILE>:    
#   <RIPETIIZIONE>

# la VARIABILE viene inizializzata all'interno del ciclo, non deve, quindi,  essere stata utilizzata prima
# Insieme alla variabile viene utilizzato un ITERABILE su cui ciclare (lista, tuple, stringa o un generatore)
# All'inizio del ciclo la VARIABILE viene inizializzata con il primo elemento dell'ITERABILE 
# A questo punto viene eseguito il corpo del ciclo con il valore della VARIABILE che si aggiorna ad ogni iterazione 
# fino a quando raggiungerà l'ultimo elemento dell'ITERABILE
iterable = 2, 3, 6
for n in iterable:
    print(n)
    if n == 6:
        print()

# Di norma si vuole che l'iterabile faccia assumere alla variabile valori crescenti, partendo da 0 e arrivando ad un valore prefissato
# Per garantire questo si utilizza la funzione --> range(START, STOP, STEP)
# questa funzione ritorna un generatore contente valori numeri compresi tra START (incluso) e STOP (esluso) con passo STEP
for i in range(5):
    print(i)
    if i == 4:
        print()
# Quando un solo valore è specificato è quello di STOP e, quindi --> START = 0, STEP = 1

# Occhio ai loop!! Il numero di iterazioni del ciclo NON viene pre-calcolato, ciò significa che se modifichiamo 
# l'iterabile (allungandolo o accorciandolo) durante le iterazioni modificheremo il numero di iterazioni del ciclo
# Nel seguente esempio di cadrebbe in un loop infinito.
# iterable = [1, 2, 3, 4, 5]
# for i in iterable:
#     print(i)
#     iterable.insert(i+1, i-1)
#     iterable.append(i)
# print(iterable)


# La sintassi del ciclo WHILE è la seguente:
# while <CONDIZIONE>;       --> finchè la condizione è True
#   <RIPETIZIONE>           --> continua ad eseguire il ciclo
continua: bool = True
i: int = 0
while continua:
    if i == 5:
        continua = False
    print(i)
    i = i + 1

print()
# Come per il ciclo FOR, anche per il ciclo WHILE si deve stare attenti a non cadere in un loop infinito
# Per questo è buona norma utilizzare il comando BREAK che, quando invocato, termina subito il ciclo
# Normalmente si prevede un numero di iterazioni massime oltre le quali non andare, il tutto accompagnato dal comando BREAK
continua: bool = True
maxiter: int = 10
i: int = 0
while continua:
    if i < 0:
        continua: False
    print(i)
    i = i + 1
    if i == maxiter:
        break           # Break blocca il ciclo dopo 10 iterazioni, altrimenti sarebbe entrato in loop!!

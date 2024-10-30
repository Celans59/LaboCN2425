
# La gestione degli errori è un aspetto fondamentale della programmazione!
# Gli errori possono verificarsi per molte ragioni: input non validi, divisioni per zero, accesso a file inesistenti, ...

# Python fornisce strumenti per gestire gli errori per evitare di bloccare il programma e facilita il debugging
# Quando si ha un errore si riceverà un TRACEBACK: un messaggio con informaiozni sul tipo di errore e dove si è verificato

def divisione(a: float, b: float) -> float:
    risultato = a / b
    return risultato

# divisione (10, 0) -->
'''
Traceback (most recent call last):
  File "/Users/andreacelani/Visual Studio Code/LaboCN2425/IntroPython/GestioneEccezzioni.py", line 12, in <module>
    divisione (10, 0)
  File "/Users/andreacelani/Visual Studio Code/LaboCN2425/IntroPython/GestioneEccezzioni.py", line 9, in divisione
    risultato = a / b
                ~~^~~
ZeroDivisionError: division by zero
'''

# Traceback (most recent call last): --> l'errore si è verificato nell'ultima operazione eseguita
# line 12, in <module> divisione (10, 0) --> mostra la linea di codice in cui l'errore avviene
#  line 9, in divisione risultato = a / b --> mostra che l'errore si è verificato nella funzione divisione, alla riga 9
# ZeroDivisionError: division by zero --> mostra il tipo di errore specifico e la sua spiegazione

'''
Vediamo gli errori più comuni in Python:
-> SyntaxError: quando il codice ottiene errori di sintassi
-> TypeError: quando si cerca di svolgere un'operazione su tipi di dato non compatibili
-> NameError: quando si cerca di usare una variabile o funzione che non è stata definita
-> IndexError: quando si tenta di accedere ad un elemento di una listausando un indice fuori dai limiti
-> KeyError: quando si tenta di accedere ad una chiave inesistente di un dizionario
-> ValueError: quando una funzione riceve un argomento valido per tipo ma non per valore
'''

# Per prevenire l'interruzione del codice, Python permette di gestire porzioni di codice che potrebbero causare errori.
# Tale porzione di codice viene inserito all'interno del blocco TRY e, se si verifica l'errore, il programma passa al blocco EXCEPT
def divisione(a: float, b: float):
    try:
        risultato = a / b
    except ZeroDivisionError:
        print("Errore: divisione per zero non consentita!")
        risultato = None
    return risultato

print(divisione(10, 0)) 

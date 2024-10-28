
# Le funzioni le conosciamo bene! Sono importanti, ovviamente, anche in Python
# Una funzione è un oggetto che prende in ingresso dei valori (INPUT), esegue delle operazioni su di essi e restituisce
# un risultato (OUTPUT). Ne abbiamo già usate molte fino ad ora: print(), len(), type(), ...

# Vediamo la loro sintassi: 
# def NOME_FUNZIONE (INPUT1, INPUT2, ...):
#   esecuzione di operazioni sugl'input
#   ...
#   return OUTPUT

# Una volta deinita possiamo sempre riutilizzarla chiamando il suo nome e passando dei valori agl'input.

def calcolaProdotto (n1: float, n2: float) -> float:
    r"""
    Dati in input due numeri n1 ed n2, restituisce il prodotto tra n1 e n2.

    Parameters:
    n1 (float): Primo numero
    n2 (float): Secondo numero

    Returns:
    (float): Risultato di n1 * n2
    """
    risultato: float = n1 * n2 # Computazione
    return risultato # Output
# -> float ciò sta a dichiarare il tipo che ci aspettiamo in output
# Inoltre abbiamo messo, tra i commenti multilinea, una documentazione della funzione.
# Tale formattazione è considerato uno standard in Python
# Ora utilizziamo la funzione all'interno di uno script...
n1: float = 3.2
n2: float = 2.0
n: float = calcolaProdotto(n1, n2)
print(f"{n1} * {n2} = {n}.\n")

# Input posizionali e non posizionali, vediamone lo scopo tramite la seguente funzione...
def calcolaDifferenza(n1: float, n2: float) -> float:
    r"""
    Dati in input due numeri n1 ed n2, restituisce la differenza tra n1 e n2.

    Parameters:
    n1 (float): Primo numero
    n2 (float): Secondo numero

    Returns:
    (float): Risultato di n1 - n2
    """
    risultato: float = n1 - n2 # Computazione
    return risultato # Output

a: int = 5
b: int = 2
differenza = calcolaDifferenza(a, b)
print(f"{a} - {b} = {differenza}.")
# Chiamando la funzione sugli input a e b in questo ordine ha associato n1 = a e n2 = b. Comportamento di default!
# Nel comportamento sopra descritto a e b sono passati come valori POSIZIONALI, poichè inseriti nello stesso oridne della funzione
# Ma possiamo passare anche valori NON POSIZIONALI ad una funzione...
# Calcoliamo la differenza con input non posizionali
differenza2 = calcolaDifferenza(n2 = a, n1 = b) # Abbiamo esplicitamente invertito i parametri
print(differenza2, end="\n\n")
# Il passaggio di valori NON POSIZIONALI diventa utile quando si considerano funzioni con tanti valori in input

# Si possono passare valori di default ai parametri che verranno assunti se non diversamente dichiarato
# Consideriamo, ad esmepio, una funzione calcolOperazione(n1, n2, op) che, inserita un'operazione sottoforma di stringa
# per il parametro op esegue esattamente quella operazione.
# Associamo ad op il valore "Somma" di default
def calcolOperazione(n1: float, n2: float, op: str = "Somma") -> float:
    r"""
    Dati in input due numeri n1 ed n2 e un'operazione, restituisce il risultato
    dell'operazione applicata ad n1 e n2.

    Parameters:
    n1 (float): Primo numero
    n2 (float): Secondo numero
    op (str): Operazione

    Returns:
    (float): Risultato di op(n1, n2)
    """
    if op == "Somma":
        risultato: float = n1 + n2
    elif op == "Differenza":
        risultato: float = n1 - n2
    elif op == "Prodotto":
        risultato: float = n1 * n2
    elif op == "Rapporto":
        if n2 != 0:
            risultato: float = n1 / n2
        else:  
            print("Errore: divisione per 0.")
            risultato = None
    else:
        print(f"Operazione {op} non definita.")
        risultato = None
    
    return risultato # Output

a: int = 3
b: int = 1
somma = calcolOperazione(a, b)  # op = "somma" di default, quindi funziona anche così per la somma
differenza = calcolOperazione(a, b, op = "Differenza")
prodotto = calcolOperazione(a, b, op = "Prodotto")
rapporto = calcolOperazione(a, b, op = "Rapporto")
print(f"La somma vale: {somma}\nLa differenza vale: {differenza}\nil prodotto vale: {prodotto}\nil rapporto vale: {rapporto}\n")


# La funzione HELP
# La formattazione discussa prima (quella tra commenti multilinea) aiuta utenti terzi a capire meglio come funzionano 
# le funzioni che noi definiamo e sviluppiamo, nascondendone la vera e propria implementazione!

# print(help(calcolOperazione)) 
    # Ci stamperà ciò che si trova tra i commenti multilinea della funzione


# Chiaramente non tutte le funzioni restituiscono qualcosa in output (VOID)!!
    # print() non restituisce nulla in output --> stampa solo a video la stringa passatagli. Stessa cosa help()
# Costruire una funzione che non restituisca nulla è emplice, basta omettere il return
# Quindi nella sua dichiarazione avremo, nella parte conclusiva: ...) -> None:
# Questo equivale a dire che se il risultato delle operazioni di una tale funzione viene assegnato ad una variabile
# essa sarà di tipo None
def saluti(nome: str) -> None:
    r"""
    Stampa a schermo dei saluti diretti al nome inserito in input.

    Parameters:
    nome (str): Il nome da salutare.
    """
    print(f"Ciao, {nome}!")

nome: str = "Andrea"
saluti(nome)
output = saluti(nome)
print(output)
print(type(output), end="\n\n")


# Al contrario, delle volte è necessario definire funzioni che restituiscono più di un ouput!
# Ciò è possibile semplicmente elencando tutto le variabili da restituire separate da una ,
def sommaProdotto(n1: float, n2: float) -> float:
    r"""
    Presi in input i numeri n1 e n2, ne ritorna somma e prodotto.

    Parameters:
    n1 (float): Primo numero
    n2 (float): Secondo numero

    Returns:
    (float): n1 + n2
    (float): n1 * n2
    """
    somma = n1 + n2
    prodotto = n1 * n2
    return somma, prodotto

n1: float = 4.0
n2: float = - 2.0
somma, prodotto = sommaProdotto(n1, n2)
print(f"{n1} + {n2} = {somma}\n{n1} x {n2} = {prodotto}")

# Cosa accade se associassimo l'output multuplo ad una sola variabile?
risultato = sommaProdotto(n1, n2)
print(risultato, end="\n\n") # La , definisce una tupla! Anche in questo caso! Avrò in output una tupla.


# Una proprietà interessante di Python è quella di associare le funzioni a delle variabili e
# utilizzarle come delle comuni variabili o stringhe, ...
# Quindi possiamo anche passarle in input ad altre funzioni!!
def quadrato(x: float) -> float:
    r"""
    Ritorna il quadrato del valore preso in input.

    Parameters:
    x (float): Numero in input

    Returns:
    (float) x^2
    """
    risultato = x ** 2
    return risultato
f = quadrato # Stiamo associando la funzione ad una variabile
print(quadrato) # Riferimento in memoria della funzione quadrato!!
print(f(3))  # Uso la variabile per richiamare la funzione quadrato con parametro 3

# Ora passiamo la variabile f come input di un'ulteriore funzione!!
def elementoXelemento(f, x: tuple[float]) -> list[float]:
    r"""
    Presa in input una funzione f e una tupla di float x, ritorna una lista
    della stessa lunghezza di x, i cui elementi sono gli f(xi).

    Parameters:
    f (function): La funzione da applicare elemento per elemento
    x (tuple): Una tupla di numeri float

    Returns:
    (list): Una tupla contenente gli f(xi)
    """
    y = [0] * len(x) # Inizializiamo la tupla di output (per salvare memoria)

    for i in range(len(x)): # Cicliamo sugli elementi di x
        xi = x[i] # Estraiamo l'i-esimo elemento di x
        y[i] = f(xi) # Calcoliamo f su xi
    
    return y

# Il vantaggio di tale approccio, è che la funzione sopra definita può essere ri-utilizzata su 
# qualunque altra funzione che vogliamo applicare elemento per elemento ad una tupla di numeri.

def cubo(x: float) -> float:
    r"""
    Ritorna il cubo del valore preso in input.

    Parameters:
    x (float): Numero in input

    Returns:
    (float) x^3
    """
    risultato = x ** 3
    return risultato

x: tuple[float] = 1, 2, 3, 4, 5
xQuadrato = elementoXelemento(quadrato, x)
xCubo = elementoXelemento(cubo, x)
print(xQuadrato)
print(xCubo, end="\n\n")


# Funzioni LAMBDA
# Funzioni molto semplici che possiamo scrivere su di una sola riga per semplificare la lettura del testo
# Vediamo la sintassi con un esempio: andiamo a definire una funzione che, preso in input un valore x, ritorna il quadrato
quad = lambda x: x ** 2
print(quad(5), end="\n\n")
# è sufficiente chiamare il comando LAMBDA eguito dai valori in input della funzione, separati da virgole, i : e 
# l'operazione da eseguire.


# Variabili LOCALI vs variabili GLOBALI
# Le variabili LOCALi sono quelle definite all'interno delle funzioni, non accessibili al di fuori della funzione stessa e
# vengono create al momento dell'utilizzo della funzione e eliminate al suo terminamento.
# Le variabili GLOBALI sono accessibili a qualsiasi livello.
def saluti(cognome: str) -> None:
    print(f"Ciao, {nome} {cognome}.")
    return None

nome: str = "Andrea" # Variabile GLOBALE che verrà stampata quando usiamo la funzione saluti!
saluti(cognome = "Celani")
# print(cognome) # ERRORE --> La variabile locale "cognome" non è più in memoria

# MA! Se all'interno di una funzione una sua variabile locale ha lo stesso nome di una variabile globale
# avrà più importanza la variabile locale al suo internom e verrà utilizzata quella.
def saluti2(nome: str) -> None:
    print(f"Ciao, {nome}.\n")
    return None

nome: str = "Andrea" # Definiamo una variabile globale "nome"
saluti2("Raffaele") # Verrà utilizzata la variabile locale a cui abbiamo passato "Raffaele" come valore

# Ovviamente quando si modifica una variabile globale all'interno di una funzione, quella modifica è permanente!
# Non scompare con la terminazione della funzione.
def fibonacciStep(valori: list) -> None:
    r"""
    Data una lista di valori, contenente una porzione della sequenza di Fibonacci, 
    aggiunge il successivo elemento della sequenza, in testa a tale lista.

    Parameters:
    valori (list): La lista con gli attuali valori della sequenza di Fibonacci
    """
    valori.append(valori[-2] + valori[-1])
    return None

valori = [1, 1] # Inizializzo una lista iniziale
print(valori) # La lista NON modificata
# Steps che modificano la lista esterna alla funzione
fibonacciStep(valori)
fibonacciStep(valori)
print(valori, end="\n\n")   # La lista modificata


# *args e **kwargs
# Può  succedere di voler definire una funzione a cui vorremmo poter passare valori in input variabili e non definiti
# Vengono in aiuto i parametri *args e *kwargs.
def somma(*args):
    r"""
    Dato in input un elenco di valori, ritorna la loro somma.
    """
    # Nota: il numero variabile di input viene caricato dentro una variabile di nome 
    # "args", che praticamente rappresenta una tupla di valori.
    print(f"Somma di {args} =", end = " ")
    # Eseguo la somma dei valori
    risultato = 0
    for valore in args:
        risultato = risultato + valore
    return risultato

# Chiamata alla funzione con un numero variabile di argomenti
print(somma(1, 2, 3))
print(somma(5, 10), end="\n\n")
# La funzione somma può accettare qualsiasi numero di parametri grazie all’input *args.

# Similmente, con **kwargs, possiamo passare un numero variabile di argomenti non posizionali con nome a una funzione.
# Questi argomenti vengono ricevuti sotto forma di dizionario (e non tupla, come avveniva con *args).
def infoStudente(**kwargs):
    for chiave, valore in kwargs.items():
        print(f"{chiave}: {valore}")

infoStudente(nome = "Andrea", età = 23, corso = "Calcolo Numerico") # Chiamata alla funzione con argomenti con nome
# infoStudente(corso = "Calcolo Numerico", età = 22, nome = "Raffaele")

print()
# è chiaramente possibile passare ad una funzione sia il valore *args che il valore **kwargs, 
# così che possa prendere in ingresso un numero non specificato sia di valori posizionali che non posizionali.
def visualizzaArgs(input1, input2, *args, **kwargs):
    print(f"inputs: {input1}, {input2}.")
    print(f"*args: {args}")
    print(f"**kwargs: {kwargs}")

visualizzaArgs("input1", "input2", 1, 2, 3, nome = "Andrea", voto = "30")

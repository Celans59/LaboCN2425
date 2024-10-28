
# Struttura di base -->

# if <CONDIZIONE>:                      --> se CONDIZIONE è True allora
#   <CORPO IF>                          --> eseguirà CORPO IF, alrimenti andrà avanti
# elif <CONDIZIONE ALTERNATIVA 1>:      --> verificando se CONDIZIONE ALTERNATIVA 1 è True
#   <CORPO ALTERNATIVO 1>               --> eseguirà CORPO ALTERNATIVO 1, altrimenti andrà avanti
# elif <CONDIZIONE ALTERNATIVA 2>:      --> e codi via...
#   <CORPO ALTERNATIVO 2>
# else:                                 --> se nessuna condizione è True allora
#   <CORPO ALTERNATIVO>                 --> verrà eseguito CORPO ALTERNATIVO

# Ad esempio
TrueCondiction = True
if TrueCondiction:
    print("Condizione IF verificata", end="\n\n")
else:
    print("Condizione ELSE verificata", end="\n\n")
# Esempio stupido. 
# Questa operazione diventa interessante quando viene usata per confrontare variabili (OPERATORI DI CONFRONTO!)
n: int = 20
if n % 2 == 0 :
    print("Il numero è pari!", end="\n\n")
else:
    print("Il numero è dispari!", end="\n\n")


# Quando abbiamo più di 1 condizione da verificare bisogna utilizzare gli operatori logici: AND, OR e NOT
a: int = 4
b: int = 2
c: int = 3

condizione1 = a > c
condizione2 = a < b ** 2 

if (condizione1) and (not condizione2): # Se la prima è verificata, mentre la seconda no, restituire "Ok!"
    print("Ok!\n")

# Quando abbiamo parecchie condizione da controllare è meglio fare unìoperazione in più di verifica di essa:
# tanto meglio fare una riga di codice in più invece che fare la verifica delle condizioni nell'if! Buona pratica...
a: float = 1.4
b: float = 0.3
c: float = 1.5

condizione = (a + b > c) and (a + c > b) and (b + c  > a) # Ecco di cosa parlavo!

if condizione:
    print(True)
else:
    print(False)


# Le librerie sono pacchetti di funzioni che svolgono specifiche funzionalità.
# La maggior parte dei pacchetti generalmente sono BUILT-IN, ovvero richiamati direttamente da Python.
# Per far ciò basta utilizzare la sintassi adeguata:
# import NOME_LIBRERIA
import random as rnd # "as rnd" si tratta di renaming, da ora ci si può riferire alla libreria random come rnd
import math

x = rnd.random() # La funzione random() del pacchetto random estra casualmente un numero compreso tra 0 e 1
y = math.exp(x) # La funzione exp() della libreria math calcola il numero e di Nepero elevato alla x
print(f"e^{x:0.3f} = {y:0.3f}.")

'''
Se si prevede di utilizzare la libreria molte volte possiamo scrivere:
from random import *
in questo modo possiamo scrivere direttamente -->
x = ranom() senza cadere in errori!
Ma occhio a definire funzioni con lo stesso nome di quelle importate! Così facendo si sovrascriverà la funzione importata.

è anche possibile importare solo alcune funzioni da una libreria, magari le uniche che ci servono -->
from math import sin, cos, tan
y = sin(x)


Chiaramente è anche possibile definire librerie dall'utente stesso!!
Anzi, ogni progetto che si rispetti importa tra i propri file le proprie funzioni sviluppate! é una pratica comune
Ma in che modo avviene?
Supponiamo di scrivere un file mieFunzioni.py che implementa due funzioni di grande importanza nel proprio progetto
a questo punto basterà scrivere -->
import mieFunzioni
all'intenro di un altro file del mio progetto, per potervi accedere liberamente!!
Mentre se il file si trovasse in un'altra cartella?
from CARTELLA import mieFunzioni
'''

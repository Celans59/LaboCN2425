
'''
la VISUALIZZAZIONE su Python viene svolta grazie alla libreria MATPLOTLIB
in particolare grazie al suo sotto-pacchetto PYPLOT,
Vediamone funzionalità base.

Tale libreria permette la rappresentazione di grafici!! è sufficiente definire due vettori di lunghezza uguale. 
Le funzioni di libreria andranno quindi a rappresentare i punti le cui coordinate sono descritte dai vettori 
    indicati sul piano bi-dimensionale, che verranno poi connessi con dei segmenti di retta.

Più formalmente, siano X = (x_1, ..., x_n) e Y = (y_1, ..., y_n) due vettori, contenente le coordinate dei dati che vogliamo rappresentare.
La funzione PLOT(X, Y) di matplotlib.pyplot andrà a rappresentare tutte le coppie (x_i, y_i) per i = 1, ..., n
e li connetterà con un segmento di retto. Il plot verrà quindi reinderizzato non appena viene chiamato il comando SHOW().

'''
import numpy as np
import matplotlib.pyplot as plt

# Creiamo due vettori di esempio
a = 0
b = 2 * np.pi
N = 50

x = np.linspace(a, b, N)
y = np.sin(x)

# Visualizzazione
plt.plot(x, y)
plt.show()
# Primo grafico!! Che rappresenta la funzione f(x) = sin(x)

'''
Il grafico doveva essere, però, composto da segmenti di retta ma appare curvo!
In realtà, la curva è un effetto ottico dovuto al numero molto alto di punti rappresentati.
'''
# Rappresentiamo meno punti
M = 8
x = np.linspace(a, b, M)
y = np.sin(x)

# Visualizzazione
plt.plot(x, y)
plt.show()

'''
Possiamo anche personalizzare i grafici aggiungendo: titolo, griglia, nomi degli assi, ...
per farlo è sufficiente inserire specifiche funzioni:
-> plt.title(str): Aggiunge un titolo
-> plt.xlabel(str): Aggiunge una label all’asse x
-> plt.ylabel(str): Aggiunge una label all’asse y
-> plt.grid(): Aggiunge la griglia al plot
-> plt.xlim([a, b]): Forza il limite di visualizzazione dell’asse x ad essere tra a e b
-> plt.ylim([a, b]): Forza il limite di visualizzazione dell’asse y ad essere tra a e b
dovranno essere insirita una per riga tra le funzioni plt.plot(x, y) che apre il plot e plt.show() che chiude il plot.
'''
# Creiamo due vettori di esempio
a = 0
b = 2 * np.pi
N = 50

x = np.linspace(a, b, N)
y = np.sin(x)

# Visualizzazione
plt.plot(x, y)
plt.title('Un grafico di f(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('y = sin(x)')
plt.grid()
plt.show()


'''
è anche possibile rappresentare più curve sullo stesso piano allo stesso tempo.
Per farlo, definiamo una nuova coppia di vettori x1 e y1, 
e inseriamo semplicemente il comando plt.plot(x1, y1) tra il comando plt.plot(x, y) e il plt.show().
'''
# Creiamo tre vettori esempio
a = 0
b = 2*np.pi
N = 50

x = np.linspace(a, b, N)
y1 = np.sin(x)
y2 = np.cos(x)

# Visualizzazione
plt.plot(x, y1)
plt.plot(x, y2)
plt.title('Un grafico di funzioni trigonometriche.')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x) = sin(x)', 'f(x) = cos(x)'])  # Funzione per inserire una legenda passando ordinatamente le curve inserite
plt.grid()
plt.show()

'''
Per quanto riguarda la legenda si ha anche la possibilità di personalizzarla ancora di più!
-> color = 'str': Cambia il colore della linea
-> linewidth = int: Cambia lo spessore della linea

Altre specifiche possono essere inserite passando in input alla funzione plt.plot() una stringa (subito dopo x e y), 
    con la seguente notazione:
-> "o": Cambia lo stile della linea a dei punti isolati
-> "--": Cambia lo stile della linea a una linea tratteggiata
-> "o-": Cambia lo stile della linea a una linea continua in cui i punti rappresentati sono segnati con dei cerchi    
'''
# Creiamo due vettori
a = 0
b = 2*np.pi
N = 50

x = np.linspace(a, b, N)
y1 = np.sin(x)
y2 = np.cos(x)

# Visualizziamo
plt.plot(x, y1, 'o', color='red')
plt.plot(x, y2, '--', color='k', linewidth=2)
plt.title('Un grafico di funzioni trigonometriche.')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x) = sin(x)', 'f(x) = cos(x)'])
plt.grid()
plt.show()


# SUBPLOTS
'''
Metodo efficiente di rappresentare graficamente un'informazione
Per definire un subplots si parte definendo una FIGURE. 
Fatto con la funzione plt.figure(figsize = (w, h)) per specificare la dimensione della figura.
Dopodiché, per aprire un subplot, si utilizza il comando --> plt.subplot(nrow, ncol, idx), dove 
-> nrow e ncol rappresentano il numero di righe e di colonne di plots nella matrice di grafici di interesse, 
-> idx è un valore incrementale che, partendo da 1, indica la posizione di ogni specifico plot all’interno del subplot. 
idx=1 rappresenta il grafico in alto a sinistra e, incremenmtando, scorre da sinistra a destra e dall’alto verso il basso.

Ogni volta che si apre un nuovo subplot, è necessario specificare il comando plt.subplot(nrow, ncol, idx), 
    con lo stesso valore di nrow e ncol, ma valore incrementale di idx.
'''
# Creiamo dei dati
N = 200

x1 = np.random.normal(0, 1, (N, ))
y1 = np.random.normal(0, 1, (N, ))

x2 = np.random.normal(0, 0.5, (N, ))
y2 = np.random.normal(0, 2, (N, ))

# Visualizziamo
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'o', color='red')
plt.title('Distribuzione normale')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([-3, 3])
plt.ylim([-4, 4])
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(x2, y2, 'o', color='k')
plt.title('Distribuzione normale di dati verticali')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([-3, 3])
plt.ylim([-4, 4])
plt.grid()

plt.show()

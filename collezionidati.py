# Le liste sono collezioni ordinate e modificabili. Permettono duplicati.
# Le tuple sono collezioni ordinate ma immutabili. Permettono duplicati.

# I set sono collezioni non ordinate e perciò non indicizzate . Non permettono duplicati.
# I dictionary sono collezioni ordinate e modificabili (dalla versione 3.7). Non permettono duplicati.

# Termini :
# - Ordinato: la collezione ha un ordine ben definito e l'aggiunta di elementi non incide.
# - Indicizzato: possiamo accedere agli elementi tramite indice (index)
# - Modificabile: possiamo aggiungere , cambiare e rimuovere elementi una volta creata la collezione.
# - Immutabile: non possiamo aggiungere , cambiare e rimuovere elementi.
# - Permette duplicati : possono esserci più elementi con lo stesso valore.

# LIST

x = ["Milano", "Roma", "Napoli"] # creazione di una lista può anche essere x = ["ciao", 99 , False]

# len() , type() , lest()

print(type(x)) # Ci riporta il tipo della variabile.
print(len(x)) # Ci riporta la lunghezza della lista 

y = list(("Milano", "Roma", "Napoli")) # Creazioe di una lista con il costruttore List

# Accedere agli elementi di una lista:
z = ["Milano", "Roma", "Napoli"]

print(z[1]) # Prende il primo elemento
print(z[2:]) # con un range prende tanti elementi dalla partenza alla fine.

# Modificare elementi di una lista:
t = ["Milano", "Roma", "Napoli"]
t[0] = "Prizzi" # per cambiare il singolo elemento
print(t)
t[1:2] = ["Prizzi","Corleone"] # Tramite range per cambiare piu elementi
print(t)

# Inserire elementi di una lista:

t.append("Lercara") # Si aggiunge alla fine
print(t)

t.insert(1, "torino") # Inserisce l'elemento nella posizione 1
print(t)

r = ["pavia", "padova", "Nicosia"]
t.extend(r) # Inserisce una lista in un'altra lista
print(t)

# Rimuovere elementi di una lista:

t.remove("Napoli") # Rimuove l'elemento 
print(t)

t.pop() # Mi va a rimuovere l'ultimo elemento della lista posso anche inserire l'indice nelle parentesi ()
print(t)

del t[0] # Mi elimina l'elemento 0 , se non specifico nulla mi elimina tutta la lista.
t.clear() # Mi pulisce la lista
print(t)

#Ciclare gli elementi : for in , per indice , while e short hand 

u = ["pavia", "padova", "Nicosia"]
for città in u:
    print(città)

# List Comprehesion : 
# sitassi: [espressione for item in lista if condizione == True]

lista_citta = ["pavia", "padova", "Nicosia" , "Prizzi"]
[print(citta) for citta in lista_citta if citta !="Prizzi"]

# Modificare l'ordine : asc , desc , reverse:

lista_citta.sort() # Ordina la mia lista in ordine alfabetico
print(lista_citta)

# Copiare una list con copy():

nuove_citta = lista_citta.copy()
print (nuove_citta)

# Unire pi+ liste insieme _ + , append(), extend()

citta_unite = lista_citta + nuove_citta
print (citta_unite)

nuove_citta.extend(citta_unite)


# TUPLE non sono modificabili utilizzano parentesi ()

tuple = ("Giorgio", "Paolo") # Puo anche essere definita cosi: x= ("giorgio", True , 765)

print(type(tuple)) # se vogliamo riportare il type tuple quando abbiamo un solo valore dobbiamo inserire la virgola
print (len(tuple)) # mi riporta la luunghezza

print (tuple[0]) # per accedere al tuple

if "Giorgio" in tuple: #verifico che un valore e dentro la mia tuple
    print("Si esiste")

#Per aggiungere/rimuovere qualcosa da una tuple dobbiamo prima trasformarla in una list ed applicare i suoi metodi

# Per spacchettare una tuple in piu variabili

paesi = ("Palazzo","Prizzi", "Corleone")

(paese1, paese2, paese3) = paesi
print (paese1)
print (paese2)
print (paese3)

#Ciclare gli elementi
for paese in paesi:
    print(paese) # oppure for i in range(len(paesi)): print(paese)

#Unire tuple con +

altripaesi = ("Lercara", "Marineo")
somma = paesi + altripaesi

print(somma)

# Metodi count(), index()
 
quanti = paesi.count("Prizzi")
print(quanti) # mi conta quante parole Prizzi ci sono

posizione = paesi.index("Corleone")
print(posizione) # mi dice in ch eposizione e la parola Prizzi 


# SET

set = {"Caio", "Buongiorno", "Bonasera"} # Puo anche essere definito cosi: set= {"giorgio", True , 765}
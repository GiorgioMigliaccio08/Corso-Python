#Commento in Python : File creato il 17 Gennaio 2025
#La prima cosa da fare prima di creare un progetto è crere il virtual environment per il singolo
#proggetto , quindi avvio il terminale dentro la cartella e scrivo: python-m venv nomeprogetto.

print("ciao") 

#Stampo un Messaggio a schermo 

messaggio = input("Inserisci qualcosa:  ") # assegno un comando di imput utente
print (messaggio) #e lo rimando a schermo sul terminale

#In Python e molto importante l'indendazione / tabulazione con gli spazi per distinguere le parti di codice
#perche in questo linguaggio non esistono ;

#if 1 < 5:
    #print("Numero inserito minore di 5") #questo pezzotto di codice e più avanti rispetto alla riga superiore



#LE VARIABILI : 

# - cos'e e come creare una variabile
# Una variabile è un contenitore di un valore/oggetto che può cambiare nel tempo.

# - nomenclatura : un nome comprensibile a noi
#variabileUno #camelCase    
#variabile_due #snake_case 
#VARIABILETRE #altro caso 
#nomi di variabili non consentiti: 4variabile / quinta-variabile / sesta variabile 

# - assegnare multipli valori
# - utilizzare una variabile
# x, y, z = 12, 20, 30
x = 10
print(x)

#TIPI DI DATI: 
#per capire che valore abbiamo : print (type(valore))

# str: x ="ciao"
# int: x =20
# float : x = 20.5
# bool : x = True , False

# list x = ["roma", "milano" ,"Napoli"]
# tuple x = ("roma", "milano" ,"Napoli")
# range x = range(6)
# dict: x = {"nome" : "Giorgio", "età": 24} rapporto Chiave/Valore
#set x = {"roma", "milano" ,"Napoli"}


#CASTING 
#Castare vuol dire cambiare il valore di una variabile come ad esempio un intero convertirlo in una stringa
#Questo si usa perche in python non si puo concatenare un numero con un testo come ad esempio in Js.
#Per ovviare a questo problema si usa il Casting in questo modo:

x = "Ciao sono Giorgio , età :  "
y = str(24)

print(x + y) # ci restituisce "Ciao sono Giorgio , età : 24" in questo modo ho unito un intero ad una stringa.




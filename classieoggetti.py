# CLASSI E OGGETTI

class persona:       # Classe
    nome = "Luca"
    cognome = "Rossi"

persona100 = persona()   # Oggetto = in istanza da Persona
persona200 = persona()

# Costruttore

class Persona:
    def __init__(self, nome, cognome):
       self.nome = nome
       self.cognome = cognome

    def saluta(self):
        print("Ciao sono " + self.nome)

persona101 = Persona("Luca", "Rossi")
persona201 = Persona("Valentino", "Bisegna")

print(persona101.nome)

persona201.saluta()

# Il Self serve a quale istanza ci stiamo riferendo

# Modificare ed eliminare proprietà di un oggetto

persona201.nome = "Maria"
persona201.saluta()

#del persona201.nome   per eliminare
#del persona201      mi elimina completamente l'oggetto


# EREDITARIETA'

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia

    def saluta(self):
        print("Buongiorno sonon l'insegnante " + self.nome + " " + self.cognome)

    def dai_voto(self):
        print("Bravo Giorgio stai imparando Python ti meriti un bel 10")

insegnante1 = Insegnante("Anna", "Neri", "Matematica")

print(insegnante1.materia)
insegnante1.saluta()
insegnante1.dai_voto()


# SCOPE è quella porzione di codice in cui abbaiamo la disponibilità della variabile 

# Scope Locale è quello dentro la funzione:
# Scope Globale invece e tutto quello che sta al di fuori della funzione

def funzione():
    x = 800
    print(x)
    return x 

x = funzione()

print(x)

# MODULI un file python contenete funzioni che vogliamo includere nel nostro programma

import miomodulo # se io dopo di questo metto un alias (ovvero un diminuitivo)
# import miomodulo as em da questo momento richiamo mio modulo con l'alias em 
# Altri alias : platform , math 

miomodulo.saluta("Giorgio")

z = miomodulo.persona1["nome"]

miomodulo.saluta(z)

# come importare una sola parte del nostro modulo 

from miomodulo  import persona1
print(persona1["nome"])


# DATETIME

import datetime

data = datetime.datetime.now()

print(data)

datauno = datetime.datetime(2025, 1 , 2)

print(datauno)

# Ci sono diversi parametri di formattazione della data e si usano in questo modo:

# print(data.strftime("%A"))


# CLASSE MATH

g = 3 + 5
h = x + 7 
i = ((x + h ) * 2 + 35)/ g

j = abs(45)
print(j)
j1 = pow(4, 3)
print(j1)
j2 = min(4,9,89)
print(j2)
j3 = max(4,9,89)
print(j3)

import math

j4 = math.sqrt(64)
print(j4)

j5 = math.ceil(64.80)  # Arrotonda pre eccesso
print(j5)

j6 = math.floor(64.90)  # Arrotonda pre difetto
print(j6)

j6 = math.pi   # pigreco
print(j6)

print (dir(math))   #questa riga di codice mi riporta tutti i metodi di math





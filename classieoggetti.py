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
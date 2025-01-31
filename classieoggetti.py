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
       self.consognome = cognome

    def saluta(self):
        print("Ciao sono " + self.nome)

persona1 = Persona("Luca", "Rossi")
persona2 = Persona("Valentino", "Bisegna")

print(persona1.nome)

persona2.saluta()

# Il Self serve a quale istanza ci stiamo riferendo

# Modificare ed eliminare proprietà di un oggetto

persona2.nome = "Maria"
persona2.saluta()

#del persona2.nome   per eliminare
#del persona2       mi elimina completamente l'oggetto
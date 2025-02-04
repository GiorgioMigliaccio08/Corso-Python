# USER IMPUT

p = input("Cosa vuoi fare?")  # Possibilità di prendere da terminale l'imput di un utente per poterlo gestire

print(p)

persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "età":24
}

operazioni = ("aggiungere", "modificare", "eliminare")

def start():
    operazione = input("Cosa vuoi fare?  ")
    if operazione == operazione[0]:
        x = input("Aggiungi chiave: valore separati da una virgola:  ") # numero telefono , 328787678
        aggiungi(x.split(","))
    elif operazione == operazione[1]:
        pass
    elif operazione == operazione[2]:
        pass

def aggiungi(param):
    chiave = param[0]
    valore= param[1]
    persona[chiave]= valore
    print(persona)

while True:
    start()
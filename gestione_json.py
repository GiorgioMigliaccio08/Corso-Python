# JSON  per comiunicare con il nostro frontend in Js e viceversa

import json  # Importa il modulo standard correttamente

# Leggere Json in Python 

x = '{"name": "Giorgio","cognome": "Migliaccio", "age": 30}'
y = json.loads(x)  # Converte la stringa JSON in un dizionario Python

print(y)
print(y["name"])

# Da Python a Json
# Dati convertibili in Json : dict, list, tuple, string, int, float, True, False, None

q = {
    "name": "Giorgio",
    "cognome": "Migliaccio",
    "age": 30
}

w = json.dumps(x)

print(w)
print(type(w))


# formattare il Json e ordinarlo

e = {
    "name": "Giorgio",
    "cognome": "Migliaccio",
    "age": 30,
    "isOnline" : False ,
    "interessi": ["calcio","tennis"],
    "moneteintasca": 4.56,
    "fidanzata": None

}

r = json.dumps(e, indent=4 , separators=(".", "= "))  # Formattazione
r = json.dumps(e, indent=4 , sort_keys=True)  # Ordinamento
print(r)



# PIP   packace manager (gestore di pacchetti in Python creati da altri come nmp)
# un pacchetto e un modulo aggiuntivo che aggiunge funzionalità ai nostri programmi 

# Comando d'istallazione:  python get-pip.py
# verificare la versione: pip --version   oppure pip --V
# sito per scaricare i pacchetti : https://pypi.org/

# importiamo il pacchhetto camelcase dopo averlo scaricato dal terminale

import camelcase

t = camelcase.CamelCase()

frase = "Ciao sono Giorgio"
print (t.hump(frase))  # Ho fatto il CamelCase tutte le parole con la lettera maiuscola

# per rimuovere un pacchetto scriviamo nel terminale : pip unistall camelcase (nome pacchetto)
# per vedere tutti i pacchetti istalliti scrive nel terminale : pip list


# TRY EXCEPT : try ci permette di testare un blocco di codice

try: 
    print(g)
except:
    print("Ce stato un errore!!")
    #pass in alternativa!

# Multiple exception :
g = 5 
try: 
    print(g + "ciao")
except NameError:
    print("Ce stato un errore nel nome!")
except:
    print("Ce stato un errore generico!")   

#esempio con else
g = 5 
try: 
    print(g )
except NameError:
    print("Ce stato un errore nel nome!") 
else:
    print("nessuno problema nel codice!!")


# Finnaly 
g = 5 
try: 
    print(g )
except NameError:
    print("Ce stato un errore nel nome!") 
finally:
    print("Finito!!") # Finally serve a mandare a schermo qualcosa a preiscindere dal risultato!


# raise/throw exception   come lanciare un exception 

k = -1 
if k < 0:
    raise Exception("Numero minore di zero!!")


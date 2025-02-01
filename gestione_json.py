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
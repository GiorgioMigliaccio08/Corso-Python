#STRINGHE 
# STRINGHE MULTIRIGA: """PROVA"""

x = """Parola 1
Parola 2"""
y = "Parola 3"
z = "Ciao sono giorgio e oggi e il giorno {} gennaio {}"
g = "Ciao sono Giorgio e sto imparando \"Python\""

print(x) # Con questa riga di codice stampo mia parola.
print(x[0]) # Con questa riga di codice dico di prendere l'indice 0 della mia parola.
print(len(x)) # Con questa riga di codice dico di prendere la lunghezza della mia parola.
print (x[:3]) # Con questa riga di codice dico di prendere una parte della mia parola.
print(x.upper()) # Con questa riga di codice dico di trasformare mia parola in maiuscolo.
#altri metodi di modifica stringa: upper() , lower () , strip() , split() , replace().

print (x + y) # Con questa riga di codice concateno x e y.
print (z.format(18, 2025)) # Il format e utilizzato per concatenare stringhe e enumeri il alternativa al Csating.
print(g) # escxape serve per mettere qualcosa tra virgolette sia doppie che singole e si usa coosi: \"Parola\"


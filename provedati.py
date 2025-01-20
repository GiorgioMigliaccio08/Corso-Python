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

#BOOLEAN
a = True
b = False

if 8 < 10: 
    print("Sono maggiore di 10")
else:
     print("Sono minore di 10")


#OPERATORI ARITMETICI
# + - * / % ** //  come in matematica prima si esegue * e / e poi tutti gli altri.

q = min(5,10,15)
print (q) # metodo che ci riporta il minore.

w = max(5,10,15)
print (w) # metodo che ci riporta il maggiore.

e = abs(-8)
print (e) # metodo che ci riporta il numero assoluto.

f = pow(5,2)
print(f) # metodo che ci riporta la potenza.


#COSTRUTTI IF/ELSE
# == uguale , != diverso , > maggiiore , < minore , >= , <=
# and entrambi verificate , or almeno una verificata , not negazione.
g = 8
h = 10

if g < h:
     print("Il primo numero e minore del secondo")
elif g == 8:
     print("Il primo numero è uguale a 8")
else:
     print ("Il secondo numero e maggiore del primo")

if g > 2 and g < 10:
     print("esatto")

if g > 2 or g < 10:
     print("errato")

if not(g < 10):
     print("errato")

#Short hand in una sola riga si può fare con una sola iscruzione 
if g > 6 :print("Ciao")

#if annidati

if g % 2 == 0:
     print("Numero pari")
     if(g <10):
        print("Numero pari e minore di 10") 
else:
     print("Numero dispari")



#COSTRUTTO WHILE
# break , continue , else
i = 1
while i < 6:
     print(i)
     if i==3:
        break # Il mio ciclo viene stoppato
     i+= 1
print("Finito")

k = 0
while k < 6:
    k += 1
    if k==3:
        continue # Il mio ciclo viene continuato
    print(k)
    
print("Finito")

l = 0
while l < 6:
     l += 1
else: #utlizzazzato come un If
     print("Finish")

#COSTRUTTO FOR
#Lo utilizzo per recuperare ad esempio tutti gli elementi di una lista.
lista_citta = ["milano", "roma", "napoli"]

for citta in lista_citta:
     print(citta)

for c in range(8):
     if c == 3:
          continue #oppure break
     print(c)
else:
     print("Ho finito")



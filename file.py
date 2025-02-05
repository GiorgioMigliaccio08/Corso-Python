# LAVORARE CON I FILE 

# r - Read: apre il file per leggere , errore se non esiste
# a - Append : apre il file per appendere , cera il file se non esiste
# w - Write : apre il file per scrivere , cera il file se non esiste
# x - Create : crea il file , da errore se esiste

# APRIRE UN FILE

f = open("testo.txt" , "r") # Read legge il file
print(f.read())
print(f.read(5))  # Per prendere una parte del testo
print(f.readline())  # Legge una riga e passa alla seconda e la rilegge.

#f.close()   # Ovviamente quando si finisce di lavorere si chiude il file

# SCRIVERE IN UN FILE
f = open("testo.txt" , "a") 
f.write("Questo e quello che ho aggiunto io")
f.close()


f = open("testo.txt" , "r")
print(f.read())

# CREARE UN FILE

e = open("prova.txt", "w")   # dato che non lo trova lo cera in automatico
# e = open("prova.txt", "X")  # metodo alternativo per creare un file

# ELIMINARE UN FILE 

import os

if os.path.exists("prova.txt"):
    os.remove("prova.txt")
else:
    print("Il file non esiste!")
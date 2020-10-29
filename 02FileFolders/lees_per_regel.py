import os
import time

bestand = open("klasgenoten.txt", "r")

tekst_regel = bestand.readline()


while tekst_regel:

    tekst_regel = tekst_regel.strip()
    os.mkdir(tekst_regel)

    tekst_regel = bestand.readline()
    
    time.sleep(0.2)

time.sleep(5)
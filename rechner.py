run = True
import sys
while run:
    eingabe = int(input("Zahl eingeben: "))
    eingabe2 = int(input("Zweite Zahl eingeben"))
    summe = eingabe * eingabe2
    print(summe)
    if(input ("exit")== "exit"):
        run = False
        
print("Willkommen beim Taschenrechner Ihres Vertrauens")
print("Was möchten Sie berechnen? Wählen Sie über die Zahl aus.")
print("1. Addieren")
print("2. Subtrahieren")
print("3. Multiplizieren")
print("4. Dividieren")

run = True

while run:
    verfahren = int(input("Eingabe: "))

    if verfahren == 1:

        eingabe = int(input("Zahl 1: "))
        eingabe2 = int(input("Zahl 2: "))
        summe = eingabe + eingabe2

        print("Ihr Ergebnis: " +str(summe)) 
    
    elif verfahren == 2:
        eingabe = int(input("Zahl 1: "))
        eingabe2 = int(input("Zahl 2: "))
        differenz = eingabe - eingabe2

        print("Ihr Ergebnis: " +str(differenz ))
    
    elif verfahren == 3:
        eingabe = int(input("Zahl 1: "))
        eingabe2 = int(input("Zahl 2: "))
        produkt = eingabe * eingabe2

        print("Ihr Ergebnis: " +str(produkt))

    else:
        eingabe = int(input("Zahl 1: "))
        eingabe2 = int(input("Zahl 2: "))
        quotient = eingabe / eingabe2

        print("Ihr Ergebnis:  " +str(quotient))
    if(input ("exit")== "exit"):
        run = False
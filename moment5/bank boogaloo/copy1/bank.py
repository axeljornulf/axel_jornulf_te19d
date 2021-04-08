saldo = 1000

while True:
    menu = ("\n=========================="
            "\n-    Suckiwacki Banken   -"
            "\n-  Välkommen till menyn  -"
            "\n=========================="
            "\nSaldo: {} kr"
            "\n1. Visa transaktioner"
            "\n2. Insätta summa"
            "\n3. Utdra summa"
            "\n4. Annullera konton "
            "\nExit (0)."
            "\nVad är ditt val?: ")

    choice = int(input(menu))

    if choice == 0:
        break

    elif choice == 1:
        print("Saldot är {} kr".format(saldo))

    elif choice == 2:
        deposit = int(input("Ange hur mycket du vill insätta: "))
        if deposit > 0:
            saldo += deposit
        else:
            print("Insättningen måste vara större än 0.")

    elif choice == 3:
        withdraw = int(input("\nAnge hur mycket du vill ta ut: "))
        if withdraw <= saldo and withdraw >= 0:
            saldo -= withdraw
        elif withdraw < 0:
            print("Utdraget måste vara större än 0")
        else:
            print("Utdraget kan inte vara större än saldot. Medges ej.")

    else:
        print("Felaktiv val.")

print("Välkommen åter.")
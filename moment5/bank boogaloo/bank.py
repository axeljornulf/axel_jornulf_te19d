from functions_sucki import *

read_file()

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
            "\nVad är ditt val?: ").format(balance())

    choice = validate_int(menu, "Felaktig inmatning.")

    if choice == 0:
        break

    elif choice == 1:
        print(print_transactions())

    elif choice == 2:
        deposit = validate_int("Ange hur mycket du vill insätta: ", "Inmatning medges ej.")
        if deposit > 0:
            add_transaction(deposit, True)
        else:
            print("Insättningen måste vara större än 0.")

    elif choice == 3:
        withdraw = validate_int("\nAnge hur mycket du vill utdra: ", "Inmatning medges ej.")
        if withdraw <= balance() and withdraw >= 0:
            add_transaction(-withdraw, True)
        elif withdraw < 0:
            print("Utdraget måste vara större än 0")
        else:
            print("Utdraget kan inte vara större än saldot. Medges ej.")

    elif choice == 4:
        os.remove(filename)
        transactions.clear()
        read_file()

    else:
        print("Felaktiv val.")

print("Välkommen åter.")
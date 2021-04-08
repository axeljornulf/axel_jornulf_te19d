from function_sucki import *
read_file()

#loop

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
            "\nVad är ditt val?: ").format(saldo())

    choice = validate_int(menu, "Inamtningen är felaktig.")

    if choice == 0:
        break

    elif choice == 1:
        print(transactions())

    elif choice == 2:
        print("\nHär insätter du pengar")
        deposit = validate_int("\nAnge hur mycket du vill insätta: ", "Inmatningen är felaktig.")
        if deposit > 0:
            add_transaction(deposit, True)
        else:
            print("Insättningen kan inte vara större än 0.")

    elif choice == 3:
        print("\nHär drar du ut pengar")
        withdraw = validate_int("\nAnge hur mycket du vill dra ut: ", "Inamtningen är felaktig.")
        if withdraw <= saldo() and withdraw >= 0:
            add_transaction(-withdraw, True)
        elif withdraw < 0:
            print("Uttaget måste vara större än 0.")
        else:
            print("Uttaget kan inte vara större än saldot. Medges ej.")

    elif choice == 4:
        os.remove(filename)
        transactions.clear()
        read_file()

    else:
        print("Felaktig val.")

print("Välkommen åter.")
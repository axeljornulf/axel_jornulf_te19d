def balance():
    balance = 0
    for i in transactions:
        balance += i
    return balance

def validate_int(output, error_msg):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_msg)
    return value

def print_transactions():
    rad = 0
    summa = 0
    header = ("\nDina transaktioner:"
        "\n{:>3} {:>12} {:>12}"
        "\n-----------------------------").format("Nr", "Händelser", "Saldo")
    print(header)

    for i in transactions:
        rad += 1
        summa += i
        print("{:>2}. {:>9} kr {:>9} kr".format(rad, i, summa))

transactions = []
transactions.append(1000)

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
            transactions.append(deposit)
        else:
            print("Insättningen måste vara större än 0.")

    elif choice == 3:
        withdraw = validate_int("\nAnge hur mycket du vill utdra: ", "Inmatning medges ej.")
        if withdraw <= balance() and withdraw >= 0:
            transactions.append(-withdraw)
        elif withdraw < 0:
            print("Utdraget måste vara större än 0")
        else:
            print("Utdraget kan inte vara större än saldot. Medges ej.")

    else:
        print("Felaktiv val.")

print("Välkommen åter.")
from config import *

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

def check_if_file_exists():
    try:
        with open(filename, "x"):
            print("Fil har skapats")

        with open(filename, "a") as f:
            f.write("{}\n".format(1000))
    except:
        return

def read_file():

    check_if_file_exists()

    with open(filename) as f:
        for lines in f:
            if len(lines) > 0:
                transactions.append(int(lines))

def add_transaction(transaction, toFile = False):
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)

def write_transaction_to_file(transaction):
    with open(filename, "a") as f:
        f.write("{}\n".format(transaction))
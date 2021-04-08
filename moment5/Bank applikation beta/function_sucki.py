from config import *


def saldo():
    sucki = 0
    for i in transactions:
        sucki += i
    return sucki

def validate_int(output,error_msg):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_msg)
    return value


def transactions():
    line = 0
    saldo = 0
    header = ("\nDina transaktioner:"
              "\n{:>3} {:>12} {:>12}"
              "\n-----------------------------").format("Nr", "Händelser", "Saldo")

    for t in transactions:
        line += 1
        saldo += t
        print("{:>2}. {:>9} kr {:>9} kr".format(line, t, saldo))

    return header

def check_file_exists():
    try:
        with open(filename, "x"):
            print("Fil har skapats.")
        with open(filename, "a") as f:
            f.write("{}\n".format(1000))
    except:
        return

def read_file():
    check_file_exists()

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                add_transaction(int(rad))


def add_transaction(transaction, toFile = False):
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)

def write_transaction_to_file(transaction):
    with open(filename, "a") as f:
        f.write("{}\n".format(transaction))
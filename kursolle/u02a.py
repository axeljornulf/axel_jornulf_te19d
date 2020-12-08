'''
    Fördjupning:
    Bygg ut applikationen så att sparbelopp, antal år och
    räntan går att mata in till systemet. Räntan vill
    jag ange som ett decimaltal.
'''

# Formeln: sparbelopp * ränta^år

sparbelopp = int(input("Ange sparbelopp: "))
ränta = float(input("Ange ränta: "))
år = int(input("Ange år: "))

print(f"Efter {år} år, med {sparbelopp} kr som sparbelopp och {ränta} som ränta, får jag {round(sparbelopp*ränta**år,1)} kr på kontot.")
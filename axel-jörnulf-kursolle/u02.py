'''
    Ulf har satt in 10 000kr på ett konto med 3 % årlig ränta,
    hur mycket pengar finns på kontot efter 15 år? Inga fler insättningar görs.
'''

# Löser med förändringsfaktor: 10000 x 1,03^15

sparbelopp = 10000
rent = 1.03
år = 15

print(f"Efter 15 år har Ulf {round(sparbelopp*rent**år,2)} kr på konton.")
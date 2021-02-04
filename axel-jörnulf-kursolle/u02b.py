'''
    Fördjupning:
    Om Ulf sätter in 0kr på kontot från början, nysparar 15000kr/år (barn-/studiebidraget) till 6.5% ränta i
    18 år så har han 486151kr på kontot. Detta utgår ifrån att han inte får ränta på detta års insatta pengar,
    men på alla pengar som fanns där när året började.
'''

# Formeln: bidrag + ränta^år

bidrag = 0

for i in range(1,18):
    bidrag += 15000

test = bidrag * 1.065**i

print(test)
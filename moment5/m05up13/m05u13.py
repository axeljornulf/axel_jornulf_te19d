import pprint
pp = pprint.PrettyPrinter(indent=2)

res = []

#Läser in alla värden
with open('provpoäng.txt') as f:
    for i in f:
        i = i.strip()
        i = i.split('|')
        x = {'name': i[0], 'points': int(i[1])}
        res.append(x)

x_min = x_max = res[0]
summan = 0

#Loopar genom listan
for i in res:
    summan += i['points']
    if i['points'] > x_max['points']:
        x_max = i
    if i['points'] < x_min['points']:
        x_min = i

#Sorterar det högsta
res_sorted = sorted(res,key=lambda i: i['points'], reverse=True)

#Skriver till fil
with open('output.txt','w') as fw:
    fw.write("Sorterade listan, högsta ligger överst.")
    for i in res_sorted:
        fw.write(f"\n{i['points']:2d} | {i['name']}")
    fw.write(f"\n== Summering ==\nMax resultat: {x_max['name']}, {x_max['points']} poäng."
             f"\nMin resultat: {x_min['name']}, {x_min['points']} poäng."
             f"\nMedelvärdet: {summan/len(res):.2f}")

#Skriver ut innehållet
with open('output.txt') as f:
    print(f.read())
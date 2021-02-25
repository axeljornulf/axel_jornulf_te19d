import pprint
pp = pprint.PrettyPrinter(indent=2)

res = []

with open('provpoäng.txt') as f:
    for i in f:
        i = i.strip()
        i = i.split('|')
        x = {'name': i[0], 'points': int(i[1])}
        res.append(x)

print('Sorterade lista:')
pp.pprint(sorted(res,key=lambda i: i['points'],reverse=True))
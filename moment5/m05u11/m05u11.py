start = startsaldo = 10000
rent = 1.03
file = 'suckiwacki.txt'

with open(file,'w') as f:
    for year in range(1,16):
        start *= rent
        f.write(f"{year:2d}|{start:.0f} kr|{((start/startsaldo)-1)*100:5.2f}%\n")

with open(file) as f:
    print(f.read())
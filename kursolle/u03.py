def loop_table(a,b,c):
    listRange = range(abs(a), abs(b), c)

    for i in listRange:
        print()
        for j in listRange:
            product = i * j
            print(f"{product : < 4}", end="")

    if a < 0 or b < 0:
        print()
        print("Talet som ni har matat in är negativt, och går inte printa ut.")

faktor1 = int(input("Ange faktor 1: "))
faktor2 = int(input("Ange faktor 2: "))

if faktor1 > faktor2:
    faktorC = int(input("Ange step värde: "))
    print("Multiplikationstabell:")
    loop_table(faktor1, faktor2,faktorC)
else:
    print("Multiplikationstabell: ")
    loop_table(faktor1, faktor2, 1)

#Gammalt skit
'''

for i in range(1, 11):
    print()
    addx = int(input(f"Ange tal för tabell {i}: "))
    for j in range(1, 11):
        print(addx*j, end=" ")
        if addx*j == 225:
            print("Tabellen innehåller produkten av 15x15, och kan inte vara större än den!")
            break
    print()


print("Multiplikationstabell", end="")
for i in range(1,11):
    print()
    for j in range(1,11):
        print(i*j, end=" ")
'''
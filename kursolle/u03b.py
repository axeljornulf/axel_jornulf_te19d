def loop(a):
    a = a + 1
    variable = 0
    for i in range(1,a):
        variable += 1
        for j in range(1, a):
            print("Multiplikationstabell upp till", variable, "x", variable, ":")
            print(i * j)

tabell = int(input("Ange multiplikationstabell: "))

loop(tabell)
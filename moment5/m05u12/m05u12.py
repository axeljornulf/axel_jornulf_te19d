tal = []

file = "cum.txt"

def summary():
    summa = 0
    for i in tal:
        summa += i
    return summa

def maximum():
    högsta = tal[0]
    for i in tal:
        if i > högsta:
            högsta = i
    return högsta

def minimum():
    lägsta = tal[0]
    for i in tal:
        if i < lägsta:
            lägsta = i
    return lägsta

f = open(file,'w')
f.close()

with open(file,'a') as f:
    while True:
        theInput = int(input("Ange ett heltal mindre än 8: "))
        if theInput == 8:
            f.write("Talet 8 är inmatad, programmet avbryts.\n")
            break
        tal.append(theInput)
        f.write(f"Hela lista: {tal}, min:{minimum()}, max:{maximum()}, summa:{summary()}.\n")

    f.write(f"Hela lista: {tal}, min:{minimum()}, max:{maximum()}, summa:{summary()}.\n")

print("\n\nUtskriften av filen")
with open(file) as f:
    print(f.read())
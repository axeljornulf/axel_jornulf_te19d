import time

antalArea = []
antalSideA = []
antalSideB = []
antalHeight = []
volume = []

def geometrical_calculator():
    for j, v in zip(antalArea, antalHeight):
        volume.append(j * v)

    print()
    print("Höjden | Volymen")
    print("-----------------")

    for i, y in zip(antalHeight, volume):
        print('{:>8}'.format(f"{i} |") + '{:>8}'.format(y))  # i = höjden

    print()
    print("Dina beräkningar: ")
    print("Area:", antalArea, "ae")
    print("Sida A:", antalSideA, "le")
    print("Side B:", antalSideB, "le")
    print("Height:", antalHeight, "le")

def omkrets(a,b):
    return 2*(a+b)

def area(a,b):
    return a*b

def inmatning():
    processor = True
    while processor == True:
        try:
            sideA = int(input("Ange rektangelns första sida: "))
        except ValueError:
            print("Ange ett heltal!")
            time.sleep(3)
            continue
        antalSideA.append(sideA)

        try:
            sideB = int(input("Ange rektangelns andra sida: "))
        except ValueError:
            print("Ange ett heltal!")
            time.sleep(3)
            continue
        antalSideB.append(sideB)

        try:
            h = int(input("Ange höjden för rätblocken: "))
        except ValueError:
            print("Ange ett heltal!")
            time.sleep(3)
            continue
        if h >= 10:
            h = 11
        elif h < 0:
            print("Höjden kan inte vara negativt!")
            h = 1
        antalHeight.append(h)

        print("Omkretsen av fyrhörningen med sidorna {} och {} är {}".format(sideA,sideB,omkrets(sideA,sideB)))
        print("Arean av samma fyrhörning är {}".format(sideA,sideB,area(sideA,sideB)))

        print()
        askUser = input("Vill du ange flera räkningar? Y/N: ")

        if askUser == "Y" or askUser == "y":
            continue
        elif askUser == "N" or askUser == "n":
            break
        else:
            print("Ange Y eller N!")
            continue

inmatning()

geometrical_calculator()
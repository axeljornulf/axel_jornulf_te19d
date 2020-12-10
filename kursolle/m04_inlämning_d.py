import time

print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")

processor = True

antalArea = []
antalSideA = []
antalSideB = []
antalHeight = []
volume = []

def geometrical_calculator(height):
    while processor != False:

        for sum1,sum2 in zip(antalSideA,antalSideB):
            antalArea.append(sum1 * sum2)

        '''
        print()
        print(f"Rektangeln har sidorna {sideA} och {sideB} le, vilketgör att arean är {area} ae")
        
        if sideA == sideB:
            print()
            print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")
        '''


        print()
        print("Höjden | Volymen")
        print("-----------------")
        for i in antalHeight:  # i = höjden
            for j,v in zip(antalArea, antalHeight):
                volume.append(j * v)
            for y in volume:
                print('{:>8}'.format(f"{i} |") + '{:>8}'.format(y))

        print()
        askUser = input("Continue? Y/N: ")

        if askUser == "N" or askUser == "n":
            print()
            print("Dina beräkningar: ")
            print("Area:", antalArea, "ae")
            print("Sida A:", antalSideA, "le")
            print("Side B:", antalSideB, "le")
            print("Height:", antalHeight, "le")
            break
        elif askUser == "Y" or askUser == "y":
            continue
        else:
            print("Ange Y eller N!")
            print("Automatiskt stänger ner.")
            break

n = 0

while n != 3:
    try:
        a = int(input("Ange rektangelns första sida: "))
    except ValueError:
        print("Ange ett heltal!")
        time.sleep(3)
        continue
    antalSideA.append(a)

    try:
        b = int(input("Ange rektangelns andra sida: "))
    except ValueError:
        print("Ange ett heltal!")
        time.sleep(3)
        continue
    antalSideB.append(b)

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
        h = 2
    else:
        h += 1
    antalHeight.append(h)
    n += 1

geometrical_calculator(h)
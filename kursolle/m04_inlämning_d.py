import time

print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")

processor = True

antalArea = []
antalSideA = []
antalSideB = []
antalHeight = []
volume = []

def geometrical_calculator():
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

        for j, v in zip(antalArea, antalHeight):
            volume.append(j * v)

        print()
        print("Höjden | Volymen")
        print("-----------------")

        for i,y in zip(antalHeight,volume):
            print('{:>8}'.format(f"{i} |") + '{:>8}'.format(y)) # i = höjden

        print()
        print("Dina beräkningar: ")
        print("Area:", antalArea, "ae")
        print("Sida A:", antalSideA, "le")
        print("Side B:", antalSideB, "le")
        print("Height:", antalHeight, "le")
        break

while processor == True:
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
        h = 1
    antalHeight.append(h)

    print()
    askUser = input("Vill du ange flera räkningar? Y/N: ")

    if askUser == "Y" or askUser == "y":
        continue
    elif askUser == "N" or askUser == "n":
        geometrical_calculator()
        break
    else:
        print("Ange Y eller N!")
        continue

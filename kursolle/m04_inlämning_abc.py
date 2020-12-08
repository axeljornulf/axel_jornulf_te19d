import time

print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")

processor = True

antalArea = []
antalSideA = []
antalSideB = []

while processor != False:
    try:
        sideA = int(input("Ange rektangelns första sida: "))
    except ValueError:
        print("Ange ett heltal!")
        time.sleep(3)
        continue

    try:
        sideB = int(input("Ange rektangelns andra sida: "))
    except ValueError:
        print("Ange ett heltal!")
        time.sleep(3)
        continue

    try:
        height = int(input("Ange höjden för rätblocken: "))
    except ValueError:
        print("Ange ett heltal!")
        time.sleep(3)
        continue
    if height >= 10:
        height = 11
    elif height < 0:
        print("Höjden kan inte vara negativt!")
        height = 2
    else:
        height += 1

    antalSideA.append(sideA)
    antalSideB.append(sideB)

    area = sideA * sideB

    antalArea.append(area)

    print()
    print(f"Rektangeln har sidorna {sideA} och {sideB} le, vilketgör att arean är {area} ae")

    if sideA == sideB:
        print()
        print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")

    print()
    print("Höjden | Volymen")
    print("-----------------")
    for i in range(1,height): # i = höjden
        v = area * i
        print('{:>8}'.format(f"{i} |") + '{:>8}'.format(v))

    print()
    askUser = input("Continue? Y/N: ")

    if askUser == "N" or askUser == "n":
        print()
        print("Dina beräkningar: ")
        print("Area:", antalArea, "ae")
        print("Sida A:", antalSideA, "le")
        print("Side B:", antalSideB, "le")
        break
    elif askUser == "Y" or askUser == "y":
        continue
    else:
        print("Ange Y eller N!")
        print("Automatiskt stänger ner.")
        break
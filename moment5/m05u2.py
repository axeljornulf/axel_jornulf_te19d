import math

def omkrets(r):
    omkretsen = 2*r*math.pi
    print(f"Om cirkelns radie är {r} blir omkretsen {round(omkretsen,3)} cm")

def area(r):
    area = (r**2)*math.pi
    print(f"Arean är också då {round(area,3)} cm^2")

r = int(input("Ange cirkelns radie: "))

omkrets(r)
area(r)
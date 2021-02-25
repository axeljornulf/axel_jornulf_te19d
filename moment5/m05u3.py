import math

def omkrets(r):
    omkretsen = 2*r*math.pi
    return omkretsen

def area(r):
    area = (r**2)*math.pi
    return area

r = int(input("Ange cirkelns radie: "))

print("Om radien på cirkeln är {} cm, är omkretsen då {} cm och arean {} cm^2".format(r,round(omkrets(r),1),round(area(r),1)))
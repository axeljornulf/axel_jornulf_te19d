from m05u5f import omkrets as o #importerar omkretsens funktion från m05u5f.py
from m05u5f import area as a #importerar areans funktion från m05u5f.py

radie = int(input("Ange cirkelns radie: ")) #användaren ska ange cirkelns radie

print("Om radien på cirkeln är {} cm, är omkretsen då {} cm och arean {} cm^2".format(radie,round(o(radie),1),round(a(radie),1)))
#printar ut resultaten där {} ersätts med funktionerna, koden avrundar också räkningarna med hjälp av round()
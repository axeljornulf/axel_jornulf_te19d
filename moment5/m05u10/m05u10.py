with open('utskrift.txt', 'w') as fw: #kodet öppnar txt filen för att skrivas, 'w' står just för 'write'
    fw.write('''
    1 2 3
    4 5 6
    7 8 9
    ''') #talet skrivs in i detta stil, d.v.s. på varandra.

    fw.write('\nHär var det rutigt!') #skapar en ny line med text inne i utskrift.txt

with open('utskrift.txt') as fr: #kodet öppnar filen igen för läsning
    print(fr.read()) #printar innehållet av vår f.d. tomma fil
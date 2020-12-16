import random as rnd

def skapaKortlek():
    kortNummer = [i for i in range(2,11)] # list comprehension
    klädkort = ["J","Q","K","A"]
    kortNummer += klädkort
    lek = 4*kortNummer
    blandaKort(lek)
    
    return lek

# blanda kort

def blandaKort(lek):
    return rnd.shuffle(lek)
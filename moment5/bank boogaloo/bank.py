from functions_sucki import *
from tkinter import *
from tkinter import messagebox

read_file()

#while True:

root = Tk() #Bestämmer 'root' som fönster funktionen
root.title("Suckiwacki bankapp")
root.geometry('300x300') #dimensionen av fönstret

def btn_clicked(): #Funktionen för saldo knappen

    saldot = StringVar() #Variablen visas som sträng
    saldot.set(balance()) #Saldot variablen använder sig av balance() i funtkions_sucki.py

    newWindow = Toplevel(root) #Anger ny fönster från 'root'
    newWindow.title("Saldo")
    newWindow.geometry('200x100')
    label = Label(newWindow, text="Din nuvarande saldo:") #Text
    label.grid(pady=5) #Vart texten ska vara
    saldo = Label(newWindow, textvariable=saldot) #Kallar saldot variablen
    saldo.grid(pady=5)

def btn1_clicked(): #Visa historia
    print_transactions() #Kallar funktionen
    messagebox.showinfo('Notice!', 'Check console') 
    #Herman om du läser detta, om jag måste kunna 100% tillämpa gränsnitten måste jag strukturera om hela programmet - så detta är min kompromiss för att spara på tid och hjärnceller :^(

def btn2_clicked(): #Insätta pengar
    newWindow = Toplevel(root)
    newWindow.title("Deposit")
    newWindow.geometry('300x100')
    label = Label(newWindow, text="Hur mycket vill du insätta? Skriv i konsollen.")
    label.grid(pady=10)
    deposit = validate_int("Ange summa: ", "Inmatning medges ej")
    if deposit > 0:
        add_transaction(deposit, True)
    else:
        messagebox.showerror('Notice!', 'OBS: Måste vara större än 0!') #Om en error kommer up, visas detta som en pop-up fönster
        print() #'Ghost print' för att validate_int() ska fortsätta

def btn3_clicked(): #Dra ut
    newWindow = Toplevel(root)
    newWindow.title("Withdraw")
    newWindow.geometry('300x100')
    label = Label(newWindow, text="Hur mycket vill du dra ut? Skriv i konsollen.")
    label.grid(pady=10)
    withdraw = validate_int("Ange summa: ", "Inmatning medges ej")
    if withdraw <= balance() and withdraw >= 0:
        add_transaction(-withdraw, True)
    elif withdraw < 0:
        messagebox.showerror('Notice!', 'OBS: Måste vara större än 0!')
    else:
        messagebox.showerror('Utdraget kan inte vara större än saldot. Medges ej.')

#meny text
menu = Label(root, text=
            "\n=========================="
            "\n-    Suckiwacki Banken   -"
            "\n-  Välkommen till menyn  -"
            "\n=========================="
            "\nVad är ditt val?")

menu.grid(column=10,row=0)

#Knappar
btn = Button(root, text="Visa saldo", command=btn_clicked)
btn1 = Button(root, text="Visa transaktioner", command=btn1_clicked)
btn2 = Button(root, text="Insätta summa", command=btn2_clicked)
btn3 = Button(root, text="Utdra summa", command=btn3_clicked)
btn4 = Button(root, text="Annullera konton", command=choice_4) #Se funtkions_sucki.py
btn0 = Button(root, text="Exit", command=root.destroy) #Stänger hela skiten

#Knapp position
btn.grid(column=10, row=20)
btn1.grid(column=10, row=30)    
btn2.grid(column=10, row=40)    
btn3.grid(column=10, row=50)
btn4.grid(column=10, row=60)
btn0.grid(column=10, row=70)


#Old shit
'''
    choice = validate_int(menu, "Felaktig inmatning.")
    if choice == btn0:
        break

    elif choice == btn1:
        print(print_transactions())

    elif choice == 2:
        deposit = validate_int("Ange hur mycket du vill insätta: ", "Inmatning medges ej.")
        if deposit > 0:
            add_transaction(deposit, True)
        else:
            print("Insättningen måste vara större än 0.")

    elif choice == 3:
        withdraw = validate_int("\nAnge hur mycket du vill utdra: ", "Inmatning medges ej.")
        if withdraw <= balance() and withdraw >= 0:
            add_transaction(-withdraw, True)
        elif withdraw < 0:
            print("Utdraget måste vara större än 0")
        else:
            print("Utdraget kan inte vara större än saldot. Medges ej.")

    else:
        print("Felaktiv val.")
'''
root.mainloop()

#print("Välkommen åter.")
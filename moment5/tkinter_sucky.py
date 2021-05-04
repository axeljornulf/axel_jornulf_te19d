from tkinter import *

window = Tk() #deklarerar Tk() funktionen från tkinter paketet med variablen "window"

window.title("Welcome to Sucky app") #anger titel för fönstret

window.geometry('350x200') #sätter vilken storlek fönstret ska vara när man startar programmet

lbl = Label(window, text="can i habe hamburger?", font=("Arial Bold", 16)) #skapar en text segment i fönstret vi deklarerade. Ger också vilket text font och storlek i pixlar.

lbl.grid(column=0,row=0) #vart i fönstret skall texten vara

txt = Entry(window,width=10) #skapar ett fönster där man kan skriva saker i

txt.grid(column=1, row = 0) #vart skrivs fönstret ska vara

def clicked(): #funktion som skapar en händelse när man klickar på knappen
    res = "Hello gamers welcome to " + txt.get() #variabel som ändrar label texten och hämtar txt variablen.
    lbl.configure(text=res) #ändrar texten med 'res' variablen.

btn = Button(window, text="Click 4 money", bg="blue", fg="yellow", command=clicked) #skapar en knapp i fönstret och ger bakgrunds färgen blå och förgrund gul. Anger sen kommandot med funktionens namn.

btn.grid(column=2, row=0) #vart i fönstret skall knappen vara

window.mainloop() #loopar kodet tills fönstret stängs
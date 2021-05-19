import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#tomma listor
gender = []
genderMF = []
ålder = []
ndd = []
nddDate = []
rdc = []
rdcDate = []
regiondata = []

def validate_choice(output, msg): #Funktionen kollar kodet för fel
    while True:
        try: #analyserar villkoret
            value = int(input(output))
            break
        except:
            print(msg) #printar error meddelande om man väljer fel
    return value

def choice_1(): #val 1

    lbl = "Smittade \nMän", "Män i \nintensivvård", "Smittade \nKvinnor", "Kvinnor i \nintensivvård" #etiketter

    df = pd.read_csv(r'C:\Users\Axel\Documents\GitHub\axel_jornulf_te19d\Dataprojekt\Gender_Data.csv') #läser csv filet

    #summerar smittning
    mänSmittad = df['Total_Cases'].iloc[0:1].sum()
    mänIntensivvård = df['Total_ICU_Admissions'].iloc[0:1].sum()
    
    kvinnorSmittad = df['Total_Cases'].iloc[1:2].sum()
    kvinnorIntensivvård = df['Total_ICU_Admissions'].iloc[1:2].sum()

    #sätter in i listan
    gender.append(mänSmittad)
    gender.append(mänIntensivvård)
    gender.append(kvinnorSmittad)
    gender.append(kvinnorIntensivvård)

    #skapar plot
    plt.pie(gender, labels=lbl, autopct='%1.1f%%')
    plt.title("COVID-19 Smittfall och intensivvård mellan män och kvinnor")
    plt.axis('equal')
    plt.show()

    #villkorlighet för ytterligare funktion
    ask = ("\nVisa åldergrupp?"
    "\n1 - Ja"
    "\n2 - Nej"
    "\n"
    )

    while True:
        val = validate_choice(ask, "Felaktig val.")

        if val == 1:
            gender.clear()
            sub_choice1()
            break
        elif val == 2:
            gender.clear() #rensar listan så att den inte fylls på med samma data
            break
        else:
            print("Felaktig val.")


def sub_choice1(): #Delar upp i åldersgrupp via val 1
    lbl = "0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90+" #ålder etiketter

    df = pd.read_csv(r'C:\Users\Axel\Documents\GitHub\axel_jornulf_te19d\Dataprojekt\National_Total_Deaths_by_Age_Group.csv')

    #tillsätter data i lista
    for i in df['Total_Cases']:
        ålder.append(i)
    
    #skapar plot
    plt.bar(lbl, ålder, width=.4, color=["pink", "red", "blue", "green", "yellow", "purple", "cyan", "orange", "indigo", "black"])
    plt.title("Totala smitt räkning bland åldersgrupp")
    plt.show()

    #Villkor
    inputThis = "Tryck på 0 för att återgå till huvudmenyn.\n"

    while True:
        val = validate_choice(inputThis, "Felaktig input.")

        if val == 0:
            ålder.clear() #rensar listan så att den inte fylls på med samma data
            break
        else:
            print("Felaktig inmatning.")
    

def choice_2(): #funktionen visar nationala dödsräkning

    df = pd.read_csv(r'C:\Users\Axel\Documents\GitHub\axel_jornulf_te19d\Dataprojekt\National_Daily_Deaths.csv')
    df2 = pd.read_csv(r'C:\Users\Axel\Documents\GitHub\axel_jornulf_te19d\Dataprojekt\Regional_Daily_Cases.csv')

    #tillsätter data i listor
    for i in df["National_Daily_Deaths"]:
        ndd.append(i)

    for j in df["Date"]:
        nddDate.append(j)

    for y in df2["Sweden_Total_Daily_Cases"]:
        rdc.append(y)

    for x in df2["Date"]:
        rdcDate.append(x)

    #deklarerar variabler med listorna för enkelhet
    axisX1 = nddDate
    axisY1 = ndd

    axisX2 = rdcDate
    axisY2 = rdc

    #skapar plots
    plt.subplot(2,1,1)
    plt.plot(axisX1, axisY1)
    plt.xticks(df.Date[::40], rotation = 15)
    plt.title('National dödsräkning och jämförelse med smitt räkning regions räkning')
    plt.ylabel('Dödsräkning')

    plt.subplot(2,1,2)
    plt.plot(axisX2, axisY2)
    plt.xticks(df2.Date[::40], rotation = 15)
    plt.xlabel('Datum')
    plt.ylabel('Smitträkning')

    plt.show()

    #Villkor
    ask = ("\nVisa smitt räkning för varje region?"
           "\n1. Ja"
           "\n2. Nej\n")

    while True:
        val = validate_choice(ask, "Felaktig Inmatning.")

        if val == 1:
            nddDate.clear()
            ndd.clear()
            rdcDate.clear()
            rdc.clear()
            sub_choice2()
            break
        elif val == 2:
            nddDate.clear()
            ndd.clear()
            rdcDate.clear()
            rdc.clear() #rensar listor så att den inte fylls på med samma data
            break
        else:
            print("Felaktig inmatning!")


def sub_choice2(): #Funktionen visar smitträkningen i varje region

    df = pd.read_csv(r'C:\Users\Axel\Documents\GitHub\axel_jornulf_te19d\Dataprojekt\Regional_Daily_Cases.csv') #Läser in csv fil

    #etiketter för landskap och städer
    bar_label = ["Blekinge", "Dalarna", "Gotland", "Gävleborg", "Halland", "Jämtland Härjedalen", "Kalmar", "Jönköpning", "Kronoberg", "Norrbotten", "Skåne", "Stockholm", "Sörmland", "Uppsala", "Värmland", "Västerbotten", "Västernorrland", "Västmanland", "Västra Götaland", "Örebro", "Östergötland"]

    #tilläger data i lista
    data = df.loc["Column_Total"] = df.iloc[:, 2:23].sum(numeric_only=True, axis=0)
    for i in data:
        regiondata.append(i)
    
    #rensar listan av "nan"-value
    cleanList = [x for x in regiondata if np.isnan(x) == False]

    #skapar plot
    plt.barh(bar_label, cleanList)
    plt.title('Smitt räkning i alla regioner och vissa tärtorter')
    plt.xlabel('Smitt räkning')
    plt.show()

    #beräknar medelvärdet
    nValue = sum(cleanList)
    indexValue = 0

    for j in cleanList:
        indexValue += 1
    
    average = nValue/indexValue

    print("Ungefär", round(average), "dagliga smittning sker över landet.")

    #Villkor
    inputThis = "Tryck på 0 för att återgå till huvudmenyn.\n"

    while True:
        val = validate_choice(inputThis, "Felaktig input.")

        if val == 0:
            regiondata.clear() #rensar listan så att den inte fylls på med samma data
            break
        else:
            print("Felaktig inmatning.")


def choice_3(): #Funktionen visar förhållandet mellan dödligheten av COVID-19 och smitträkningen i landet

    df = pd.read_csv(r'C:\Users\Axel\Documents\GitHub\axel_jornulf_te19d\Dataprojekt\Regional_Daily_Cases.csv')
    df2 = pd.read_csv(r'C:\Users\Axel\Documents\GitHub\axel_jornulf_te19d\Dataprojekt\National_Daily_Deaths.csv')
    
    totalCases = df['Sweden_Total_Daily_Cases'].sum()
    totalDeaths = df2['National_Daily_Deaths'].sum()

    #Förhållandet
    ratio = totalDeaths/totalCases

    #Jämförelse graf
    caseList = df['Sweden_Total_Daily_Cases'].to_numpy() #y-axel nr 1
    deathList = df2['National_Daily_Deaths'].to_numpy() #y-axel nr 2

    for i in df2['Date']:
        nddDate.append(i)

    for j in df['Date']:
        rdcDate.append(j)

    #skapar plot
    plt.plot(rdcDate, caseList, label = "Smitträkning")
    plt.xticks(df.Date[::40], rotation = 20)

    plt.plot(nddDate, deathList, label = "Dödlighet")
    plt.xticks(df2.Date[::40], rotation = 20)

    plt.xlabel('Datum')
    plt.ylabel('Frekvens')
    plt.title('Jämförelse mellan smitt och dödlighet')
    plt.legend()
    plt.show()

    #prinar förhållander
    print('Förhållandet mellan smitt- och dödligheträkning är', round(ratio,2))

    inputThis = "Tryck på 0 för att återgå till huvudmenyn.\n"

    while True:
        val = validate_choice(inputThis, "Felaktig input.")

        if val == 0:
            nddDate.clear()
            rdcDate.clear() #rensar listor så att den inte fylls på med samma data
            break
        else:
            print("Felaktig inmatning.")


def main(): #huvudmenyn
    while True:
        mainMenu = ("\n========================="
                    "\n-   COVID-19 STATISTIK  -"
                    "\n-  Välkommen till menyn -"
                    "\n========================="
                    "\n\n1 - Gemför kön"
                    "\n2 - National dödsräkning"
                    "\n3 - Dödlighet och smitt förhållandet"
                    "\nExit. (0)"
                    "\n")

        val = validate_choice(mainMenu, "Felaktig val.") #Kollar om inamtningen är godtagbar

        if val == 0:
            break #stoppar programmet

        elif val == 1:
            choice_1() #Kön funktionen

        elif val == 2:
            choice_2() #Nationala dödsräkning

        elif val == 3:
            choice_3() #Dödlighet och smitt förhållande

        else:
            print("Felaktig val.") #printas om man väljer fel
main() #Kallar alltid denna funktion när man startar programmet
print("Välkommen åter.")
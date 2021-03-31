import PySimpleGUI as sg

def start_gui():
    sg.ChangeLookAndFeel('Reds')
    sg.SetOptions(text_justification = 'left')
    layout = [[sg.Text('Tillämpad programmering', font=('Helvetica', 35))],
              [sg.Input(key='-IN-')], [sg.Button('Counter:')]]

    window = sg.Window('Tillämpad programmering', layout, font=("Helvetica", 22))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Counter:':
            print('This button has now been pressed: ')

    event, values = window.read()

start_gui()
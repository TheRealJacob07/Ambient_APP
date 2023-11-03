import API
import PySimpleGUI as sg

def app():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Ambient API APP')],
                [sg.Text('API Key: '), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]
    layout2 = [ [sg.Text('The Current Temp is: ' + str(API.run()['tempf']))],
                [sg.Text('The Current Humidity is: ' + str(API.run()['humidity']))]  ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            apiKEY = values[0]
            window.close()
            window2 = sg.Window('test', layout2)
            event2, values2 = window2.read()
        

    window.close()
            
            

    
import api
import PySimpleGUI as sg
import time
from datetime import datetime
import os

def api_app():
    layout = [  [sg.Text('Ambient API APP')],
                [sg.Text('API Key: '), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]
    
    apiwindow = sg.Window("API", layout)
    
    while True:
        event, value = apiwindow.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        if event == 'Ok':
            key = value[0]
            os.environ['API'] = key
            break
    apiwindow.close()
            
def app():
    sg.theme('DarkAmber')
    layout2 = [ [sg.Text('The Current Temp is: ' + str(api.run()['tempf']))],
                [sg.Text('The Current Humidity is: ' + str(api.run()['humidity']))],
                [sg.Text('Last updated: ' + str(datetime.now().timestamp() * 1000 - api.run()['dateutc']))],
                [sg.Button('Cancel'), sg.Button('Refresh')]]

    
    window = sg.Window('Ambient Api', layout2)
    
    while True:
        event = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break
        if event == 'Refresh':
            window.refresh()
            
        

    window.close()
            
            

    
import api
import PySimpleGUI as sg
from datetime import datetime
import time
import sys
path =sys.path[0]

def app(json):
    sg.theme('DarkAmber')   
    
    
    layout = [  [sg.Image(str(path) + "\\" + "Aeris_WxIcons_55x55" + "\\" + json['icon']),sg.Text('The Current Temp is: ' + str(json['tempF']))],
                [sg.Text("Updated: " + json['dateTimeISO']),sg.Text('The Current Humidity is: ' + str(json['humidity'])+ '%')],
                [sg.Button('Refresh'), sg.Button('Cancel'), sg.Button('Radar')]]

    
    window = sg.Window('Ambient Weather API App', layout)
    
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break
        if event == 'Refresh':
            print('Refreshing...')
            window.close()
            app(api.run())
        if event == 'Radar':
            radar()
            
        

    window.close()
    
def radar():
    layout = [ [sg.Image(api.image_api(), key="img")]]
    window = sg.Window('Radar', layout)
    while True:
        event, values = window.Read(timeout=100)
        if event == sg.WINDOW_CLOSED:
            break
        elif event == sg.TIMEOUT_EVENT:
            window.Element('img').UpdateAnimation('tmp.gif',  time_between_frames=50)
            
def api_app():
    layout = [  [sg.Text('Ambient API APP')],
                [sg.Text('API Key: '), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]
    window = sg.Window('Window Title', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Ok':
            return values
    window.close()
    
def mac_app():
    layout = [[sg.Text('PKEY')],
              [sg.Text('API Private Key: '), sg.Input()],
              [sg.Button('OK'), sg.Button('Cancel')]]
    window = sg.Window('PKEY', layout)
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        if event == 'OK':
            return value
    window.close()    
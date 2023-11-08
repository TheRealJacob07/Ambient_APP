import api
import api
import PySimpleGUI as sg
import time
from datetime import datetime
import os
import time
from datetime import datetime
import os

def app():
    sg.theme('DarkAmber')   
    
    
    layout = [  [sg.Text('The Current Temp is: ' + str(api.run()['tempf']))],
                [sg.Text('The Current Humidity is: ' + str(api.run()['humidity']))],
                [sg.Button('Refresh'), sg.Button('Cancel')]]

    
    window = sg.Window('Ambient Weather API App', layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break
        if event == 'Refresh':
            window.refresh()
            print('Refreshing...')
            
        

    window.close()
    
def api_app():
    sg.theme('DarkAmber')   
    
    
    layout = [  [sg.Text('The Current Temp is: ' + str(api.run()['tempf']))],
                [sg.Text('The Current Humidity is: ' + str(api.run()['humidity']))],
                [sg.Button('Refresh'), sg.Button('Cancel')]]

    
    window = sg.Window('Ambient Weather API App', layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break
        if event == 'Refresh':
            window.refresh()
            print('Refreshing...')
            
        

    window.close()
    
def api_app():
    layout = [  [sg.Text('Ambient API APP')],
                [sg.Text('API Key: '), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]
    window = sg.Window('Window Title', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Ok':
            apikey = values[0]
            f = open('api.txt', 'w+t')
            f.write(apikey)
            f.close()
            print("Writing data to file")
            break
    window.close()
    
def mac_app():
    layout = [[sg.Text('MAC ADDRESS')],
              [sg.Text('Mac Adress: '), sg.Input()],
              [sg.Button('OK'), sg.Button('Cancel')]]
    window = sg.Window('MAC', layout)
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        if event == 'OK':
            macaddr = value[0]
            f = open('mac.txt', 'w+t')
            f.write(macaddr)
            print("Writing data to file")
            break
    window.close()


    
    


    
    
            
            

    
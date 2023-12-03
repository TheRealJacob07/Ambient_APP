import api
import PySimpleGUI as sg
from datetime import datetime
import time
import sys
path =sys.path[0]

def location(newrow):
    sg.theme('DarkAmber')
    
    layout = [  [sg.Text('What Location Would You Like to Use?')],
                [sg.InputText(), sg.Checkbox("PWS", key = 'p')],
                [sg.Button('Done')]]
    
    window = sg.Window('Location', layout)
    
    if newrow == 'n': 
        window.add_row([sg.Text('ERROR!!!: No Input For Location Provided')])
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Done':
            if value[0] == 'auto':
                re = ':auto'
            elif value['p'] == True:
                re = "pws_" + str(value[0])
            elif value[0] == '':
                window.close()
                location('n')
                print('ERROR!!!: No Input For Location Provided')
        window.close()
        return re    
    
        
            
def app(json, location):
    sg.theme('DarkAmber')   
    
    
    layout = [  [sg.Image(str(path) + "\\" + "Aeris_WxIcons_55x55" + "\\" + json['icon'], size = (100,100)),sg.Text('The Current Temp is: ' + str(json['tempF']) + 'F'), sg.Text('The Current Humidity is: ' + str(json['humidity']) + '%')],
                [sg.Table(api.forecast_run(location), ['High', "Low", "Humidity", "Precip"], justification= 'center', display_row_numbers= True, alternating_row_color = 'black')],
                [sg.Text("Updated: " + json['dateTimeISO'])],
                [sg.Button('Refresh'), sg.Button('Cancel'), sg.Button('Radar')]]

    
    window = sg.Window('Ambient Weather API App', layout, auto_size_text= True, element_justification='c')
    
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
        event, values = window.Read(timeout=1000)
        if event == sg.WINDOW_CLOSED:
            break
        elif event == sg.TIMEOUT_EVENT:
            window.refresh()
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
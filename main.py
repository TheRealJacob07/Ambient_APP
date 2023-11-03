import asyncio
from datetime import date
from aiohttp import ClientSession
from aioambient import API
import time
import PySimpleGUI as sg
apikey = "9e281fbcef234b959f4b5ff30dbb7af0666af6e63a2749e4b061498402fb386f"
devkey = "945ff3ad565840198a0bb530c1b4f3d64eaf83beb7844e8eab0cd1bf5e350782"
mac = "BC:FF:4D:0F:85:AB"
async def main() -> None:
    api = API(apikey, devkey)
    data = await api.get_device_details(mac)
    return data
def run():
    result = asyncio.run(main())
    smallResult = result[0]
    return smallResult

def clearScreen():
    print("\n" * 100)
    

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Ambient API APP')],
            [sg.Text('API Key: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
layout2 = [ [sg.Text('The Current Temp is: ' + run()['tempf'])],
            [sg.Text('The Current Humidity is: ' + run()['humidity'])]  ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
        apikey = values[0]
    

window.close()
        
        


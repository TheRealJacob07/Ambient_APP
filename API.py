import asyncio
from datetime import date
from aiohttp import ClientSession
from aioambient import API
import window
import time
import os
import PySimpleGUI as sg
devkey = "945ff3ad565840198a0bb530c1b4f3d64eaf83beb7844e8eab0cd1bf5e350782"
async def main() -> None:
    api = API(str(os.environ['API']), devkey)
    data = await api.get_device_details(str(os.environ['MAC']))
    return data
def run():
    result = asyncio.run(main())
    smallResult = result[0]
    return smallResult

def clearScreen():
    print("\n" * 100)
    




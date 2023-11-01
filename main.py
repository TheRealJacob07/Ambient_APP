import asyncio
from datetime import date
from aiohttp import ClientSession
from aioambient import API
import time
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
        
        
        


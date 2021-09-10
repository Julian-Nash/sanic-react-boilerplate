import asyncio
import datetime


async def utctime(request, ws):

    data = await ws.recv()
    print("Received: " + data)

    await asyncio.sleep(1)

    while True:
        await ws.send(datetime.datetime.utcnow().isoformat())
        await asyncio.sleep(0.1)

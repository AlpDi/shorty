import subprocess



import asyncio
from websockets.server import serve


def formatWSS(num):
    if int(num) < 10:
        return "0.0" + num
    else:
        return "0." + num


async def echo(websocket):
    async for message in websocket:
        subprocess.run(["nircmdc.exe", "setappvolume", "Spotify.exe", formatWSS(message)], shell=True)


async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())


""" i = 0.1

while True:
    subprocess.run(["nircmdc.exe", "setappvolume", "Spotify.exe", str(i)], shell=True)
    if i >= 1:
        i = 0.1
    i += 0.1 """
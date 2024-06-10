import subprocess



import asyncio
from websockets.server import serve


apps = ["Spotify.exe", "Discord.exe", "CS2.exe", "Destiny2.exe", "Minecraft.exe", "Firefox.exe"]


def formatWSS(num):

    if int(num) < 10:
        return "0.0" + num
    else:
        return "0." + num


async def echo(websocket):
    async for message in websocket:
        subprocess.run(["nircmdc.exe", "setappvolume", apps[int(message.split(",")[0]) - 1], formatWSS(message.split(",")[1])], shell=True)


async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())



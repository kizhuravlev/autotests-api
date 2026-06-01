import asyncio
import websockets
from websockets import ServerConnection

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for i in range(1, 6):
            responce = f"{i} Сообщение пользователя: {message}"
            await websocket.send(responce)
       

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())
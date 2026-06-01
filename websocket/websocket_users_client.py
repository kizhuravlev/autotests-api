import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = 'Initial message'
        print(f"Sended message {message}")
        await websocket.send(message)

        for _ in range(1, 6):
            responce = await websocket.recv()
            print(f"Responce from server: {responce}")

asyncio.run(client())

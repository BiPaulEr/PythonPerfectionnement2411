import asyncio
import time

async def worker():
    print("Je suis en train de travailler")
    time.sleep(2)
    print("J'ai finis de travailler")

async def main():
    print("WORKER 1")
    await worker()
    print("WORKER 2")
    await worker()

asyncio.run(main())
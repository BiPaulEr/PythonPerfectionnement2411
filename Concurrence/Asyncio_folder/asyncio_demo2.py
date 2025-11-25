import asyncio
import time

async def worker(name):
    print(name, "Je suis en train de travailler")
    await asyncio.sleep(2)
    print(name, "J'ai finis de travailler")
    return 42

async def main():
    print("WORKER 1")
    t1 = asyncio.create_task(worker("1"))
    print("WORKER 2")
    t2 = asyncio.create_task(worker("2"))
    await t1
    print(t1.result())
    await t2

asyncio.run(main())
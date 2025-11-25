import asyncio, aiofiles
import time, os

async def read_file(file_name):
    async with aiofiles.open(file_name) as file:
        content = await file.read()
        return(f"Contents of {file_name} is {content}")

async def main():
    files = [os.path.join(os.path.dirname(__file__), "fichier.txt")]*5
    tasks = []
    results = await asyncio.gather(*(read_file(file) for file in files))
    print(results)

asyncio.run(main())

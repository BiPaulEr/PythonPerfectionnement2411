import asyncio
import time, random

async def read_file(file_name):
    r = random.randint(1, 10)
    print(f"{file_name} needs to wait {r}")
    await asyncio.sleep(r)
    print(f"{file_name} read successfully")
    return(f"Contents of {file_name}")

async def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    for task in asyncio.as_completed((read_file(file) for file in files)):
        result = await task
        print(result)

asyncio.run(main())

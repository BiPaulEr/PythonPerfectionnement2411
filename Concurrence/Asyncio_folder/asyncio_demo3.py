import asyncio
import time

async def read_file(file_name):
    await asyncio.sleep(4)  # Simulate the delay of reading a file
    print(f"{file_name} read successfully")
    return(f"Contents of {file_name}")

async def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    tasks = []
    results = await asyncio.gather(*(read_file(file) for file in files))
    print(results)
    results = await asyncio.gather(read_file("file1.txt"), read_file("file2.txt"))
    print(results)

asyncio.run(main())

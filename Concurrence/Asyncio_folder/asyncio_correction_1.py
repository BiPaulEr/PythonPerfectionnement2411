import asyncio
import time

async def read_file(file_name):
    await asyncio.sleep(4)  # Simulate the delay of reading a file
    print(f"{file_name} read successfully")
    return(f"Contents of {file_name}")

def print_result(task):
    print(task.result())

async def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    tasks = []
    for file in files:
        task = asyncio.create_task(read_file(file))
        task.add_done_callback(print_result)
        tasks.append(task)
    for task in tasks:
        await task
    

asyncio.run(main())
import asyncio
import time, random

async def do_work(duration):
    await asyncio.sleep(duration)
    if random.randint(0, 100) < 30:
        raise ValueError(f"{duration} seconds tasks has an error")
    return f"Finished work in {duration} seconds"

async def main():
    durations =  [3, 1, 4, 2]
    tasks = [do_work(duration) for duration in durations]
    for task in asyncio.as_completed(tasks):
        try:
            result = await task
        except Exception as e:
            print(f"{e}")
        else:
            print(result)
        
        

 
asyncio.run(main())
import asyncio
import time, random

async def fetch_weather(city):
    await asyncio.sleep(1)  # Simulez un délai de réseau
    temperature = random.randint(15, 25)  # Générez une température aléatoire
    print(f"Température pour {city} : {temperature}°C")
    return {"ville": city, "température": temperature}

async def main():
    files = ["City1.txt", "City2.txt", "City3.txt"]
    results = await asyncio.gather(*(fetch_weather(file) for file in files))
    print(results) #[{'ville': 'City1.txt', 'température': 15}, {'ville': 'City2.txt', 'température': 24}, {'ville': 'City3.txt', 'température': 24}]
    print(sum(map(lambda dictionnaire: dictionnaire["température"], results))/3)
asyncio.run(main())
import asyncio

class MonAsyncContextManager:
    async def __aenter__(self):
        print("Entrée dans le contexte asynchrone")
        return self  
    async def __aexit__(self, exc_type, exc_value, traceback):
            print("Sortie du contexte asynchrone")

async def main():
    async with MonAsyncContextManager():
        print("Faisons quelque chose d'asynchrone ici")

asyncio.run(main())
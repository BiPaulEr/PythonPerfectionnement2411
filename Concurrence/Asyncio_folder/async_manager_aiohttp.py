import asyncio, aiohttp

class AioHttpSessionManager:
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self.session
    async def __aexit__(self, exc_type, exc_instance, traceback):
        await self.session.close()
        return True
        
async def main():
    async with AioHttpSessionManager() as session:
        headers = {"Accept": "text/plain"}
        async with session.get("https://icanhazdadjoke.com", headers = headers) as response:
            if response.status == 200:
                result = await response.text()
                print(result)

asyncio.run(main())
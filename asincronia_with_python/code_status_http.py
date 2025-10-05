import asyncio
import aiohttp

async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}>> status: {response.status}")

async def main():
    urls ={
        '1': 'https://realpython.com',
        '2': 'https://pycoders.com',
        '3': 'https://www.python.org'
    } 

    await asyncio.gather(
        *(check(url) for url in urls.values())
    )

if __name__ == "__main__":
    asyncio.run(main())
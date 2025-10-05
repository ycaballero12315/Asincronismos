import asyncio
import time

async def count():
    print('One')
    await asyncio.sleep(1)
    print('Two')
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(count(), count(), count())
    
if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter()-start
    print(f'{__file__} execute in {elapsed:0.2f} secunds')

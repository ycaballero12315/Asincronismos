import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('Other')

routine = main()
# routine
asyncio.run(routine)
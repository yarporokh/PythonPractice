import asyncio
import time


async def show_text(text):
    await asyncio.sleep(2)
    print(text)

async def main():
    task1 = asyncio.create_task(show_text("Hello"))
    task2 = asyncio.create_task(show_text("World"))

    print(f"Start at {time.strftime('%X')}")
    await task1
    await task2
    print(f"End at {time.strftime('%X')}")

asyncio.run(main())
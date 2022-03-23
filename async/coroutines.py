import asyncio
import time


async def show_text(text):
    await asyncio.sleep(2)
    print(text)

async def main():
    print(f"Start at {time.strftime('%X')}")
    await show_text("Hello")
    await show_text("World")
    print(f"End at {time.strftime('%X')}")

asyncio.run(main())
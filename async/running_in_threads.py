import asyncio
import time


def func():
    print(f"Start func() at: {time.strftime('%X')}")
    for i in range(5):
        print(i)
        time.sleep(1)

    print(f"End func() at: {time.strftime('%X')}")


async def main():
    print(f"Start program at: {time.strftime('%X')}")

    await asyncio.gather(asyncio.to_thread(func), asyncio.sleep(1))

    print(f"End program at: {time.strftime('%X')}")


asyncio.run(main())

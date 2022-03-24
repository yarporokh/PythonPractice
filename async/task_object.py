import asyncio


async def cancel():
    print('cancel() start')
    await asyncio.sleep(1000)
    print('cancel() end')


async def func():
    print('func() start')
    await asyncio.sleep(1)
    print('func() end')
    return 1


async def main():
    task = asyncio.create_task(cancel(), name="First task")
    task2 = asyncio.create_task(func())
    task2.set_name("Second task")

    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("cancel() is cancelled")

    print(task.cancelled())  # True
    print(task.done())  # True
    print(task2.result())  # 1
    print(task.get_name())  # First task
    print(task2.get_name())  # Second task


asyncio.run(main())

# Expected output:
#
# cancel() start
# func() start
# func() end
# cancel() is cancelled
# True
# True
# 1
# First task
# Second task
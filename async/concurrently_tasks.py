import asyncio


async def person_info(name, cars):
    i = 0  # cars length
    for car in cars:
        print(f'{name} has a {car}')
        await asyncio.sleep(1)
        i += 1
    print(f'{name} has {i} cars')
    return i


async def main():
    number_of_cars = await asyncio.gather(
        person_info("John", ['BMW', 'Toyota']),
        person_info("Kate", ['Mercedes', 'Hyundai', 'Ford', 'Chevrolet']),
        person_info("Bob", ['Renault', 'BMW', 'Fiat'])
    )

    print(number_of_cars)


asyncio.run(main())

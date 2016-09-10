import asyncio


async def print_number(number):
    print(number)


def start():
    print('asyncapp started!')
    loop = asyncio.get_event_loop()

    loop.run_until_complete(
       asyncio.wait([
           print_number(number)
           for number in range(10)
       ])
    )
    loop.close()

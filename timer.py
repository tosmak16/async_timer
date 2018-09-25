import asyncio

timer = {'hours': 0, 'minutes': 0, 'seconds': 0}


async def handle_second():
    while True:
        for sec_count in range(60):
            timer['seconds'] = sec_count
            print('{0}h:{1}m:{2}s'.format(timer['hours'], timer['minutes'],
                                          timer['seconds']))
            await asyncio.sleep(1)


async def handle_minute():
    await count_and_update_timer(59, 60, 'minutes')


async def handle_hour():
    await count_and_update_timer(11, 3600, 'hours')


async def count_and_update_timer(count_range, delay_in_seconds, timer_key):

    while True:
        for count in range(1, count_range):
            await asyncio.sleep(delay_in_seconds)
            timer[timer_key] = count


def run_timer():

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.gather(handle_second(), handle_minute(),
                                           handle_hour()))

    loop.close()


run_timer()
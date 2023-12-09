import asyncio
import datetime
import os
import sys

import aiohttp

import settings
from db.engine import update_temp

sys.path.insert(1, os.path.join(sys.path[0], ''))


async def request(url, town):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            res = await response.json()
    dct = res['data']['current_condition'][0]
    data = (dct['temp_C'],
            datetime.datetime.now())
    update_temp(town=town,
                temp=int(data[0]),
                timestamp=data[1])
    return data


async def main():
    tasks = []
    for key, value in settings.COORD.items():
        url = (f"http://api.worldweatheronline.com/premium/v1/weather.ashx?key={settings.KEY}&q="
               f"{value}&num_of_days=1&temp=1&format=json")
        tasks.append(asyncio.create_task(request(url, town=key)))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

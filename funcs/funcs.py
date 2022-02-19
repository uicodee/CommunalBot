import aiohttp
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import lxml

AREAS_URL = "https://uzoplata.com/?uo-ajax=inferior_field&serviceid=131&field=paysystemid&value={area_id}"
INFO_URL = "https://uzoplata.com/?uo-ajax=check_perform_payment"


async def get_cities(area_id: int) -> list:
    data = []
    async with ClientSession() as session:
        async with session.get(url=AREAS_URL.format(area_id=area_id)) as response:
            r: dict = await response.json(encoding='utf-8')
            soup = BeautifulSoup(r.get('data').get('html'), "lxml")
            cities = soup.find_all(name="option")

            for i in range(1, len(cities)):
                s = cities[i].text.split('-')
                data.append({
                    s[1].strip(): s[0].strip()
                })
    return data


async def get_info(city_code: int, account_id: str) -> list:
    user = []
    data = {
        "paysystemid": 11,
        "soato": city_code,
        "quantity": 5000,
        "account_id": account_id,
        "proceed-to-checkout": 131
    }
    async with aiohttp.ClientSession(headers={"Content-Types": "form-data"}) as session:
        async with session.post(url=INFO_URL, data=data) as response:
            info = (await response.json(encoding="utf-8")).get('data').get('url')

    async with aiohttp.ClientSession() as session:
        async with session.post(url=info) as response:
            r = (await response.text()).replace("<br>", "\n")
            soup = BeautifulSoup(r, "lxml")
            tables = soup.find(name="table", attrs={"class": "table table-bordered mb-5"}).find_all("tr")

            index = 0
            for name, tag in tables:
                index += 1
                if index != 6:
                    user.append({name.text: tag.text})
                else:
                    [user.append({j[0]: j[1]}) for j in [i for i in [s.split(":") for s in tag.text.split("\n")]][:-2]]
    return user


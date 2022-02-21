import datetime
import typing

from loader import users


async def new(user_id: int, firstname: str, language: str) -> typing.Any:
    await users.insert_one({
        "user_id": user_id,
        "firstname": firstname,
        "date": datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
        "language": language
    })


async def user(user_id: int) -> bool:
    if await users.count_documents({"user_id": user_id}) == 0:
        return False
    else:
        return True


async def get_language(user_id: int) -> dict:
    language = await users.find_one({"user_id": user_id})
    return language


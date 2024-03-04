import asyncio
import os

from ringoapi import RingoAPI


async def main():
    ringo = RingoAPI(os.environ.get("RINGO_LINK"))
    print(await ringo.unlock_door(0, 1))


asyncio.run(main())

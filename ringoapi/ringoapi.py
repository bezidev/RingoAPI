import re

import httpx


BASE_URL = "https://www.ringodoor.com"


class RingoAPI:
    def __init__(self, ringo_url: str):
        self.client = httpx.AsyncClient()
        s = re.search(r"https:\/\/www.ringodoor.com\/door\/\?hash=(.*)", ringo_url, re.IGNORECASE)
        if not s:
            raise Exception(f"Invalid URL to parse: {ringo_url}")
        self.ringo_hash = s.group(1)

    async def unlock_door(self, lock_id: int, relay_id: int | None = None, pin: int | None = None) -> dict:
        r = await self.client.post(f"{BASE_URL}/ajax", data={
            "action": "open_lock",
            "hash": self.ringo_hash,
            "pin": pin,
            "relay_id": 0 if relay_id is None else relay_id,
            "lock_id": lock_id,
        }, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/121.0.0.0 Safari/537.36",
        })
        return r.json()

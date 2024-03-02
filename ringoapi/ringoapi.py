import httpx


class RingoAPI:
    def __init__(self, ringo_url):
        self.client = httpx.AsyncClient()
        self.ringo_url = ringo_url
        if not ringo_url:
            raise Exception("Invalid URL")

    def unlock_door(self, door_id):
        self.client.post(f"")

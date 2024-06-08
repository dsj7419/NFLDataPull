import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()

class APIHandler:
    def __init__(self):
        self.base_url = "https://nfl-api1.p.rapidapi.com/nflteamlist"
        self.headers = {
            'x-rapidapi-key': os.getenv('RAPIDAPI_KEY'),
            'x-rapidapi-host': "nfl-api1.p.rapidapi.com"
        }

    async def fetch_teams(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, headers=self.headers) as response:
                return await response.json()

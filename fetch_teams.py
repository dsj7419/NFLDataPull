import os
import asyncio
import aiohttp
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

async def fetch_teams(session):
    url = "https://nfl-api1.p.rapidapi.com/nflteamlist"
    headers = {
        'x-rapidapi-key': os.getenv('RAPIDAPI_KEY'),
        'x-rapidapi-host': "nfl-api1.p.rapidapi.com"
    }
    async with session.get(url, headers=headers) as response:
        return await response.json()  # Parse JSON response

async def main():
    async with aiohttp.ClientSession() as session:
        teams = await fetch_teams(session)
        print(teams)  # Print the data fetched

if __name__ == "__main__":
    asyncio.run(main())

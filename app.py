import asyncio
from api_handler import APIHandler
from db_manager import DatabaseManager

async def update_data():
    api_handler = APIHandler()
    db_manager = DatabaseManager()
    teams = await api_handler.fetch_teams()
    db_manager.update_teams(teams)
    print("Data updated successfully.")

def main():
    while True:
        command = input("Enter command (update, team name, or exit): ").strip()
        if command.lower() == 'exit':
            break
        elif command.lower() == 'update':
            asyncio.run(update_data())
        else:
            db_manager = DatabaseManager()
            details = db_manager.get_team_details(command)
            if details:
                for detail in details:
                    print(detail)
            else:
                print("No details found for the team.")

if __name__ == "__main__":
    main()

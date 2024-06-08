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
    db_manager = DatabaseManager()  # Initialize it once for all commands
    while True:
        user_input = input("Enter command (update, team name, list teams, or exit): ").strip()
        command = user_input.lower()  # Use a lowercase version for command checking

        if command == 'exit':
            break
        elif command == 'update':
            asyncio.run(update_data())
        elif command == 'list teams':
            team_names = db_manager.list_all_teams()
            print("Available teams:")
            for name in team_names:
                print(name)
        else:
            details = db_manager.get_team_details(user_input)  # Use the original case input for team details
            if details:
                for detail in details:
                    print(detail)
            else:
                print("No details found for the team.")

if __name__ == "__main__":
    main()

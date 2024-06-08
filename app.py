import asyncio
from api_handler import APIHandler
from db_manager import DatabaseManager
from tabulate import tabulate

def print_details(details):
    headers = ['ID', 'Slug', 'Abbrev.', 'Display Name', 'Short Name', 'Name', 'Nickname', 'Location', 'Active', 'All-Star']
    print(tabulate(details, headers=headers, tablefmt='pretty'))

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
                print_details(details)  # Use the new print_details function
            else:
                print("No details found for the team.")

if __name__ == "__main__":
    main()
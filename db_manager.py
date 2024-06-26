import psycopg2
import os
from dotenv import load_dotenv
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

class DatabaseManager:
    def __init__(self):
        # Establish a connection to the database
        self.conn = psycopg2.connect(os.getenv('DATABASE_URL'))

    def update_teams(self, teams):
        """Inserts or updates team records in the database."""
        with self.conn.cursor() as cursor:
            for team in teams['sports'][0]['leagues'][0]['teams']:
                # Extract the necessary details from each team
                slug = team['team']['slug']
                abbreviation = team['team']['abbreviation']
                display_name = team['team']['displayName']
                short_display_name = team['team']['shortDisplayName']
                name = team['team']['name']
                nickname = team['team']['nickname']
                location = team['team']['location']
                is_active = team['team']['isActive']
                is_all_star = team['team']['isAllStar']

                # SQL command for inserting or updating data
                cursor.execute(
                    """
                    INSERT INTO teams (slug, abbreviation, display_name, short_display_name, name, nickname, location, is_active, is_all_star) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (slug) DO UPDATE SET
                        abbreviation = EXCLUDED.abbreviation,
                        display_name = EXCLUDED.display_name,
                        short_display_name = EXCLUDED.short_display_name,
                        name = EXCLUDED.name,
                        nickname = EXCLUDED.nickname,
                        location = EXCLUDED.location,
                        is_active = EXCLUDED.is_active,
                        is_all_star = EXCLUDED.is_all_star;
                    """,
                    (slug, abbreviation, display_name, short_display_name, name, nickname, location, is_active, is_all_star)
                )

            # Commit the transaction
            self.conn.commit()
            logging.info("Teams data updated successfully.")

    def get_team_details(self, team_name):
        """Retrieves and returns details of a specific team by a partial match of its display name."""
        with self.conn.cursor() as cursor:
            # Use ILIKE for case-insensitive partial matching
            cursor.execute("SELECT * FROM teams WHERE display_name ILIKE %s;", ('%' + team_name + '%',))
            result = cursor.fetchall()
            if result:
                logging.info(f"Details found for {team_name}: {result}")
            else:
                logging.info(f"No details found for {team_name}")
            return result
     
    def list_all_teams(self):
        """Retrieves and returns a list of all teams."""
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT team_id, display_name, short_display_name FROM teams ORDER BY display_name;")
            team_list = cursor.fetchall()
            return team_list


    def close(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()

# Usage example:
# db_manager = DatabaseManager()
# db_manager.update_teams(teams_data_fetched_from_api)
# print(db_manager.get_team_details('Broncos'))
# db_manager.close()

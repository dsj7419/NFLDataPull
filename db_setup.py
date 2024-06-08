import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to connect to the database
def connect_to_db():
    return psycopg2.connect(os.getenv('DATABASE_URL'))

# Function to create tables
def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS teams (
            team_id SERIAL PRIMARY KEY,
            slug VARCHAR(255),
            abbreviation VARCHAR(10),
            display_name VARCHAR(255),
            short_display_name VARCHAR(255),
            name VARCHAR(255),
            nickname VARCHAR(255),
            location VARCHAR(255),
            is_active BOOLEAN,
            is_all_star BOOLEAN
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS logos (
            logo_id SERIAL PRIMARY KEY,
            team_id INT,
            href TEXT,
            type VARCHAR(50),
            FOREIGN KEY (team_id) REFERENCES teams (team_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS colors (
            team_id INT PRIMARY KEY,
            primary_color CHAR(6),
            alternate_color CHAR(6),
            FOREIGN KEY (team_id) REFERENCES teams (team_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS links (
            link_id SERIAL PRIMARY KEY,
            team_id INT,
            type VARCHAR(50),
            url TEXT,
            FOREIGN KEY (team_id) REFERENCES teams (team_id)
        );
        """
    )
    conn = None
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        # Create table one by one
        for command in commands:
            cur.execute(command)
        # Close communication with the PostgreSQL database server
        cur.close()
        # Commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not closed:
            conn.close()

if __name__ == '__main__':
    create_tables()

import os
import psycopg2
import logging
from dotenv import load_dotenv

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
            slug VARCHAR(255) UNIQUE,
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
        # Commit the changes
        conn.commit()
        logging.info("Tables created successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"An error occurred: {error}")
        if conn:
            conn.rollback()
    finally:
        if conn is not None:
            if not conn.closed:
                conn.close()
            logging.info("Database connection closed.")

if __name__ == '__main__':
    create_tables()

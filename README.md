# NFL Data API Project

This project uses the NFL API to fetch and store team data in a PostgreSQL database. It allows users to update the database, retrieve details for specific teams, and list all available teams.

## Prerequisites
- Python 3.8+
- PostgreSQL
- Git (optional, for cloning the repository)

## Installation

### Clone the repository
If you have git installed, you can clone the repository using:
git clone https://github.com/yourusername/nfl-data-api.git
Alternatively, you can download the ZIP file and extract it.

### Set up Python environment
It's recommended to create a virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix or MacOS

### Install dependencies
pip install -r requirements.txt

## Configuration

### Database setup
Ensure PostgreSQL is installed and running. Create a database named `nfl_data`:
createdb -U postgres nfl_data  # You may need to adjust this command based on your PostgreSQL setup.

### Environment variables
Copy the `.env.example` file to a new file named `.env` and update the values accordingly:
DATABASE_URL=postgresql://username:password@localhost:5432/nfl_data
RAPIDAPI_KEY=your_rapidapi_key_here

## Usage

Run the db setup script:
python db_setup.py

Run the application:
python app.py

Follow the on-screen prompts to interact with the application. You can type 'update' to fetch and store the latest team data, or type a team name to retrieve specific details. Type 'exit' to close the application.

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

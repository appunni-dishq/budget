import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL is None:
    raise ValueError("The DATABASE_URL environment variable is not set. Please set it to continue.")

# Sample .env
# DATABASE_URL=mysql://user:password@localhost/dbname

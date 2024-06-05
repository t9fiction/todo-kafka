from sqlmodel import create_engine
from dotenv import load_dotenv, find_dotenv
import os


# conn_str = 'postgresql://sohail.sohailishaq:Iap2zhSVLRg0@ep-restless-night-a56nuf5e.us-east-2.aws.neon.tech/todo-docker?sslmode=require'

# Load environment variables from .env file if it exists
load_dotenv(find_dotenv())

# Get the database URL from the environment variable
conn_str = os.getenv('DATABASE_URL')

# Ensure the connection string is retrieved correctly
if not conn_str:
    raise ValueError("No DATABASE_URL environment variable set")

# Create the engine with the connection string
engine = create_engine(conn_str, echo=False)
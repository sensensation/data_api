from dotenv import load_dotenv
import os

from sqlalchemy import create_engine

load_dotenv()

DB_URL = os.environ.get("SQL_ALCHEMY_URL")

engine = create_engine(DB_URL)

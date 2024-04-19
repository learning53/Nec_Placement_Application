import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Read database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Ensure DATABASE_URL is set
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create the SQLAlchemy engine
db_engine = create_engine(DATABASE_URL)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

# Create a base class for declarative models
Base = declarative_base()

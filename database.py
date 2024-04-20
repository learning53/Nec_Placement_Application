from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = 'postgresql://root:5HveBxrbtFCFfmpmn2SFdeGrxjv1LKCS@dpg-coh4htuv3ddc73fh2jvg-a.oregon-postgres.render.com/nec_placement'

# Create the database engine with the specific dialect
db_engine = create_engine(
    DATABASE_URL,
    pool_size=5,  # Set the pool size to 5 connections
    max_overflow=10,  # Allow up to 10 additional connections to be created temporarily
    pool_timeout=30,  # Set the connection pool timeout to 30 seconds
    pool_recycle=3600,  # Recycle connections every 1 hour (3600 seconds)
    dialect='postgresql'
)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

# Create a declarative base
base = declarative_base()

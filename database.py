from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = 'postgres://root:5HveBxrbtFCFfmpmn2SFdeGrxjv1LKCS@dpg-coh4htuv3ddc73fh2jvg-a.oregon-postgres.render.com/nec_placement'

# Create the database engine with the specific dialect
db_engine = create_engine(DATABASE_URL, dialect='postgresql')

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

# Create a declarative base
Base = declarative_base()

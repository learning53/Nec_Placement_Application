from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgres://root:5HveBxrbtFCFfmpmn2SFdeGrxjv1LKCS@dpg-coh4htuv3ddc73fh2jvg-a.oregon-postgres.render.com/nec_placement'

db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

base=declarative_base()

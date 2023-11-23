from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = 'fl0user'
DB_PASS = '4qWeDjYl1ixT'
DB_HOST = 'ep-billowing-sun-46121554.eu-central-1.aws.neon.fl0.io'
DB_NAME = 'database'
DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?sslmode=require'

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

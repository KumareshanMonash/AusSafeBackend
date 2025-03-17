from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "postgresql://postgres:postgres@"
    "aussafedb.chwc6yes47vo.ap-southeast-2.rds.amazonaws.com:5432/postgres"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()
metadata.reflect(bind=engine)
Base = declarative_base(metadata=metadata)

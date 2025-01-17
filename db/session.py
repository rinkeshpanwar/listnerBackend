from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL ='mysql+pymysql://root:root@db/root'

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

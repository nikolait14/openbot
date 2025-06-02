from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Integer, String, Column


Base = declarative_base()
engine = create_engine("")
Session = sessionmaker(bind=engine)
s = Session()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    vip = Column(Integer)
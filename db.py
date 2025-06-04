# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import Integer, String, Column
#
#
# Base = declarative_base()
# engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/data")
# Session = sessionmaker(bind=engine)
# s = Session()
#
#
# class Openbot(Base):
#     __tablename__ = "openbot"
#     id = Column(Integer, primary_key=True)
#     vip = Column(Integer, nullable=False)
#     payment = Column(String, nullable=False)
#
#
# data = s.query(Openbot).all()
# Base.metadata.create_all(engine)
#
# Base.metadata.create_all(engine)
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Integer, String, Column


Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/data")
Session = sessionmaker(bind=engine)
s = Session()


class Openbot(Base):
    __tablename__ = "openbot"
    id = Column(Integer, primary_key=True)
    status_pay = Column(String, nullable=False)
    token_balance = Column(Integer, nullable=False)


st1 = Openbot(id=0, status_pay="F", token_balance=10)
st2 = Openbot(id=1, status_pay="T", token_balance=100)
st3 = Openbot(id=2, status_pay="F", token_balance=100)

s.merge(st1)
s.merge(st2)
s.merge(st3)
s.commit()

data = s.query(Openbot).all()
Base.metadata.create_all(engine)
print(data)
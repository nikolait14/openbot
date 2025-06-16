from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


def upd(data_to_update: list):
    if data_to_update[1] == 'vip':
        s.query(Users).filter(Users.id == data_to_update[0]).update({'status': 'vip'})


engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/openbot")
Base = declarative_base()
Session = sessionmaker(bind=engine)
s = Session()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)      #id
    status = Column(String, nullable=False)                     #статус юзера default / vip далее от этого зависит
                                                                #кол - во токенов для запросов
    date = Column(Integer, nullable=False)                      #осталось дней до конца подписки(если есть)


first = Users(id=1, status='vip', date=10)
s.merge(first)
s.commit()

Base.metadata.create_all(engine)

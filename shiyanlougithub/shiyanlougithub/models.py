from sqlalchemy import DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlougithub?charset=utf8')    
Base = declarative_base()


class Repositories(Base):
    __tablename__ = 'repositories'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    update_time = Column(DateTime)
    commits = Column(Integer)
    branches = Column(Integer)
    releases = Column(Integer)

if __name__=='__main__':
    Base.metadata.create_all(engine)
    

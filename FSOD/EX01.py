from lib2to3.pytree import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    tablename = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def repr(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                self.name, self.fullname, self.nickname)
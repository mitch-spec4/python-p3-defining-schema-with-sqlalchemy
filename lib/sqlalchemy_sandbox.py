#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__='student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    pass

if __name__ == '__main__':
    engine = create_engine('sqlite:///student.db')
    Base.metadata.create_all(engine)
    pass

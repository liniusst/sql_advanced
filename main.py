# pylint: disable= missing-docstring
import datetime

from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///database/projektai.db")
Base = declarative_base()


@dataclass
class Users(Base):
    __tablename__ = "Users"
    id: int = Column(Integer, primary_key=True)
    name: str = Column("Name", String)
    surname: str = Column("Surname", String)
    date_of_birth: str = Column("Date of birth", String)
    salary: int = Column("Salary", Integer)
    start_date = Column("Started working", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, surname, date_of_birth, salary):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.salary = salary

    def __repr__(self):
        return f"ID: {self.id} User: {self.name} {self.surname} Born date: {self.date_of_birth} and salary: {self.salary}"


Base.metadata.create_all(engine)

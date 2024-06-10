from app.db.database import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer)
    name = Column(String)
    street = Column(String)
    district = Column(String)
    state = Column(String)
    housetype = Column(String)
    floor = Column(Integer)
    numberofbedroom = Column(Integer)
    numberofbathroom = Column(Integer)
    hospital = Column(Integer)
    school = Column(Integer)
    college = Column(Integer)
    price = Column(Integer)

class PropertyBase(BaseModel):
    userid: int
    name: str
    street: str
    district : str
    state: str
    housetype: str
    floor: int
    numberofbedroom: int
    numberofbathroom: int
    hospital: int
    school: int
    college: int
    price: int

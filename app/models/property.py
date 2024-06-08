from app.db.database import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer)
    address = Column(String)
    housetype = Column(String)
    floor = Column(Integer)
    numberofbedroom = Column(Integer)
    numberofbathroom = Column(Integer)
    other = Column(String)

class PropertyBase(BaseModel):
    userid: int
    address: str
    housetype: str
    floor: int
    numberofbedroom: int
    numberofbathroom: int
    other: str
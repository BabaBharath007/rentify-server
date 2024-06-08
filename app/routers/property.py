from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.db.database import get_db
from app.models.property import Property,PropertyBase

app = APIRouter()

@app.post("/")
def index(property: PropertyBase, db: Session = Depends(get_db)):
    db_user = Property(userid=property.userid, address=property.address, housetype=property.housetype, floor =property.floor, numberofbedroom=property.numberofbedroom, numberofbathroom=property.numberofbathroom, other=property.other)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/")
def get_users(db: Session = Depends(get_db)):
    Properties = db.query(Property).all()
    return {"property": Properties}
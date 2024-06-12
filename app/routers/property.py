from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter,HTTPException,status
from app.db.database import get_db
from app.models.property import Property,PropertyBase,PropertyUpdate

app = APIRouter()

@app.post("/")
def index(property: PropertyBase, db: Session = Depends(get_db)):
    db_user = Property(userid=property.userid, name=property.name, street=property.street, district=property.district, state=property.state, housetype=property.housetype, floor =property.floor, numberofbedroom=property.numberofbedroom, numberofbathroom=property.numberofbathroom, hospital=property.hospital,school=property.school,college=property.college,price=property.price)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/post/{id}")
def get_post(id: int,db: Session = Depends(get_db)):
    post = db.query(Property).filter(Property.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")  
    db.commit()
    db.refresh(post)
    return post



@app.get("/")
def get_users(db: Session = Depends(get_db)):
    Properties = db.query(Property).all()
    return Properties


@app.put("/{id}")
def update_property(id: int, property_update: PropertyUpdate, db: Session = Depends(get_db)):
    db_property = db.query(Property).filter(Property.id == id).first()
    if not db_property:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    
    for key, value in property_update.dict(exclude_unset=True).items():
        setattr(db_property, key, value)
    
    db.commit()
    db.refresh(db_property)
    return db_property

@app.delete("/{id}")
def delete_property(id: int, db: Session = Depends(get_db)):
    db_property = db.query(Property).filter(Property.id == id).first()
    if not db_property:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    
    db.delete(db_property)
    db.commit()
    return db_property
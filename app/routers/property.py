from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter,HTTPException,status,File,UploadFile,Form
from app.db.database import get_db
from app.models.property import Property,PropertyUpdate
from app.models.image import Image
from secrets import token_hex
import os

app = APIRouter()

image = "./image/"

@app.post("/")
async def index(
    userid: int = Form(...),
    name: str = Form(...),
    street: str = Form(...),
    district: str = Form(...),
    state: str = Form(...),
    housetype: str = Form(...),
    floor: int = Form(...),
    numberofbedroom: int = Form(...),
    numberofbathroom: int = Form(...),
    hospital: int = Form(...),
    school: int = Form(...),
    college: int = Form(...),
    price: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    os.makedirs(image, exist_ok=True)
    
    file_ext = file.filename.split(".").pop()
    file_name = token_hex(10)
    file_path = os.path.join(image, f"{file_name}.{file_ext}")
    
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    db_user = Property(
        userid=userid,
        name=name,
        street=street,
        district=district,
        state=state,
        housetype=housetype,
        floor=floor,
        numberofbedroom=numberofbedroom,
        numberofbathroom=numberofbathroom,
        hospital=hospital,
        school=school,
        college=college,
        price=price,
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db_img = Image(name=file_path, propertyId=db_user.id)
    db.add(db_img) 
    db.commit()  
    db.refresh(db_img)
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
from fastapi import UploadFile,File,APIRouter,Depends
from secrets import token_hex
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.models.image import Image,ImageBase


app = APIRouter()

@app.post("/upload/{id}")
async def upload(id: int, file:UploadFile = File(...), db: Session = Depends(get_db)):
    file_ext=file.filename.split(".").pop()
    file_name = token_hex(10)
    file_path = f"images/{file_name}.{file_ext}"
    with open(file_path,"wb") as f:
        content = await file.read()
        f.write(content)
    db_img = Image(name=file_path, propertyId=id)
    db.add(db_img) 
    db.commit()  
    db.refresh(db_img)
    return db_img

    
    
    
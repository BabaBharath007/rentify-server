from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.db.database import get_db
from app.models.user import UserBase, User

app = APIRouter()

@app.post("/")
def index(user: UserBase, db: Session = Depends(get_db)):
    db_user = User(firstname=user.firstname, lastname=user.lastname, email=user.email, phonenumber=user.phonenumber, password=user.password, type=user.type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {"users": users}

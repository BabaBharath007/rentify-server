from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user,property
from app.db.database import engine, Base

app =FastAPI()

Base.metadata.create_all(engine)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(property.app, tags=['Property'], prefix='/api/property')
app.include_router(user.app, tags=['Users'], prefix='/api/users')


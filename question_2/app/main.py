from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, joke_service, schemas
from databse import engine, SessionLocal

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/jokes", response_model=list[schemas.JokeSchema])
def get_jokes(db: Session = Depends(get_db)):
    jokes = db.query(models.Joke).all()
    return jokes

@app.post("/fetch-jokes", response_model=list[schemas.JokeSchema])
def fetch_and_store_jokes(db: Session = Depends(get_db)):
    jokes_data = joke_service.fetch_jokes()
    stored_jokes = []
    for joke_data in jokes_data:
        stored_joke = joke_service.save_joke_to_db(db, joke_data)
        stored_jokes.append(stored_joke)
    return stored_jokes

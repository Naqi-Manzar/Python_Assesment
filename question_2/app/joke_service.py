import httpx
from models import Joke
from databse import SessionLocal
from sqlalchemy.orm import Session

JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any?amount=10"

def fetch_jokes() -> list[dict]:
    response = httpx.get(JOKE_API_URL)
    response.raise_for_status()
    return response.json().get("jokes", [])

def save_joke_to_db(db: Session, joke_data: dict):
    joke = Joke(
        category=joke_data["category"],
        type=joke_data["type"],
        joke=joke_data.get("joke"),
        setup=joke_data.get("setup"),
        delivery=joke_data.get("delivery"),
        nsfw=joke_data["flags"]["nsfw"],
        political=joke_data["flags"]["political"],
        sexist=joke_data["flags"]["sexist"],
        safe=joke_data["safe"],
        lang=joke_data["lang"],
    )
    db.add(joke)
    db.commit()
    db.refresh(joke)
    return joke

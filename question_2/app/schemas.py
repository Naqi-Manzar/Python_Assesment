from pydantic import BaseModel

class JokeSchema(BaseModel):
    id: int
    category: str
    type: str
    joke: str | None
    setup: str | None
    delivery: str | None
    nsfw: bool
    political: bool
    sexist: bool
    safe: bool
    lang: str

    class Config:
        orm_mode = True

from sqlalchemy import Column, Integer, String, Boolean
from databse import Base

class Joke(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    type = Column(String)
    joke = Column(String, nullable=True)
    setup = Column(String, nullable=True)
    delivery = Column(String, nullable=True)
    nsfw = Column(Boolean, default=False)
    political = Column(Boolean, default=False)
    sexist = Column(Boolean, default=False)
    safe = Column(Boolean, default=True)
    lang = Column(String)

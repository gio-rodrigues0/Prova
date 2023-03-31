from sqlalchemy import Column, String, Integer
from model.base import Base

class Jogos():
    __tablename__ = "Jogos"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    platform = Column(String)
    price = Column(Integer)
    number = Column(Integer)

def __repr__(self):
    return f"Jogo: {self.name}, {self.platform}, {self.price}, {self.number}"
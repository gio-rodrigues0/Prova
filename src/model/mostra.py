from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import create_engine
from model.jogo import Jogos

engine = create_engine("sqlite:///banco.db", echo=True)

session = Session(engine)

jogos = select(Jogos)

for jogo in session.scalars(jogos):
    print(jogo)
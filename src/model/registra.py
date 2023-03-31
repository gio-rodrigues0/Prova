from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model.base import Base
from model.jogo import Jogos

engine = create_engine("sqlite:///banco.db", echo=True)

with Session(engine) as session:
    jogo1 = Jogos(
        name = "DEAD SPACE REMAKE",
        platform = "PS5",
        price = 350,
        number = 10
    )
    jogo2 = Jogos(
        name = "FORSPOKEN",
        platform = "PC",
        price = 299,
        number = 8
    )
    jogo3 = Jogos(
        name = "DEAD ISLAND 2",
        platform = "PS5",
        price = 350,
        number = 10
    )
    jogo4 = Jogos(
        name = "HOGWARTS LEGACY",
        platform = "PC",
        price = 219,
        number = 7
    )
    jogo5 = Jogos(
        name = "WILD HEARTS",
        platform = "XBox Series",
        price = 350,
        number = 7
    )
    jogo6 = Jogos(
        name = "RESIDENT EVIL 4",
        platform = "PS5",
        price = 289,
        number = 10
    )
    jogo7 = Jogos(
        name = "THE LEGEND OF ZELDA: TEARS OF THE KINGDOM",
        platform = "Switch",
        price = 350,
        number = 10
    )

    session.add_all([jogo1, jogo2, jogo3, jogo4, jogo5, jogo6, jogo7])

    session.commit()


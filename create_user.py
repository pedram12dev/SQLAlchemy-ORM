from sqlalchemy import insert , select,create_engine,URL
from User import User
from sqlalchemy.orm import Session,sessionmaker
from environs import Env


env = Env()
env.read_env('.env')

url = URL.create(
    drivername="postgresql+psycopg2",
    username = env.str("POSTGRES_USER"),
    password = env.str("POSTGRES_PASSWORD"),
    host = env.str("DATABASE_HOST"),
    port = 5432,
    database = env.str("POSTGRES_DB")
).render_as_string(hide_password=False)

engine= create_engine(url , echo=True)
sessionpool = sessionmaker(bind=engine)


class Repo:
    def __init__(self, session : Session):
        self.session = session

    def add_user(
            self,
            telegram_id: int,
            full_name: str,
            username: str = None,
            referrer_id: int=None,
    ):
        stmt = insert(User).values(
            telegram_id=telegram_id,
            full_name=full_name,
            username=username,
            referrer_id=referrer_id,
        )
        self.session.execute(stmt)
        self.session.commit()




with sessionpool() as session:
    repo = Repo(session)
    repo.add_user(
        telegram_id=1,
        full_name="pedram najafi",
        username="pedram",
        referrer_id=1,
    )
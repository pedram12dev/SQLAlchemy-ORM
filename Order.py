"""
    create sqlalchemy orm table without this value:

    CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES users(telegram_id)
        ONDELETE CASCADE

"""
from mixins import TimestampMixin,TableNameMixin
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase
from sqlalchemy import BIGINT,Integer,ForeignKey


class Base(DeclarativeBase):
    pass


class Order(Base,TimestampMixin,TableNameMixin):
    order_id = Mapped[int] = mapped_column(
        Integer , primary_key=True
    )
    user_id = Mapped[int] = mapped_column(
        BIGINT , ForeignKey("users.telegram_id", ondelete="SET NULL")
    )
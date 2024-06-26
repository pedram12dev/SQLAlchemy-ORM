"""
    create sqlalchemy orm table without this value:

    CREATE TABLE products(
    product_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT ,
    created_at TIMESTAMP DEFAULT NOW()

"""
from typing import Optional
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer,VARCHAR
from mixins import TimestampMixin, TableNameMixin


class Base(DeclarativeBase):
    pass


class Product(Base,TableNameMixin,TimestampMixin):
    product_id = Mapped[int] = mapped_column(
        Integer,primary_key=True
    )
    title = Mapped[str] = mapped_column(
        VARCHAR(255)
    )
    description = Mapped[Optional[str]] = mapped_column(
        VARCHAR(255)
    )
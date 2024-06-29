"""
    create sqlalchemy orm table without this value:


    CREATE TABLE users(
        telegram_id BIGINT PRIMARY KEY ,
        full_name VARCHAR(255) NOT NULL,
        username VARCHAR(255),
        language_code VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT NOW()
        referrer_id BIGINT,
        FOREIGN KEY(referrer_id)
            REFERENCES users(telegram_id)
            ON DELETE SET NULL
    )
"""
from typing import Optional
from sqlalchemy import BIGINT, VARCHAR, create_engine, ForeignKey, URL,Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from mixins import TimestampMixin

url = URL.create(
    drivername="postgresql+psycopg2",
    username="testuser",
    password="password",
    host="localhost",
    port=5432
)
engine = create_engine(url, echo=True)


class Base(DeclarativeBase):
    pass


class User(Base,TimestampMixin):
    """ create user table  """
    __tablename__ = "users"

    telegram_id: Mapped['int'] = mapped_column(
        BIGINT, primary_key=True
    )
    full_name: Mapped['str'] = mapped_column(
        VARCHAR(255)
    )
    username: Mapped[Optional['str']] = mapped_column(
        VARCHAR(255)
    )
    language_code: Mapped['int'] = mapped_column(
        VARCHAR(255), nullable=False
    )
    referrer_id: Mapped[Optional['int']] = mapped_column(
        BIGINT, ForeignKey("users.telegram_id", ondelete="SET NULL")
    )


class Product(Base, TimestampMixin):
    __tablename__ = "products"
    product_id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    title: Mapped[str] = mapped_column(
        VARCHAR(255)
    )
    description: Mapped[Optional[str]] = mapped_column(
        VARCHAR(255)
    )


"""
    create sqlalchemy orm table without this value:

    CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES users(telegram_id)
        ONDELETE CASCADE

"""


class Order(Base, TimestampMixin):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.telegram_id", ondelete="CASCADE")
    )


"""
    create sqlalchemy orm table without this value:
    CREATE TABLE order_products(
        order_id = INTEGER NOT NULL,
        product_id = INTEGER NOT NULL,
        quantity = INTEGER NOT NULL,
        FOREIGN KEY (order_id)
            REFERENCES orders(order_id)
            ON DELETE CASCADE,
        FOREIGN KEY (product_id)
            REFERENCES products(product_id)
            ON DELETE CASCADE,);
"""


class OrderProduct(Base):
    __tablename__ = "orderproducts"
    order_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("orders.order_id", ondelete="CASCADE"), primary_key=True
    )
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("products.product_id", ondelete="RESTRICT"), primary_key=True
    )
    quantity: Mapped[int]



Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)
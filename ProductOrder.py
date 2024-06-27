"""
    create sqlalchemy orm table without this value:

    CREATE TABLE products(
    product_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT ,
    created_at TIMESTAMP DEFAULT NOW()

"""
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, VARCHAR, BIGINT, ForeignKey, URL, create_engine
from mixins import TimestampMixin, TableNameMixin


class Base(DeclarativeBase):
    pass


class Product(Base, TableNameMixin, TimestampMixin):
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


class Order(Base, TimestampMixin, TableNameMixin):
    order_id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.telegram_id", ondelete="SET NULL")
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


class OrderProduct(Base, TableNameMixin):
    order_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("orders.order_id", ondelete="CASCADE"), primary_key=True
    )
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("products.product_id", ondelete="RESTRICT"), primary_key=True
    )
    quantity: Mapped[int]



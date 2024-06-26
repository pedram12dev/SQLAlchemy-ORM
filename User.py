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
from datetime import datetime
from typing import Optional
from sqlalchemy import BIGINT, VARCHAR, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from mixins import TableNameMixin, TimestampMixin


class Base(DeclarativeBase):
    pass


class User(Base, TableNameMixin, TimestampMixin):
    """ create user table  """
    telegram_id = Mapped['int'] = mapped_column(
        BIGINT, primary_key=True
    )
    full_name = Mapped['str'] = mapped_column(
        VARCHAR(255)
    )
    username = Mapped[Optional['str']] = mapped_column(
        VARCHAR(255)
    )
    language_code = Mapped['int'] = mapped_column(
        VARCHAR(255), nullable=False
    )
    referrer_id = Mapped[Optional['int']] = mapped_column(
        BIGINT, ForeignKey('users.telegram_id', ondelete='SET NULL')
    )

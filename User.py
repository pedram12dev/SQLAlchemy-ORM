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


class Base(DeclarativeBase):
    pass


class User(Base):
    """ create user table  """
    __tablename__ = "users"
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
    created_at = Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    referrer_id = Mapped[Optional['int']] = mapped_column(
        BIGINT, ForeignKey('users.telegram_id', ondelete='SET NULL')
    )

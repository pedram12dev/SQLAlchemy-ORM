from datetime import datetime
from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import Mapped, mapped_column


class TimestampMixin:
    created_at = Mapped[datetime] = mapped_column(
        TIMESTAMP, nullabe=True, server_defualt=func.now()
    )
    updated_at = Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=True, server_default=func.now(), onupdate=func.now()
    )


class TableNameMixin:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"

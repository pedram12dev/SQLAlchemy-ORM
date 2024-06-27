import datetime
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.functions import func


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now()
    )



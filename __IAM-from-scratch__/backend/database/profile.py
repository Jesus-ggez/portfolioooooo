from typing import Optional

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import TEXT


from .core import Base


class Profile(Base):
    __tablename__ = 'profile'


    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey('users.id', ondelete='CASCADE'),
        primary_key=True,
    )

    alias: Mapped[Optional[str]] = mapped_column(TEXT, nullable=True)
    name: Mapped[Optional[str]] = mapped_column(TEXT, nullable=True)

    username: Mapped[str] = mapped_column(
        TEXT,
        nullable=False,
        unique=True,
    )


    __table_args__ = (
        CheckConstraint(
            "username ~ '^[a-zA-Z0-9_]{3,20}$'",
            name='check_username_fmt'
        )
    )


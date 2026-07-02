from datetime import datetime
from typing import Optional


from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.types import UUID, TEXT, TIMESTAMP, BIGINT
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, func


from .core import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, default=lambda: datetime.isoformat(datetime.now())
    )

    email: Mapped[str] = mapped_column(TEXT, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(TEXT, nullable=False)



class UserFiles(Base):
    __tablename__ = 'user_files'

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

    file_size: Mapped[Optional[str]] = mapped_column(BIGINT, nullable=False)
    mime_type: Mapped[Optional[str]] = mapped_column(TEXT, nullable=False)
    file_name: Mapped[str] = mapped_column(TEXT, nullable=False)
    file_key: Mapped[str] = mapped_column(TEXT, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

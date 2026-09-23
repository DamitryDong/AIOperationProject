import os

from sqlalchemy import String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# Local default matches docker-compose.yml. Override with DATABASE_URL if needed.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://opspilot:opspilot@localhost:5432/opspilot",
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

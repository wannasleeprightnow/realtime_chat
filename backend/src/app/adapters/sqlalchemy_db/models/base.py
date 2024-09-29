from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": (
                "fk_%(table_name)s_%(column_0_name)"
                "s_%(referred_table_name)s"
            ),
            "pk": "pk_%(table_name)s",
        }
    )

    def __repr__(self) -> str:
        cols: list[str] = [
            f"{col}={getattr(self, col)}"
            for col in self.__table__.columns.keys()
        ]
        return " ".join(cols)

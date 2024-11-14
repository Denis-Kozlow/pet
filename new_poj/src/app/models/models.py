from typing import Annotated
from datetime import datetime
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.app.config.database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"))]


class TypePackageOrm(Base):
    __tablename__ = "typepackage"
    id: Mapped[intpk]
    nametype: Mapped[str]
    packages = relationship("PackageOrm", back_populates="typepackage")


class PackageOrm(Base):
    __tablename__ = "package"
    id: Mapped[intpk]
    name: Mapped[str]
    weight: Mapped[float]
    typ: Mapped[int] = mapped_column(ForeignKey("typepackage.id"))
    cost: Mapped[float]
    created_at: Mapped[created_at]
    user_token: Mapped[str]
    delivery_cost: Mapped[float]
    package_id: Mapped[str]

    typepackage = relationship("TypePackageOrm", back_populates="packages")

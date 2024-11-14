from pydantic import BaseModel, ConfigDict, field_validator
from fastapi import HTTPException


class TypePackageId(BaseModel):
    id: int


class SortPag(BaseModel):
    offset: int = 0
    limit: int = 5
    category: int | None = None

    @field_validator("offset")
    def offset_valid(cls, value):
        if value < 0:
            raise HTTPException(
                status_code=422, detail="Не может быть отрицательным числом")
        return value

    @field_validator("limit")
    def limit_valid(cls, value):
        if value < 0:
            raise HTTPException(
                status_code=422, detail="Не может быть отрицательным числом")
        return value

    @field_validator("category")
    def category_valid(cls, value):
        if value is None:
            return None
        else:
            if 1 > value or value > 3:
                raise HTTPException(
                    status_code=422, detail="Категория от 1 до 3")
            return value


class Package(BaseModel):
    name: str
    weight: float
    typ: int
    cost: float

    @field_validator("weight")
    def weight_valid(cls, value):
        if value <= 0:
            raise HTTPException(status_code=422, detail="Не корректный вес")
        return value

    @field_validator("typ")
    def typ_valid(cls, value):
        if 1 > value or value > 3:
            raise HTTPException(
                status_code=422, detail="Значение typ: от 1 до 3")
        return value

    @field_validator("cost")
    def cost_valid(cls, value):
        if value <= 0:
            raise HTTPException(
                status_code=422, detail="Цена не может быть отрецательной")
        return value


class PackageId(Package):
    id: int
    model_config = ConfigDict(from_attributes=True)


class TypePackageV(BaseModel):
    id: int
    nametype: str
    model_config = ConfigDict(from_attributes=True)


class ResponsePackage(BaseModel):
    name: str
    weight: float
    typ: str
    cost: float
    delivery_cost: float
    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_tuple(cls, tupl):
        if len(tupl) != 5:
            raise ValueError("Invalid tuple length")
        return cls(
            name=tupl[0],
            weight=tupl[1],
            typ=tupl[2],
            cost=tupl[3],
            delivery_cost=tupl[4],
        )

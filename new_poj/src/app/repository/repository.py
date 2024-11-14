import asyncio
from sqlalchemy import select, and_, text
from src.app.models.models import PackageOrm, TypePackageOrm
from src.app.config.database import async_session, sync_session
from src.app.schemas.schemas import Package, PackageId, TypePackageV, ResponsePackage, SortPag
from src.app.logic.calc import unique_id, price_delivery
from src.app.integrations.get_rate_dollar import rate_dollar
from fastapi import Request
from uuid import uuid4


def add_package(data):
    with sync_session() as session:
        new_package = PackageOrm(
            **data,
            delivery_cost=price_delivery(
                data["weight"], data["cost"], rate_dollar()),
        )
        session.add(new_package)
        session.commit()


async def get_type():
    async with async_session() as session:
        query = select(TypePackageOrm)
        result = await session.execute(query)
        type_models = result.scalars().all()
        types = [TypePackageV.model_validate(
            type_model) for type_model in type_models]

        return types


def get_user_token(request: Request) -> str:
    if "user_id" not in request.session:
        request.session["user_id"] = str(uuid4())
    return request.session["user_id"]


async def get_package_by_id(id: str):
    async with async_session() as session:
        query = (
            select(
                PackageOrm.name,
                PackageOrm.weight,
                TypePackageOrm.nametype,
                PackageOrm.cost,
                PackageOrm.delivery_cost,
            )
            .join(TypePackageOrm, PackageOrm.typ == TypePackageOrm.id)
            .filter(PackageOrm.package_id == id))
        res = await session.execute(query)
        try:
            model = res.one()
            package_model = ResponsePackage.from_tuple(model)
            return package_model
        except:
            return {"data": "Id not found"}


async def get_my_packages(request: Request, sort: SortPag):
    async with async_session() as session:
        token = get_user_token(request)
        query = (
            select(
                PackageOrm.name,
                PackageOrm.weight,
                TypePackageOrm.nametype,
                PackageOrm.cost,
                PackageOrm.delivery_cost,
            )
            .join(TypePackageOrm, PackageOrm.typ == TypePackageOrm.id))
        if sort.category:
            query = query.filter(
                and_(
                    PackageOrm.user_token == token,
                    PackageOrm.typ == sort.category,
                )).limit(sort.limit).offset(sort.offset)
        else:
            query = query.filter(PackageOrm.user_token == token).limit(
                sort.limit).offset(sort.offset)
        res = await session.execute(query)
        models = res.all()
        packages = [
            ResponsePackage.from_tuple(model) for model in models]
    return packages

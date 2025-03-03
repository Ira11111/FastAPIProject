from database import async_session, engine, session
from models import Base, Recipe
from sqlalchemy import desc, update
from sqlalchemy.future import select


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def count_visit(obj: Recipe):
    await session.execute(
        update(Recipe).filter(Recipe.id == obj.id).values(view_count=obj.view_count + 1)
    )


async def get_recipes_order():
    return await session.execute(select(Recipe).order_by(desc(Recipe.view_count)))


async def get_recipe_by_id(r_id: int):
    obj = await session.execute(select(Recipe).filter(Recipe.id == r_id))
    rec_obj = obj.scalar()
    if rec_obj is not None:
        await count_visit(rec_obj)

    return rec_obj


async def add_recipe(new_rec: Recipe):
    new_session = async_session()
    async with new_session.begin():
        session.add(new_rec)

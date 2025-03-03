from contextlib import asynccontextmanager
from typing import List, Union

import models
import schemas
from CRUD import add_recipe, create_tables, get_recipe_by_id, get_recipes_order
from fastapi import FastAPI, Path


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=app_lifespan)


@app.post("/recipes/", response_model=schemas.RecipeIn)
async def create_recipe(recipe: schemas.RecipeIn):
    new_rec = models.Recipe(**recipe.dict())
    await add_recipe(new_rec)
    return new_rec


@app.get("/recipes/", response_model=List[schemas.RecipeOutFirst])
async def get_popular_recipes():
    rec = await get_recipes_order()
    return rec.scalars().all()


@app.get("/recipes/{rec_id}", response_model=Union[schemas.RecipeOutSecond, str])
async def get_recipe(rec_id: int = Path(...)):  # noqa: B008
    return await get_recipe_by_id(rec_id)

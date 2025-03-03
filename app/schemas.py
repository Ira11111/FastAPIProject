from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(..., max_length=48)
    amount: int


class BaseRecipe(BaseModel):
    name: str = Field(..., max_length=48)
    cooking_time: int


class RecipeOutFirst(BaseRecipe):
    view_count: int

    class Config:
        orm_mode = True


class RecipeOutSecond(BaseRecipe):
    id: int
    ingredients: list[Product]
    description: str = Field(..., title="how to cook?", max_length=512)

    class Config:
        orm_mode = True


class RecipeIn(BaseRecipe):
    description: str
    ingredients: list[Product]

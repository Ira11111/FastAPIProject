from database import Base
from sqlalchemy import JSON, Column, Integer, String, Text


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    view_count = Column(Integer, default=0)
    cooking_time = Column(Integer, nullable=False)
    description = Column(Text, default="нет описания")
    ingredients = Column(JSON, nullable=False)

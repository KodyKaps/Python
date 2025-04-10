from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from recipe import Recipe
from recipe_orm import RecipeORM
import os
db_config = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 3306)),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_NAME', '')
    }
db_url = (
    f"mysql+pymysql://{db_config['user']}:{db_config['password']}"
    f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

new_recipe = Recipe("Pasta", ["noodles", "tomato", "basil"], 12)
new_recipe.calculate_difficulty()
session.add(new_recipe)
session.commit()

recipes = session.query(RecipeORM).all()

for recipe in recipes:
    print(f"ID: {recipe.id}")
    print(f"Name: {recipe.name}")
    print(f"Ingredients: {recipe.ingredients}")
    print(f"Cooking Time: {recipe.cooking_time} minutes")
    print(f"Difficulty: {recipe.difficulty}")
    print(f"Image URL: {recipe.image_url}\n")

recipe_0 = {
    'name': 'Cookies',
    'cooking_time': 45,
    'ingredients': ['Flour','Sugar',"eggs"]
}

recipe_1 = {
    'name': 'Tea',
    'cooking_time': 5,
    'ingredients': ['Tea leaves','Sugar',"water"]
}
recipe_2 = {
    'name': 'Pasta',
    'cooking_time': 20,
    'ingredients': ['Pasta', 'Tomato sauce', 'Garlic', 'Olive oil', 'Salt']
}

recipe_3 = {
    'name': 'Salad',
    'cooking_time': 10,
    'ingredients': ['Lettuce', 'Tomato', 'Cucumber', 'Olive oil', 'Lemon juice']
}

recipe_4 = {
    'name': 'Omelette',
    'cooking_time': 10,
    'ingredients': ['Eggs', 'Milk', 'Salt', 'Pepper', 'Cheese']
}

recipe_5 = {
    'name': 'Soup',
    'cooking_time': 30,
    'ingredients': ['Carrots', 'Onions', 'Celery', 'Chicken broth', 'Salt', 'Pepper']
}

#outer strcutre must be sequential so use list
all_recipes = [
    recipe_0,
    recipe_1,
    recipe_2,
    recipe_3,
    recipe_4,
    recipe_5
]

for r in all_recipes:
    print(r)
import pickle

def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"
    
    def take_recipe():
        recipe = {}
    
    
    recipe["name"] = input("Enter the recipe name: ")
    
    while True:
        try:
            recipe["cooking_time"] = int(input("Enter cooking time (in minutes): "))
            break
        except ValueError:
            print("Please enter a valid number for cooking time.")

            ingredients = input("Enter the ingredients separated by commas: ").split(",")
            recipe["ingredients"] = [ingredient.strip() for ingredient in ingredients]

            recipe["difficulty"] = calc_difficulty(recipe["cooking_time"], recipe[ingredients])

            return recipe

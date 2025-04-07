
from recipe import Recipe


def take_recipe():
    
    name = input("Enter the recipe name: ")

    try:
        cooking_time = int(input("Enter cooking time (in minutes): "))
        print("Please enter a valid number for cooking time.")

        ingredients = input("Enter the ingredients separated by commas: ").split(",")
        ingredients = [ingredient.strip() for ingredient in ingredients]

        #difficulty = calc_difficulty(recipe["cooking_time"], recipe["ingredients"])
        recipe = Recipe(name, ingredients, cooking_time)
        return recipe
    except ValueError as e:
        print("Error parsing recipe",e)

def main():
    recipes_list = []
    ingredients_list = []
    #create a recipe
    # then put into recipe class
    num_recipes = int(input("How many recipes do you want to enter: "))
    for i in range(0, num_recipes):
        r = take_recipe()
        recipes_list.append(r)
        ingredients_list.extend(r.get_ingredients())
    
    print("recipes_list", recipes_list)
    print("ingredients_list",ingredients_list)

if __name__ == "__main__":
    main()
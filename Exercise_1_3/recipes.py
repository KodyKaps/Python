#global defined vars
recipes_list =[]
ingredients_list =[]

def take_recipe():
    name = input("Name:")
    cooking_time = input("cooking_time(min):")
    ingredients = input("ingredients (comma separated):")
    i_list = ingredients.split(',')
    for i in i_list:
        if i not in ingredients_list:
            ingredients_list.append(i)
    recipe = {
        'name': name, 'cooking_time': cooking_time, 'ingredients': i_list
    }
    return recipe


#entry point
def main():
    print("Welcome to recipe.io!")
    num_recipes = int(input("How many recipes do you want to enter: "))
    for i in range(0, num_recipes):
        r = take_recipe()
        recipes_list.append(r)
    print(recipes_list)
    print(ingredients_list)

#if in main srun it
if __name__ == "__main__":
    main()
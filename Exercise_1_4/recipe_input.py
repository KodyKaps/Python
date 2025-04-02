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

    try:
        recipe["cooking_time"] = int(input("Enter cooking time (in minutes): "))
        print("Please enter a valid number for cooking time.")

        ingredients = input("Enter the ingredients separated by commas: ").split(",")
        recipe["ingredients"] = [ingredient.strip() for ingredient in ingredients]

        recipe["difficulty"] = calc_difficulty(recipe["cooking_time"], recipe["ingredients"])

        return recipe
    except ValueError as e:
        print("Error parsing recipe",e)

def read_csv(filename):
    data = []
    with open(filename, "r+") as f:
        for l in f.readlines():
            print(l)
            data.append(l)
    return data

def read_pickle(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

def dump_pickle(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def main():
    recipes_list = []
    ingredients_list = []
    #get input from files -> take_recipe
    try:
        #open file load contents
        raw_data_from_pkl = read_pickle("recipe.pkl")
        
        #now store pkl data in lists
        recipes_list.extend(raw_data_from_pkl["recipes_list"])
        ingredients_list.extend(raw_data_from_pkl["ingredients_list"])
        print("laoded from file successfully")
        print("recipes_list", recipes_list)
        print("ingredients_list",ingredients_list)
        print("Now you can add more recipes")
        num_recipes = int(input("How many recipes do you want to enter: "))
        for i in range(0, num_recipes):
            r = take_recipe()
            recipes_list.append(r)
            ingredients_list.extend(r["ingredients"])
        # print(r)
        parent_obj = {
            "recipes_list" : recipes_list,
            "ingredients_list" : ingredients_list       
        }
        dump_pickle("recipe.pkl",parent_obj)
        # print(read_pickle("recipe.pkl"))
        #parse input from user
        #save to file
        
    except FileNotFoundError as e:
        print("Could not find file",e, "Creating new file")
        r = take_recipe()
        parent_obj = {
            "recipes_list" :[r],
            "ingredients_list" :r["ingredients"]     
        }
        dump_pickle("recipe.pkl",parent_obj)
    finally:
        pass

if __name__ == "__main__":
    main()
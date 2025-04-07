import pickle

from recipe_input import read_pickle

def display_recipe(recipe):
    print(recipe)

def search_ingredient(i_list, searchI):
    for i in i_list:
        if(i.lower() == searchI.lower()):
            print(i, "Ingredient is in list")
            break
    print("All available ingredients", i_list)
def main():
    recipes_list = []
    ingredients_list = []
    try:
        
        #open file load contents, hard-code file for now
        raw_data_from_pkl = read_pickle("recipe.pkl")
        #now store pkl data in lists
        recipes_list.extend(raw_data_from_pkl["recipes_list"])
        ingredients_list.extend(raw_data_from_pkl["ingredients_list"])
        print(raw_data_from_pkl)
        recipe_to_view = input("Search recipe: ")
        #how to find reicpe?
        #search thrugh recipe list by name
        for r in recipes_list:
            if(r["name"].lower() == recipe_to_view.lower()):
                display_recipe(r)
        ingred_to_view = input("Search ingredient: ")
        #how to find reicpe?
        #search thrugh recipe list by name
        search_ingredient(ingredients_list, ingred_to_view)
    except FileNotFoundError as e:
         print("Could not find file",e, "Creating new file")

if __name__ == "__main__":
    main()
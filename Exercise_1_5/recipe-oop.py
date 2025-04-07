class Recipe(object):
    difficulty = "Easy"
    def __init__(self, name, ingredients, cooking_time):
        self._name =name
        self._ingredients = ingredients
        self._cooking_time = cooking_time
        self._difficulty = None

    # Getter and Setter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and Setter for cooking_time
    def get_cooking_time(self):
        return self._cooking_time

    def set_cooking_time(self, cooking_time):
        self._cooking_time = cooking_time
        self._difficulty = None  # reset difficulty if cooking time changes

    # Add ingredients (variable length)
    def add_ingredients(self, *ingredients):
        self._ingredients.extend(ingredients)
        self.update_all_ingredients()
        self._difficulty = None  # reset difficulty if ingredients change

    # Getter for ingredients
    def get_ingredients(self):
        return self._ingredients

    # Calculate difficulty
    def calculate_difficulty(self):
        num_ingredients = len(self._ingredients)
        if self._cooking_time < 10 and num_ingredients < 4:
            self._difficulty = "Easy"
        elif self._cooking_time < 10 and num_ingredients >= 4:
            self._difficulty = "Medium"
        elif self._cooking_time >= 10 and num_ingredients < 4:
            self._difficulty = "Intermediate"
        elif self._cooking_time >= 10 and num_ingredients >= 4:
            self._difficulty = "Hard"

    # Getter for difficulty
    def get_difficulty(self):
        if not self._difficulty:
            self.calculate_difficulty()
        return self._difficulty

    # Search for an ingredient
    def search_ingredient(self, ingredient):
        return ingredient in self._ingredients

    # Update all_ingredients class variable
    def update_all_ingredients(self):
        for item in self._ingredients:
            Recipe.all_ingredients.add(item)

    # String representation
    def __str__(self):
        self.calculate_difficulty()
        return (
            f"Recipe Name: {self._name}\n"
            f"Cooking Time: {self._cooking_time} minutes\n"
            f"Ingredients: {', '.join(self._ingredients)}\n"
            f"Difficulty: {self._difficulty}"
        )

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
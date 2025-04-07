class Recipe(object):
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

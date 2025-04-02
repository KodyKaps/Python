import pytest#package used for testing
from Exercise_1_4.recipe_input import calc_difficulty, take_recipe

#helps make inidviual test cases more transparent when they fail instead of one method
@pytest.mark.parametrize(
    "cooking_time, ingredients, expected",
    [
        (5, ["salt", "pepper"], "Easy"),
        (5, ["salt", "pepper", "garlic", "onion"], "Medium"),
        (15, ["salt", "pepper"], "Intermediate"),
        (15, ["salt", "pepper", "garlic", "onion"], "Hard"),
        # Edge cases
        (9, ["salt", "pepper", "garlic"], "Easy"),
        (9, ["salt", "pepper", "garlic", "onion"], "Medium"),
        (10, ["salt", "pepper", "garlic"], "Intermediate"),
        (10, ["salt", "pepper", "garlic", "onion"], "Hard"),
    ]
)
def test_calc_difficulty(cooking_time, ingredients, expected):
    #call my method assert some rule
    assert calc_difficulty(cooking_time, ingredients) == expected

@pytest.mark.parametrize(
    "user_inputs, expected_recipe",
    [
        (["Pasta", "20", "tomato, garlic, onion, basil"], 
         {"name": "Pasta", "cooking_time": 20, "ingredients": ["tomato", "garlic", "onion", "basil"], "difficulty": "Hard"}),

        (["Salad", "5", "lettuce, tomato"], 
         {"name": "Salad", "cooking_time": 5, "ingredients": ["lettuce", "tomato"], "difficulty": "Easy"}),
    ]
)
def test_take_recipe(monkeypatch, user_inputs, expected_recipe):
    monkeypatch.setattr("builtins.input", lambda _: user_inputs.pop(0))

    recipe = take_recipe()

    assert recipe is not None
    assert recipe == expected_recipe

#pytest test_recipes.py
import pytest
from main import Ingredient, Recipe

class TestIngredient:
    def test_init(self):
        ingr = Ingredient("Сахар", 100, "г")
        assert ingr.name == "Сахар"
        assert ingr.quantity == 100
        assert ingr.unit == "г"

    def test_str(self):
        ingr = Ingredient("Масло", 200, "г")
        assert str(ingr) == "Масло: 200.0 г"

    def test_equality(self):
        ingr1 = Ingredient("Соль", 10, "г")
        ingr2 = Ingredient("Соль", 5, "г")
        ingr3 = Ingredient("Перец", 10, "г")
        assert ingr1 == ingr2
        assert ingr1 != ingr3

class TestRecipe:
    def test_init(self):
        ingr1 = Ingredient("Мука", 500, "г")
        ingr2 = Ingredient("Яйца", 3, "шт")
        recipe = Recipe("Блинчики", [ingr1, ingr2])
        assert recipe.title == "Блинчики"
        assert recipe.ingredients == [ingr1, ingr2]

    def test_add_ingredient(self):
        ingr1 = Ingredient("Молоко", 200, "мл")
        ingr2 = Ingredient("Молоко", 100, "мл")
        ingr3 = Ingredient("Сахар", 50, "г")
        recipe = Recipe("Каша", [ingr1])
        recipe.add_ingredient(ingr2)
        assert recipe.ingredients[0].quantity == 300
        recipe.add_ingredient(ingr3)

    def test_scale(self):
        ingr1 = Ingredient("Мука", 500, "г")
        ingr2 = Ingredient("Яйца", 3, "шт")
        recipe = Recipe("Блинчики", [ingr1, ingr2])
        scaled_recipe = recipe.scale(2)
        assert scaled_recipe.ingredients[0].quantity == 1000
        assert scaled_recipe.ingredients[1].quantity == 6
        with pytest.raises(ValueError):
            recipe.scale(0)

        with pytest.raises(ValueError):
            recipe.scale(-1)

    def test_len(self):
        ingr1 = Ingredient("Мука", 500, "г")
        ingr2 = Ingredient("Яйца", 3, "шт")
        recipe = Recipe("Блинчики", [ingr1, ingr2])
        assert len(recipe) == 2
    

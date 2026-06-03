#pytest test_recipes.py
from unittest import result

import pytest
from main import Ingredient, Recipe, ShoppingList

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
    
class TestShoppingList:
    def test_add_recipe(self):
        ingr1 = Ingredient("Мука", 500, "г")
        ingr2 = Ingredient("Яйца", 3, "шт")
        recipe = Recipe("Блинчики", [ingr1, ingr2])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe, 2)
        assert shopping_list._items == [(Ingredient("Мука", 1000, "г"), "Блинчики"), (Ingredient("Яйца", 6, "шт"), "Блинчики")]
        with pytest.raises(ValueError):
            shopping_list.add_recipe(recipe, 0)


    def test_remove_recipe(self):
        ingr1 = Ingredient("Мука", 500, "г")
        ingr2 = Ingredient("Яйца", 3, "шт")
        recipe1 = Recipe("Блинчики", [ingr1, ingr2])
        recipe2 = Recipe("Омлет", [ingr2])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe1, 2)
        shopping_list.add_recipe(recipe2, 1)
        assert shopping_list._items == [(Ingredient("Мука", 1000, "г"), "Блинчики"), (Ingredient("Яйца", 6, "шт"), "Блинчики"), (Ingredient("Яйца", 3, "шт"), "Омлет")]
        shopping_list.remove_recipe(recipe1)
        assert shopping_list._items == []

    def test_get_list(self):
        ingr1 = Ingredient("Мука", 500, "г")
        ingr2 = Ingredient("Яйца", 3, "шт")
        recipe = Recipe("Блинчики", [ingr1, ingr2])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe, 2)
        result = shopping_list.get_list()
    
        assert len(result) == 2
        assert result[0].name == "Мука"
        assert result[0].quantity == 1000
        assert result[0].unit == "г"
        assert result[1].name == "Яйца"
        assert result[1].quantity == 6
        assert result[1].unit == "шт"

    def test_add(self):
        ingr1 = Ingredient("Мука", 500, "г")
        ingr2 = Ingredient("Яйца", 3, "шт")
        recipe1 = Recipe("Блинчики", [ingr1, ingr2])
        shopping_list1 = ShoppingList()
        shopping_list1.add_recipe(recipe1, 2)
    
        ingr3 = Ingredient("Молоко", 200, "мл")
        ingr4 = Ingredient("Яйца", 2, "шт")
        recipe2 = Recipe("Омлет", [ingr3, ingr4])
        shopping_list2 = ShoppingList()
        shopping_list2.add_recipe(recipe2, 1)
    
        shopping_list3 = shopping_list1.__add__(shopping_list2)
    
        assert len(shopping_list3._items) == 4
        assert shopping_list3._items[0][0].name == "Мука"
        assert shopping_list3._items[0][0].quantity == 1000
        assert shopping_list3._items[0][1] == "Блинчики"
    
        assert shopping_list3._items[1][0].name == "Яйца"
        assert shopping_list3._items[1][0].quantity == 6
        assert shopping_list3._items[1][1] == "Блинчики"
    
        assert shopping_list3._items[2][0].name == "Молоко"
        assert shopping_list3._items[2][0].quantity == 200
        assert shopping_list3._items[2][1] == "Омлет"
    
        assert shopping_list3._items[3][0].name == "Яйца"
        assert shopping_list3._items[3][0].quantity == 2
        assert shopping_list3._items[3][1] == "Омлет"
    
        assert len(shopping_list1._items) == 2
        assert len(shopping_list2._items) == 2
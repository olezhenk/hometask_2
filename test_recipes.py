from main import Ingredient

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


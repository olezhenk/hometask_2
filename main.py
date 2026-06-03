class Ingredient:
  def __init__(self, name, quantity, unit):
    self.name = name
    self.quantity = quantity
    self.unit = unit

  @property
  def quantity(self):
    return self._quantity

  @quantity.setter
  def quantity(self, input_value):
    if input_value < 0:
      raise ValueError("Количество должно быть положительным")
    else:
      self._quantity = float(input_value)

  def __str__(self):
    return f"{self.name}: {self._quantity} {self.unit}"

  def __repr__(self):
    return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

  def __eq__(self, other):
    if isinstance(other, Ingredient):
      if self.name == other.name and self.unit == other.unit:
        return True
      else:
        return False
    else:
       raise TypeError("Сравнение возможно только между объектами класса Ingredient")


class Recipe:
    def __init__(self, title, ingredients: list):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient):
        for ingr in self.ingredients:
            if ingr.name == ingredient.name and ingr.unit == ingredient.unit:
                ingr.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if ratio.isinstance(float):
            if ratio <=0:
                return False
            else:
                return True
        else:
            return False

    def scale(self, ratio:float):
        for ingr in self.ingredients:
            ingr.quantity *= ratio
        return self

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        return f"{self.title}: {self.ingredients}"

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
      if portions <=0:
         raise ValueError("Количество порций должно быть положительным")
      else:
         recipe.scale(portions)
         for ingr in recipe.ingredients:
            self._items.append((ingr, recipe.title))

    def remove_recipe(self, recipe: Recipe):
        for item in self._items:
            if item[1] == recipe.title:
                self._items.remove(item)

    def get_list(self):
        total_list = {}
        for item in self._items:
            ingr = item[0]
            if ingr.name in total_list:
                total_list[ingr.name] += ingr.quantity
            else:
                total_list[ingr.name] = ingr.quantity
        return total_list
    
    def __add__(self, other):
        new_list = ShoppingList()
        for item in self._items:
            new_list._items.append(item)
        for item in other._items:
            new_list._items.append(item)
        return new_list

class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients: None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio:float):
       super().scale(ratio)
       return DietaryRecipe(self.title, self.diet_type, self.ingredients)   

    def __str__(self):
           return f"{self.title} [{self.diet_type}]: {self.ingredients}"           
      
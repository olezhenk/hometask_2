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

  def __eq__(ingr1, ingr2):
    if ingr1.name == ingr2.name and ingr1.unit == ingr2.unit:
      return Ingredient(ingr1.name, ingr1.quantity + ingr2.quantity, ingr1.unit)
    else:
      return ingr1


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
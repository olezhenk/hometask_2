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
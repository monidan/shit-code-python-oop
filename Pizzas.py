
class Pizza:
  def __init__(self, size):
    self._size = size 

    self._price = 0
    self.is_discounted = False

  @property
  def size(self):
    return self._size

  @property
  def size_naming(self):
    if self.size == 1:
      return 'Маленька'
    elif self.size == 2:
      return 'Стандартна'
    elif self.size == 3:
      return'Велика'

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, new_price):
    if self.size_naming  == 'Маленька':
      self._price = round(new_price * 0.6 * 1.05)
    elif self.size_naming == 'Стандартна':
      self._price = round(new_price)
    elif self.size_naming == 'Велика':
      self._price = round(new_price * 1.4)
    return self._price 

  def apply_discount(self, discount):
    if self.is_discounted:
      return None
    self.price *= (1 - discount)
    self.is_discounted = True

  def __repr__(self):
    raise Exception('Override __repr__ method')


class PizzaMeat10(Pizza):
  def __init__(self, size):
    super().__init__(size)

    self.standart_price = 115
    self.price = self.standart_price

  def __repr__(self):
    pizza_name = "Піцца 'чотири мʼяса'"
    return '{name} (ціна: {price} грн, розмір: {size})'.format(name=pizza_name, price=str(self.price), size=self.size_naming) 


class PizzaHunt14(Pizza):
  def __init__(self, size):
    super().__init__(size)

    self.standart_price = 105
    self.price = self.standart_price

  def __repr__(self):
    pizza_name = "Піцца 'Мисливська'"
    return '{name} (ціна: {price} грн, розмір: {size})'.format(name=pizza_name, price=str(self.price), size=self.size_naming) 



class PizzaSeafood8(Pizza):
  def __init__(self, size):
    super().__init__(size)

    self.standart_price = 185
    self.price = self.standart_price

  def __repr__(self):
    pizza_name = "Піцца з морепродуктами"
    return '{name} (ціна: {price} грн, розмір: {size})'.format(name=pizza_name, price=str(self.price), size=self.size_naming) 


class PizzaCaprichosis5(Pizza):
  def __init__(self, size):
    super().__init__(size)

    self.standart_price = 145
    self.price = self.standart_price

  def __repr__(self):
    pizza_name = "Капрічоза"
    return '{name} (ціна: {price} грн, розмір: {size})'.format(name=pizza_name, price=str(self.price), size=self.size_naming) 


class PizzaBBQ15(Pizza):
  def __init__(self, size):
    super().__init__(size)

    self.standart_price = 150
    self.price = self.standart_price

  def __repr__(self):
    pizza_name = "Курка BBQ"
    return '{name} (ціна: {price} грн, розмір: {size})'.format(name=pizza_name, price=str(self.price), size=self.size_naming) 

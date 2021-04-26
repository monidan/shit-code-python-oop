
from Pizzas import PizzaMeat10, PizzaHunt14, PizzaBBQ15, PizzaSeafood8, PizzaCaprichosis5
import BankAccount

class Order:
  def __init__(self, bank_account):
    self.pizzas = []
    self.bank_account = bank_account
    self.is_discount_applied = None
    
  def add_product_in_order(self, product_number, pizza_size_id):
    if product_number == 1:
      pizza = PizzaMeat10(pizza_size_id)
      self.pizzas.append({'id': len(self.pizzas), 'pizza': pizza, 'size_id': pizza_size_id})
    elif product_number == 2:
      pizza = PizzaHunt14(pizza_size_id)
      self.pizzas.append({'id': len(self.pizzas), 'pizza': pizza, 'size_id': pizza_size_id})
    elif product_number == 3: 
      pizza = PizzaSeafood8(pizza_size_id)
      self.pizzas.append({'id': len(self.pizzas), 'pizza': pizza, 'size_id': pizza_size_id})
    elif product_number == 4: 
      pizza = PizzaBBQ15(pizza_size_id)
      self.pizzas.append({'id': len(self.pizzas), 'pizza': pizza, 'size_id': pizza_size_id})
    elif product_number == 5:
      pizza = PizzaCaprichosis5(pizza_size_id)
      self.pizzas.append({'id': len(self.pizzas), 'pizza': pizza, 'size_id': pizza_size_id})

    if pizza_size_id == 3:
      self.is_discount_applied = True

  def confirm(self):
    if len(self.pizzas) >= 3:
      self.print_order()
      is_sub_menu_showing = True

      while (is_sub_menu_showing):
        print('\n1 - Перевірити банківський рахунок')
        print('2 - Показати замовлення')
        print('3 - Оплатити')
        print('4 - Повернутися до вибору')
        if self.bank_account.is_able_to_withdraw(self.count_final_sum()):
          print('Ви здатні оплатити!')
        else:
          print('Ви не здатні оплатити!')
        choice = input()
        is_sub_menu_showing = self.sub_menu_choice_handler(int(choice))
    else:
      print("У заказі повинно бути не менше 3-х піцц!")

  def reject(self):
    print("Ви впевнені? (так/ні)")
    choice = input()

    if choice == 'так':
      self.pizzas = []
      print("Замовлення онульоване!")
    elif choice == 'ні':
      print("Дуже гарно, що ви змінили своє рішення :)")
    else: 
      print("Шо?")

  def apply_discounts(self):
    DISCOUNT = 0.05
    if self.is_discount_applied:
      for pizza in self.pizzas:
        if pizza['size_id'] != 3:
          pizza['pizza'].apply_discount(DISCOUNT)

  def count_final_sum(self):
    total = 0

    self.apply_discounts()

    for pizza in self.pizzas:
      total += pizza['pizza'].price
    return round(total)

  def print_order(self):
    print('Ваше замовлення:')
    self.apply_discounts()
    for (index, pizza) in enumerate(self.pizzas):
      print('{0} - {1}'.format(index + 1, pizza['pizza']))
    print('Усе це коштує {0} грн'.format(self.count_final_sum()))

  def get_check(self):
    self.print_order()
    print('Загальна сума чеку: {0} грн'.format(str(self.count_final_sum())))
  
  def sub_menu_choice_handler(self, choice):
    if choice == 1:
      print(self.bank_account)
      return True
    elif choice == 2:
      self.print_order()
      return True
    elif choice == 3:
      if self.bank_account.is_able_to_withdraw(self.count_final_sum()):
        self.bank_account.withdraw_money(self.count_final_sum())
        self.get_check()
        print(self.bank_account)
        return False
      print('Нє, мало грошей в тебе!')
      return True
    elif choice == 4:
      return False
    print('Шо?')
    return True
      


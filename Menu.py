
from Order import Order

class Menu:
  def __init__(self, bank_account):
    self.is_menu_visible = None
    self.order = Order(bank_account)
    
  def show_pizzas_menu(self):
      print("___МЕНЮ___")
      print("1 - Піцца 'чотири мʼяса'")
      print("2 - Піцца 'Мисливська'")
      print("3 - Піцца з морепродуктами")
      print("4 - Курча BBQ")
      print("5 - 'Капрічоза'")
      print("9 - Підтвердити замовлення")
      print("0 - Відмінити замовлення")

      return input()

  def show_pizzas_type(self):
    print("___ТИП ПІЦЦИ___")
    print("1 - Маленька")
    print("2 - Стандартна")
    print("3 - Велика")

    return input()

  def show_menu(self):
    self.is_menu_visible = True

    while (self.is_menu_visible):
      pizza_choice = self.show_pizzas_menu()

      if pizza_choice == 'домінос':
        print('Ну давай, до побачення, зрадник..')
        self.is_menu_visible = False
        break

      pizza_choice = int(pizza_choice)

      if pizza_choice >= 1 and pizza_choice <= 5:
        pizza_size = int(self.show_pizzas_type())

      for menu_index in range(0, 10):
        if pizza_choice == menu_index:
          if pizza_choice == 9:
            self.order.confirm()
          elif pizza_choice == 0:
            self.order.reject()
          else:
            self.order.add_product_in_order(pizza_choice, pizza_size)
        


            

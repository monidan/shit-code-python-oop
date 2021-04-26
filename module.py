from Pizzas import PizzaBBQ15, PizzaCaprichosis5, PizzaHunt14, PizzaMeat10, PizzaSeafood8 
from BankAccount import Account
from Menu import Menu

def init():
  account = Account(1300)
  menu = Menu(account)

  menu.show_menu()


init()

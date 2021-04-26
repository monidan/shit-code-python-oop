class Account:
  def __init__(self, money_amount):
    self.money_amount = money_amount

  def put_money(self, putting_money_amount):
    if putting_money_amount > 0:
      self.money_amount += putting_money_amount 
      return True
    return False

  def withdraw_money(self, withdrawing_money_amount):
    if self.is_able_to_withdraw(withdrawing_money_amount):
      self.money_amount -= withdrawing_money_amount
      return True  
    return False
 
  def is_able_to_withdraw(self, amount_of_money):
    if self.money_amount >= amount_of_money:
      return True
    return False

  def __repr__(self):
    return 'Кількість грошей на рахунку: {0} грн'.format(round(self.money_amount))

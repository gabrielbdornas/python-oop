class Employee:
  '''
  Classe Employee desenvolvido durante aulas oop
  '''

  raise_amount = 1.05
  employee_count = 0

  def __init__(self, first_name, last_name, pay):
    '''
    Método init dos empregados da empresa xxxx
    '''
    self.first_name = first_name
    self.last_name = last_name
    self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
    self.pay = pay
    Employee.employee_count += 1

  def __str__(self):
    return f'{self.full_name()} - {self.pay}'

  def full_name(self):
    return f'{self.first_name} {self.last_name}'

  def raise_pay(self):
      self.pay = self.pay * Employee.raise_amount

  @classmethod
  def change_raise_amount(cls, amount):
    cls.raise_amount = amount

  @classmethod
  def from_string(cls, string):
    first_name, last_name, pay = string.split(',')
    return cls(first_name, last_name, pay)

  @staticmethod
  def work_day(year, month, day):
    import datetime
    my_date = datetime.date(year, month, day)
    if my_date.weekday() == 6 or my_date.weekday() == 5:
      return False
    else:
      return True

empl_1 = Employee('Gabriel', 'Dornas', 50000)
# print(empl_1)

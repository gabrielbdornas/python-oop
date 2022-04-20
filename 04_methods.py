# Métodos regulares: Vistos até agora (self)
# Métodos de classe: Não recebem self e utilizam @classmethod decorator
# Métodos estáticos
# Decorators: Modifica o funcionamento de um método
# Exemplo para atualizar raise_ammount
# Exemplo para criar new employee com meu próprio método contrutor alternativo from_
# Exemplo método estático

class Employee:

  raise_amount = 1.05
  employee_count = 0

  def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
    self.pay = pay
    Employee.employee_count += 1

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

string_1 = 'Gabriel,Dornas,50000'
string_2 = 'Maria,Jose,6000'
empl_1 = Employee.from_string(string_1)
empl_2 = Employee.from_string(string_2)

print(empl_1.full_name())
print(empl_2.full_name())

print(empl_1.work_day(2022, 4, 23))
print(empl_2.work_day(2022, 4, 23))
print(Employee.work_day(2022, 4, 23))



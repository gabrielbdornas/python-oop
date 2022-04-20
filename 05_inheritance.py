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

class Developer(Employee):
  def __init__(self, first_name, last_name, pay, language):
    super().__init__(first_name, last_name, pay)
    self.language = language

class Manager(Employee):
  def __init__(self, first_name, last_name, pay, employees=[]):
    super().__init__(first_name, last_name, pay)
    self.employees = employees

  def add_dev(self, dev):
    if dev not in self.employees:
      self.employees.append(dev)

  def remove_dev(self, dev):
    if dev in self.employees:
      self.employees.remove(dev)

empl_1 = Developer('Gabriel', 'Dornas', 50000, 'Python')
empl_2 = Developer('Maria', 'Jose', 6000, 'Java')
empl_3 = Developer('Jose', 'Maria', 4000, 'Python')
empl_4 = Manager('João', 'Santos', 70000,  [empl_1, empl_2])

empl_4.add_dev(empl_3)
for dev in empl_4.employees:
  print(dev.full_name())









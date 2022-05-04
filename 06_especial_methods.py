# Métodos especiais ou mágicos (underline duplo ou dunder)

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

  def __repr__(self):
    return f"Employee('{self.first_name}', '{self.last_name}', {self.pay})"

  def __str__(self):
    return f'{self.first_name} {self.last_name} - {self.email}'

  def __add__(self, other):
    return self.first_name + ' ' + other.first_name

empl_1 = Employee('Maria', 'Jose', 6000)
empl_2 = Employee('Gabriel', 'Dornas', 5000)

print(empl_1 + empl_2)







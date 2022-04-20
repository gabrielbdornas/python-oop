# Variáveis de classe x Variáveis de instância
    # Classe: compartilhada entre todas as instâncias da classe
    # Instância: Únicas em cada instância

# 1 - Criando variáveis de classe

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

empl_1 = Employee('Gabriel', 'Dornas', 50000)
empl_2 = Employee('Maria', 'Jose', 6000)
empl_3 = Employee('Jose', 'Maria', 4000)
empl_4 = Employee('João', 'Santos', 70000)

print(Employee.employee_count)


# Variáveis de classe x Variáveis de instância
    # Classe: compartilhada entre todas as instâncias da classe
    # Instância: Únicas em cada instância

# 1 - Criando classes variáveis

class Employee:

    raise_amount = 1.05
    total_employees = 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
        self.pay = pay
        Employee.total_employees += 1

    def full_name(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Não será necessário utilizar self como primeiro argumento durante criação da instância
# Não precisamos mais das instâncias e atributos definidas manualmente anteriormente
empl_gabriel = Employee('Gabriel', 'Dornas', 50000)
print(Employee.total_employees)
empl_maria = Employee('Maria', 'José', 60000)
print(Employee.total_employees)
empl_jose = Employee('José', 'Maria', 40000)
print(Employee.total_employees)

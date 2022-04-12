# Variáveis de classe x Variáveis de instância
    # Classe: compartilhada entre todas as instâncias da classe
    # Instância: Únicas em cada instância

# 1 - Criando classes variáveis

""" class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
        self.pay = pay

    def full_name(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def apply_raise(self):
        self.pay = int(self.pay * 1.05)

# Não será necessário utilizar self como primeiro argumento durante criação da instância
# Não precisamos mais das instâncias e atributos definidas manualmente anteriormente
empl_gabriel = Employee('Gabriel', 'Dornas', 50000)
empl_maria = Employee('Maria', 'José', 60000)
empl_jose = Employee('José', 'Maria', 40000)

print(empl_gabriel.pay)"""

# Mas porque não criar uma variável de classe para compartilhar com todos - raise_amount
# Melhorar a forma de atualizar os 5% de aumento

""" class Employee:

    raise_amount = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
        self.pay = pay

    def full_name(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

# Não será necessário utilizar self como primeiro argumento durante criação da instância
# Não precisamos mais das instâncias e atributos definidas manualmente anteriormente
empl_gabriel = Employee('Gabriel', 'Dornas', 50000)
empl_maria = Employee('Maria', 'José', 60000)

print(Employee.__dict__)
print(empl_gabriel.__dict__)

print(empl_gabriel.pay)
empl_gabriel.apply_raise()
print(empl_gabriel.pay) """

# 1 - Criando classes variáveis

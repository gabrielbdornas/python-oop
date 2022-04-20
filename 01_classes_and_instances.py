# Criação de classes
# Criação de instâncias de classes
# Quase tudo visto até agora são classes

# Pq utilizar classes ou objetos?
  # Permite agrupar dados e comportamentos de modo que a reutilização de código fica mais fácil
  # data = atributos
  # comportamentos = métodos

# Pense em uma classe como uma forma, que poderá ser utilizada para criação de vários objetos ao longo da exeução
# de seu programa.

# Criação da classe Empregado como exemplo. Cada Empregado terá:
  # Nome
  # E-mail
  # Pagamento/salário
  # Específicos métodos

# A classe Empregado é nossa forma
# Cada Empregado criado a partir desta forma, com suas características e ações próprias será uma instância
# desta classe

# 1 - Cada instância criada será única

class Employee:

  def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
    self.pay = pay

  def full_name(self):
    return f'{self.first_name} {self.last_name}'

empl_1 = Employee('Gabriel', 'Dornas', 50000)
empl_2 = Employee('Maria', 'Jose', 6000)
empl_3 = Employee('Jose', 'Maria', 4000)

print(empl_1.last_name)
print(empl_2.last_name)

print(empl_1.email)
print(empl_2.email)

print(empl_1.full_name())
print(empl_2.full_name())
print(empl_3.full_name())

# 4 - Full Name: Método de classe
  # Possível realizar manualmente
  # Não esqueça do parênteses após full_name pois isto é um método e não um atributo

# Cuidado: Não esqueça o primeiro argumento de métodos de classe - self

# Resumo
  # Criamos nossa primeira classe
  # Criamos instâncias dessa classe
  # Criamos instâncias atributos e métodos

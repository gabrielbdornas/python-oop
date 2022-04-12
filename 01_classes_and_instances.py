# Criação de classes
# Criação de instâncias de classes
# Quase tudo visto até agora são classes

# Pq utilizar classes ou objetos?
  # Permite agrupar dados e funções/comportamentos de modo que a reutilização de código fica mais fácil
  # data = atributos
  # funções/comportamentos = métodos

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

""" class Employee:
  pass

empl_gabriel = Employee()
empl_maria = Employee()
empl_jose = Employee() """

# Únicos em diferentes locais na memória
""" print(empl_gabriel)
print(empl_maria)
print(empl_jose) """

# 1 - Cada instância criada será única

# 2 -  Variáveis de instâncias são variáveis únicas para cada instância de uma classe

""" empl_gabriel.first_name = 'Gabriel'
empl_gabriel.last_name = 'Dornas'
empl_gabriel.email = 'gabriel.dornas@company.com'
empl_gabriel.pay = 50000

empl_maria.first_name = 'Maria'
empl_maria.last_name = 'José'
empl_maria.email = 'maria.jose@company.com'
empl_maria.pay = 60000

empl_jose.first_name = 'Jose'
empl_jose.last_name = 'Maria'
empl_jose.email = 'jose.maria@company.com'
empl_jose.pay = 40000

print(empl_gabriel.email)
print(empl_maria.email)
print(empl_jose.email) """

# 2 -  Variáveis de instâncias são variáveis únicas para cada instância de uma classe

# 3 - Refatorando nosso código para criar variáveis de instância durante a criação da classe
  # Evitar códigos repetidos
  # Evitar erros
  # Método especial __init__ - construtor
  # __init__ recebe a instância automaticamente como primeiro argumento = self
  # Utilizar self = empl_gabriel.last_name, mas agora será feito automaticamente

""" class Employee:

  def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
    self.pay = pay

# Não será necessário utilizar self como primeiro argumento durante criação da instância
# Não precisamos mais das instâncias e atributos definidas manualmente anteriormente
empl_gabriel = Employee('Gabriel', 'Dornas', 50000)
empl_maria = Employee('Maria', 'José', 60000)
empl_jose = Employee('José', 'Maria', 40000)

# Tudo continua funcionando
print(empl_gabriel.email)
print(empl_maria.email)
print(empl_jose.email)

print(f'{empl_gabriel.first_name} recebe R${empl_gabriel.pay}')
print(f'{empl_maria.first_name} recebe R${empl_maria.pay}')
print(f'{empl_jose.first_name} recebe R${empl_jose.pay}') """

# 3 - Refatorando nosso código para criar variáveis de instância durante a criação da classe

# 4 - Full Name: Nosso primeiro método de classe
  # Possível realizar manualmente

class Employee:

  def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
    self.pay = pay

  def full_name(self):
    return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

empl_gabriel = Employee('gabriel', 'dornas', 50000)
empl_maria = Employee('maria', 'josé', 60000)
empl_jose = Employee('josé', 'maria', 40000)

# Não esqueça do parênteses após full_name pois isto é um método e não um atributo
""" print(empl_gabriel.first_name)
print(empl_maria.first_name)
print(empl_jose.first_name)

print(empl_gabriel.full_name())
print(empl_maria.full_name())
print(empl_jose.full_name()) """

# 4 - Full Name: Nosso primeiro método de classe

# Cuidado: Não esqueça o primeiro argumento de métodos de classe - self

# Print para mostrar que é a mesma coisa
print(Employee.full_name(empl_gabriel)) # Aqui chamo o método pela classe e ele não sabe qual instância desejo
print(empl_gabriel.full_name()) # Passa self automaticamente

# Resumo
  # Criamos nossa primeira classe
  # Criamos instâncias dessa classe
  # Criamos classes atributos e métodos


# Criação de classes
# Criação de instâncias de classes
# Quase tudo visto até agora são classes

# Pq utilizar classes ou objetos?
  # Permite agrupar dados e comportamentos de modo que a reutilização de código fica mais fácil
  # data = atributos
  # comportamentos = métodos

class Employee:

    def __init__(self, name, full_name):
        self.name = name
        self.full_name = full_name

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

# 2 -  Variáveis de instâncias são variáveis únicas para cada instância de uma classe

# 3 - Refatorando nosso código para criar variáveis de instância durante a criação da classe
  # Evitar códigos repetidos
  # Evitar erros
  # Método especial __init__ - construtor
  # __init__ recebe a instância automaticamente como primeiro argumento = self
  # Utilizar self = empl_gabriel.last_name, mas agora será feito automaticamente

# 4 - Full Name: Nosso primeiro método de classe
  # Possível realizar manualmente
  # Não esqueça do parênteses após full_name pois isto é um método e não um atributo

# Cuidado: Não esqueça o primeiro argumento de métodos de classe - self

# Resumo
  # Criamos nossa primeira classe
  # Criamos instâncias dessa classe
  # Criamos instâncias atributos e métodos

# Crie a classe Alunos com:

# Variáveis de instância:
# Nome (string)
# Sobrenome (string)
# Idade (Inteiro)
# Genero (string)
# Nota Português (float)
# Nota Matemática (float)

# Método Nome Completo (Retornar uma string)

# Método Adiciona nota (Retorna a nova nota)

# Método Passou de ano (Retornar True ou False)
# Notas de Português e Matemática Maior que 70

# Método de Classe com a contagem dos alunos

class Alunos:

    def __init__(self, nome, sobrenome, idade, genero, nota_portugues, nota_matematica):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.genero = genero
        self.nota_portugues = nota_portugues
        self.nota_matematica = nota_matematica

aluno_1 = Alunos('Gabriel', 'Dornas', 37, 'Masculino', 70, 75)

print(aluno_1.nome)
print(aluno_1.nota_matematica)

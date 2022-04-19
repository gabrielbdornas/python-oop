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

# Variável de Classe com a contagem dos alunos

class Alunos:

    num_alunos = 0

    def __init__(self, nome, sobrenome, idade, genero, nota_portugues, nota_matematica, nota_historia):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.genero = genero
        self.nota_portugues = nota_portugues
        self.nota_matematica = nota_matematica
        self.nota_historia = nota_historia

        Alunos.num_alunos +=1

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def add_nota(self, materia, nota):
        if materia == 'Português':
            self.nota_portugues += nota
        elif materia == 'Matemática':
            self.nota_matematica += nota
        elif materia == 'História':
            self.nota_historia += nota

    def passou_de_ano(self):
        if self.nota_matematica >= 70 and self.nota_portugues >= 70 and self.nota_historia >= 70:
            return True
        else:
            return False

aluno_1 = Alunos('Gabriel', 'Dornas', 37, 'Masculino', 68, 75, 80)
aluno_1 = Alunos('Maria', 'José', 20, 'Feminino', 68, 75, 80)
aluno_1 = Alunos('Maria', 'José', 20, 'Feminino', 68, 75, 80)
aluno_1 = Alunos('Maria', 'José', 20, 'Feminino', 68, 75, 80)
aluno_1 = Alunos('Maria', 'José', 20, 'Feminino', 68, 75, 80)

""" print(aluno_1.nome)
print(aluno_1.nota_portugues)
aluno_1.add_nota('Português', 2)
print(aluno_1.nota_portugues)
print(aluno_1.nome_completo())
print(aluno_1.passou_de_ano()) """
print(Alunos.num_alunos)

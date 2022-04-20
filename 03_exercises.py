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

# Método de classe para criar alunos a partir de um arquivo csv

# Método estático para falar se hoje é dia de aula

class Alunos():

    alunos_count = 0

    def __init__(self, nome, sobrenome, idade, genero, nota_portugues, nota_matematica):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = int(idade)
        self.genero = genero
        self.nota_portugues = int(nota_portugues)
        self.nota_matematica = int(nota_matematica)

        Alunos.alunos_count += 1

    def nome_completo(self):
        return f'{self.nome.upper()} {self.sobrenome.upper()}'

    def ad_notas(self, materia, nota):
        if materia == 'Português':
            self.nota_portugues += nota
        elif materia == 'Matemática':
            self.nota_matematica += nota

    def passou_de_ano(self):
        if (self.nota_portugues + self.nota_matematica)/2 >= 70:
            return 'Sim'
        else:
            return 'Não'

    @classmethod
    def do_arquivo_csv(cls, atributos):
        return cls(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4], atributos[5])

    @staticmethod
    def dia_de_aula(year, month, day):
        import datetime
        minha_data = datetime.date(year, month, day).weekday()
        if minha_data >= 4:
            return 'Não é dia de aula'
        else:
            return 'É dia de aula'

class Monitor(Alunos):
    def __init__(self, nome, sobrenome, idade, genero, nota_portugues, nota_matematica, disciplina, alunos=[]):
        super().__init__(nome, sobrenome, idade, genero, nota_portugues, nota_matematica)
        self.disciplina = disciplina
        self.alunos = alunos

    def add_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)

    def remove_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

monitor = Monitor('Júlio', 'Pereira', 40, 'Masculino,', 99, 70, 'Portugês')

meus_alunos = []
with open('alunos.csv') as arquivo:
    import csv
    reader = csv.reader(arquivo, delimiter=',')
    for linha in reader:
        aluno = Alunos.do_arquivo_csv(linha)
        meus_alunos.append(aluno)

for aluno in meus_alunos:
    print(f'{aluno.nome_completo()} tirou {aluno.nota_matematica} em matemática e {aluno.nota_portugues} em português')


monitor.add_aluno(meus_alunos[0])
monitor.add_aluno(meus_alunos[-1])
print(monitor.alunos)
monitor.remove_aluno(meus_alunos[-1])
print(monitor.alunos)


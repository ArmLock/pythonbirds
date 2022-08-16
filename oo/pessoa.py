class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 55

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa) :
    def cumprimentar(self):
        return 'Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    Romao = Mutante(nome='Romão')
    Ronaldo = Pessoa(Romao, nome='Ronaldo')
    print(Pessoa.cumprimentar(Ronaldo))
    print(id(Ronaldo))
    print(Ronaldo.cumprimentar())
    print(Ronaldo.nome)
    print(Ronaldo.idade)
    for filho in  Ronaldo.filhos:
        print(filho.nome)
    Ronaldo.sobrenome = 'Lima'
    del Ronaldo.filhos
    Ronaldo.olhos = 1
    del Ronaldo.olhos
    print(Ronaldo.__dict__)
    print(Romao.__dict__)
    print(Pessoa.olhos)
    print(Ronaldo.olhos)
    print(Romao.olhos)
    print(id(Pessoa.olhos), id(Ronaldo.olhos), id(Romao.olhos))
    print(Pessoa.metodo_estatico(), Ronaldo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Ronaldo.nome_e_atributos_de_classe())
    pessoa = Pessoa ('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(Romao, Pessoa))
    print(isinstance(Romao, Homem))
    print(Romao.olhos)
    print(Ronaldo.cumprimentar())
    print(Romao.cumprimentar())

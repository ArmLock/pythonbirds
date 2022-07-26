class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Romao = Pessoa(nome='Romão')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Ronaldo.olhos)
    print(Romao.olhos)
    print(id(Pessoa.olhos), id(Ronaldo.olhos), id(Romao.olhos))


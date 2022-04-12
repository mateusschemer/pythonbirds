class Pessoa:
    def __init__(self, *filhos, nome=None, idade=38):
        self.idade=idade
        self.nome = nome
        self.filhos=list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    mateus = Pessoa(nome='Mateus')
    helena = Pessoa(mateus, nome='Helena')
    print(Pessoa.cumprimentar(helena))
    print(id(helena))
    print(helena.cumprimentar())
    print(helena.nome)
    print(helena.idade)
    for filho in mateus.filhos:
        print(filho.mateus)
    mateus.sobrenome ='Schemer'
    del mateus.filhos
    print(mateus.sobrenome)
    print(mateus.__dict__)
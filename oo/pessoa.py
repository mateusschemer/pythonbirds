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
    print(Pessoa.cumprimentar(mateus))
    print(id(mateus))
    print(mateus.cumprimentar())
    print(mateus.nome)
    print(mateus.idade)
    print(helena.filhos)


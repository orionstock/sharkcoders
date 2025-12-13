class pessoa:
    def __init__(self, idade, nacionalidade):
        self.idade = idade
        self.nacionalidade = nacionalidade

    def mostra_idade(self):
        print(self.idade)

    def mostra_nacionalidade(self):
        print(self.nacionalidade)

pedro = pessoa(19, "português")
pedro.mostra_idade()
pedro.mostra_nacionalidade()
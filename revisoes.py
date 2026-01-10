class produto:
    def __init__(self, preco, nome, stock):
        self.preco = preco
        self.nome = nome
        self.stock = stock

    def mostra_produto(self):
        print(f"Preço: {self.preco}")
        print(f"Nome: {self.nome}")
        print(f"Stock: {self.stock}")

    def comprar_produto(self, quantidade):
        if quantidade <= self.stock:
            self.stock -= quantidade
            total = self.preco * quantidade
            return total
        else:
            print("Sem stock.")

    def adicionar_stock(self, quantidade):
        self.stock += quantidade


class loja:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            produto.mostra_produto()

    def comprar_produtoo(self, produto, quantidade):
        if produto in self.produtos:
            total = produto.comprar_produto(quantidade)
            print(total)

    def valor_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.stock * produto.preco
        return total


produto1 = produto(0.23, "Laranja", 6)
produto2 = produto(1.40, "Arroz", 5)

loja = loja()
loja.adicionar_produto(produto1)
loja.adicionar_produto(produto2)

loja.listar_produtos()

loja.comprar_produtoo("Laranja", 3)

loja.listar_produtos()

print(f"\nValor total da loja: {loja.valor_total()}€")

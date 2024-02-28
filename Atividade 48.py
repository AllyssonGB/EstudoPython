class Produtos:
    def __init__(self, tipo, nome, preco):
        self.tipo = tipo
        self.nome = nome
        self.preco = preco

    def produto(self):
        print(self.tipo)
        print(self.nome)
        print(self.preco)


expresso = Produtos("Café", "Expresso", 4.9)
cf_com_leite_medio = Produtos("Café", "Café com leite Médio", 5.7)
cf_com_chantilly = Produtos("Café", "Café com Chantilly", 8)
cf_duplo = Produtos("Café", "Café Duplo", 8.5)
cf_com_cointreau = Produtos("Café", "Café com Cointreau", 8.5)
cf_italiano = Produtos("Café", "Café Italiano", 8.5)
cpp_pequeno = Produtos("Café", "Cappuccino pequeno", 5.5)
cpp_grande = Produtos("Café", "Cappuccino grande", 8)
cpp_gelado = Produtos("Café", "Cappuccino Gelado", 14.5)
latte_macchiatto = Produtos("Café", "Latte Macchiatto", 7)

print(cf_com_leite_medio.tipo)
print(cf_com_chantilly.tipo)
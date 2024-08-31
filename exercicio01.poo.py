class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        return (self.saude - self.fome) / 2


bichinho = BichinhoVirtual("Tama", 5, 8, 2)
print(f"Nome: {bichinho.retornar_nome()}")
print(f"Fome: {bichinho.retornar_fome()}")
print(f"Saúde: {bichinho.retornar_saude()}")
print(f"Idade: {bichinho.retornar_idade()}")
print(f"Humor: {bichinho.calcular_humor()}")

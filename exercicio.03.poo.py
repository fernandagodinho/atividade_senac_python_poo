import random

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.saude = random.randint(0, 10)
        self.idade = 0

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

    def __str__(self):
        return (f"Nome: {self.nome}, Fome: {self.fome}, Saúde: {self.saude}, "
                f"Idade: {self.idade}, Humor: {self.calcular_humor()}")

class FazendaBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionar_bichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentar_todos(self):
        for bichinho in self.bichinhos:
            bichinho.alterar_fome(max(bichinho.retornar_fome() - 1, 0))

    def brincar_todos(self):
        for bichinho in self.bichinhos:
            bichinho.alterar_saude(min(bichinho.retornar_saude() + 1, 10))

    def ouvir_todos(self):
        for bichinho in self.bichinhos:
            print(f"Nome: {bichinho.retornar_nome()}, Fome: {bichinho.retornar_fome()}, Saúde: {bichinho.retornar_saude()}, Idade: {bichinho.retornar_idade()}, Humor: {bichinho.calcular_humor()}")

    def mostrar_atributos(self):
        for bichinho in self.bichinhos:
            print(bichinho)

# Exemplo de uso
fazenda = FazendaBichinhos()
fazenda.adicionar_bichinho(BichinhoVirtual("Tama"))
fazenda.adicionar_bichinho(BichinhoVirtual("Gushi"))

# Menu de opções
while True:
    print("\n1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ouvir todos os bichinhos")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        fazenda.alimentar_todos()
    elif opcao == "2":
        fazenda.brincar_todos()
    elif opcao == "3":
        fazenda.ouvir_todos()
    elif opcao == "4":
        break
    elif opcao == "secreto":
        fazenda.mostrar_atributos()
    else:
        print("Opção inválida!")

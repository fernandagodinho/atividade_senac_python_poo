class BichinhoVirtualMais:
    
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = 0



    def alimentar(self, quantidade):
        self.fome -= quantidade
        if self.fome < 0:
            self.fome = 30

    def brincar(self, tempo):
        self.tedio -= tempo
        self.saude += tempo
        if self.tedio < 0:
            self.tedio = 0
        if self.saude > 100:
            self.saude = 100

    def retornar_tedio(self):
        return self.tedio

    def humor(self):
        return (self.saude - self.fome - self.tedio) / 3
    
    def retornar_nome(self):
        return self.nome
    
    def retornar_fome(self):
        return self.fome
    
    def retornar_saude(self):
        return self.saude
    
    def retornar_idade(self):
        return self.idade + 1 if self.idade < 10 else 10
    
    def crescer(self):
        self.idade += 1
        if self.idade > 10:
            self.idade = 10
            
    
bichinho = BichinhoVirtualMais("Tamagushi")
bichinho.alimentar(10)
bichinho.brincar(5)

print(f"Nome: {bichinho.retornar_nome()}")
print(f"Fome: {bichinho.retornar_fome()}")
print(f"Saúde: {bichinho.retornar_saude()}")
print(f"Idade: {bichinho.retornar_idade()}")
print(f"Tédio: {bichinho.retornar_tedio()}")
print(f"Humor: {bichinho.humor()}")

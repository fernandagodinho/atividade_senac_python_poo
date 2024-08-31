class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        if self.bucho:
            self.bucho.pop(0)

# Criando dois macacos
macaco1 = Macaco("Macaco1")
macaco2 = Macaco("Macaco2")

# Alimentando os macacos com diferentes alimentos
macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Laranja")

macaco2.comer("Manga")
macaco2.comer("Abacaxi")
macaco2.comer("Melancia")

# Verificando o conteúdo do estômago após cada refeição
print(f"{macaco1.nome} tem no bucho: {macaco1.verBucho()}")
print(f"{macaco2.nome} tem no bucho: {macaco2.verBucho()}")

# Fazendo um macaco digerir
macaco1.digerir()
macaco2.digerir()

print(f"Após a digestão, {macaco1.nome} tem no bucho: {macaco1.verBucho()}")
print(f"Após a digestão, {macaco2.nome} tem no bucho: {macaco2.verBucho()}")

# Fazendo um macaco comer o outro

macaco1.comer(macaco2)

print(f"Após comer o outro macaco, {macaco1.nome} tem no bucho: {macaco1.verBucho()}")

# Simulando um macaco canibal

macaco3 = Macaco("Macaco3")
macaco3.comer(macaco1)

print(f"Após comer o outro macaco (canibal), {macaco3.nome} tem no bucho: {macaco3.verBucho()}")


#Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos
#nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e
#digerir(). Faça um programa ou teste interativamente, criando pelo menos dois
#macacos, alimentando-os com pelo menos 3 alimentos diferentes e
#verificando o conteúdo do estomago a cada refeição. Experimente fazer com
#que um macaco coma o outro. É possível criar um macaco canibal?
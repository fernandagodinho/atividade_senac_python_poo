from abc import ABC, abstractmethod

# Classe abstrata Conta
class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

# Classe ContaCorrente que herda de Conta
class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite_extra):
        super().__init__(agencia, numero, saldo)
        self.limite_extra = limite_extra

    def sacar(self, valor):
        if self.saldo + self.limite_extra >= valor:
            self.saldo -= valor
            return True
        return False

# Classe ContaPoupanca que herda de Conta
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

# Classe abstrata Pessoa
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

# Classe Cliente que herda de Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

# Classe Banco
class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.contas.append(cliente.conta)

    def autenticar(self, agencia, numero, cliente):
        if cliente in self.clientes:
            conta = cliente.conta
            if conta.agencia == agencia and conta.numero == numero:
                return True
        return False

# Criando contas
conta_corrente = ContaCorrente(123, 456, 1000, 500)
conta_poupanca = ContaPoupanca(123, 789, 2000)

# Criando clientes
cliente1 = Cliente("Geovani", 30, conta_corrente)
cliente2 = Cliente("Fernanda", 25, conta_poupanca)

# Criando banco e adicionando clientes
banco = Banco()
banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

# Testando autenticação e operações
if banco.autenticar(123, 456, cliente1):
    cliente1.conta.sacar(1200)
    print(f"Saldo após saque: {cliente1.conta.saldo}")

if banco.autenticar(123, 789, cliente2):
    cliente2.conta.depositar(500)
    print(f"Saldo após depósito: {cliente2.conta.saldo}")


#um sistema bancário com as classes Conta, ContaCorrente, ContaPoupanca, Pessoa, Cliente e Banco. 
# Implementamos os métodos de depósito e saque,
#  e a autenticação do banco para garantir que apenas clientes autenticados possam realizar operações.
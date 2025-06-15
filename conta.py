class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"\nDepósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("\nValor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor:.2f}")
            print(f"\nSaque de R${valor:.2f} realizado com sucesso!")
        else:
            print("\nSaldo insuficiente ou valor inválido.")

    def mostrar_extrato(self):
        print("\nExtrato da Conta")
        print("-----------------")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for item in self.extrato:
                print(item)
        print(f"\nSaldo atual: R${self.saldo:.2f}")

from usuario import Usuario
from conta import Conta

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def cadastrar_usuario(self):
        cpf = input("CPF (somente números): ")
        if self._buscar_usuario(cpf):
            print("\nUsuário já cadastrado!")
            return

        nome = input("Nome completo: ")
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        endereco = input("Endereço (logradouro, número - bairro - cidade/estado): ")

        novo_usuario = Usuario(nome, nascimento, cpf, endereco)
        self.usuarios.append(novo_usuario)
        print("\nUsuário cadastrado com sucesso!")

    def criar_conta(self):
        cpf = input("CPF do usuário: ")
        usuario = self._buscar_usuario(cpf)

        if not usuario:
            print("\nUsuário não encontrado. Cadastre primeiro!")
            return

        numero_conta = len(self.contas) + 1
        nova_conta = Conta(numero_conta, usuario)
        self.contas.append(nova_conta)
        print(f"\nConta {numero_conta} criada com sucesso para {usuario.nome}!")

    def acessar_conta(self):
        cpf = input("Informe o CPF do titular: ")
        numero = int(input("Informe o número da conta: "))

        conta = self._buscar_conta(cpf, numero)

        if not conta:
            print("\nConta não encontrada!")
            return

        while True:
            print("\n[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                valor = float(input("Valor para depósito: R$ "))
                conta.depositar(valor)

            elif opcao == "2":
                valor = float(input("Valor para saque: R$ "))
                conta.sacar(valor)

            elif opcao == "3":
                conta.mostrar_extrato()

            elif opcao == "4":
                break

            else:
                print("\nOpção inválida!")

    def _buscar_usuario(self, cpf):
        return next((u for u in self.usuarios if u.cpf == cpf), None)

    def _buscar_conta(self, cpf, numero):
        return next((c for c in self.contas if c.numero == numero and c.cliente.cpf == cpf), None)

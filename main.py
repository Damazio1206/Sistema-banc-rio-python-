from banco import Banco
from usuario import Usuario
from utils import menu_principal

banco = Banco()

while True:
    opcao = menu_principal()

    if opcao == "1":
        banco.cadastrar_usuario()

    elif opcao == "2":
        banco.criar_conta()

    elif opcao == "3":
        banco.acessar_conta()

    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")


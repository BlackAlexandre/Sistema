from agenda import Agenda


def menu():
    agenda = Agenda()

    while True:
        print("\n══════════════════════════════")
        print("   SISTEMA DE CONTROLE DE EVENTO")
        print("══════════════════════════════")
        print("1. Cadastrar evento")
        print("2. Listar eventos")
        print("3. Listar e")
        print("0. Sair")
        print("──────────────────────────────")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            agenda.cadastrar_evento()
        elif opcao == "2":
            agenda.listar_eventos()
        elif opcao == "0":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()

from agenda import Agenda


def menu():
    agenda = Agenda()

    while True:
        print("\n══════════════════════════════")
        print("   SISTEMA DE CONTROLE DE EVENTO")
        print("══════════════════════════════")
        print("1. Cadastrar contratante")
        print("2. Listar contratantes")
        print("3. Cadastrar evento")
        print("4. Listar eventos")
        print("0. Sair")
        print("──────────────────────────────")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            agenda.cadastrar_contratante()
        elif opcao == "2":
            agenda.listar_contratantes()
        elif opcao == "3":
            agenda.cadastrar_evento()
        elif opcao == "4":
            agenda.listar_eventos()
        elif opcao == "0":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()

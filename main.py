from agenda import Agenda

def menu():
    agenda = Agenda()

    while True:
        print("\n══════════════════════════════")
        print("BEM-VINDO AO SISTEMA DE CONTROLE DE EVENTO")
        print("══════════════════════════════")
        print("1. Cadastrar evento")
        print("2. Listar eventos")
        print("3. Quantidade total de eventos no mês")
        print("4. Remover evento")
        print("5. Editar evento")
        print("6. Gerar relatório (txt)")
        print("0. Sair")
        print("──────────────────────────────")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            agenda.cadastrar_evento()
        elif opcao == "2":
            agenda.listar_eventos()
        elif opcao == "3": 
            agenda.contar_eventos_no_mes()
        elif opcao == "4":
            agenda.remover_evento()
        elif opcao == "5":
            agenda.editar_evento()
        elif opcao == "6":
            agenda.gerar_relatorio_txt()
        elif opcao == "0":
            print("\nSaindo do sistema. Até logo!")
            break
        
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
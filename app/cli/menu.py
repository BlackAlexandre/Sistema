from app.services.agenda_service import AgendaService


def executar_menu():
    agenda = AgendaService()

    while True:
        print("\n══════════════════════════════════════")
        print("SISTEMA DE GESTÃO DE EVENTOS")
        print("══════════════════════════════════════")
        print("1. Cadastrar novo evento")
        print("2. Listar todos os eventos")
        print("3. Consultar evento pelo código")
        print("4. Contar eventos por mês e ano")
        print("5. Editar evento")
        print("6. Remover evento")
        print("7. Adicionar item de custo")
        print("8. Exibir resumo financeiro geral")
        print("9. Exibir relatório financeiro por mês")
        print("10. Gerar relatório completo em TXT")
        print("0. Sair")
        print("──────────────────────────────────────")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            agenda.cadastrar_evento()
        elif opcao == "2":
            agenda.listar_eventos()
        elif opcao == "3":
            agenda.consultar_evento()
        elif opcao == "4":
            agenda.contar_eventos_no_mes()
        elif opcao == "5":
            agenda.editar_evento()
        elif opcao == "6":
            agenda.remover_evento()
        elif opcao == "7":
            agenda.adicionar_custo()
        elif opcao == "8":
            agenda.exibir_resumo_financeiro()
        elif opcao == "9":
            agenda.exibir_relatorio_financeiro_mensal()
        elif opcao == "10":
            agenda.gerar_relatorio_txt()
        elif opcao == "0":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\n⚠️ Opção inválida.")

from datetime import date

from contratante import Contratante
from evento import Evento, formatar_reais
from base_dados import EVENTOS_INICIAIS


class Agenda:
    """
    Controla a base de eventos, as validações, as consultas e os relatórios.
    """

    def __init__(self):
        self.eventos = []
        self.proximo_id = 1
        self._carregar_base_inicial()

    def _carregar_base_inicial(self):
        """
        Converte os registros em tuplas da base interna em objetos do sistema.
        """
        for registro in EVENTOS_INICIAIS:
            (
                evento_id,
                event_name,
                event_day,
                event_month,
                event_year,
                event_date,
                event_time,
                event_location,
                number_people,
                dados_contratante,
                itens_custo
            ) = registro

            enterprise_name, tipo_documento, cnpj_cpf, whats = dados_contratante

            contratante = Contratante(
                enterprise_name,
                tipo_documento,
                cnpj_cpf,
                whats
            )

            evento = Evento(
                evento_id,
                event_name,
                event_day,
                event_month,
                event_year,
                event_date,
                event_time,
                event_location,
                number_people,
                contratante,
                itens_custo
            )

            self.eventos.append(evento)

        if self.eventos:
            self.proximo_id = max(evento.evento_id for evento in self.eventos) + 1

    def _dia_ocupado(self, day, month, year, ignorar_evento_id=None):
        """
        Procura outro evento na mesma data.
        """
        for evento in self.eventos:
            if ignorar_evento_id is not None and evento.evento_id == ignorar_evento_id:
                continue

            if (
                evento.event_day == day
                and evento.event_month == month
                and evento.event_year == year
            ):
                return evento

        return None

    def _pedir_data(self, ignorar_evento_id=None):
        """
        Solicita uma data existente e sem conflito com outro evento.
        """
        while True:
            try:
                event_day = int(input("Qual o dia do evento? "))
                event_month = int(input("Qual o mês do evento? "))
                event_year = int(input("Qual o ano do evento? "))
            except ValueError:
                print("\n⚠️ Digite apenas números inteiros.")
                continue

            if event_year < 2026 or event_year > 2100:
                print("\n⚠️ Ano inválido. Digite entre 2026 e 2100.")
                continue

            try:
                date(event_year, event_month, event_day)
            except ValueError:
                print("\n⚠️ Data inexistente. Digite uma data válida.")
                continue

            conflito = self._dia_ocupado(
                event_day,
                event_month,
                event_year,
                ignorar_evento_id
            )

            if conflito:
                print("\n❌ Já existe um evento nessa data: '{}'. Escolha outro dia.".format(
                    conflito.event_name
                ))
                continue

            return event_day, event_month, event_year

    def _pedir_documento(self):
        while True:
            print("\nTipo de documento:")
            print("1. CPF")
            print("2. CNPJ")
            tipo_opcao = input("Escolha uma opção: ").strip()

            if tipo_opcao == "1":
                tipo = "CPF"
                digitos = 11
            elif tipo_opcao == "2":
                tipo = "CNPJ"
                digitos = 14
            else:
                print("\n⚠️ Opção inválida. Escolha 1 para CPF ou 2 para CNPJ.")
                continue

            numero = input("Digite o {} (apenas números): ".format(tipo)).strip()

            if not numero.isdigit() or len(numero) != digitos:
                print("\n⚠️ {} inválido. Digite exatamente {} números.".format(tipo, digitos))
                continue

            return tipo, numero

    def _pedir_whatsapp(self):
        while True:
            whats = input("Qual o WhatsApp de contato? (Apenas números, 11 dígitos): ").strip()

            if not whats.isdigit() or len(whats) != 11:
                print("\n⚠️ WhatsApp inválido. Digite exatamente 11 números.")
                continue

            return whats

    def _pedir_horario(self):
        while True:
            horario = input("Qual o horário do evento? (Ex: 14:30) ").strip()

            if len(horario) != 5 or horario[2] != ":":
                print("\n⚠️ Digite no formato HH:MM. Exemplo: 14:30.")
                continue

            hora, minuto = horario.split(":")

            if not hora.isdigit() or not minuto.isdigit():
                print("\n⚠️ Use apenas números. Exemplo: 14:30.")
                continue

            if not 0 <= int(hora) <= 23 or not 0 <= int(minuto) <= 59:
                print("\n⚠️ Horário inválido.")
                continue

            return horario

    def _pedir_valor(self):
        """
        Aceita valor com ponto ou vírgula e impede zero, negativos e letras.
        """
        while True:
            entrada = input("Valor do item: R$ ").strip().replace(",", ".")

            try:
                valor = float(entrada)
            except ValueError:
                print("\n⚠️ Digite um valor numérico válido.")
                continue

            if valor <= 0:
                print("\n⚠️ O valor deve ser maior que zero.")
                continue

            return valor

    def _pedir_itens_custo(self):
        itens = []

        while True:
            resposta = input("\nDeseja adicionar um item de custo? (s/n): ").strip().lower()

            if resposta == "n":
                return itens

            if resposta != "s":
                print("\n⚠️ Digite apenas s ou n.")
                continue

            while True:
                nome = input("Nome do item: ").strip()

                if nome:
                    break

                print("\n⚠️ O nome do item não pode ser vazio.")

            valor = self._pedir_valor()
            itens.append((nome, valor))
            print("\n✅ Item adicionado com sucesso!")

    def _buscar_evento_por_id(self, evento_id):
        for evento in self.eventos:
            if evento.evento_id == evento_id:
                return evento

        return None

    def _pedir_id_evento(self):
        try:
            return int(input("\nDigite o código do evento: ").strip())
        except ValueError:
            print("\n⚠️ Digite um código numérico.")
            return None

    def cadastrar_evento(self):
        print("\n── Dados do Evento ──")

        while True:
            event_name = input("Qual o nome do evento? ").strip()

            if event_name:
                break

            print("\n⚠️ O nome do evento não pode ser vazio.")

        event_day, event_month, event_year = self._pedir_data()
        event_date = "{}-{:02d}-{:02d}".format(event_year, event_month, event_day)
        event_time = self._pedir_horario()

        while True:
            event_location = input("Qual o local do evento? ").strip()

            if event_location:
                break

            print("\n⚠️ O local do evento não pode ser vazio.")

        while True:
            try:
                number_people = int(input("Qual a quantidade de pessoas no evento? "))
            except ValueError:
                print("\n⚠️ Digite um número inteiro.")
                continue

            if number_people < 1:
                print("\n⚠️ Digite pelo menos 1 pessoa.")
                continue

            break

        print("\n── Dados do Contratante ──")

        while True:
            enterprise_name = input("Qual o nome do contratante? ").strip()

            if enterprise_name:
                break

            print("\n⚠️ O nome do contratante não pode ser vazio.")

        tipo_documento, cnpj_cpf = self._pedir_documento()
        whats = self._pedir_whatsapp()
        itens_custo = self._pedir_itens_custo()

        contratante = Contratante(enterprise_name, tipo_documento, cnpj_cpf, whats)

        evento = Evento(
            self.proximo_id,
            event_name,
            event_day,
            event_month,
            event_year,
            event_date,
            event_time,
            event_location,
            number_people,
            contratante,
            itens_custo
        )

        self.eventos.append(evento)
        self.proximo_id += 1

        print("\n✅ Evento cadastrado com sucesso!")
        print("🆔 Código do novo evento: {}".format(evento.evento_id))

    def listar_eventos(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado.")
            return

        print("\n══════ LISTA DE EVENTOS ══════")

        for evento in self.eventos:
            evento.exibir_dados()

    def consultar_evento_por_id(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado!")
            return

        evento_id = self._pedir_id_evento()

        if evento_id is None:
            return

        evento = self._buscar_evento_por_id(evento_id)

        if evento is None:
            print("\n❌ Evento não encontrado.")
            return

        evento.exibir_dados()

    def contar_eventos_no_mes(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado!")
            return

        try:
            mes = int(input("Digite o mês para consulta (1-12): ").strip())
            ano = int(input("Digite o ano: ").strip())
        except ValueError:
            print("\n⚠️ Digite apenas números.")
            return

        if not 1 <= mes <= 12:
            print("\n⚠️ Mês inválido.")
            return

        eventos_filtrados = [
            evento for evento in self.eventos
            if evento.event_month == mes and evento.event_year == ano
        ]

        print("\n📊 Total de eventos em {:02d}/{}: {}".format(
            mes,
            ano,
            len(eventos_filtrados)
        ))

    def remover_evento(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado!")
            return

        evento_id = self._pedir_id_evento()

        if evento_id is None:
            return

        evento = self._buscar_evento_por_id(evento_id)

        if evento is None:
            print("\n❌ Evento não encontrado.")
            return

        evento.exibir_dados()

        confirmacao = input("\nTem certeza que deseja remover? (s/n): ").strip().lower()

        if confirmacao == "s":
            self.eventos.remove(evento)
            print("\n✅ Evento removido com sucesso!")
        else:
            print("\nRemoção cancelada.")

    def editar_evento(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado!")
            return

        evento_id = self._pedir_id_evento()

        if evento_id is None:
            return

        evento = self._buscar_evento_por_id(evento_id)

        if evento is None:
            print("\n❌ Evento não encontrado.")
            return

        while True:
            evento.exibir_dados()

            print("\nO que deseja editar?")
            print("1. Nome do evento")
            print("2. Data")
            print("3. Horário")
            print("4. Local")
            print("5. Quantidade de pessoas")
            print("0. Concluir edição")

            opcao = input("Escolha: ").strip()

            if opcao == "1":
                novo = input("Novo nome: ").strip()

                if novo:
                    evento.event_name = novo
                    print("\n✅ Nome atualizado!")
                else:
                    print("\n⚠️ Nome não pode ser vazio.")

            elif opcao == "2":
                day, month, year = self._pedir_data(evento.evento_id)
                evento.event_day = day
                evento.event_month = month
                evento.event_year = year
                evento.event_date = "{}-{:02d}-{:02d}".format(year, month, day)
                print("\n✅ Data atualizada!")

            elif opcao == "3":
                evento.event_time = self._pedir_horario()
                print("\n✅ Horário atualizado!")

            elif opcao == "4":
                novo = input("Novo local: ").strip()

                if novo:
                    evento.event_location = novo
                    print("\n✅ Local atualizado!")
                else:
                    print("\n⚠️ Local não pode ser vazio.")

            elif opcao == "5":
                try:
                    novo = int(input("Nova quantidade de pessoas: "))
                except ValueError:
                    print("\n⚠️ Digite um número inteiro.")
                    continue

                if novo < 1:
                    print("\n⚠️ Digite pelo menos 1 pessoa.")
                    continue

                evento.number_people = novo
                print("\n✅ Quantidade atualizada!")

            elif opcao == "0":
                print("\n✅ Edição concluída!")
                return

            else:
                print("\n⚠️ Opção inválida.")

    def adicionar_custo_ao_evento(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado!")
            return

        evento_id = self._pedir_id_evento()

        if evento_id is None:
            return

        evento = self._buscar_evento_por_id(evento_id)

        if evento is None:
            print("\n❌ Evento não encontrado.")
            return

        while True:
            nome = input("Nome do item de custo: ").strip()

            if nome:
                break

            print("\n⚠️ O nome não pode ser vazio.")

        valor = self._pedir_valor()
        evento.adicionar_item_custo(nome, valor)

        print("\n✅ Item adicionado com sucesso!")
        print("💵 Novo total: {}".format(formatar_reais(evento.calcular_custo_total())))

    def exibir_resumo_financeiro(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado!")
            return

        total = sum(evento.calcular_custo_total() for evento in self.eventos)
        media = total / len(self.eventos)
        mais_caro = max(self.eventos, key=lambda evento: evento.calcular_custo_total())
        mais_barato = min(self.eventos, key=lambda evento: evento.calcular_custo_total())

        print("\n══════ RESUMO FINANCEIRO ══════")
        print("Eventos cadastrados: {}".format(len(self.eventos)))
        print("Total movimentado: {}".format(formatar_reais(total)))
        print("Média de custo: {}".format(formatar_reais(media)))
        print("Evento mais caro: {} - {}".format(
            mais_caro.event_name,
            formatar_reais(mais_caro.calcular_custo_total())
        ))
        print("Evento mais barato: {} - {}".format(
            mais_barato.event_name,
            formatar_reais(mais_barato.calcular_custo_total())
        ))

    def exibir_relatorio_financeiro_mensal(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado!")
            return

        try:
            mes = int(input("Digite o mês (1-12): ").strip())
            ano = int(input("Digite o ano: ").strip())
        except ValueError:
            print("\n⚠️ Digite apenas números.")
            return

        eventos_filtrados = [
            evento for evento in self.eventos
            if evento.event_month == mes and evento.event_year == ano
        ]

        if not eventos_filtrados:
            print("\nNenhum evento encontrado nesse período.")
            return

        total = sum(evento.calcular_custo_total() for evento in eventos_filtrados)
        media = total / len(eventos_filtrados)
        mais_caro = max(eventos_filtrados, key=lambda evento: evento.calcular_custo_total())

        print("\n══════ RELATÓRIO FINANCEIRO {:02d}/{} ══════".format(mes, ano))
        print("Eventos cadastrados: {}".format(len(eventos_filtrados)))
        print("Total movimentado: {}".format(formatar_reais(total)))
        print("Média de custo: {}".format(formatar_reais(media)))
        print("Evento mais caro do período: {} - {}".format(
            mais_caro.event_name,
            formatar_reais(mais_caro.calcular_custo_total())
        ))

    def gerar_relatorio_txt(self):
        if not self.eventos:
            print("\n⚠️ Não há eventos para gerar o relatório.")
            return

        with open("relatorio_eventos.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("📋 RELATÓRIO GERAL DE EVENTOS\n")
            arquivo.write("=" * 50 + "\n\n")

            for evento in self.eventos:
                arquivo.write("🆔 CÓDIGO: {}\n".format(evento.evento_id))
                arquivo.write("🎉 EVENTO: {}\n".format(evento.event_name))
                arquivo.write("📅 DATA: {} às {}\n".format(evento.event_date, evento.event_time))
                arquivo.write("📍 LOCAL: {}\n".format(evento.event_location))
                arquivo.write("👥 PÚBLICO: {} pessoas\n".format(evento.number_people))
                arquivo.write("🏢 CONTRATANTE: {}\n".format(evento.contratante.enterprise_name))
                arquivo.write("📱 WHATSAPP: {}\n".format(evento.contratante.whats))
                arquivo.write("\n💰 ITENS DE CUSTO:\n")

                for nome, valor in evento.itens_custo:
                    arquivo.write("- {}: {}\n".format(nome, formatar_reais(valor)))

                arquivo.write("💵 TOTAL DO EVENTO: {}\n".format(
                    formatar_reais(evento.calcular_custo_total())
                ))

                arquivo.write("-" * 50 + "\n\n")

            total = sum(evento.calcular_custo_total() for evento in self.eventos)
            media = total / len(self.eventos)
            mais_caro = max(self.eventos, key=lambda evento: evento.calcular_custo_total())
            mais_barato = min(self.eventos, key=lambda evento: evento.calcular_custo_total())

            arquivo.write("📊 RESUMO FINANCEIRO\n")
            arquivo.write("=" * 50 + "\n")
            arquivo.write("Total de eventos: {}\n".format(len(self.eventos)))
            arquivo.write("Total movimentado: {}\n".format(formatar_reais(total)))
            arquivo.write("Média de custo: {}\n".format(formatar_reais(media)))
            arquivo.write("Evento mais caro: {} - {}\n".format(
                mais_caro.event_name,
                formatar_reais(mais_caro.calcular_custo_total())
            ))
            arquivo.write("Evento mais barato: {} - {}\n".format(
                mais_barato.event_name,
                formatar_reais(mais_barato.calcular_custo_total())
            ))

        print("\n✅ Relatório 'relatorio_eventos.txt' gerado com sucesso!")

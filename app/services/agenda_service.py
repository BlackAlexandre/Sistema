from datetime import date

from app.models.contratante import Contratante
from app.models.evento import Evento
from app.repositories.evento_repository import EventoRepository
from app.services.relatorio_service import RelatorioService
from app.utils.formatadores import formatar_reais
from app.utils.validadores import (
    validar_data,
    validar_documento,
    validar_horario,
    validar_whatsapp,
)


class AgendaService:
    """
    Concentra as regras de negócio do sistema.
    """

    def __init__(self):
        self.repository = EventoRepository()
        self.relatorio_service = RelatorioService()
        self.eventos = self.repository.carregar_eventos()
        self.proximo_id = self._calcular_proximo_id()

    def _calcular_proximo_id(self):
        if not self.eventos:
            return 1
        return max(evento.evento_id for evento in self.eventos) + 1

    def _salvar(self):
        self.repository.salvar_eventos(self.eventos)

    def _buscar_por_id(self, evento_id):
        for evento in self.eventos:
            if evento.evento_id == evento_id:
                return evento
        return None

    def _dia_ocupado(self, dia, mes, ano, ignorar_id=None):
        for evento in self.eventos:
            if ignorar_id is not None and evento.evento_id == ignorar_id:
                continue
            if evento.dia == dia and evento.mes == mes and evento.ano == ano:
                return evento
        return None

    def _pedir_id(self):
        try:
            return int(input("\nDigite o código do evento: ").strip())
        except ValueError:
            print("\n⚠️ Digite um código numérico.")
            return None

    def _pedir_data(self, ignorar_id=None):
        while True:
            try:
                dia = int(input("Qual o dia do evento? "))
                mes = int(input("Qual o mês do evento? "))
                ano = int(input("Qual o ano do evento? "))
            except ValueError:
                print("\n⚠️ Digite apenas números inteiros.")
                continue

            if ano < 2026 or ano > 2100:
                print("\n⚠️ Ano inválido. Digite entre 2026 e 2100.")
                continue

            if not validar_data(dia, mes, ano):
                print("\n⚠️ Data inexistente. Digite uma data válida.")
                continue

            conflito = self._dia_ocupado(dia, mes, ano, ignorar_id)
            if conflito:
                print("\n❌ Já existe um evento nessa data: {}.".format(conflito.nome))
                continue

            return dia, mes, ano

    def _pedir_horario(self):
        while True:
            horario = input("Qual o horário do evento? (Ex: 14:30) ").strip()
            if validar_horario(horario):
                return horario
            print("\n⚠️ Horário inválido. Use HH:MM. Exemplo: 14:30.")

    def _pedir_documento(self):
        while True:
            print("\nTipo de documento:")
            print("1. CPF")
            print("2. CNPJ")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                tipo = "CPF"
            elif opcao == "2":
                tipo = "CNPJ"
            else:
                print("\n⚠️ Opção inválida.")
                continue

            numero = input("Digite o {}: ".format(tipo)).strip()
            if validar_documento(tipo, numero):
                return tipo, numero

            print("\n⚠️ Documento inválido.")

    def _pedir_whatsapp(self):
        while True:
            numero = input("Qual o WhatsApp? (11 números): ").strip()
            if validar_whatsapp(numero):
                return numero
            print("\n⚠️ WhatsApp inválido.")

    def _pedir_valor(self):
        while True:
            entrada = input("Valor do item: R$ ").strip().replace(",", ".")
            try:
                valor = float(entrada)
            except ValueError:
                print("\n⚠️ Digite um valor numérico.")
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

            nome = input("Nome do item: ").strip()
            if not nome:
                print("\n⚠️ O nome não pode ficar vazio.")
                continue

            valor = self._pedir_valor()
            itens.append((nome, valor))
            print("\n✅ Item adicionado.")

    def cadastrar_evento(self):
        print("\n── Dados do Evento ──")

        while True:
            nome = input("Qual o nome do evento? ").strip()
            if nome:
                break
            print("\n⚠️ O nome não pode ficar vazio.")

        dia, mes, ano = self._pedir_data()
        data_formatada = "{}-{:02d}-{:02d}".format(ano, mes, dia)
        horario = self._pedir_horario()

        while True:
            local = input("Qual o local do evento? ").strip()
            if local:
                break
            print("\n⚠️ O local não pode ficar vazio.")

        while True:
            try:
                quantidade = int(input("Qual a quantidade de pessoas? "))
            except ValueError:
                print("\n⚠️ Digite um número inteiro.")
                continue

            if quantidade < 1:
                print("\n⚠️ Digite pelo menos 1 pessoa.")
                continue

            break

        print("\n── Dados do Contratante ──")

        while True:
            nome_contratante = input("Qual o nome do contratante? ").strip()
            if nome_contratante:
                break
            print("\n⚠️ O nome não pode ficar vazio.")

        tipo_documento, documento = self._pedir_documento()
        whatsapp = self._pedir_whatsapp()
        itens_custo = self._pedir_itens_custo()

        contratante = Contratante(nome_contratante, tipo_documento, documento, whatsapp)

        evento = Evento(
            self.proximo_id,
            nome,
            dia,
            mes,
            ano,
            data_formatada,
            horario,
            local,
            quantidade,
            contratante,
            itens_custo,
        )

        self.eventos.append(evento)
        self.proximo_id += 1
        self._salvar()

        print("\n✅ Evento cadastrado e salvo!")
        print("🆔 Código: {}".format(evento.evento_id))

    def listar_eventos(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado.")
            return

        print("\n══════ LISTA DE EVENTOS ══════")
        for evento in self.eventos:
            evento.exibir_dados()

    def consultar_evento(self):
        evento_id = self._pedir_id()
        if evento_id is None:
            return

        evento = self._buscar_por_id(evento_id)
        if evento is None:
            print("\n❌ Evento não encontrado.")
            return

        evento.exibir_dados()

    def contar_eventos_no_mes(self):
        try:
            mes = int(input("Digite o mês (1-12): "))
            ano = int(input("Digite o ano: "))
        except ValueError:
            print("\n⚠️ Digite apenas números.")
            return

        eventos_filtrados = [e for e in self.eventos if e.mes == mes and e.ano == ano]
        print("\n📊 Total de eventos em {:02d}/{}: {}".format(mes, ano, len(eventos_filtrados)))

    def editar_evento(self):
        evento_id = self._pedir_id()
        if evento_id is None:
            return

        evento = self._buscar_por_id(evento_id)
        if evento is None:
            print("\n❌ Evento não encontrado.")
            return

        while True:
            evento.exibir_dados()
            print("\nO que deseja editar?")
            print("1. Nome")
            print("2. Data")
            print("3. Horário")
            print("4. Local")
            print("5. Quantidade de pessoas")
            print("0. Concluir")

            opcao = input("Escolha: ").strip()

            if opcao == "1":
                novo = input("Novo nome: ").strip()
                if novo:
                    evento.nome = novo
                    self._salvar()
                    print("\n✅ Nome atualizado.")

            elif opcao == "2":
                dia, mes, ano = self._pedir_data(evento.evento_id)
                evento.dia = dia
                evento.mes = mes
                evento.ano = ano
                evento.data_formatada = "{}-{:02d}-{:02d}".format(ano, mes, dia)
                self._salvar()
                print("\n✅ Data atualizada.")

            elif opcao == "3":
                evento.horario = self._pedir_horario()
                self._salvar()
                print("\n✅ Horário atualizado.")

            elif opcao == "4":
                novo = input("Novo local: ").strip()
                if novo:
                    evento.local = novo
                    self._salvar()
                    print("\n✅ Local atualizado.")

            elif opcao == "5":
                try:
                    novo = int(input("Nova quantidade: "))
                except ValueError:
                    print("\n⚠️ Digite um número inteiro.")
                    continue

                if novo < 1:
                    print("\n⚠️ Digite pelo menos 1 pessoa.")
                    continue

                evento.quantidade_pessoas = novo
                self._salvar()
                print("\n✅ Quantidade atualizada.")

            elif opcao == "0":
                print("\n✅ Edição concluída.")
                return

            else:
                print("\n⚠️ Opção inválida.")

    def remover_evento(self):
        evento_id = self._pedir_id()
        if evento_id is None:
            return

        evento = self._buscar_por_id(evento_id)
        if evento is None:
            print("\n❌ Evento não encontrado.")
            return

        evento.exibir_dados()
        confirmar = input("\nTem certeza que deseja remover? (s/n): ").strip().lower()

        if confirmar == "s":
            self.eventos.remove(evento)
            self._salvar()
            print("\n✅ Evento removido e apagado da base.")
        else:
            print("\nRemoção cancelada.")

    def adicionar_custo(self):
        evento_id = self._pedir_id()
        if evento_id is None:
            return

        evento = self._buscar_por_id(evento_id)
        if evento is None:
            print("\n❌ Evento não encontrado.")
            return

        nome = input("Nome do item de custo: ").strip()
        if not nome:
            print("\n⚠️ O nome não pode ficar vazio.")
            return

        valor = self._pedir_valor()
        evento.adicionar_item_custo(nome, valor)
        self._salvar()

        print("\n✅ Custo adicionado e salvo.")
        print("💵 Novo total: {}".format(formatar_reais(evento.calcular_custo_total())))

    def exibir_resumo_financeiro(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado.")
            return

        total = sum(e.calcular_custo_total() for e in self.eventos)
        media = total / len(self.eventos)
        mais_caro = max(self.eventos, key=lambda e: e.calcular_custo_total())
        mais_barato = min(self.eventos, key=lambda e: e.calcular_custo_total())

        print("\n══════ RESUMO FINANCEIRO ══════")
        print("Eventos cadastrados: {}".format(len(self.eventos)))
        print("Total movimentado: {}".format(formatar_reais(total)))
        print("Média por evento: {}".format(formatar_reais(media)))
        print("Mais caro: {} - {}".format(mais_caro.nome, formatar_reais(mais_caro.calcular_custo_total())))
        print("Mais barato: {} - {}".format(mais_barato.nome, formatar_reais(mais_barato.calcular_custo_total())))

    def exibir_relatorio_financeiro_mensal(self):
        try:
            mes = int(input("Digite o mês (1-12): "))
            ano = int(input("Digite o ano: "))
        except ValueError:
            print("\n⚠️ Digite apenas números.")
            return

        eventos_filtrados = [e for e in self.eventos if e.mes == mes and e.ano == ano]

        if not eventos_filtrados:
            print("\nNenhum evento encontrado nesse período.")
            return

        total = sum(e.calcular_custo_total() for e in eventos_filtrados)
        media = total / len(eventos_filtrados)
        mais_caro = max(eventos_filtrados, key=lambda e: e.calcular_custo_total())

        print("\n══════ RELATÓRIO {:02d}/{} ══════".format(mes, ano))
        print("Eventos: {}".format(len(eventos_filtrados)))
        print("Total: {}".format(formatar_reais(total)))
        print("Média: {}".format(formatar_reais(media)))
        print("Mais caro: {} - {}".format(mais_caro.nome, formatar_reais(mais_caro.calcular_custo_total())))

    def gerar_relatorio_txt(self):
        self.relatorio_service.gerar_relatorio_txt(self.eventos)

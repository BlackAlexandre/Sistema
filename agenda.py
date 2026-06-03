from datetime import date
from pathlib import Path
import pprint

from modelos.contratante import Contratante
from modelos.evento import Evento, formatar_reais
from dados.base_dados import EVENTOS


class Agenda:
    def __init__(self):
        self.eventos = []
        self._carregar_base()
        self.proximo_id = max((e.evento_id for e in self.eventos), default=0) + 1

    def _carregar_base(self):
        for registro in EVENTOS:
            (
                evento_id,
                nome,
                dia,
                mes,
                ano,
                data_formatada,
                horario,
                local,
                quantidade,
                dados_contratante,
                itens_custo,
            ) = registro

            nome_contratante, tipo_documento, documento, whatsapp = dados_contratante

            contratante = Contratante(
                nome_contratante,
                tipo_documento,
                documento,
                whatsapp,
            )

            self.eventos.append(
                Evento(
                    evento_id,
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
            )

    def _salvar_base(self):
        registros = []

        for evento in self.eventos:
            registros.append(
                (
                    evento.evento_id,
                    evento.nome,
                    evento.dia,
                    evento.mes,
                    evento.ano,
                    evento.data_formatada,
                    evento.horario,
                    evento.local,
                    evento.quantidade_pessoas,
                    (
                        evento.contratante.nome,
                        evento.contratante.tipo_documento,
                        evento.contratante.documento,
                        evento.contratante.whatsapp,
                    ),
                    tuple(evento.itens_custo),
                )
            )

        caminho = Path(__file__).resolve().parent / "dados" / "base_dados.py"

        conteudo = (
            "# Banco de dados interno em Python.\n"
            "# Cada evento é armazenado como uma tupla.\n"
            "# O sistema atualiza este arquivo automaticamente.\n\n"
            "EVENTOS = "
            + pprint.pformat(registros, width=120, sort_dicts=False)
            + "\n"
        )

        caminho.write_text(conteudo, encoding="utf-8")

    def _buscar_por_id(self, evento_id):
        for evento in self.eventos:
            if evento.evento_id == evento_id:
                return evento
        return None

    def _pedir_id(self):
        try:
            return int(input("\nDigite o código do evento: "))
        except ValueError:
            print("\n⚠️ Digite apenas números.")
            return None

    def _pedir_valor(self):
        while True:
            entrada = input("Valor: R$ ").strip().replace(",", ".")
            try:
                valor = float(entrada)
            except ValueError:
                print("\n⚠️ Digite um valor válido.")
                continue

            if valor <= 0:
                print("\n⚠️ O valor deve ser maior que zero.")
                continue

            return valor

    def cadastrar_evento(self):
        print("\n── Cadastro de evento ──")
        nome = input("Nome do evento: ").strip()

        while True:
            try:
                dia = int(input("Dia: "))
                mes = int(input("Mês: "))
                ano = int(input("Ano: "))
                date(ano, mes, dia)
                break
            except ValueError:
                print("\n⚠️ Data inválida. Tente novamente.")

        horario = input("Horário (HH:MM): ").strip()
        local = input("Local: ").strip()
        quantidade = int(input("Quantidade de pessoas: "))

        print("\n── Dados do contratante ──")
        nome_contratante = input("Nome do contratante: ").strip()
        tipo_documento = input("Tipo de documento (CPF ou CNPJ): ").strip().upper()
        documento = input("Número do documento: ").strip()
        whatsapp = input("WhatsApp: ").strip()

        contratante = Contratante(
            nome_contratante,
            tipo_documento,
            documento,
            whatsapp,
        )

        evento = Evento(
            self.proximo_id,
            nome,
            dia,
            mes,
            ano,
            "{}-{:02d}-{:02d}".format(ano, mes, dia),
            horario,
            local,
            quantidade,
            contratante,
            [],
        )

        while True:
            resposta = input("\nAdicionar custo? (s/n): ").strip().lower()
            if resposta == "n":
                break

            nome_item = input("Nome do custo: ").strip()
            valor = self._pedir_valor()
            evento.adicionar_item_custo(nome_item, valor)

        self.eventos.append(evento)
        self.proximo_id += 1
        self._salvar_base()

        print("\n✅ Evento cadastrado e salvo!")
        print("🆔 Código: {}".format(evento.evento_id))

    def listar_eventos(self):
        for evento in self.eventos:
            evento.exibir_dados()

    def consultar_evento(self):
        evento_id = self._pedir_id()
        evento = self._buscar_por_id(evento_id)

        if evento:
            evento.exibir_dados()
        else:
            print("\n❌ Evento não encontrado.")

    def editar_evento(self):
        evento_id = self._pedir_id()
        evento = self._buscar_por_id(evento_id)

        if not evento:
            print("\n❌ Evento não encontrado.")
            return

        print("1. Nome")
        print("2. Local")
        print("3. Quantidade de pessoas")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            evento.nome = input("Novo nome: ").strip()
        elif opcao == "2":
            evento.local = input("Novo local: ").strip()
        elif opcao == "3":
            evento.quantidade_pessoas = int(input("Nova quantidade: "))
        else:
            print("\n⚠️ Opção inválida.")
            return

        self._salvar_base()
        print("\n✅ Evento atualizado e salvo.")

    def remover_evento(self):
        evento_id = self._pedir_id()
        evento = self._buscar_por_id(evento_id)

        if not evento:
            print("\n❌ Evento não encontrado.")
            return

        self.eventos.remove(evento)
        self._salvar_base()

        print("\n✅ Evento removido da base.")

    def adicionar_custo(self):
        evento_id = self._pedir_id()
        evento = self._buscar_por_id(evento_id)

        if not evento:
            print("\n❌ Evento não encontrado.")
            return

        nome_item = input("Nome do custo: ").strip()
        valor = self._pedir_valor()

        evento.adicionar_item_custo(nome_item, valor)
        self._salvar_base()

        print("\n✅ Custo adicionado e salvo.")

    def resumo_financeiro(self):
        total = sum(evento.calcular_total() for evento in self.eventos)
        media = total / len(self.eventos)
        mais_caro = max(self.eventos, key=lambda e: e.calcular_total())

        print("\n══════ RESUMO FINANCEIRO ══════")
        print("Eventos cadastrados: {}".format(len(self.eventos)))
        print("Total movimentado: {}".format(formatar_reais(total)))
        print("Média por evento: {}".format(formatar_reais(media)))
        print("Evento mais caro: {}".format(mais_caro.nome))

    def relatorio_mensal(self):
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))

        filtrados = [
            evento for evento in self.eventos
            if evento.mes == mes and evento.ano == ano
        ]

        if not filtrados:
            print("\nNenhum evento encontrado.")
            return

        total = sum(evento.calcular_total() for evento in filtrados)

        print("\n══════ RELATÓRIO MENSAL ══════")
        print("Eventos: {}".format(len(filtrados)))
        print("Total: {}".format(formatar_reais(total)))

    def gerar_relatorio_txt(self):
        caminho = Path(__file__).resolve().parent / "relatorios" / "relatorio_eventos.txt"

        with open(caminho, "w", encoding="utf-8") as arquivo:
            for evento in self.eventos:
                arquivo.write("EVENTO: {}\n".format(evento.nome))
                arquivo.write("CÓDIGO: {}\n".format(evento.evento_id))
                arquivo.write("DATA: {} às {}\n".format(evento.data_formatada, evento.horario))
                arquivo.write("LOCAL: {}\n".format(evento.local))
                arquivo.write("CONTRATANTE: {}\n".format(evento.contratante.nome))

                arquivo.write("CUSTOS:\n")
                for nome, valor in evento.itens_custo:
                    arquivo.write("- {}: {}\n".format(nome, formatar_reais(valor)))

                arquivo.write("TOTAL: {}\n".format(formatar_reais(evento.calcular_total())))
                arquivo.write("-" * 40 + "\n")

        print("\n✅ Relatório criado em relatorios/relatorio_eventos.txt")

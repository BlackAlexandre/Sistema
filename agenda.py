from contratante import Contratante
from evento import Evento


class Agenda:
    def __init__(self):
        self.contratantes = []
        self.eventos = []

    # ── Contratante ──────────────────────────────────────────────────────────

    def cadastrar_contratante(self):
        enterprise_name = input("Qual o nome do contratante? (Empresa/Pessoa responsável): ")
        cnpj_cpf = input("Digite o CPF/CNPJ(Somente números): ")
        whats = input("Qual o WhatsApp de contato? (Apenas números): ")

        contratante = Contratante(enterprise_name, cnpj_cpf, whats)
        self.contratantes.append(contratante)

        print("\nContratante cadastrado com sucesso!")

    def listar_contratantes(self):
        if len(self.contratantes) == 0:
            print("\nNenhum contratante cadastrado.")
        else:
            print("\n──── CONTRATANTES ────")
            for contratante in self.contratantes:
                contratante.exibir_dados()

    # ── Evento ───────────────────────────────────────────────────────────────

    def cadastrar_evento(self):
        event_name = input("Qual o nome do evento? ")

        try:
            event_day   = int(input("Qual o dia do evento? "))
            event_month = int(input("Qual o mês do evento? "))
            event_year  = int(input("Qual o ano do evento? "))
            number_people = int(input("Qual a quantidade de pessoas no evento? "))
        except ValueError:
            print("\nDevem ser digitados apenas números.")
            return

        event_date     = "{}-{:02d}-{:02d}".format(event_year, event_month, event_day)
        event_time     = input("Qual o horário do evento? ")
        event_location = input("Qual o local do evento? ")

        evento = Evento(event_name, event_day, event_month, event_year,
                        event_date, event_time, event_location, number_people)
        self.eventos.append(evento)

        print("\nEvento cadastrado com sucesso!")

    def listar_eventos(self):
        if len(self.eventos) == 0:
            print("\nNenhum evento cadastrado.")
        else:
            print("\n──── LISTA DE EVENTOS ────")
            for evento in self.eventos:
                evento.exibir_dados()

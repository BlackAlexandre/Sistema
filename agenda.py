from contratante import Contratante
from evento import Evento


class Agenda:
    def __init__(self):
        self.eventos = []

    # ── Validações ────────────────────────────────────────────────────────────

    def _dia_ocupado(self, day, month, year):
        """Retorna o evento já cadastrado nessa data, ou None."""
        for evento in self.eventos:
            if evento.event_day == day and evento.event_month == month and evento.event_year == year:
                return evento
        return None

    def _pedir_data(self):
        """Solicita dia/mês/ano e verifica se a data já está ocupada. Repete até obter uma data livre."""
        while True:
            try:
                event_day   = int(input("Qual o dia do evento? "))
                event_month = int(input("Qual o mês do evento? "))
                event_year  = int(input("Qual o ano do evento? "))
            except ValueError:
                print("\n⚠️  Devem ser digitados apenas números para a data.")
                continue

            conflito = self._dia_ocupado(event_day, event_month, event_year)
            if conflito:
                print("\n❌ Já existe um evento cadastrado nessa data: '{}'.".format(conflito.event_name))
                print("   Por favor, escolha outro dia.\n")
            else:
                return event_day, event_month, event_year

    def _pedir_documento(self):
        """Pergunta CPF ou CNPJ e valida os dígitos."""
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
                print("\n⚠️  Opção inválida. Escolha 1 para CPF ou 2 para CNPJ.")
                continue

            while True:
                numero = input("Digite o {} (apenas números): ".format(tipo)).strip()

                if not numero.isdigit():
                    print("\n⚠️  {} deve conter apenas números, sem pontos ou traços.".format(tipo))
                    continue

                if len(numero) != digitos:
                    print("\n⚠️  {} inválido: deve ter exatamente {} dígitos. Você digitou {}.".format(
                        tipo, digitos, len(numero)))
                    continue

                return tipo, numero

    def _pedir_whatsapp(self):
        """Solicita WhatsApp e valida 11 dígitos numéricos."""
        while True:
            whats = input("Qual o WhatsApp de contato? (Apenas números, 11 dígitos): ").strip()

            if not whats.isdigit():
                print("\n⚠️  WhatsApp deve conter apenas números, sem espaços ou símbolos.")
                continue

            if len(whats) != 11:
                print("\n⚠️  WhatsApp inválido: deve ter exatamente 11 dígitos. Você digitou {}.".format(len(whats)))
                continue

            return whats

    # ── Cadastro ──────────────────────────────────────────────────────────────

    def cadastrar_evento(self):
        print("\n── Dados do Evento ──")
        event_name = input("Qual o nome do evento? ")

        event_day, event_month, event_year = self._pedir_data()
        event_date = "{}-{:02d}-{:02d}".format(event_year, event_month, event_day)

        event_time     = input("Qual o horário do evento? ")
        event_location = input("Qual o local do evento? ")

        try:
            number_people = int(input("Qual a quantidade de pessoas no evento? "))
        except ValueError:
            print("\n⚠️  Quantidade de pessoas deve ser um número.")
            return

        print("\n── Dados do Contratante ──")
        enterprise_name = input("Qual o nome do contratante? (Empresa/Pessoa responsável): ")

        tipo_documento, cnpj_cpf = self._pedir_documento()
        whats = self._pedir_whatsapp()

        contratante = Contratante(enterprise_name, tipo_documento, cnpj_cpf, whats)
        evento = Evento(event_name, event_day, event_month, event_year,
                        event_date, event_time, event_location, number_people,
                        contratante)
        self.eventos.append(evento)

        print("\n✅ Evento cadastrado com sucesso!")

    # ── Listagem ──────────────────────────────────────────────────────────────

    def listar_eventos(self):
        if len(self.eventos) == 0:
            print("\nNenhum evento cadastrado.")
        else:
            print("\n══════ LISTA DE EVENTOS ══════")
            for evento in self.eventos:
                evento.exibir_dados()

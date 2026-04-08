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
        
        while True:
            try:
                event_day = int(input("Qual o dia do evento? "))
            except ValueError:
                print("\n⚠️  Digite apenas números.")
                continue
            if event_day < 1 or event_day > 31:
                print("\n⚠️  Dia inválido. Digite entre 1 e 31.")
                continue
            break

        while True:
            try:
                event_month = int(input("Qual o mês do evento? "))
            except ValueError:
                print("\n⚠️  Digite apenas números.")
                continue
            if event_month < 1 or event_month > 12:
                print("\n⚠️  Mês inválido. Digite entre 1 e 12.")
                continue
            break

        while True:
            try:
                event_year = int(input("Qual o ano do evento? "))
            except ValueError:
                print("\n⚠️  Digite apenas números.")
                continue
            if event_year < 2026 or event_year > 2100:
                print("\n⚠️  Ano inválido. Digite entre 2026 e 2100.")
                continue
            break

        conflito = self._dia_ocupado(event_day, event_month, event_year)
        if conflito:
            print("\n❌ Já existe um evento nessa data: '{}'.".format(conflito.event_name))
            print("   Escolha outro dia.\n")
            return self._pedir_data()

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
        
    def _pedir_horario(self):
        while True:
            horario = input("Qual o horário do evento? (Ex: 14:30) ").strip()

            if len(horario) != 5:
                print("\n⚠️  Digite no formato HH:MM, exemplo: 14:30")
                continue

            if ":" not in horario:
                print("\n⚠️  Use dois pontos no meio, exemplo: 14:30")
                continue

            partes = horario.split(":")
            hora   = partes[0]
            minuto = partes[1]

            if not hora.isdigit() or not minuto.isdigit():
                print("\n⚠️  Use apenas números, exemplo: 14:30")
                continue

            if int(hora) > 23:
                print("\n⚠️  Hora inválida. Digite entre 00 e 23.")
                continue

            if int(minuto) > 59:
                print("\n⚠️  Minuto inválido. Digite entre 00 e 59.")
                continue

            return horario

    # ── Cadastro ──────────────────────────────────────────────────────────────

    def cadastrar_evento(self):
        print("\n── Dados do Evento ──")
        while True:
            event_name = input("Qual o nome do evento? ").strip()
            if event_name == "":
                print("\n⚠️  O nome do evento não pode ser vazio.")
                continue
            break

        event_day, event_month, event_year = self._pedir_data()
        event_date = "{}-{:02d}-{:02d}".format(event_year, event_month, event_day)

        event_time = self._pedir_horario()  
        
        while True:
            event_location = input("Qual o local do evento? ").strip()
            if event_location == "":
                print("\n⚠️  O local do evento não pode ser vazio.")
                continue
            break
        
        while True:
            try:
                number_people = int(input("Qual a quantidade de pessoas no evento? "))
            except ValueError:
                print("\n⚠️  Quantidade de pessoas deve ser um número inteiro. Ex: 100")
                continue
            if number_people < 1:
                print("\n⚠️  Quantidade inválida. Digite pelo menos 1 pessoa.")
                continue
            break

        print("\n── Dados do Contratante ──")
        
        while True:
            enterprise_name = input("Qual o nome do contratante? (Empresa/Pessoa responsável): ").strip()
            if enterprise_name == "":
                print("\n⚠️  O nome do contratante não pode ser vazio.")
                continue
            break

        tipo_documento, cnpj_cpf = self._pedir_documento()
        whats = self._pedir_whatsapp()

        contratante = Contratante(enterprise_name, tipo_documento, cnpj_cpf, whats)
        evento = Evento(event_name, event_day, event_month, event_year, event_date, event_time, event_location, number_people, contratante)
        self.eventos.append(evento)

        print("\n✅ Evento cadastrado com sucesso!")
        
    def contar_eventos_no_mes(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado!")
            return
        
        while True:
            try:
                mes_busca = int(input("Digite o mês para consulta (1-12): ").strip())
            except ValueError:
                print("\n⚠️ Digite apenas números.")
                continue
            if mes_busca < 1 or mes_busca > 12:
                print("\n⚠️ Mês inválido. Digite entre 1 e 12.")
                continue
            break

        while True:
            try:
                ano_busca = int(input("Digite o ano (Ex: 2026): ").strip())
            except ValueError:
                print("\n⚠️ Digite apenas números.")
                continue
            if ano_busca < 2026 or ano_busca > 2100:
                print("\n⚠️ Ano inválido. Digite entre 2026 e 2100.")
                continue
            break
                
        contagem = 0
        
        for evento in self.eventos:
            if evento.event_month == mes_busca and evento.event_year == ano_busca:
                contagem += 1
                
        print(f"\n📊 Total de eventos em {mes_busca:02d}/{ano_busca}: {contagem}")



    # ── Listagem ──────────────────────────────────────────────────────────────

    def listar_eventos(self): 
        if len(self.eventos) == 0:
            print("\nNenhum evento cadastrado.")
        else:
            print("\n══════ LISTA DE EVENTOS ══════")
            for evento in self.eventos:
                evento.exibir_dados()

    def _buscar_evento(self, nome):
        for evento in self.eventos:
            if evento.event_name.lower() == nome.lower():
                return evento
        return None

    def remover_evento(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado!")
            return

        nome = input("\nDigite o nome do evento que deseja remover: ").strip()

        evento = self._buscar_evento(nome)

        if evento is None:
            print("\n❌ Evento '{}' não encontrado.".format(nome))
            return

        evento.exibir_dados()
        confirmacao = input("\nTem certeza que deseja remover? (s/n): ").strip().lower()

        if confirmacao == "s":
            self.eventos.remove(evento)
            print("\n✅ Evento '{}' removido com sucesso!".format(nome))
        else:
            print("\nRemoção cancelada.")

    def editar_evento(self):
        if not self.eventos:
            print("\nNenhum evento cadastrado!")
            return

        nome = input("\nDigite o nome do evento que deseja editar: ").strip()

        evento = self._buscar_evento(nome)

        if evento is None:
            print("\n❌ Evento '{}' não encontrado.".format(nome))
            return

        # loop do menu de edição — fica aqui até o usuário escolher 0
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
                while True:
                    novo = input("Novo nome: ").strip()
                    if novo == "":
                        print("\n⚠️  Nome não pode ser vazio.")
                        continue
                    break
                evento.event_name = novo
                print("\n✅ Nome atualizado!")

            elif opcao == "2":
                event_day, event_month, event_year = self._pedir_data()
                evento.event_day   = event_day
                evento.event_month = event_month
                evento.event_year  = event_year
                evento.event_date  = "{}-{:02d}-{:02d}".format(event_year, event_month, event_day)
                print("\n✅ Data atualizada!")

            elif opcao == "3":
                evento.event_time = self._pedir_horario()
                print("\n✅ Horário atualizado!")

            elif opcao == "4":
                while True:
                    novo = input("Novo local: ").strip()
                    if novo == "":
                        print("\n⚠️  Local não pode ser vazio.")
                        continue
                    break
                evento.event_location = novo
                print("\n✅ Local atualizado!")

            elif opcao == "5":
                while True:
                    try:
                        novo = int(input("Nova quantidade de pessoas: "))
                    except ValueError:
                        print("\n⚠️  Digite um número inteiro.")
                        continue
                    if novo < 1:
                        print("\n⚠️  Digite pelo menos 1 pessoa.")
                        continue
                    break
                evento.number_people = novo
                print("\n✅ Quantidade atualizada!")

            elif opcao == "0":
                print("\n✅ Edição concluída!")
                break

            else:
                print("\n⚠️  Opção inválida.")
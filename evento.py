def formatar_reais(valor):
    """
    Recebe um número e devolve o valor formatado em reais.
    Exemplo: 8500 vira R$ 8.500,00
    """
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class Evento:
    def __init__(
        self,
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
        itens_custo=None
    ):
        self.evento_id = evento_id
        self.event_name = event_name
        self.event_day = event_day
        self.event_month = event_month
        self.event_year = event_year
        self.event_date = event_date
        self.event_time = event_time
        self.event_location = event_location
        self.number_people = number_people
        self.contratante = contratante

        # Caso nenhum custo seja informado, o evento começa com uma lista vazia.
        self.itens_custo = itens_custo if itens_custo is not None else []

    def adicionar_item_custo(self, nome, valor):
        """
        Adiciona um novo item de custo ao evento.
        Cada custo é armazenado como uma tupla: (nome, valor).
        """
        self.itens_custo.append((nome, valor))

    def calcular_custo_total(self):
        """
        Soma automaticamente todos os custos cadastrados no evento.
        """
        return sum(valor for nome, valor in self.itens_custo)

    def exibir_dados(self):
        print("\n──────────────────────────────")
        print("🆔 Código: {}".format(self.evento_id))
        print("🎉 Evento: {}".format(self.event_name))
        print("📅 Data: {}".format(self.event_date))
        print("⌚ Horário: {}".format(self.event_time))
        print("📍 Local: {}".format(self.event_location))
        print("👥 Pessoas: {}".format(self.number_people))
        print("")

        self.contratante.exibir_dados()

        print("\n💰 Itens de custo:")

        if len(self.itens_custo) == 0:
            print("- Nenhum custo cadastrado.")
        else:
            for nome, valor in self.itens_custo:
                print("- {}: {}".format(nome, formatar_reais(valor)))

        print("\n💵 Custo total: {}".format(
            formatar_reais(self.calcular_custo_total())
        ))

        print("──────────────────────────────")
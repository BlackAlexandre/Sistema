from app.utils.formatadores import formatar_reais


class Evento:
    """
    Representa um evento e seus itens de custo.
    """

    def __init__(
        self,
        evento_id,
        nome,
        dia,
        mes,
        ano,
        data_formatada,
        horario,
        local,
        quantidade_pessoas,
        contratante,
        itens_custo=None,
    ):
        self.evento_id = evento_id
        self.nome = nome
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.data_formatada = data_formatada
        self.horario = horario
        self.local = local
        self.quantidade_pessoas = quantidade_pessoas
        self.contratante = contratante
        self.itens_custo = list(itens_custo) if itens_custo is not None else []

    def adicionar_item_custo(self, nome, valor):
        self.itens_custo.append((nome, valor))

    def calcular_custo_total(self):
        return sum(valor for nome, valor in self.itens_custo)

    def exibir_dados(self):
        print("\n──────────────────────────────")
        print("🆔 Código: {}".format(self.evento_id))
        print("🎉 Evento: {}".format(self.nome))
        print("📅 Data: {}".format(self.data_formatada))
        print("⌚ Horário: {}".format(self.horario))
        print("📍 Local: {}".format(self.local))
        print("👥 Pessoas: {}".format(self.quantidade_pessoas))
        print("")

        self.contratante.exibir_dados()

        print("\n💰 Itens de custo:")
        if not self.itens_custo:
            print("- Nenhum custo cadastrado.")
        else:
            for nome, valor in self.itens_custo:
                print("- {}: {}".format(nome, formatar_reais(valor)))

        print("\n💵 Custo total: {}".format(formatar_reais(self.calcular_custo_total())))
        print("──────────────────────────────")

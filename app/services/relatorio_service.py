from pathlib import Path

from app.utils.formatadores import formatar_reais


class RelatorioService:
    """
    Responsável por criar relatórios financeiros.
    """

    def __init__(self):
        self.caminho_saida = Path(__file__).resolve().parents[2] / "output" / "relatorio_eventos.txt"

    def gerar_relatorio_txt(self, eventos):
        if not eventos:
            print("\n⚠️ Não há eventos para gerar o relatório.")
            return

        with open(self.caminho_saida, "w", encoding="utf-8") as arquivo:
            arquivo.write("📋 RELATÓRIO GERAL DE EVENTOS\n")
            arquivo.write("=" * 60 + "\n\n")

            for evento in eventos:
                arquivo.write("🆔 CÓDIGO: {}\n".format(evento.evento_id))
                arquivo.write("🎉 EVENTO: {}\n".format(evento.nome))
                arquivo.write("📅 DATA: {} às {}\n".format(evento.data_formatada, evento.horario))
                arquivo.write("📍 LOCAL: {}\n".format(evento.local))
                arquivo.write("👥 PÚBLICO: {} pessoas\n".format(evento.quantidade_pessoas))
                arquivo.write("🏢 CONTRATANTE: {}\n".format(evento.contratante.nome))
                arquivo.write("\n💰 ITENS DE CUSTO:\n")

                for nome, valor in evento.itens_custo:
                    arquivo.write("- {}: {}\n".format(nome, formatar_reais(valor)))

                arquivo.write("💵 TOTAL DO EVENTO: {}\n".format(
                    formatar_reais(evento.calcular_custo_total())
                ))
                arquivo.write("-" * 60 + "\n\n")

            total = sum(evento.calcular_custo_total() for evento in eventos)
            media = total / len(eventos)
            mais_caro = max(eventos, key=lambda evento: evento.calcular_custo_total())
            mais_barato = min(eventos, key=lambda evento: evento.calcular_custo_total())

            arquivo.write("📊 RESUMO FINANCEIRO\n")
            arquivo.write("=" * 60 + "\n")
            arquivo.write("Total de eventos: {}\n".format(len(eventos)))
            arquivo.write("Total movimentado: {}\n".format(formatar_reais(total)))
            arquivo.write("Média de custo: {}\n".format(formatar_reais(media)))
            arquivo.write("Evento mais caro: {} - {}\n".format(
                mais_caro.nome,
                formatar_reais(mais_caro.calcular_custo_total())
            ))
            arquivo.write("Evento mais barato: {} - {}\n".format(
                mais_barato.nome,
                formatar_reais(mais_barato.calcular_custo_total())
            ))

        print("\n✅ Relatório criado em output/relatorio_eventos.txt")

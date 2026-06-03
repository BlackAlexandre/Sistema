from pathlib import Path
import pprint

from app.models.contratante import Contratante
from app.models.evento import Evento
from data.eventos import EVENTOS_INICIAIS


class EventoRepository:
    """
    Responsável por ler e gravar a base de dados em Python.
    """

    def __init__(self):
        self.caminho_base = Path(__file__).resolve().parents[2] / "data" / "eventos.py"

    def carregar_eventos(self):
        eventos = []

        for registro in EVENTOS_INICIAIS:
            (
                evento_id,
                nome,
                dia,
                mes,
                ano,
                data_formatada,
                horario,
                local,
                quantidade_pessoas,
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

            evento = Evento(
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
                itens_custo,
            )

            eventos.append(evento)

        return eventos

    def salvar_eventos(self, eventos):
        registros = []

        for evento in eventos:
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

        conteudo = (
            "# Banco de dados interno em Python.\n"
            "# Cada registro principal é uma tupla.\n"
            "# Este arquivo é atualizado automaticamente pelo sistema.\n\n"
            "EVENTOS_INICIAIS = "
            + pprint.pformat(registros, width=120, sort_dicts=False)
            + "\n"
        )

        self.caminho_base.write_text(conteudo, encoding="utf-8")

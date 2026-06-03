from app.repositories.evento_repository import EventoRepository
from app.services.agenda_service import AgendaService


def executar_teste():
    repository = EventoRepository()
    eventos = repository.carregar_eventos()

    assert len(eventos) >= 100
    assert eventos[0].calcular_custo_total() > 0

    agenda = AgendaService()
    assert agenda.proximo_id > 100

    print("Teste concluído com sucesso.")


if __name__ == "__main__":
    executar_teste()

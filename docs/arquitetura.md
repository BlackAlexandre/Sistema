# Arquitetura do projeto

## Fluxo principal

```text
main.py
   ↓
app/cli/menu.py
   ↓
app/services/agenda_service.py
   ↓
app/repositories/evento_repository.py
   ↓
data/eventos.py
```

## Separação de responsabilidades

- `models`: representa as entidades.
- `repositories`: persiste e recupera dados.
- `services`: executa regras de negócio.
- `utils`: reúne funções auxiliares.
- `cli`: recebe entradas do usuário.

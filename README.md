# Sistema de Gestão de Eventos

Projeto acadêmico em Python com estrutura modular, banco interno em Python e cálculos financeiros.

## Como executar

Abra o terminal dentro da pasta do projeto e rode:

```bash
python main.py
```

## Estrutura

```text
sistema_gestao_eventos_profissional/
├── main.py
├── app/
│   ├── cli/
│   │   └── menu.py
│   ├── models/
│   │   ├── contratante.py
│   │   └── evento.py
│   ├── repositories/
│   │   └── evento_repository.py
│   ├── services/
│   │   ├── agenda_service.py
│   │   └── relatorio_service.py
│   └── utils/
│       ├── formatadores.py
│       └── validadores.py
├── data/
│   └── eventos.py
├── output/
│   └── relatorio_eventos.txt
├── tests/
│   └── test_smoke.py
├── docs/
│   └── arquitetura.md
└── README.md
```

## Responsabilidade de cada pasta

- `app/models`: classes que representam os dados.
- `app/repositories`: leitura e gravação do banco interno.
- `app/services`: regras de negócio e relatórios.
- `app/utils`: funções auxiliares e validações.
- `app/cli`: menu do terminal.
- `data`: banco de dados em Python com lista de tuplas.
- `output`: relatórios gerados.
- `tests`: testes básicos.
- `docs`: explicação da arquitetura.

## Persistência

O arquivo `data/eventos.py` é atualizado automaticamente quando um evento é cadastrado, editado ou removido.

## Estruturas de dados

- Lista: conjunto de eventos.
- Tupla: registro de cada evento.
- Tupla: dados do contratante.
- Tupla: item financeiro no formato `(nome, valor)`.

## Relações

```text
Contratante 1 ───── N Evento 1 ───── N Item de custo
```

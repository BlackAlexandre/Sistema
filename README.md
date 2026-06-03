# Sistema de Gestão de Eventos

Projeto em Python para controlar eventos, contratantes e valores financeiros.

## Estrutura simples e organizada

```text
projeto_eventos_estruturado_simples/
├── main.py
├── agenda.py
├── modelos/
│   ├── contratante.py
│   └── evento.py
├── dados/
│   └── base_dados.py
├── relatorios/
└── README.md
```

## Pastas

- `modelos`: classes que representam evento e contratante.
- `dados`: banco interno em Python com 100 eventos.
- `relatorios`: local onde o relatório TXT será criado.

## Como executar

```bash
python main.py
```

## Persistência

Ao cadastrar, editar, remover ou adicionar custo, o sistema atualiza automaticamente:

```text
dados/base_dados.py
```

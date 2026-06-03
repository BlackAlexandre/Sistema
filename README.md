# Sistema de Gestão de Eventos — Projeto 4

Aplicação de linha de comando desenvolvida em Python para gerenciar eventos, contratantes e custos financeiros.

## Problema resolvido

O sistema ajuda a controlar eventos e os serviços que compõem cada orçamento, como buffet, banda, aluguel do espaço, DJ, fotógrafo, segurança e decoração.

## Estrutura do projeto

- `main.py`: menu principal.
- `agenda.py`: regras de negócio, validações, consultas e relatórios.
- `evento.py`: classe `Evento` e formatação de valores em reais.
- `contratante.py`: classe `Contratante`.
- `base_dados.py`: base interna com 100 registros em Python.

## Estruturas de dados utilizadas

A base de dados foi implementada com uma **lista de tuplas**.

- A lista reúne vários eventos.
- Cada tupla principal representa um evento.
- Os dados do contratante também ficam agrupados em uma tupla.
- Cada item de custo é uma tupla no formato `(nome, valor)`.

## Relações

```text
Contratante 1 ───── N Evento 1 ───── N Item de custo
```

Cada evento possui um contratante e pode possuir vários itens de custo.

## Funcionalidades

1. Cadastrar evento.
2. Listar eventos.
3. Consultar pelo código.
4. Contar eventos por mês.
5. Editar evento.
6. Remover evento.
7. Adicionar custo.
8. Exibir resumo financeiro geral.
9. Exibir relatório financeiro mensal.
10. Gerar relatório completo em TXT.

## Validações

- Campos obrigatórios.
- CPF com 11 dígitos.
- CNPJ com 14 dígitos.
- WhatsApp com 11 dígitos.
- Horário válido.
- Data existente.
- Bloqueio de eventos na mesma data.
- Quantidade de pessoas maior que zero.
- Valor monetário maior que zero.

## Como executar

Abra o terminal dentro da pasta do projeto e use:

```bash
python main.py
```

## Base populada

O arquivo `base_dados.py` contém 100 eventos de exemplo. Ao iniciar o sistema, esses eventos são carregados automaticamente.

## Evolução em relação ao projeto anterior

A versão anterior possuía cadastro, listagem, edição, remoção e relatório simples. A nova versão adiciona códigos identificadores, 100 registros iniciais, itens de custo, valores em reais, cálculos automáticos e relatórios financeiros.

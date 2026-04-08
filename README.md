# 📅 Sistema de Gestão de Eventos e Contratantes

Aplicação em Python (linha de comando) para centralizar o cadastro de eventos e dos responsáveis contratantes, com validações de negócio, listagem, edição, remoção, relatório em texto e contagem de eventos por período.

---

## Regras de Negócio e Validações Técnicas

As regras abaixo refletem o comportamento implementado em `agenda.py` e nos fluxos de cadastro/edição.

### Datas

| Regra | Descrição |
|--------|-----------|
|Conflito no mesmo dia | Não é permitido cadastrar dois eventos na **mesma combinação dia + mês + ano**. Se já existir um evento na data informada, o sistema informa o nome do evento em conflito e solicita outra data. |
| **Limite de ano** | O ano do evento deve estar entre **2026** e **2100** (inclusive). |
| **Componentes da data** | Dia entre **1** e **31**; mês entre **1** e **12**; apenas entrada numérica (valores inválidos são rejeitados com mensagem). |

**Importante:** A consulta de *quantidade de eventos no mês* também exige mês **1–12** e ano **2026–2100**, alinhado ao cadastro.

### Horários

| Regra | Descrição |
|--------|-----------|
| **Formato** | Obrigatório **HH:MM** (cinco caracteres), com **dois pontos** entre hora e minutos (ex.: `14:30`). |
| **Hora** | Apenas dígitos; valor entre **00** e **23**. |
| **Minuto** | Apenas dígitos; valor entre **00** e **59**. |

Entradas como `9:5` ou sem `:` são rejeitadas: o sistema exige o padrão completo, como nos exemplos de mensagem do programa.

### Documentos (CPF e CNPJ)

| Tipo | Dígitos | Conteúdo permitido |
|------|---------|---------------------|
| **CPF** | Exatamente **11** | Somente **números** (sem pontos, traços ou máscara). |
| **CNPJ** | Exatamente **14** | Somente **números** (sem formatação). |

O usuário escolhe **1** para CPF ou **2** para CNPJ antes de digitar o número.

### Contato (WhatsApp)

| Regra | Descrição |
|--------|-----------|
| **Quantidade** | Exatamente **11 dígitos** (padrão comum para DDD + número no Brasil). |
| **Conteúdo** | Apenas **números**; espaços e símbolos não são aceitos. |

---

## Manual do Usuário — Menu Principal (`main.py`)

Ao executar o programa, o menu principal oferece as opções abaixo.

| Opção | Função |
|-------|--------|
| **1** | **Cadastrar evento** — Coleta dados do evento (nome, data, horário, local, público) e do contratante (nome, documento CPF/CNPJ, WhatsApp) e grava na agenda. |
| **2** | **Listar eventos** — Exibe todos os eventos cadastrados com detalhes do contratante. |
| **3** | **Quantidade total de eventos no mês** — Solicita o **mês** (1–12) e o **ano** (2026–2100) e exibe quantos eventos existem naquele mês/ano. Se não houver eventos cadastrados, informa antes de pedir mês/ano. |
| **4** | **Remover evento** — Busca pelo nome do evento, mostra os dados, pede confirmação (`s`/`n`) e remove se confirmado. |
| **5** | **Editar evento** — Localiza o evento pelo nome e permite alterar nome, data, horário, local ou quantidade de pessoas (submenu até concluir com **0**). |
| **6** | **Gerar relatório (txt)** — Gera o arquivo `relatorio_eventos.txt` na pasta do projeto com o resumo dos eventos. |
| **0** | **Sair** — Encerra o sistema. |

### Destaque: opção 3 — Quantidade total de eventos no mês

Esta função permite uma visão rápida da **carga mensal**: após informar mês e ano válidos, o sistema conta quantos eventos possuem `event_month` e `event_year` correspondentes.

Exemplo ilustrativo de saída:

```text
Digite o mês para consulta (1-12): 4
Digite o ano (Ex: 2026): 2026

📊 Total de eventos em 04/2026: 3
```

**Atenção:** Se não existir nenhum evento na agenda, a mensagem exibida é `Nenhum evento cadastrado!` e não há pedido de mês/ano.

---

## Estrutura de Dados e POO

O modelo segue composição clássica: a **agenda** agrega **eventos**, e cada **evento** referencia um **contratante**.

- **`Agenda`** (`agenda.py`): mantém a lista `eventos` e concentra as operações (cadastro com validações, listagem, busca por nome, remoção, edição, contagem mensal, exportação do relatório). É o *facade* do domínio em relação ao menu.
- **`Evento`** (`evento.py`): representa um evento com nome, componentes de data (`event_day`, `event_month`, `event_year`), string `event_date` (formato `AAAA-MM-DD`), horário, local, número de pessoas e uma referência ao objeto **`Contratante`** (`self.contratante`). O método `exibir_dados()` imprime o evento e delega a exibição do contratante.
- **`Contratante`** (`contratante.py`): encapsula nome (`enterprise_name`), tipo de documento (`"CPF"` ou `"CNPJ"`), número (`cnpj_cpf`) e WhatsApp (`whats`).

Em termos de relação: **Agenda 1 — N Evento**, e **Evento N — 1 Contratante** (cada evento tem um contratante; o mesmo conjunto de dados de contratante pode ser reutilizado apenas se cadastrado em outro evento como novo objeto, conforme o fluxo atual).

---

## Como executar

Requisito: **Python 3** instalado.

```bash
python main.py
```

---

## Arquivos principais

| Arquivo | Papel |
|---------|--------|
| `main.py` | Ponto de entrada; exibe o menu e delega para `Agenda`. |
| `agenda.py` | Lógica de negócio, validações e persistência em memória (lista de eventos). |
| `evento.py` | Classe `Evento` e exibição consolidada. |
| `contratante.py` | Classe `Contratante` e exibição dos dados do responsável. |

---

## Relatório em texto

Ao usar a opção **6**, é criado (ou sobrescrito) o arquivo **`relatorio_eventos.txt`** no diretório do projeto, em **UTF-8**, com os eventos cadastrados.

**Importante:** Se não houver eventos, o relatório não é gerado e o sistema avisa que não há dados para exportar.

# 📅 Sistema de Gestão de Eventos e Contratantes

> Aplicação de linha de comando desenvolvida em Python com Programação Orientada a Objetos para gerenciar eventos e seus respectivos contratantes. Permite cadastrar, listar, editar e remover eventos com validações de negócio completas — datas, horários, CPF/CNPJ e WhatsApp, além de contagem mensal e exportação de relatório em `.txt`. Sem dependências externas, banco de dados ou instalações adicionais: basta ter Python 3.

---

## 📑 Índice

1. [Visão Geral](#-visão-geral)
2. [Arquitetura do Sistema](#-arquitetura-do-sistema)
3. [Pré-requisitos](#-pré-requisitos)
4. [Como Executar](#-como-executar)
5. [Menu Principal](#-menu-principal)
6. [Funcionalidades em Detalhe](#-funcionalidades-em-detalhe)
7. [Regras de Negócio e Validações](#-regras-de-negócio-e-validações)
8. [Estrutura de Classes e POO](#-estrutura-de-classes-e-poo)
9. [Relatório em Texto](#-relatório-em-texto)

---

## 🔭 Visão Geral

O sistema centraliza o controle de eventos para profissionais autônomos ou pequenas empresas que precisam de uma agenda simples e confiável, sem depender de ferramentas externas. Cada evento possui dados completos de data, horário, local e público, e está vinculado a um **contratante** (empresa ou pessoa física responsável), identificado por CPF ou CNPJ.

Todas as entradas passam por **validações rigorosas** antes de serem aceitas: o sistema rejeita datas inválidas, formatos de horário incorretos, documentos com número errado de dígitos e números de WhatsApp fora do padrão brasileiro — sempre exibindo mensagens claras e solicitando nova entrada, sem travar ou encerrar o programa.

---

## 🏗️ Arquitetura do Sistema

```
projeto/
│
├── main.py           # Ponto de entrada: exibe o menu e captura a opção do usuário
├── agenda.py         # Lógica de negócio, validações e persistência em memória
├── evento.py         # Classe Evento e exibição consolidada dos dados
└── contratante.py    # Classe Contratante e exibição dos dados do responsável
```

### Responsabilidade de cada arquivo

| Arquivo | Responsabilidade |
|---------|-----------------|
| `main.py` | Inicializa a `Agenda`, exibe o loop do menu principal e delega cada opção ao método correspondente da `Agenda` |
| `agenda.py` | Mantém a lista de eventos em memória e concentra todas as operações: cadastro com validações, listagem, busca por nome, remoção com confirmação, edição por campo, contagem mensal e exportação do relatório `.txt` |
| `evento.py` | Encapsula os dados de um evento (nome, data, horário, local, público) e a referência ao objeto `Contratante`; possui o método `exibir_dados()` que imprime o evento e delega a exibição do contratante |
| `contratante.py` | Encapsula nome, tipo de documento (`"CPF"` ou `"CNPJ"`), número do documento e WhatsApp; possui o método `exibir_dados()` |

---

## 💻 Pré-requisitos

| Requisito | Versão mínima | Como verificar |
|-----------|--------------|----------------|
| Python | 3.x | `python --version` |

Nenhuma biblioteca externa é necessária. O projeto utiliza apenas recursos nativos do Python.

---

## ▶️ Como Executar

### 1. Execute o programa

```bash
python main.py
```

O menu principal será exibido imediatamente no terminal. Nenhuma configuração adicional é necessária.

---

## 📋 Menu Principal

Ao executar o programa, o seguinte menu é exibido em loop até que o usuário escolha sair:

```
══════════════════════════════
BEM-VINDO AO SISTEMA DE CONTROLE DE EVENTO
══════════════════════════════
1. Cadastrar evento
2. Listar eventos
3. Quantidade total de eventos no mês
4. Remover evento
5. Editar evento
6. Gerar relatório (txt)
0. Sair
──────────────────────────────
Escolha uma opção:
```

| Opção | Função |
|-------|--------|
| `1` | Cadastrar um novo evento com todos os dados do evento e do contratante |
| `2` | Listar todos os eventos cadastrados com detalhes completos |
| `3` | Exibir a quantidade total de eventos em um determinado mês e ano |
| `4` | Buscar um evento pelo nome, exibir seus dados, pedir confirmação e removê-lo |
| `5` | Buscar um evento pelo nome e editar campos individualmente via submenu |
| `6` | Gerar o arquivo `relatorio_eventos.txt` na pasta do projeto |
| `0` | Encerrar o programa |

Qualquer entrada diferente das opções acima exibe `"Opção inválida. Tente novamente."` e retorna ao menu sem encerrar o programa.

---

## 🔍 Funcionalidades em Detalhe

### Opção 1 — Cadastrar Evento

O cadastro é dividido em duas etapas: **dados do evento** e **dados do contratante**.

**Dados do evento (nesta ordem):**

1. **Nome do evento** — não pode ser vazio; o sistema rejeita entradas em branco e solicita novamente;
2. **Data** — coletada em três campos separados (dia, mês, ano) com validações individuais; verifica também conflito de data com eventos já cadastrados;
3. **Horário** — obrigatório no formato `HH:MM`, com validação completa de hora e minuto;
4. **Local** — não pode ser vazio;
5. **Quantidade de pessoas** — deve ser um número inteiro maior ou igual a 1.

**Dados do contratante (na sequência):**

1. **Nome do contratante** — empresa ou pessoa responsável; não pode ser vazio;
2. **Tipo de documento** — o usuário escolhe entre `1` (CPF) ou `2` (CNPJ);
3. **Número do documento** — validado por quantidade de dígitos e conteúdo numérico;
4. **WhatsApp** — exatamente 11 dígitos numéricos.

Ao final, o evento é armazenado na lista da `Agenda` e a mensagem `✅ Evento cadastrado com sucesso!` é exibida.

---

### Opção 2 — Listar Eventos

Exibe todos os eventos cadastrados, um a um, com os seguintes dados:

```
──────────────────────────────
🎉 Evento: Show de Jazz
📅 Data: 2026-07-15
⌚ Horário: 20:00
📍 Local: Teatro Guaíra
👥 Pessoas: 500

🏢 Contratante: Eventos Curitiba Ltda.
📄 CNPJ: 12345678000190
📱 WhatsApp: 41999998888
──────────────────────────────
```

Se não houver nenhum evento cadastrado, exibe: `Nenhum evento cadastrado.`

---

### Opção 3 — Quantidade Total de Eventos no Mês

Solicita o **mês** (1–12) e o **ano** (2026–2100) e exibe quantos eventos possuem aquela combinação de mês e ano.

**Comportamento especial:** se não houver nenhum evento cadastrado, exibe `Nenhum evento cadastrado!` e **não solicita mês nem ano** — evitando entrada desnecessária de dados.

**Exemplo de saída:**
```
Digite o mês para consulta (1-12): 7
Digite o ano (Ex: 2026): 2026

📊 Total de eventos em 07/2026: 3
```

---

### Opção 4 — Remover Evento

1. Solicita o nome do evento (busca insensível a maiúsculas/minúsculas);
2. Se não encontrado, exibe `❌ Evento 'X' não encontrado.` e retorna ao menu;
3. Se encontrado, exibe os dados completos do evento;
4. Solicita confirmação: `Tem certeza que deseja remover? (s/n)`;
5. Se `s`: remove o evento e exibe `✅ Evento 'X' removido com sucesso!`;
6. Se `n` ou qualquer outra entrada: exibe `Remoção cancelada.` e retorna ao menu sem remover.

---

### Opção 5 — Editar Evento

1. Solicita o nome do evento;
2. Se não encontrado, retorna ao menu com mensagem de erro;
3. Se encontrado, exibe os dados atuais e apresenta o submenu de edição:

```
O que deseja editar?
1. Nome do evento
2. Data
3. Horário
4. Local
5. Quantidade de pessoas
0. Concluir edição
```

Cada campo pode ser editado individualmente e as mesmas validações do cadastro se aplicam. O submenu permanece em loop até que o usuário escolha `0` para concluir. Ao editar a **data**, o sistema remove temporariamente o evento da lista antes de validar a nova data, garantindo que o conflito de datas não aponte para o próprio evento sendo editado.

---

### Opção 6 — Gerar Relatório (txt)

Cria (ou sobrescreve) o arquivo **`relatorio_eventos.txt`** na pasta raiz do projeto, em encoding **UTF-8**, com todos os eventos cadastrados.

**Comportamento especial:** se não houver nenhum evento cadastrado, exibe `⚠️ Não há eventos para gerar o relatório.` e **não cria o arquivo**.

**Formato do arquivo gerado:**
```
📋 RELATÓRIO GERAL DE EVENTOS - 2026
========================================

🎉 EVENTO: Show de Jazz
📅 DATA: 2026-07-15 às 20:00
📍 LOCAL: Teatro Guaíra
👥 PÚBLICO: 500 pessoas
🏢 CONTRATANTE: Eventos Curitiba Ltda.
📱 WHATSAPP: 41999998888
------------------------------
```

---

## ✅ Regras de Negócio e Validações

### Datas

| Regra | Detalhe |
|-------|---------|
| **Dia** | Entre `1` e `31`; somente números inteiros |
| **Mês** | Entre `1` e `12`; somente números inteiros |
| **Ano** | Entre `2026` e `2100` (inclusive); somente números inteiros |
| **Conflito de data** | Não é permitido cadastrar dois eventos na mesma combinação de dia + mês + ano; o sistema informa o nome do evento em conflito e solicita outra data |

> A mesma validação de mês (1–12) e ano (2026–2100) se aplica à consulta da **opção 3**.

### Horários

| Regra | Detalhe |
|-------|---------|
| **Formato obrigatório** | `HH:MM` — exatamente 5 caracteres com `:` na posição central |
| **Hora** | Somente dígitos; entre `00` e `23` |
| **Minuto** | Somente dígitos; entre `00` e `59` |
| **Exemplos rejeitados** | `9:5`, `930`, `25:00`, `14:60` |

### Documentos

| Tipo | Dígitos obrigatórios | Conteúdo aceito |
|------|---------------------|-----------------|
| **CPF** | Exatamente **11** | Somente números (sem pontos ou traços) |
| **CNPJ** | Exatamente **14** | Somente números (sem pontos, barras ou traços) |

### WhatsApp

| Regra | Detalhe |
|-------|---------|
| **Quantidade de dígitos** | Exatamente **11** (padrão DDD + número no Brasil) |
| **Conteúdo** | Somente números; espaços e símbolos são rejeitados |

### Campos de texto

| Campo | Restrição |
|-------|-----------|
| Nome do evento | Não pode ser vazio |
| Local do evento | Não pode ser vazio |
| Nome do contratante | Não pode ser vazio |

### Quantidade de pessoas

| Regra | Detalhe |
|-------|---------|
| **Tipo** | Número inteiro |
| **Valor mínimo** | `1` pessoa |

---

## 🏛️ Estrutura de Classes e POO

O modelo segue **composição clássica**: a `Agenda` agrega `Evento`s, e cada `Evento` contém um `Contratante`.

```
Agenda  1 ───────── N  Evento  N ───────── 1  Contratante
```

### Classe `Contratante` (`contratante.py`)

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `enterprise_name` | `str` | Nome da empresa ou pessoa responsável |
| `tipo_documento` | `str` | `"CPF"` ou `"CNPJ"` |
| `cnpj_cpf` | `str` | Número do documento (somente dígitos) |
| `whats` | `str` | Número de WhatsApp (11 dígitos) |

**Método:** `exibir_dados()` — imprime os dados do contratante formatados com emojis.

---

### Classe `Evento` (`evento.py`)

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `event_name` | `str` | Nome do evento |
| `event_day` | `int` | Dia (1–31) |
| `event_month` | `int` | Mês (1–12) |
| `event_year` | `int` | Ano (2026–2100) |
| `event_date` | `str` | Data formatada como `AAAA-MM-DD` |
| `event_time` | `str` | Horário no formato `HH:MM` |
| `event_location` | `str` | Local do evento |
| `number_people` | `int` | Quantidade de pessoas esperadas |
| `contratante` | `Contratante` | Objeto contratante vinculado ao evento |

**Método:** `exibir_dados()` — imprime os dados do evento e chama `contratante.exibir_dados()`.

---

### Classe `Agenda` (`agenda.py`)

Atua como **facade** do domínio: centraliza todas as operações e validações, expondo apenas os métodos públicos chamados pelo menu.

**Métodos públicos:**

| Método | Descrição |
|--------|-----------|
| `cadastrar_evento()` | Coleta e valida todos os dados, cria os objetos e adiciona à lista |
| `listar_eventos()` | Itera sobre a lista e chama `exibir_dados()` em cada evento |
| `contar_eventos_no_mes()` | Solicita mês/ano e conta os eventos correspondentes |
| `remover_evento()` | Busca, exibe, pede confirmação e remove |
| `editar_evento()` | Busca e abre o submenu de edição por campo |
| `gerar_relatorio_txt()` | Grava `relatorio_eventos.txt` com todos os eventos |

**Métodos privados (auxiliares):**

| Método | Descrição |
|--------|-----------|
| `_pedir_data()` | Coleta e valida dia, mês, ano e verifica conflito de datas |
| `_pedir_horario()` | Coleta e valida o horário no formato `HH:MM` |
| `_pedir_documento()` | Apresenta o menu CPF/CNPJ e valida o número informado |
| `_pedir_whatsapp()` | Coleta e valida o número de WhatsApp |
| `_dia_ocupado(day, month, year)` | Verifica se já existe um evento na data informada |
| `_buscar_evento(nome)` | Busca um evento pelo nome (case-insensitive) |

---

## 📄 Relatório em Texto

Ao selecionar a opção `6`, o arquivo **`relatorio_eventos.txt`** é criado (ou sobrescrito) **na mesma pasta onde o programa foi executado**, em encoding **UTF-8**.

**Pontos importantes:**

- Se o arquivo já existir de uma execução anterior, ele será **sobrescrito** com os dados atuais;
- Se não houver eventos cadastrados, o arquivo **não é criado** e o sistema avisa;
- O relatório contém **todos** os eventos cadastrados na sessão atual — a lista não persiste entre execuções (sem banco de dados).

> **Atenção:** como os dados ficam em memória, ao encerrar o programa (opção `0`) todos os eventos são perdidos. Para preservá-los, gere o relatório antes de sair.

## 👥 Autores
Alexandre Zampronne Zaccaron Rocha
Wesley Henrique de Matos Nascimento
Vinicius Oliveira Prado
Matheus Felipe Alves Ferreira
Eduardo Oliveira da Silva

Desenvolvido como projeto acadêmico - 2026
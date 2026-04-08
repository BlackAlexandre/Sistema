# 🎉 Sistema de Controle de Eventos

Sistema em Python para gerenciamento de eventos, com cadastro de contratantes vinculados a cada evento e validações de dados.

---

## 📁 Estrutura do Projeto

```
├── main.py           # Ponto de entrada — exibe o menu principal
├── agenda.py         # Lógica principal: cadastro, listagem e validações
├── evento.py         # Classe Evento
├── contratante.py    # Classe Contratante
```

---

## ▶️ Como Executar

Certifique-se de ter o **Python 3** instalado. No terminal, dentro da pasta do projeto:

```bash
python main.py
```

---

## 🖥️ Menu Principal

````
1. Cadastrar evento
2. Listar eventos
3. Quantidade total de eventos no mês
4. Remover evento
5. Editar evento
0. Sair
```

---

## ✏️ Cadastro de Evento

Ao selecionar a opção **1**, o sistema coleta as seguintes informações:

### Dados do Evento
| Campo         | Descrição                        |
|---------------|----------------------------------|
| Nome          | Nome do evento                   |
| Dia           | Dia do evento (número)           |
| Mês           | Mês do evento (número)           |
| Ano           | Ano do evento (número)           |
| Horário       | Horário do evento                |
| Local         | Local onde ocorrerá o evento     |
| Nº de pessoas | Quantidade de pessoas esperadas  |

### Dados do Contratante
| Campo        | Descrição                                      |
|--------------|------------------------------------------------|
| Nome         | Nome da empresa ou pessoa responsável          |
| CPF ou CNPJ  | Escolha entre CPF (11 dígitos) ou CNPJ (14 dígitos) |
| WhatsApp     | Número de contato com DDD (11 dígitos)         |

---

## ✅ Validações

### 📅 Data do Evento
- Não é permitido cadastrar dois eventos no mesmo dia, mês e ano
- Se a data já estiver ocupada, o sistema informa qual evento está agendado e solicita uma nova data

### 📄 CPF / CNPJ
- O sistema pergunta se o contratante possui **CPF** ou **CNPJ**
- **CPF:** deve conter exatamente **11 dígitos numéricos**
- **CNPJ:** deve conter exatamente **14 dígitos numéricos**
- Não são aceitos pontos, traços, barras ou letras
- O sistema informa quantos dígitos foram digitados em caso de erro

### 📱 WhatsApp
- Deve conter exatamente **11 dígitos numéricos** (DDD + número)
- Não são aceitos espaços, traços ou parênteses
- O sistema informa quantos dígitos foram digitados em caso de erro

---

## 📋 Listagem de Eventos

Ao selecionar a opção **2**, o sistema exibe todos os eventos cadastrados com seus respectivos dados e contratante:

```
══════ LISTA DE EVENTOS ══════

──────────────────────────────
🎉 Evento: [Nome do evento]
📅 Data: [AAAA-MM-DD]
⌚ Horário: [Horário]
📍 Local: [Local]
👥 Pessoas: [Quantidade]

🏢 Contratante: [Nome do contratante]
📄 CPF/CNPJ: [Número]
📱 WhatsApp: [Número]
──────────────────────────────
```

---

## 🔗 Relacionamento entre Classes

```
Agenda
 ├── cadastrar_evento()
 │    ├── _pedir_data()        → valida data e conflito
 │    ├── _pedir_documento()   → valida CPF ou CNPJ
 │    └── _pedir_whatsapp()    → valida WhatsApp
 │
 ├── listar_eventos()
 │
 └── eventos[]
      └── Evento
           └── Contratante
```

---

## 🐍 Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária

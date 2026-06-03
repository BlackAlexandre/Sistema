from datetime import date


def validar_data(dia, mes, ano):
    try:
        date(ano, mes, dia)
        return True
    except ValueError:
        return False


def validar_horario(horario):
    if len(horario) != 5 or horario[2] != ":":
        return False

    hora, minuto = horario.split(":")

    if not hora.isdigit() or not minuto.isdigit():
        return False

    return 0 <= int(hora) <= 23 and 0 <= int(minuto) <= 59


def validar_documento(tipo, numero):
    if not numero.isdigit():
        return False

    if tipo == "CPF":
        return len(numero) == 11

    if tipo == "CNPJ":
        return len(numero) == 14

    return False


def validar_whatsapp(numero):
    return numero.isdigit() and len(numero) == 11

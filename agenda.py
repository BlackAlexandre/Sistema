from contratante import Contratante
from evento import Evento

#Contratante
class contratante:
    def __init__(self):
        self.contratante = []

def cadastrar_evento(self):
    enterprise_name = input("Qual nome do contratante? (Empresa/Pessoa responsável): ")
    cnpj_cpf = input("Digite o CPF/CNPJ: ")
    whats = input("Qual o WhatsApp de contato? (Apenas números) ")
    
    contratante = Contratante ()
    self.contratante.append(enterprise_name, cnpj_cpf, whats)
    

    
    print("\nContratante cadastrado")


#Evento
class evento:
    def __init__(self):
        self.evento = []

def cadastrar_evento(self):
    event_name = input("Qual o nome do evento? ")

    event_date = "{}-{:02d}-{:02d}".format(event_year, event_month, event_day)
    event_time = input("Qual o horário do evento? ")
    event_location = input("Qual o local do evento? ")
    
    try:
        number_people = int(input("Qual a quantidade de pessoas no evento? "))
        event_day = int(input("Qual o dia do evento? "))
        event_month = int(input("Qual o mês do evento? "))
        event_year = int(input("Qual o ano do evento? "))
    except ValueError:
        print("\nDevem ser digitados apenas numeros")
        return
    
    
    evento = Evento ()
    self.evento.append(event_name, event_day, event_month, event_year, event_date, event_time, event_location, number_people)
    print("\nEvento cadastrado com sucesso")
    
    def listar_evento(self):
        if len(self.livros) == 0:
            print("\nNenhum evento cadastrado")
        else:
            print("\nLISTA DE EVENTOS")
            for evento in self.evento:
                evento.exibir_dados()
                
    def listar_contratante(self):
    if len(self.contratante) == 0:
        print("\nNenhum contratante cadastrado")
    else:
        print("\nCONTRATANTE")
        for contratante in self.contratante:
            evento.exibir_dados()



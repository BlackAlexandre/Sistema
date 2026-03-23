from agenda import Agenda

def menu():
    agenda = Agenda()
    
    while True:
        print("\nSISTEMA DE CONTROLE DE EVENTO")
        print("1.Cadastrar evento")
        print("2.Listar evento")
        print("0.Sair")
        
        opcao = input("Escolha uma opção")
        if opcao == "1":
            agenda.cadastrar_evento
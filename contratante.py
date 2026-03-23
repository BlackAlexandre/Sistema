class Contratante:
    def __init__(self, enterprise_name, cnpj_cpf, whats):
        self.enterprise_name = enterprise_name
        self.cnpj_cpf = cnpj_cpf
        self.whats = whats

    def exibir_dados(self):
        print("\nDados do contratante:")
        print("🏢 Contratante: {}".format(self.enterprise_name))
        print("📄 CPF/CNPJ: {}".format(self.cnpj_cpf))
        print("📱 WhatsApp: {}".format(self.whats))

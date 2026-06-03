class Contratante:
    """
    Representa a pessoa ou empresa responsável por contratar um evento.
    """

    def __init__(self, enterprise_name, tipo_documento, cnpj_cpf, whats):
        self.enterprise_name = enterprise_name
        self.tipo_documento = tipo_documento
        self.cnpj_cpf = cnpj_cpf
        self.whats = whats

    def exibir_dados(self):
        print("🏢 Contratante: {}".format(self.enterprise_name))
        print("📄 {}: {}".format(self.tipo_documento, self.cnpj_cpf))
        print("📱 WhatsApp: {}".format(self.whats))

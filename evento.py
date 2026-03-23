from contratante import Contratante


class Evento:
    def __init__(self, event_name, event_day, event_month, event_year, event_date, event_time, event_location, number_people, contratante):
        self.event_name = event_name
        self.event_day = event_day
        self.event_month = event_month
        self.event_year = event_year
        self.event_date = event_date
        self.event_time = event_time
        self.event_location = event_location
        self.number_people = number_people
        self.contratante = contratante

    def exibir_dados(self):
        print("\n──────────────────────────────")
        print("🎉 Evento: {}".format(self.event_name))
        print("📅 Data: {}".format(self.event_date))
        print("⌚ Horário: {}".format(self.event_time))
        print("📍 Local: {}".format(self.event_location))
        print("👥 Pessoas: {}".format(self.number_people))
        print("")
        self.contratante.exibir_dados()
        print("──────────────────────────────")

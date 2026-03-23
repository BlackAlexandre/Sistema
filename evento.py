class Contratante: 
    def __init__(self, event_name, event_day, event_month, event_year, event_date, event_time, event_location, number_people):
        self.event_name = event_name
        self.event_day = event_day
        self.event_month = event_month
        self.event_year = event_year
        self.event_date = event_date
        self.event_time = event_time
        self.event_location = event_location
        self.number_people = number_people
        

def exibir_dados(self):

    print("\nDados do evento:")
    print("📅 Data: {}".format(self.event_name))
    print("📅 Data: {}".format(self.event_date))
    print("⌚ Horario: {}".format(self.event_time))
    print("📍 Local: {}".format(self.event_location))
    print("👥 Pessoas: {}".format(self.number_people))
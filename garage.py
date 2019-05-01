class Garage:
    def __init__(self,
                employes,
                clients,
                voitures,
                voitures_reparees = 0):

        self.employes = employes
        self.clients = clients
        self.voitures = voitures
        self.voitures_reparees = voitures_reparees

    def fix(self, number):
        self.voitures -= number
        self.voitures_reparees += number

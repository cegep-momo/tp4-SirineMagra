
class Mesure:
    'classe de base pour un objet mesure'
    
    def __init__(self,dateHeureMesure,dataMesure):
        self.dateHeureMesure = dateHeureMesure
        self.dataMesure = dataMesure
        
    def __repr__(self):
        return self.dateHeureMesure + self.dataMesure
    
    def afficherMesure(self):
        pass

class Mesure:
    'classe de base pour un objet mesure'
    
    def __init__(self,dateHeureMesure,dataMesure):
        self.dateHeureMesure = dateHeureMesure
        self.dataMesure = dataMesure
        
    def __repr__(self):
        return self.dateHeureMesure +self.dataMesure[0]+self.dataMesure[1]
    
    def afficherMesure(self):
        return f"Date :{self.dateHeureMesure}\n"+f"{self.dataMesure[0]}\n"+f"{self.dataMesure[1]}"
    
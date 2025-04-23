from time import sleep
from view.view import View

class Controler:
    "Gère les interations entre la vue et le modele"
    
    def __init__(self,platine):
        self.platine = platine
        self.vue = View(platine.lcd)
        
        
    def debuter(self):
        while True:
            if self.platine.bouton_debut.is_pressed :
                print("Début de la prise des mesures")
            sleep(0.1)
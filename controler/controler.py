from time import sleep
from view.view import View
import threading

class Controler:
    "Gère les interations entre la vue et le modele"
    
    def __init__(self,platine):
        self.platine = platine
        self.vue = View(platine.lcd)
        
    def appeler_thread_debut(self):
        pass
    
    def attendre_bouton_debut(self):
        while True:
            if self.platine.bouton_debut.is_pressed:
                if self.platine.debut_appuye == False:
                    self.platine.debut_appuye = True
                    self.vue.afficher_debut()
                    sleep(2)
                    self.vue.effacer()
                else:
                    self.platine.debut_appuye = False
                    self.vue.afficher_fin()
                    sleep(2)
                    self.vue.effacer()
                
            sleep(0.1)
    
    def prendre_mesures(self):
        pass    
                               
    def debuter(self):
        try:
            thread_bouton_debut = threading.Thread(target = self.attendre_bouton_debut,daemon=True)
            thread_bouton_debut.start()

            while True:
                if self.platine.debut_appuye == True:
                    sleep(5)
                    valeurADC = self.platine.adc.analogRead(0)
                    voltage = valeurADC / 255.0*3.3
                    self.vue.afficher_mesures(valeurADC,voltage)
    
                sleep(0.1)
                
        except KeyboardInterrupt:
            self.vue.effacer()
    
        
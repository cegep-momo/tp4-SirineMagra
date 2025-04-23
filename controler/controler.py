from time import sleep
from view.view import View
import threading
from model.moduleTP4 import Mesure
import datetime

class Controler:
    "Gère les interations entre la vue et le modele"
    
    def __init__(self,platine):
        self.platine = platine
        self.vue = View(platine.lcd)
        self.mesure = Mesure(0,0)
        self.valeur_adc = 0
        self.valeur_voltage = 0
        self.debut_appuye = False
    
    def attendre_bouton_debut(self):
        while True:
            if self.platine.bouton_debut.is_pressed:
                if self.debut_appuye == False:
                    self.debut_appuye = True
                    self.vue.afficher_debut()
                    sleep(2)
                    self.vue.effacer()
                else:
                    self.debut_appuye = False
                    self.vue.afficher_fin()
                    sleep(2)
                    self.vue.effacer()
                
            sleep(0.1) 
    def attendre_bouton_mesure(self):
        while True:
            if self.debut_appuye == True:
                if self.platine.bouton_sauvegarde.is_pressed:
                    self.vue.afficher_prise_mesure()
                    self.mesure.dateHeureMesure = str(datetime.datetime.now())
                    self.mesure.dataMesure = [{self.valeur_adc},{self.valeur_voltage}]
                    print(self.mesure.afficherMesure())
                    self.mesure.sauvegarder_json()
                    sleep(1)
         
            sleep(0.1) 
                              
    def debuter(self):
        try:
            thread_bouton_debut = threading.Thread(target = self.attendre_bouton_debut,daemon=True)
            thread_bouton_debut.start()

            thread_bouton_mesure = threading.Thread(target = self.attendre_bouton_mesure,daemon=True)
            thread_bouton_mesure.start()
            
            while True:
                if self.debut_appuye == True:
                    sleep(5)
                    self.valeur_adc = self.platine.adc.analogRead(0)
                    self.valeur_voltage = self.valeur_adc / 255.0*3.3
                    self.vue.afficher_mesures(self.valeur_adc,self.valeur_voltage)
                else:
                    self.vue.effacer()
                        
                sleep(0.1)
            
               
        except KeyboardInterrupt:
            self.vue.effacer()
    
        
from time import sleep

class View:
    "interface utilisateur pour afficher des éléments sur l'écran LCD"
    
    def __init__(self,lcd):
        self.lcd = lcd
        
    def afficher_debut(self):
        self.effacer()
        self.lcd.write(0,0,"Debut des")
        self.lcd.write(2,1,"mesures")
    
    def afficher_fin(self):
        self.effacer()
        self.lcd.write(0,0,"Fin des")
        self.lcd.write(2,1,"mesures")
    
    def afficher_mesures(self,adc,voltage):
        self.effacer()
        self.lcd.write(0,0,f"Valeur ADC: {adc}")
        self.lcd.write(0,1,"Voltage: %.2f"%(voltage))  
        
    def afficher_prise_mesure(self):
        self.effacer()
        self.lcd.write(0,0,"Prise des")
        self.lcd.write(2,1,"mesures")
        sleep(2)
        
    def effacer(self):
        self.lcd.clear()
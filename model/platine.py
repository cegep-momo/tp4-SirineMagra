from gpiozero import *
from ADCDevice import *
from time import sleep

class Platine:
    'Classe de base pour un objet Platine'
    
    def __init__(self):
        self.adc = ADCDevice()
        if self.adc.detectI2C(0x4b):
            self.adc = ADS7830()
        else:
            print("Erreur : adresse I2C  non trouvée")
            exit(-1) 
        
        self.bouton_debut = Button(21)
        self.bouton_sauvegarde = Button(20)
        
    
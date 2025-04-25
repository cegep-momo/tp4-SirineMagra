from gpiozero import *
from ADCDevice import *
from time import sleep
from LCD1602 import CharLCD1602

class Platine:
    'Classe de base pour un objet Platine'
    
    def __init__(self):
        #initialisation du capteur analogique
        self.adc = ADCDevice()
        if self.adc.detectI2C(0x4b):
            self.adc = ADS7830()
        else:
            print("Erreur : adresse I2C  non trouvée")
            exit(-1) 
            
        #initialisation des boutons 
        self.bouton_debut = Button(21)
        self.bouton_sauvegarde = Button(20)
        
        #initialisation de l'écran LCD
        self.lcd = CharLCD1602()
        self.lcd.init_lcd(None,1)
        self.lcd.clear()

    
    def retourner_texte_debut(self):
        if self.bouton_debut.is_pressed:
            return "Début"
    
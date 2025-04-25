import unittest
from model.platine import Platine
from gpiozero.pins.mock import MockFactory
from gpiozero import Device

#configure le simulateur
Device.pin_factory = MockFactory()

class TestBoutonAppuyer_0(unittest.TestCase):
    def setUp(self):
        #configure une platine
        self.platine1 = Platine()
    
    def test_appuyerBouton(self):
        self.platine1.bouton_debut.pin.drive_low()
        self.assertTrue(self.platine1.bouton_debut.is_pressed)
    
    def test_verifier_retour_debut(self):
        self.platine1.bouton_debut.pin.drive_low()
        valeur_retour = self.platine1.retourner_texte_debut()
        self.assertTrue(valeur_retour == "Début")
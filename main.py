from controler import controler
from model import platine
from LCD1602 import CharLCD1602

if __name__ == "__main__":

    platine1 = platine.Platine()

    app = controler.Controler(platine1)
    
    app.debuter()
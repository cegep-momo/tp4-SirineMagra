import os
import json
import codecs

class Mesure:
    'classe de base pour un objet mesure'
    
    def __init__(self,dateHeureMesure,dataMesure):
        self.dateHeureMesure = dateHeureMesure
        self.dataMesure = dataMesure
        
    def __repr__(self):
        return self.dateHeureMesure +self.dataMesure[0]+self.dataMesure[1]
    
    def afficherMesure(self):
        return f"Date :{self.dateHeureMesure}\n"+f"Valeur ACD : {self.dataMesure[0]}\n"+f"Valeur Voltage : {self.dataMesure[1]}"
    
    def sauvegarder_json(self):
        chemin_fichier = "./mesures.json"
        
        #si le fichier n'existe pas on le crée, sinon on ajoute les informations à l'intérieur
        if not os.path.exists(chemin_fichier):
            dictionnaire_mesures = {
               "Mesures":[{     
               "datePartie": "",
               "valeurACD":"",
               "valeurVoltage":""             
                }]           
               }
            dictionnaire_mesures["Mesures"][0]["datePartie"]=self.dateHeureMesure
            dictionnaire_mesures["Mesures"][0]["valeurACD"]=str(self.dataMesure[0])
            dictionnaire_mesures["Mesures"][0]["valeurVoltage"]=str(self.dataMesure[1])
            
            with codecs.open("mesures.json","w",encoding='utf-8') as fichier_json:
                json.dump(dictionnaire_mesures,fichier_json,ensure_ascii=False, indent=4,sort_keys=True)
        else:
            dictionnaire_mesures = {
                "datePartie": "",
                "valeurACD":0,
                "valeurVoltage":0  
            }
            dictionnaire_mesures["datePartie"]=self.dateHeureMesure
            dictionnaire_mesures["valeurACD"]=str(self.dataMesure[0])
            dictionnaire_mesures["valeurVoltage"]=str(self.dataMesure[1])
            
            #ajout dans un fichier json
            with codecs.open("mesures.json","r",encoding='utf-8') as fichier_json:
                data = json.load(fichier_json)

            data["Mesures"].append(dictionnaire_mesures)

            with codecs.open("mesures.json","w",encoding='utf-8') as fichier_json:
                json.dump(data,fichier_json,ensure_ascii=False, indent=4,sort_keys=True)
        
    
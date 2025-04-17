'''
@author: Daniel Victor Freire
@name: Plant.py 
@version: 0.0.1
@license: private
@project: Cannabis Grower Assistant For Cannabis Growers
@file: Plant.py
@filepath: src/lib/Plant.py
@description: This file contains the Plant class, which is used to manage the cannabis plants.
@copyright: 2021 Daniel Victor Freire. All rights reserved.
@maintainer: Daniel Victor Freire
@date: 2025-04-10
@since: 2025-04-10
@description: Plant class for managing cannabis plants.
@see : https://github.com/danielvictorfreire/cannahelper
@documentation: https://cannahelper.readthedocs.io/en/latest/
@documentation: https://cannahelper.readthedocs.io/en/latest/Plant.html
@usage: from Plant import Plant
@usage: plant = Plant("White Widow", 1, 10.0, 6.0, 30, "Sativa")
@usage: plant.getInfo(self: object) -> dict
@usage: plant.checkPhLevel(self: object) -> str
@usage: plant.updateGrowStage(self: object) -> int
@usage: plant.getCurrentGrowStage(self: object) -> int
@usage: plant.getCurrentHeight(self: object) -> float
@usage: plant.equals(self: object, other_plant: object) -> bool
'''

'''
@method __init__(self: object, strain: str, growStage: int, height: float, phLevel: float, daysOld: int, geneticOrigin: str) -> None
@method_description: This method initializes the attributes of the class with the provided parameters.
@description: The constructor for the Plant class.
@param self: The instance of the class.
@param strain: The strain of the plant.
@param growStage: The grow stage of the plant.
@param height: The height of the plant.
@param phLevel: The pH level of the plant.
@param daysOld: The days old of the plant.
@param geneticOrigin: The genetic origin of the plant.
@return: None
'''
@classmethod
class Plant (object):

    @staticmethod
    def __init__(self: object, strain: str, growStage: int, height: float, phLevel: float, daysOld: int, geneticOrigin: str) -> None:

        self.strain = strain
        self.growStage = growStage
        self.height = height
        self.phLevel = phLevel
        self.daysOld = daysOld
        self.geneticOrigin = geneticOrigin
        

    '''
    @method getInfo
    @method_description: This method returns a dictionary with the attributes of the class.
    @abstract: This method is used to get the information of the class.
    @description: This method is used to get the information of the class.
    @return: dictionary with the attributes of the class.
    @usage : plant = Plant.getInfo()
    @return: dict
    @usage : plant.getInfo()
    '''
    @classmethod
    def getInfo(self: object) -> dict:
        return {
            "strain": self.strain,
            "growStage": self.growStage,
            "height": self.height,
            "phLevel": self.phLevel,
            "daysOld": self.daysOld,
            "geneticOrigin": self.geneticOrigin
        }
    
    '''
    @method checkPhLevel
    @method_description: This method checks the pH level of the plant and returns a string with the result.
    @description: This method checks the pH level of the plant and returns a string with the result.
    @return: string with the result.
    @usage : plant = Plant.checkPhLevel()
    @return: string with the result.
    @usage : plant.checkPhLevel()
    '''
    def checkPhLevel(self: object) -> str:
        
        if self.phLevel < 5.5:
            return "Ph muito ácido, adicione cal para aumentar o pH."
        elif self.phLevel >= 5.5 and self.phLevel <= 6.5:
            return "Ph adequado."
        else:
            return "Ph muito alcalino, adicione ácido para diminuir o pH."
    
    '''
    @method updateGrowStage
    @method_description: This method updates the grow stage of the plant based on the days old.
    @description: This method updates the grow stage of the plant based on the days old.
    @return: int with the current grow stage of the plant.
    @usage : plant = Plant.updateGrowStage()
    @return: int with the current grow stage of the plant.
    @usage : plant.updateGrowStage()
    '''
    def updateGrowStage(self: object) -> int:
        
        if self.daysOld < 21:
            self.growStage = 1
        elif self.daysOld < 60:
            self.growStage = 2
        else:
            self.growStage = 3
    
    '''
    @method getCurrentGrowStage
    @method_description: This method returns the current grow stage of the plant.
    @description: This method returns the current grow stage of the plant.
    @return: int with the current grow stage of the plant.
    @usage : plant = Plant.getCurrentGrowStage()
    @return: int with the current grow stage of the plant.
    @usage : plant.getCurrentGrowStage()
    '''
    def getCurrentGrowStage(self: object) -> int:
                
        return self.growStage
    
    def getCurrentHeight(self: object) -> float:
        
        return self.height
    
    def equals(self: object, other: object) -> bool:
        
        return self.strain == other.strain and self.growStage == other.growStage and self.height == other.height and self.phLevel == other.phLevel and self.daysOld == other.daysOld and self.geneticOrigin == other.geneticOrigin
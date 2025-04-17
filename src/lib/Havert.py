'''
@author: Daniel Victor Freire
@date: 2025-10-01
@since 2025-10-01
@version: 0.0.1
@copyright: Copyright © 2025 Daniel Victor Freire. All rights reserved.
@license: This project is licensed under the MIT License. See the LICENSE file for details.
@maintainer: Daniel Victor Freire
@project: Cannabis Grower Assistant
@name: Haverts.py
@file: Haverts.py
@description: This file contains the Haverts class, which is used to manage the harvesting process of cannabis plants.'''

'''
@import: typing
@description: This module is used to define the type hints for the class.
'''
'''
@classinstance: Haverts
'''
from typing import override  # type hinting for class method cehckHavertsReadiness

class Haverts (object) :
    
    # @constructor: Haverts
    # @description: This method initializes the class.
    # @param: floweringStage: int, thrichomesrReady: int, curringMethod: str, dryingDays: int, currentWeeks: int, havertsTechnique: str
    # @usage : haverst = Haverts(floweringStage, thrichomesrReady, curringMethod, dryingDays, currentWeeks, havertsTechnique)
    # @return: None
    # @example : haverst = Haverts(1, 2, "manual", 3, 4, "manual")
    def __init__ (self: object, floweringStage: int, thrichomesrReady: int, estimatedUYield: int, curringMethod: str, dryingDays: int, currentWeeks: int, havertsTechnique: str) -> None:
        
        self.flowerinStage = floweringStage
        self.thrichomesrReady = thrichomesrReady
        self.estimatedUYield = estimatedUYield
        self.curringMethod = curringMethod
        self.dryingDays = dryingDays
        self.currentWeeks = currentWeeks
        self.havertsTechnique = havertsTechnique
        self.havertsTechnique = havertsTechnique
        self.floweringStage = floweringStage
        self.thrichomesrReady = thrichomesrReady
    
    # @method getInfo
    # @description: This method returns a dictionary with the attributes of the class.
    # @return: dict
    # @description: This method returns a dictionary with the attributes of the class.
    # @usage : haverst = Haverts.getInfo()
    # @abstract : This method is used to get the information of the class.
    @classmethod
    def getInfo(self) -> dict:
        return {
            "floweringStage": self.floweringStage,
            "trichomesReady": self.thrichomesrReady,
            "estimatedUYield": self.estimatedUYield,
            "curringMethod": self.curringMethod,
            "dryingDays": self.dryingDays,
            "currentWeeks": self.currentWeeks,
            "havertsTechnique": self.havertsTechnique
        }

    
    # @method setInfo
    # @description: This method sets the attributes of the class.
    # @param: floweringStage: int, thrichomesrReady: int, curringMethod: str, dryingDays: int, currentWeeks: int, havertsTechnique: str
    # @usage : haverst.setInfo(floweringStage, thrichomesrReady, curringMethod, dryingDays, currentWeeks, havertsTechnique)
    # @abstract : This method is used to set the information of the class.
    @classmethod
    def checkHavertsReadiness(self) -> str:
        if self.flowringWeeks < 6:
            return "Muito cedo para colheita"
        elif self.flowringWeeks >= 6 and self.floweringStage <= 9:
            return "Verifique os tricomas para determinar o momento certo para a colheita"
        elif self.floweringStage > 9:
            return "Muito tarde para colheita"
    
    # @method checkHarvestReadiness
    # @description: This method checks the harvest readiness of the plant.
    # @param: None
    # @usage : haverst.checkHarvestReadiness()
    # @abstract : This method is used to check the harvest readiness of the plant.
    # @return: str
    # @example : haverst.checkHarvestReadiness()
    # @description: This method checks the harvest readiness of the plant.    
    @override
    def checkHarvestReadiness(self) -> str:
        if self.floweringWeeks < 6:
            return "Tricomas ainda não estão prontos para a colheita é muito cedo para colheita"
        elif self.thrichomesrReady >= 6 and self.thrichomesrReady <= 9:
            if self.trichomesrReady:
                return "Está na olha tanto esperar a colheita ! <3"
            else:
                return "Verifique os tricomas para determinar o momento certo para a colheita"
        else:
            return "Talvez pasou do ponto de colheota e os tricomas estão muito maduros, a colheita deve ser feita imediatamente"



'''
@author: Daniel Freire
@date: 2025-13-04
@since 2025-13-04
@project: CannaHelper
@package: main.py
@version: 0.0.1
@description: This is a simple program to help you grow your plants. It will help you with the following:
@mainter: Daniel Freire
@license: The Unlicense
@github: https://github.com/proxyanony/CannaHelper.git
@see: https://www.cannahelper.com
@link : https://www.cannahelper.com
@contact: danielfreire56@gmail.com
@copyright: Copyright (c) 2025 Daniel Freire
'''

'''
@import * from lib.py
@description: This is a simple program to help you grow your plants. It will help you with the following:
@mainter: Daniel Freire

@import walk from os
@description: This is a simple program to help you grow your plants. It will help you with the followings
'''
from lib import Plant, CannaHelper, Harvest, LightConfiguration, WaterSystem, Nutrients
from os import walk

'''
@class CannaHelper
@description: This is a simple program to help you grow your plants. It will help you with the following:
@abstract: This is a simple program to help you grow your plants. It will help you with the following:
@mainter: Daniel Freire
@version: 0.0.1
@license: The Unlicense
@github: https://github.com/proxyanony/CannaHelper.git
@copyright: Copyright (c) 2025 Daniel Freire
'''
class CannaHelperMain (object):
    
    '''
    @description: This is a simple program to help you grow your plants. It will help you with the following:
    @abstract: This is a simple program to help you grow your plants. It will help you with the following:
    @params: plant: Plant
    @params: harvest: Harvest
    @params: light_configuration: LightConfiguration
    @params: water_system: WaterSystem
    @params: nutrients: Nutrients
    @return: None
    '''
    @staticmethod
    def __init__(self: object, plant: Plant, harvest: Harvest=None, light_configuration: LightConfiguration=None, water_system: WaterSystem=None, nutrients: Nutrients=None) -> None:
        
        self.class_list = []
        self.plant = plant
        self.haverst = harvest
        self.light_configuration = light_configuration
        self.water_system = water_system
        self.nutrients = nutrients
    
    @classmethod
    def get_class_list(self: object) -> None:
        
        for i, name in walk("./src/lib"):
            if name.endswith(".py"):
                self.class_list.append(name[:-3])
        
        self.class_list = self.class_list
    
    @classmethod
    def list_class(self: object):
        [print(name) for name in self.class_list]

GreenCrackStrain: Plant = Plant("Green Crack", 1, 10.0, 6.5, 30, "Sativa")
#GreenCrackStrain: Plant = Plant(strain="Green Crack", yield=10.0, height=6.5, age=30, type="Sativa") # Exemplo usando o nome dos argumentos da classe
CannaHelperMain: CannaHelperMain = CannaHelperMain(GreenCrackStrain) # type: ignore
CannaHelperMain.get_class_list()
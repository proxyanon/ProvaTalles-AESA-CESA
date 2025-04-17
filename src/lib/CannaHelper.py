'''
[+] Projeto CannaHelper.py - Classe principal para o projeto CannaHelper

[CannaHelper.py disclaimers]
Este arquivo é parte do projeto CannaHelper, que é um sistema de gerenciamento de
dados para o cultivo de cana. Ele fornece uma interface para o usuário para
gerenciar e visualizar os dados de cultivo de cana, bem como para realizar
cálculos e análises estatísticas.
[/CannaHelper.py disclaimers]

@author Daniel Victor Freire
@file CnnaHelper.py
@date 2025-08-04
@since 2025-08-04
@class CnnaHelper
@version 0.0.1
@license private
@package CannaHelper 
@copyright Copyright (c) 2025 Daniel Victor Freire
@description This module is part of the CannaHelper project, which is a Python
@about This module is part of the CannaHelper project, which is a Python
@abstract This module is part of the CannaHelper project, which is a Python
@usage cannahelper = new CannaHelper(plant, harvest, watersystem, lightconfiguration, nutrients)
@usage_description This module is main class of the CannaHelper project, which is a Python

'''
class CnnaHelper:
    def __init__(self, plant: str, haverst: str, watersystem: list, lightConfiguration: str, nutrients: list) -> None:
        
        ''' Inicializa a classe CnnaHelper com os parâmetros fornecidos '''
        
        # @param self: Objeto da classe CnnaHelper
        # @param plant: Objeto da classe Plant
        # @param haverst: Objeto da classe Harvest
        # @param watersystem: Objeto da classe WaterSystem
        # @param lightconfiguration: Objeto da classe LightConfiguration
        # @param nutrients: Objeto da classe Nutrients
        
        self.plant = plant # Objeto da classe Plant defini a planta ou genética que viverá ser cultivada
        # @type: Plant
        self.harverst = haverst # Objeto da classe Harvest define a colheita que será realizada
        # @type: Harvest
        self.watersystem = watersystem # Objeto da classe WaterSystem define o sistema de irrigação que será utilizado
        # @type: WaterSystem
        self.lightconfiguration = lightConfiguration # Objeto da classe LightConfiguration define a configuração de luz que será utilizada  
        # @type: list
        self.nutrients = nutrients # Objeto da classe Nutrients define os nutrientes que serão utilizados
        # @type: Nutrients

    # Lista todas as classes do projeto CannaHelper
    # @rtype: list | bool
    # @description: Lista todas as classes do projeto CannaHelper
    # @usage: cannahelper.list_classes()
    # @usage_description: Lista todas as classes do projeto CannaHelper
    # @access public
    # @access_description: Lista todas as classes do projeto CannaHelper
    # @access_type: public
    # @classmethod CannaHelper.list_classes
    # @return: Lista de classes do projeto CannaHelper
    
    @classmethod
    def list_classes(self) -> list | bool:
        
        #Lista todas as clases do projeto CannaHelper
        try:
            # Retorna uma lista de todas as classes definidas na classe CnnaHelper
            return [cls for cls in dir(self) if isinstance(getattr(self, cls), type)] # Retorna uma lista de todas as classes definidas na classe CnnaHelper
        except AttributeError as e:
            # Em caso de erro, imprime a mensagem de erro e retorna uma lista vazia
            print(f"Erro ao listar classes: {e}") # Imprime a mensagem de erro
            return False # Retorna um boolean False se ocorrer um erro
        except Exception as e:
            # Em caso de erro, imprime a mensagem de erro e retorna uma lista vazia
            print(f"Erro ao listar classes: {e}")
            return False # Retorna um boolean False se ocorrer um erro
        finally:
            # Retorna uma lista de todas as classes definidas na classe CnnaHelper
            return [cls for cls in dir(self) if isinstance(getattr(self, cls), type)] # Retorna uma lista de todas as classes definidas na classe CnnaHelper
            # Retorna uma lista de todas as classes definidas na classe CnnaHelper
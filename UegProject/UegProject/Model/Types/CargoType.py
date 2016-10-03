from enum import Enum

"""
Enumarate types of Cargos in Elections
"""
class CargoType(Enum):
    prefeito = 0
    vereador = 1
    governador = 2
    senador = 3
    presidente = 4
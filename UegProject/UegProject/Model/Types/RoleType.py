from enum import Enum

"""
Enumarate types of Regiao in Elections
"""


class RoleType(Enum):
    PREFEITO = "PREFEITO"
    VEREADOR = "VEREADOR"
    GOVERNADOR = "GOVERNADOR"
    SENADOR = "SENADOR"
    PRESIDENTE = "PRESIDENTE"
    DEPUTADO = "DEPUTADO"

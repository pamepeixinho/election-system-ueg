from enum import Enum

"""
Enumarate types of Errors in Communication mainly
"""


# TODO put this enum in Class Diagram
class ErrorCodes(Enum):
    INVALID_UEV = 1
    INVALID_TIME_ELECTION = 2
    CONNECTION_PROBLEM = 3
    WRONG_REQUEST = 4

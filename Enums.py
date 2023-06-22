from enum import Enum

class Standard(Enum):
    Kindergarten = 0
    First = 1
    Second = 45
    Third = 3
    Fourth = 4

print(Standard.Second.value)
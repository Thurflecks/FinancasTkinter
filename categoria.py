from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Categoria(Enum):
    CONTA_FIXA = auto()
    RECEITA = auto()
    DESPESA = auto()
    
    

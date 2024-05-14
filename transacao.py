from dataclasses import dataclass
from categoria import Categoria


@dataclass
class Transacao:
    valor: float = 0
    descricao: str = 0
    categoria: Categoria = 0
    
    def adc_valor(self, v, d, c):
        self.valor += v
        self.descricao = d
        self.categoria = c
    
    def getvalor(self):
        return self.valor
      
   
  
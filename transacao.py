from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transacao:
    valor: float
    descricao: str
    categoria: Categoria
    
    def adc_valor(self, v, d, c):
        self.valor += v
        self.descricao = d
        self.categoria = c
        
    def total_total(self):
        return self.valor
        
    def ultimaTransacao(self):
        print(f"O valor total é: {self.total_total()}, a descrição foi: {self.descricao} e foi nessa categoria: {self.categoria.name}")
class Plano:
    def __init__(self,
                nome:str=None,
                valor:int=None,                
                ):
        self.setNome(nome)
        self.setValor(valor)

    def getNome(self) -> str:
        return self.nome

    def getValor(self) -> int:
        return self.valor


    def setNome(self, nome:str):
        self.nome = nome

    def setValor(self, valor:int):
        self.valor = valor

    def toString(self) -> str:
        return ("Nome: {self.nome} | Valor: {self.valor}")
import datetime as dt

class Mensalidade:
    def __init__ (self,
                ):
        self.data_criacao = dt.datetime.now()
    
    def getDatacriacao(self) -> dt:
        return self.data_criacao

    def getDatavencimento (self) -> dt:
        return self.data_vencimento

    def getValorcobranca (self) -> float:
        return self.valor_cobranca

    def getMulta (self) -> float:
        return self.multa


    def setDatacriacao(self, data_criacao:dt):
        self.data_criacao = data_criacao

    def setDatavencimento(self, data_vencimento:dt):
        self.data_vencimento = data_vencimento

    def setValorcobranca(self, valor_cobranca:float):
        self.valor_cobranca = valor_cobranca

    def setMulta(self, multa:float):
        self.multa = multa

    
    def toString(self) -> str:
        return ("Data de Criação = {self.data_criacao} | Data de Vencimento = {self.data_vencimento} | Valor da Cobrança = {self.valor_cobranca} | Multa = {self.multa}")
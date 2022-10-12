import  datetime as dt

class Socio:
    def __init__(self,
                nome:str=None,
                CPF:str=None,
                telefone:str=None,
                email:str=None,
                endereco:str=None,
                ):
        self.setNome(nome)
        self.setCPF(CPF)
        self.setTelefone(telefone)
        self.setEmail(email)
        self.setEndereco(endereco)
        self.dataAssociacao = dt.datetime.now()
        self.datadDesativacao = None
    

    #Getters
    def getNome(self) -> str:
        return self.nome

    def getCPF(self) -> str:
        return self.CPF

    def getTelefone(self) -> str:
        return self.telefone

    def getEmail(self) -> str:
        return self.email

    def getEndereco(self) -> str:
        return self.endereco

    def getDataAssociacao(self) -> dt:
        return self.dataAssociacao

    def getDataDesativacao(self) -> dt:
        return self.dataDesativacao    


    #Setters
    def setNome(self, nome:str):
        self.nome = nome

    def setCPF(self, CPF:str):
        self.CPF = CPF

    def setTelefone(self, telefone:str):
        self.telefone = telefone

    def setEmail(self, email:str):
        self.email = email

    def setEndereco(self, endereco:str):
        self.endereco = endereco

    def setDataDesativacao(self):
        self.dataDesativacao = dt.datetime.now()

    def toString(self) -> str:
        return f""" Nome: {self.nome} | 
                    CPF: {self.CPF} | 
                    Telefone: {self.telefone} | 
                    Email: {self.email} | 
                    Endereco: {self.endereco} | 
                    Data de associação: {self.dataAssociacao} | 
                    data de desativação: {self.dataDesativacao}"""
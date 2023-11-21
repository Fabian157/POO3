class Cuenta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construyendo el objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extracto(self):
        print("Saldo: {} del titular {}".format(self.saldo, self.titular))
        
    def depositar(self, valor):
        self.saldo += valor
        
    def retirar(self, valor):
        if valor > self.saldo:
            print("No cuenta con esa cantidad disponible para retirar")
        else:
            self.saldo -= valor
    
    def transferir(self, valor, destino):
        self.retirar;
        destino.depositar;
       
    def get_saldo(self):
        return self.saldo;
    
    def get_titular(self):
        return self.titular
    
    @property
    def limite(self):
        return self.limite;
    
    @limite.setter
    def limite(self, limite):
        self.limite = limite
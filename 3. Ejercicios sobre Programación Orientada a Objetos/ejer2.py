class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    
    def ingresar_dinero(self,cantidad):
        self.saldo += cantidad
    
    def retirar_dinero(self,cantidad):
        if (self.saldo == 0):
            print("ERROR :/ No hay dinero en su cuenta")
            return
        self.saldo -= cantidad
    
    def imprimir_saldo(self):
        print(f"Su saldo en la cuenta es = {self.saldo}")

cuentaBanca = CuentaBancaria("Samuel", 500)

cuentaBanca.ingresar_dinero(50)
cuentaBanca.retirar_dinero(20)
cuentaBanca.imprimir_saldo()

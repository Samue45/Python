class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo

    def mostrar_saldo(self):
        print(f"Su saldo es = {self.__saldo}")
    
    def ingresar_dinero(self,cantidad):
        self.__saldo += cantidad
    
    def retirar_dinero(self,cantidad):
        if (self.__saldo == 0):
            print("ERROR :/ No hay dinero en su cuenta")
            return
        self.__saldo -= cantidad
    
    def imprimir_saldo(self):
        print(f"Su saldo en la cuenta es = {self.__saldo}")

cuentaBanca = CuentaBancaria("Samuel", 500)

try:
    print(cuentaBanca.__saldo)
except AttributeError as e:
    print(f"Error : {e}")

cuentaBanca.mostrar_saldo()

cuentaBanca.ingresar_dinero(50)
cuentaBanca.retirar_dinero(20)
cuentaBanca.imprimir_saldo()

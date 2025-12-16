class CuentaBancaria:
    def __init__(self,titular, saldo, tipo_de_cuenta):
        self.__titular = titular
        self.__saldo = saldo
        self.__tipo_de_cuenta = tipo_de_cuenta

    # Getter
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def tipo_de_cuenta(self):
        return self.__tipo_de_cuenta

    # Setter
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo
    
    
    @tipo_de_cuenta.setter
    def tipo_de_cuenta(self,tipo_de_cuenta):
        self.__tipo_de_cuenta = tipo_de_cuenta

    # Métodos

    def depositar(self,cantidad):
        if cantidad <= 0:
            print("Error, la cantidad no puede ser 0 o menor")
            return
        self.__saldo += cantidad

    
    def reitrar(self,cantidad):
        if cantidad <= 0:
            print("Error, la cantidad no puede ser 0 o menor")
            return
        self.__saldo -= cantidad

    def mostrar_saldo(self):
        print(f"Su saldo actual es de {self.__saldo} €")

    def tipo_cuenta(self):
        print(f"Su cuenta es de tipo '{self.__tipo_de_cuenta}'")

Cuenta1 = CuentaBancaria("Samuel",500,"Individual")

Cuenta1.depositar(50)
Cuenta1.reitrar(10)
Cuenta1.mostrar_saldo()
Cuenta1.tipo_cuenta()
class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def consultar_saldo(self):
        return self.saldo

cuenta = CuentaBancaria()
cuenta.depositar(30)
cuenta.depositar(10)
print("Saldo actual:", cuenta.consultar_saldo())

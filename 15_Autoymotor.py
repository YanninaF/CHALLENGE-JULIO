class Motor:
    def __init__(self, tipo, cilindros):
        self.tipo = tipo
        self.cilindros = cilindros

    def describir(self):
        return f"Motor de tipo {self.tipo} con {self.cilindros} cilindros."

class Auto:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def describir_auto(self):
        return f"Auto de marca {self.marca}, modelo {self.modelo}. {self.motor.describir()}"


motor = Motor("Gasolina", 4)
auto = Auto("Toyota", "Ractis", motor)

print(auto.describir_auto())

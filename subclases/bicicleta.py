from superclases.vehiculo import Vehiculo

class bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def arranacar(self):
        print(f"La bicicleta {self.tipo} lista para arranacar")

    def frenar(self):
        print(f"La bicicleta {self.tipo} se para")

    def __str__(self):
        return f"La bicicleta({self.tipo}) de color {self.color},tiene {self.ruedas} ruedas"
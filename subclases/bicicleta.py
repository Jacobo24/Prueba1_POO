from superclases.vehiculo import Vehiculo

class bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(self, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} urbana, {} deportiva".format(self.tipo)
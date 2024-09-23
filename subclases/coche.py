from superclases.vehiculo import Vehiculo

class coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color{}, {} km/h, {} ruedas, {} cilindrada".format(self.color, self.velocidad, self.ruedas, self.cilindrada)
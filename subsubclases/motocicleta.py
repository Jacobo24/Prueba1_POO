import subclases.bicicleta as bicicleta

class motocicleta(bicicleta):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        bicicleta.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return bicicleta.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
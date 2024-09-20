import superclases.vehiculo as Vehiculo

class bicicleta(Vehiculo):
    def __init__(self, color, ruedas, urbana, deportiva):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = (urbana/deportiva)
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} urbana, {} deportiva".format(self.tipo)
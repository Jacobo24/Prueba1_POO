import subclases.coche as coche

class camioneta(coche):
    def __init__(self, color, ruedas, carga):
        coche.__init__(self, color, ruedas)
        self.tipo = (carga)
    def __str__(self):
        return coche.__str__(self) + ", {}".format(self.tipo)
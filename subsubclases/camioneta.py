from subclases.coche import coche

class camioneta(coche):
    def __init__(self, color, ruedas, carga):
        super().__init__(self, color, ruedas)
        self.tipo = (carga)
    def __str__(self):
        return coche.__str__(self) + ", {}".format(self.tipo)
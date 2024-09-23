from subclases.coche import coche

class camioneta(coche):
    def __init__(self, color, ruedas, carga, velocidad, cilindrada):
        super().__init__(self, color, ruedas)
        self.tipo = (carga)

        def __str__(self):
            return f"Camioneta(color={self.color}, ruedas={self.ruedas}, carga={self.tipo}, velocidad={self.velocidad}, cilindrada={self.cilindrada})"

    def arrancar(self):
        print(f"La camioneta arranca")

    def frenar(self):
        print(f"La camioneta se para")

    def cargar(self):
        print(f"La camioneta se carga ")

    def descargar(self):
        print(f"La camioneta se descarga")
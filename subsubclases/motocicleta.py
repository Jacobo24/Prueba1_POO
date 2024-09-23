from subclases.bicicleta import bicicleta

class motocicleta(bicicleta):
    def __init__(self, color, ruedas, velocidad, cilindrada, tipo):
        super().__init__(tipo, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def arrancar(self):
        print(f"La motocicleta arranca")

    def frenar(self):
        print(f"La motocicleta se para")

    def __str__(self):
        return f"Vehiculo de color {self.color}, con {self.ruedas} ruedas, de {self.tipo}, va a {self.velocidad} km/h, tiene {self.cilindrada} cc"
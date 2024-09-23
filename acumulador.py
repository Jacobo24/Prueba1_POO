from subclases.bicicleta import bicicleta
from subclases.coche import coche
from subsubclases.motocicleta import motocicleta
from subsubclases.camioneta import camioneta


def acumulador():
    vehiculos = []

    mi_vehiculo = coche("azul", 4, 150, 1200)
    vehiculos.append(mi_vehiculo)

    mi_vehiculo2 = bicicleta("verde", 2, "urbana")
    vehiculos.append(mi_vehiculo2)

    mi_vehiculo3 = camioneta("blanca", 4, 150, 2000, 500)
    vehiculos.append(mi_vehiculo3)

    mi_vehiculo4 = motocicleta("negra", "deportiva", 689, 2, 1000)
    vehiculos.append(mi_vehiculo4)

    for vehiculo in vehiculos:
        print(vehiculo)

    def catalogar(vehiculo, ruedas):
        contador = 0
        for v in vehiculo:
            if v.ruedas == ruedas:
                contador += 1
        return contador
    
    catalogar(vehiculos)
    catalogar(vehiculos, 0)
    catalogar(vehiculos, 2)
    catalogar(vehiculos, 4)

# Expected output:
# Vehiculo de color azul, 4 ruedas, 150 km/h, 1200 cc
# Vehiculo de color verde, 2 ruedas, urbana
# Vehiculo de color blanca, 4 ruedas, 500 kg, 2000 cc, 150 km/h
# Vehiculo de color negra, 2 ruedas, deportiva, 689 km/h, 1000 cc
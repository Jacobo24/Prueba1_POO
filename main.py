from subclases.bicicleta import bicicleta
from subclases.coche import coche
from subsubclases.motocicleta import motocicleta
from subsubclases.camioneta import camioneta


if __name__ == '__main__':
    vehiculos = []

    mi_vehiculo = coche("azul", 4, 150, 1200)
    vehiculos.append(mi_vehiculo)

    mi_vehiculo2 = bicicleta("verde", 2, "urbana", "deportiva")
    vehiculos.append(mi_vehiculo2)

    mi_vehiculo3 = camioneta("blanca", 4, 150, 2000, 500)
    vehiculos.append(mi_vehiculo3)

    mi_vehiculo4 = motocicleta("negra", "urbana" ,"deportiva", 689, 2, 1000)
    vehiculos.append(mi_vehiculo4)

    for vehiculo in vehiculos:
        print(vehiculo)



# Expected output:
# Vehiculo de color azul, 4 ruedas, 150 km/h, 1200 cc
# Vehiculo de color verde, 2 ruedas, urbana
# Vehiculo de color blanca, 4 ruedas, 500 kg, 2000 cc, 150 km/h
# Vehiculo de color negra, 2 ruedas, deportiva, 689 km/h, 1000 cc
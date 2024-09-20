import subclases.bicicleta as bicicleta
import superclases.vehiculo as coche
import subsubclases.motocicleta as motocicleta
import subsubclases.camioneta as camioneta


if __name__ == '__main__':
    mi_vehiculo = coche("azul", 4, 150, 1200)
    print (mi_vehiculo)
    mi_vehiculo2 = bicicleta("verde", 2, "urbana", "deportiva")
    print (mi_vehiculo2)
    mi_vehiculo3 = camioneta("blanca", 4, 1000)
    print (mi_vehiculo3)
    mi_vehiculo4 = motocicleta("negra", 2, 180, 900)
    print (mi_vehiculo4)
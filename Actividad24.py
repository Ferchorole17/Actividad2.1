colores = ('amarillo','azul','rojo','blanco')
color = input("Introduce un color\n")
if color in colores:
    print("El color {} se encuentra en la tupla".format(color))
else:
    print("El color {} no se encuentra en la tupla".format(color))

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
colores('azul', 'rojo')
def suma(*args):
	res = args[0] + args[1] + args[2] + args[3] + args[4]
	print("El resultado de la suma es: {}".format(res))
suma(3, 1, 7, 8, 9)
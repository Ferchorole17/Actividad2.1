x = 0
while x < 30:
    x += 1
    if x == 15:
        print("Se rompió la ejecucion del bucle cuando x valia {}".format(x))
        break
    else:
        if x == 4 or x == 6 or x == 10:
            print("Se saltó el valor {} de x".format(x))
        else:
            print("El valor del bucle es {}".format(x))
            
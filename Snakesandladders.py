#Se importa random para tirar el dado en posiciones aleatorias
import random

#Se crean arreglos para guardar las posiciones tanto de las escaleras y sus respectivos finales como de las serpientes
ladders = [3, 6, 9, 10]
endladders = [11, 17, 18, 12]
snakes = [14, 19, 22, 24]
endsnakes = [4, 8, 20, 16]
position = 0

#Se crea el metodo para verificar si la posición corresponde a alguna escalera y si es asi a donde sube
#Se imprime la posición correspondiente si cae en alguna escalera
def ifladders(position):
    if position == ladders[0]:
        position = endladders[0]
        print("Jugador sube por escalera al cuadro:", position)
    if position == ladders[1]:
        position = endladders[1]
        print("Jugador sube por escalera al cuadro:", position)
    if position == ladders[2]:
        position = endladders[2]
        print("Jugador sube por escalera al cuadro:", position)
    if position == ladders[3]:
        position = endladders[3]
        print("Jugador sube por escalera al cuadro:", position)

    return position

#Se crea el metodo para verificar si la posicion corresponde a alguna serpiente y si es asi a donde baja
#Se imprime la posición correspondiente si cae en alguna serpiente
def ifsnakes(position):
    if position == snakes[0]:
        position = endsnakes[0]
        print("Jugador desciende al cuadro:", position)
    if position == snakes[1]:
        position = endsnakes[1]
        print("Jugador desciende al cuadro:", position)
    if position == snakes[2]:
        position = endsnakes[2]
        print("Jugador desciende al cuadro:", position)
    if position == snakes[3]:
        position = endsnakes[3]
        print("Jugador desciende al cuadro:", position)

    return position

#El loop se repite mientras la posicion sea menor a 25
while (position < 25):
    #Se randomiza el valor del dado en ese turno y se guarda en una variable
    dice = random.randint(1, 6)
    #Se imprime el valor del dado
    print("Dado arroja:", dice)
    position = dice + position
    #Para verificar si el jugador se salta x casillas se usa un if
    if position > 25:
        #Se guarda la posicion antes de tirar los dados en ese turno
        baseposition = position - dice
        #Se calcula el extra de casillas
        extras = position - 25
        print("Te saltaste:", extras, "cuadros")
        #La posicion vuelve a ser la misma desde antes de tirar los dados para que este solo pueda terminar el juego si obtiene 25 exactos
        position = baseposition
        print("Volviste a la posicion:", position)

    position = ifladders(position)
    position = ifsnakes(position)
    #Se imprime la posicion
    print("Jugador avanza a cuadro:", position)


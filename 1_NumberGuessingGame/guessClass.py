from random import randrange


class guessClass:
    def __init__(self, minimo, maximo):
        if (minimo < maximo):
            self.__minimo = minimo
            self.__maximo = maximo
        else:
            self.__minimo = maximo
            self.__maximo = minimo
        self.__aleatorio = randrange(self.__minimo, self.__maximo)

    def getMinimo(self):
        return self.__minimo

    def getMaximo(self):
        return self.__maximo

    # cuando funcione comentamos esto
    def getAleatorio(self):
        return self.__aleatorio

    def probarNumero(self, num):
        print("Juegas con el numero: ", num, type(num))
        print("Intentas acertar el numero: ",
              self.__aleatorio, type(self.__aleatorio))
        if (num < self.__aleatorio):
            print("Tu número esta por debajo")
            return False
        elif (num > self.__aleatorio):
            print("Tu número esta por encima")
            return False
        elif (num < self.__minimo or num > self.__maximo):
            # SI
            print("Te saliste de rango. Ese número no esta dentro de las posibilidades")
            return False
        elif (num == self.__aleatorio):
            print("Acertaste")
            return True
        elif (num > self.__aleatorio):
            print("Tu número esta por debajo")
            return False
        elif (num > self.__aleatorio):
            print("Tu número esta por encima")
            return False
        else:
            print("Patata")

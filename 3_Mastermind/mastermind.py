from random import randrange


class Mastermind:
    def __init__(self):
        self.__solucion = []
        for i in range(4):
            self.__solucion.append(randrange(0, 10))

    def getSolucion(self):
        return str(''.join(map(str, self.__solucion)))

    def testSolucion(self, num=0):
        listNum = [int(x) for x in str(num)]
        aciertos = 0
        aciertosDesordenados = 0
        if (num == 0):
            print(
                "Si introduces 0 o no introduces número lo considero como error. No continuare")
            return False
        elif (len(str(num)) != 4):
            print(
                "Debes de introducir un número de 4 cifras")
        for i in str(num):
            for j in self.__solucion:
                # print(f"i: {i} {type(i)} {listNum.index(int(i))}")
                # print(f"j: {j} {type(j)} {self.__solucion.index(j)}")

                if ((int(i) == int(j))):
                    if ((listNum.index(int(i)) == self.__solucion.index(j))):
                        # print(f"Coinciden en la posicion: posicion: {
                        #     self.__solucion.index(j)}")
                        aciertos += 1
                    else:
                        # print(f"Coinciden numeros en distintas posiciones {
                        #       listNum.index(int(i))} != {self.__solucion.index(j)}")
                        aciertosDesordenados += 1
        print(f"Has acertado en : {aciertos} en su posicion")
        print(f"Has acertado en : {
              aciertosDesordenados} pero no en su posicion")
        if (aciertos == 4):
            print("FELICIDADES, ACERTASTE TODO")
        else:
            print("Sigue probando")


print("Te estas equivocando al ejecutar el archivo main de python")

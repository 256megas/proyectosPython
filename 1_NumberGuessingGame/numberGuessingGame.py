# Most of the geeks from a CS (Computer Science) background, think of their very first project after doing a Programming Language. Here, you will get your very first project and the basic one, in this article.

# Task: Below are the steps:

#     Build a Number guessing game, in which the user selects a range.
#     Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
#     Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

from guessClass import guessClass

partida = guessClass(5, 50)
print("Minimo ", partida.getMinimo())
print("Maximo ", partida.getMaximo())
print("debe de adivinarse el ", partida.getAleatorio())
print(partida.probarNumero(10))

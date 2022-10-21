"""FIZZBUZZ

    La famosa serie FizzBuzz para un número natural N es una sucesión desde 1 hasta N donde:

    Los números que sean múltiplos de 3 se cambian por Fizz.
    Los números que sean múltiplos de 5 se cambian por Buzz.
    Los números que sean múltiplos de 3 y 5 se cambian por FizzBuzz.
    Si no cumple con ninguna de éstas condiciones imprimer el numero actual de la sucesión.

    Escriba un programa que lea N e imprima la serie FizzBuzz.

    N = 15
    1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
"""
def main():
    n = int(input('ingrese el numero: '))

    for i in range(1, n+1): # si coloco solo hasta n  no me toma n :p
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == "__main__":
    main()

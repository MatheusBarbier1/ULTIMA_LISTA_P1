"""
Escreva uma função que receba a base e a altura de um triangulo e retorne sua area 
"""


def main():
    altura = float(input("Qual a altura do triangulo? "))
    base = float(input("Qual a base do triangulo? "))
    print(calcula_area_triangulo(altura, base))


def calcula_area_triangulo(altura, base):
    area = (altura * base) / 2
    return area


main()
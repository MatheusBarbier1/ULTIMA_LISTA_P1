lado1 = float(input("Qual o primeiro lado? "))
lado2 = float(input("Qual o segundo lado? "))
lado3 =float(input("Qual o terceiro lado? "))

if lado1 > (lado2 - lado3) and lado1 < (lado2 + lado3):
    print("É um triangulo")

elif lado2 > (lado1 - lado3) and lado2 < (lado1 + lado3):
    print("É um triangulo")

elif lado3 > (lado1 - lado2) and lado3 < (lado1 + lado2):
    print("É um triangulo")

else:
    print("Não é um triangulo")
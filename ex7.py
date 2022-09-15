
nota = -1


while nota > 10 or nota < 0:
    nota = float(input("Qual a nota? "))
    if nota > 10 or nota < 0:
        print("Nota inválida! ")


print("Sua nota é:", nota)


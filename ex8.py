
pais_a = 80000
taxa_crescimento_a = 0.03
pais_b = 200000
taxa_crescimento_b = 0.015
ano = 2022


while pais_a < pais_b :
    pais_a += int((taxa_crescimento_a * pais_a))
    pais_b += int((taxa_crescimento_b * pais_b))
    ano += 1


print(ano, pais_a, pais_b)
# FOLHA DE PAGAMENTO
salario_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalhou? "))
salario_bruto = horas_trabalhadas * salario_hora
Imposto_renda = 0
sindicato = salario_bruto * 0.03


if salario_bruto < 0:
    print("Salário inválido!")

elif salario_bruto <= 900:
    Imposto_renda = salario_bruto * 0
    salario_liquido = salario_bruto - (Imposto_renda + sindicato)
    fgts = salario_bruto * 0.11

elif salario_bruto <= 1500:
    Imposto_renda = salario_bruto * 0.05
    salario_liquido = salario_bruto - (Imposto_renda + sindicato)
    fgts = salario_bruto * 0.11

elif salario_bruto <= 2500:
    Imposto_renda = salario_bruto * 0.1
    salario_liquido = salario_bruto - (Imposto_renda + sindicato)
    fgts = salario_bruto * 0.11

elif salario_bruto > 2500:
    Imposto_renda = salario_bruto * 0.2
    salario_liquido = salario_bruto - (Imposto_renda + sindicato)
    fgts = salario_bruto * 0.11

print("Seu FGTS é:", fgts)
print("Seu salario líquido é:", salario_liquido)

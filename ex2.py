
def main():
    print("O seu resultado é:", result(pergunta_n()))


def pergunta_n():
    n = int(input("Qual o valor de n? "))
    while n <= 0:
        print("O seu valor de 'n' nao pode ser menor ou igual a 0")
        n = int(input("Qual o valor de n? "))
    return n


def result(n):
    cont = 2
    m = 3
    vlr = 0
    
    while cont <= n:
        vlr += cont / m
        print("{:.2f} = {} / {}".format(vlr, cont, m))
        cont += 1
        m += 2

    return vlr


main()
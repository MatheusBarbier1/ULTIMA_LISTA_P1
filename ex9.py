fibonacci = 0
fibonacci2 = 0
fibonacci_final = 1
cont = 1

while fibonacci_final <= 500:
    if cont % 2 != 0:
        fibonacci_final += fibonacci
        fibonacci = fibonacci_final
    elif cont % 2 == 0:
        fibonacci_final += fibonacci2
        fibonacci2 = fibonacci_final
    cont += 1
    print(fibonacci_final)
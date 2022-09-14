
letra = input("Qual a letra? ")
letra = letra.upper().strip()

def acha_vogal_consoante(letra):
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("Sua letra é uma vogal!")


    else:
        print("Sua letra é uma consoante!")

acha_vogal_consoante(letra)
peso = input("Digite o peso: ")

def calcularMulta(peso):
    peso = float(peso)
    if peso > 50:
        multa = 4*(peso - 50)
    else:
        multa = 0
    return multa

print("O valor da multa e de: R$%.2f"%calcularMulta(peso))

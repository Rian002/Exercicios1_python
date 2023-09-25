altura =  input ("Digite sua altura: ")

def calculaPesoHomem(altura):
    peso_ideal = (72.7*float(altura)-58)
    return peso_ideal

def calculaPesoMulher(altura):
    peso_ideal = (62.1*float(altura)-44.7)
    return peso_ideal

print(f"a. Para homens: {calculaPesoHomem(altura)}")
print(f"b. Para mulheres: {calculaPesoMulher(altura)}")

altura =  input ("Digite sua altura: ")

def calculaPeso(altura):
    peso_ideal = (72.7*float(altura)-58)
    return peso_ideal

print (calculaPeso(altura))

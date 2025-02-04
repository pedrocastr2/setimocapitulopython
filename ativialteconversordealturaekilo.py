def convert_em2metr(centimetros): #converte centimetros em metros 
    return centimetros/100

def convert_2kilo(gramas): # converte gramas em kilos
  return gramas/100


centimetros = int(input("Digite sua altura em centimetros: "))
gramas =int(input("digite seu peso em gramas: " ))

metros = convert_em2metr(centimetros)
kilos=convert_2kilo(gramas)

print("-------------------------------------------------------------------------------------")
print("Sua altura em centimetros é ", centimetros,"Seu peso é ", gramas )
print("Sua altura em metros é ",metros, "Seu peso em kilos ", kilos)
print("-------------------------------------------------------------------------------------")
def convert_em2cm(polegadas):
    return polegadas *2.4

def convert_lb2kg(libras):
  return libras / 2.2

altura_pl = int(input("Digite sua altura em polegadas: ")) 
peso_ln = int(input("Digite seu peso em libras: "))

altura_cm = convert_em2cm(altura_pl)
peso_kg = convert_lb2kg(peso_ln)

ping_pong_altura = round(altura_cm /4)
ping_pong_peso = round(peso_kg *1000/2.7)

pes = altura_pl // 12
polegadas = altura_pl %12

print("-------------------------------------------------------------------------------------")
print("Você tem ",pes,"pés,",polegadas,"polegadas de altura, e ", altura_pl,"libras.")
print("Você mede",ping_pong_altura," bolas de ping-pong de altura")
print("Você pesa o mesmo que ",ping_pong_peso ,"bolas de ping-pong")    
print("-------------------------------------------------------------------------------------")
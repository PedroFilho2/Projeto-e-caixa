numero = int(input("valor para sacar: "))

duzentos =int(numero /200)
numero = numero % 200

cem =int(numero / 100)
numero = numero % 100

cinquenta =int( numero /50)
numero = numero % 50

vinte =int( numero /20)
numero = numero % 20

dez =int(numero /10 )
numero = numero % 10

cinco =int(numero /5)
numero = numero % 5
um=numero

print("notas R$ 200,00 = ", duzentos)
print("notas R$ 100,00 = ", cem )
print("notas R$ 50,00 = ", cinquenta)
print("notas R$ 20,00 = ", vinte)
print("notas R$ 10,00 = " , dez)
print("notas R$ 5,00 = " , cinco)
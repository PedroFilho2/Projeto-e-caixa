# Criar uma função
def imprimir(texto):
    print(texto)
def media(n1=0,n2=0,n3=0):
    media=(n1+n2+n3)/3
    print(media)

imprimir("cesar")
media(8,9,10)

def calculaIMC(peso,altura):
    imc = peso /(altura* altura)
    imprimir(imc)
    if(imc < 18.5):
        imprimir("abaixo de peso")
    elif(imc > 18.8 and imc < 24.99):
        imprimir("peso normal")
    elif(imc > 25 and imc < 29.99):
        imprimir("sobrepeso")
    else:
        imprimir("obesidade")



calculaIMC(55,1.55)
imprimir("Pedro do Carmo")

def diasvividos(ano_nascimento):
    ano_atual = 2024
    dias = (ano_atual - ano_nascimento) * 365
    horas = dias * 24
    minutos= horas * 60
    segundos = minutos * 60
    imprimir(dias)
    imprimir(horas)
    imprimir(minutos)
    imprimir(segundos)
diasvividos(2008)
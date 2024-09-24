import random

palavras=["Arthur" ,"Mouse" ," são paulo", "cadeira" , "carro" ,"ze raimundo" , "computador" , "php" , "javascript"]
palavraEscolhida = random.choice(palavras)

letraEscolhida = ["_"] * len(palavraEscolhida)
quantidadeErros = len(palavraEscolhida) - 1
meusErros = 0 

print("A palavra sorteada tem " + str(len (palavraEscolhida))+ " letras")



while "_" in letraEscolhida and meusErros < quantidadeErros:
   print("Palavra:" + " ".join(letraEscolhida))
   letraInformada = input("INFORME UMA LETRA: ").lower()
   if letraInformada in palavraEscolhida:
      for i in range(len(palavraEscolhida)):
         if palavraEscolhida[i] == letraInformada:
            letraEscolhida[i] = letraInformada 
   else:
      meusErros +=1
      print("ERRRRRRREOU....")











# while erros < erro:  
#     for letra in palavraEscolhida:
#      if(l == letra):
#         print("A letra " + str(l) + " estar na posicao " + str (palavraEscolhida.index(l)+1))
#      else:
#         erros += 1

print(palavraEscolhida)
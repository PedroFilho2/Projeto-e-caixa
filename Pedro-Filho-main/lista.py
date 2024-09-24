# Nomes = ["Raul", "Gaby", "Arthur", "Bruno" ,"Guilerme"]
# idade = ["10" , "11" ,"12" ,"13" , "14"]
# print(Nomes[2] + " tem idade de " + idade[2])
# Nome = "infomática"
# Notas = [5,9,8,4, 5.5]
# print(len(Nomes))
# print(len(idade))
# print(len(Nome))

# Notas.sort()
# Nomes.sort()
# Nomes.reverse()

# print(Nomes)
# print(max(Notas))
# print(min(Notas))
# Nomes=[]
# print(Nomes)

# for x in range (4):
#     Nome = input ("informe um nome:")
#     Nomes.append(Nome)
# Nomes.sort()
# print(Nomes)

# aluno=["pedro", "joão", "chico", "maria", "paulo"]
# notas=[[8,6,7], [4,6,9], [8,9,10], [2,10,10],[6,7,4]]

# print(sum(notas[1])/len(notas[1]))
for x  in range (5):
    aluno=input("informe o nome do aluno")
    N1=int(input("informe o nome 1 do aluno"))
    N2=int(input("informe o nome 2 do aluno"))
    N3=int(input("informe o nome 3 do aluno"))
MEDIA= (N1+N2+N3)/3
print(MEDIA)
if MEDIA <6:
    print("O ALUNO" +aluno+ "ESTÁ REPROVADO")
if MEDIA >6:
     print("O ALUNO" +aluno+ "ESTÁ REPROVADO")
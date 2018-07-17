matricula=input("Digite sua matricula! : ")
nota1=float(input("Insira a nota da prova: "))
nota2=float(input("Insira a nota do trabalho: "))

media=(nota1+nota2)/2

if(media >= 6):
    print("Aprovado!!!")

else:
    print("Reprovado!!!")


print("A media é: ", media)


nome=input("Informe seu nome: ")
diaria=int(input("Quantos dias você ficou? "))

conta = diaria * 60

if diaria > 15:
    taxa = diaria * 5.5
elif diaria == 15:
   taxa = diaria * 6   
else:
    taxa = diaria * 8

conta = (diaria * 60) + taxa

print(nome, "Total da conta", conta)

    

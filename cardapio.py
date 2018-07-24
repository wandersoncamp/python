print("### TABELA DE PREÇOS ###")
print("100 - HOT DOG")
print("101 - BAURU SIMPLES")
print("102 - BAURO COM OVO")
print("103 - HAMBURGER")
print("104 - CHEESEBURGUER")
print("105 - REFRIGERANTE")


cod=int(input("Insira o código do lanche: "))
quant=int(input("Quantos lanches? "))


if cod == 100:
    print("valor total", quant * 1.1)
elif cod == 101:
    print("valor total", quant * 1.3)
elif cod == 102:
    print("valor total", quant * 1.5)
elif cod == 103:
    print("valor total", quant * 1.1)
elif cod == 104:
    print("valor total", quant * 1.3)
elif cod == 105:
    print("valor total", quant * 1.0)
    

    
    


print("#  Digite o código de acordo com o cargo #")
print("101 para Gerente")
print("102 para Engenheiro")
print("103 para Técnico")

salario=float(input("Informe o salario: "))
cargo=int(input("Informe o cargo: "))


if cargo == 101:
    print("Seu sálario é", salario+(salario*10/100)) 
elif cargo == 102:
    print("Seu salário é", salario +(salario*20/100))
elif cargo == 103:
    print("Seu salário é", salario +(salario*30/100))
else:
    print("Seu salário é", salario+(salario*40/100))

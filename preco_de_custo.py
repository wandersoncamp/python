pc=float(input("Informe o preço de custo do produto: "))
pv=float(input("informe o valor de venda do produto: "))

if pc < pv:
    print("Lucro!!")
elif pc > pv:
    print("Prejuizo :(")
elif pc == pv:
    print("Empate!")

print("O lucro foi ", pv - pc)

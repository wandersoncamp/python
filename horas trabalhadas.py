ht=int(input("Informe as horas trabalhadas no mês: "))
vh=int(input("Valor da hora trabalhada :" ))
pd=int(input("percentual de desconto: "))



sb=ht*vh
td=(pd/100)*sb
sl=sb-td

print("Total de horas trabalhadas:",ht,  "Salário bruto:",sb , "Total de descontos:",td , "Salário liquido:",sl)

ano=int(input("Qual o ano do carro? "))
valor=float(input("Qual o valor do carro? "))


if ano == 2018:
    desc = ((valor*15)/100)
    print("O valor do carro é", valor,", e com desconto é", valor-desc)


elif ano > 2010:
    desc = ((valor*10)/100)
    print("O valor do carro é", valor,", e com desconto é", valor-desc)


elif ano <= 2010:
    desc = ((valor*5)/100)
    print("O valor do carro é", valor,", e com o desconto é ", valor-desc )

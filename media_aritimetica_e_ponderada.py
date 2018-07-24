media=input("Digite 1 para media aritimetica ou 2 para ponderada: ")
n1=float(input("Informe a primeira nota: "))
n2=float(input("Informe a segunda nota: "))
n3=float(input("Informe a terceira nota: "))
       
if media == "1":
       print("A media é", (n1 + n2 + n3) /3)
elif media == "2":
       print("A media é", (n1 * 3 + n2 * 3 + n3 * 4) /10)

n=int(input("Digite um valor inteiro: "))

fat = n

for x in range(2,n):
    fat=fat*x
print("Fatorial de ", n, " = ", fat)

nota=int(input("Informe a nota: "))

if nota >= 0 and nota <= 49:
         print("Insuficiente")
elif nota >= 50 and nota <= 64:
         print("Regular")
elif nota >= 65 and nota <= 84:
        print("Bom")
elif nota >= 85 and nota <= 100:
         print("Ótimo")
else:
    print("Valor invalido")


n1=int(input("Informe o primeiro numero: "))
operador=(input("Informe um operador! +, -, *, / : "))
n2=int(input("Informe o segundo numero: "))

if operador == '+' :
    print("A soma é ", n1+n2)
elif operador == '*' :
    print("A mutiplicação é ", n1*n2)
elif operador == '-' :
    print("A subtração é ", n1-n2)
elif operador == '/' :
    print("A divisão é ", n1/n2)

diaria=int(input('Quantos dias você ficou com o carro? '))
km=float(input('Quantos KM você rodou com o carro? '))

pago = (diaria * 60) + (km * 0.15)
print('total a pagar é de R$: ',pago)

#Convertedor de temperatura
print('Olá, esse é o nosso medidor de temperatura')
cel = float(input('Insira a temperatura em Celsius: ºC '))
c = cel * 9 
c2 = 5 *32
c3 = 5 - c2
c4 = c + c2
c5 = c4 / 5
print('A temperatuda de {}ºC em Fahrenheit é {}ºF'.format(cel, c5))

#Aluguel de carros
print('Olá, hora da devolução... Preencha as informações abaixo para realizar o pagamento')
dias = int(input('Diga quantos dias você ficou com o carro: '))
Km = float(input('Diga quantos quilômetros você percorreu: '))
pago = (dias * 60) + (Km * 0.15)
print('Você percorreu {} Km por {} dias, o total a se pagar é R$ {:.2f}'.format(Km, dias, pago))
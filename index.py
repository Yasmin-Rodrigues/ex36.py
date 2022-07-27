peso =float(input('Qual o seu peso?:'))
altura =float(input('Qual a sua altura?:'))
imc = peso / (altura * altura)
print('Seu IMC é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc == 18.5 or imc < 25:
    print('Peso ideal')
elif imc == 25 or imc < 30:
    print('Acima do peso')
else:
    print('Obesidade mórbida')
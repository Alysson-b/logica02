numero = float(input('Insira o numero a ser verificado.'))

if numero > 0:
    print(f'O número {numero:.2f} é maior que zero, entao ele é positivo')
elif numero < 0:
    print(f'O número {numero:.2f} é menor que zero, então ele é negativo')
else:
    print(f'O número {numero:.2f} é zero')

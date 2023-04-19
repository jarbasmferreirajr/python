print()
title = 'EXEMPLOS DA AULA 07'
print(title)
print()
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
divi = n1 / n2
di = n1 // n2
rst = n1 % n2
expo = n1 ** n2
print(' A soma é {},\n a subtração é {},\n o produto é {}\n e a divisão é {:.3f} '.format(soma, subt, mult, divi), end='| >>> ')
print('A divisão inteira é {} e o resto {},\n a exponenciação é {}'.format(di, rst, expo))
print()
print('FIM')

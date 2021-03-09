# 4 tipos primitivos mais comum são:
# int(inteiros), float(reais ou pontos flutuante),
# bool(valores lógicos ou boleanos) e str(valores caracteres ou strings)
#int - 7 -4 0 9875
#float - 4.5 0.076 -15.223 7.0
#bool - True False (primeira letra maiscula)
#str - 'Olá' '7.5' ''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2

#print('A soma vale', s)

print('A soma vale {}'.format(s))

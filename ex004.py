#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

x = input('Digite algo: ')
print('O tipo primitivo desse caracter é ', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabetico?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está em maiúsculas?', x.isupper())
print('Esta em minusculas?', x.islower())
print('Esta capitalizada?', x.istitle())

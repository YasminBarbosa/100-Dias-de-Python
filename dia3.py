#Crie um programa que calcule e exiba a média aritmética de três notas inseridas pelo usuário.

nota1 = int(input('Insira a 1° nota: '))
nota2 = int(input('Insira a 2° nota: '))
nota3 = int(input('Insira a 3° nota: '))

media = (nota1 + nota2 + nota3) / 3

print('A média da nota do aluna é: ', int(media))
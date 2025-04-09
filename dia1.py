#Escreva um programa que solicite ao usuário dois números e exiba a adição, 
# subtração, multiplicação e divisão entre eles

num1 = int(input('Insira um 1° número: '))
num2 = int(input('Insira um 2° número: '))

adicao = (num1 + num2)
subtracao = (num1 - num2)
multiplicacao = (num1 * num2)
divisao = (num1 / num2)

print('Os calculos da adição é: ', adicao,
      'Substração: ', subtracao, 
      'Multiplicacao: ', multiplicacao,
      'Divisão: ', divisao,  )
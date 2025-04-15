#Crie um programa que calcule e exiba o perímetro de um círculo, solicitando ao usuário o raio.

import math

raio = float(input("Insira o raio do circulo: "))

perimetro = 2 * math.pi * raio

print('O valor do perímetro é: ', round(perimetro,2))
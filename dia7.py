#7. Escreva um programa que calcule a área de um círculo a partir do raio, usando a fórmula A = πr²
 
import math

raio = float(input("Insira o tamanho do raoio em Cm: "))


CalculoArea = (round(math.pi, 2) * (raio ** raio))


print("O resultado do cálculo da área em cm² é: ", round(CalculoArea))


#REVISAR CÓDIGO

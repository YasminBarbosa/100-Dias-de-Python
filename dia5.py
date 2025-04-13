#Escreva um programa que calcule o IMC de um indivíduo, utilizando a fórmula IMC = peso/altura²

altura = float(input("Insira sua altura: "))
peso = float(input("Insira o seu peso: "))

imc = (peso / (altura**2))

format(imc)
print(f"O cálculo do seu IMC é: ", round(imc,2))


# Programa digite o nome do funcionário o salário dele e imprima o nome e o salário reajustado em 10%.

funcionario = str(input("Digite o nome do funcionário: ")) # Entrada nome do funcionário

salario = float(input("Digite o salário do funcionário: ")) # Entrada salário do funcionário

salarioReajustado = salario * 1.10

print ('O salário do funcionário ' + str(funcionario) + ' é de R$ ' + str(salarioReajustado) + '.')
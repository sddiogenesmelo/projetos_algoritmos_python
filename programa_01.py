# Programa digite o nome, sexo, endereço, ano de nascimento. calcule a idade e imprima os valores.

print ('Olá Mundo!')

name = input('Qual é o seu nome? ') # Entrada nome
print ('Olá ' + name + ' !')

sexo = input('Qual é o seu sexo? ') # Entrada sexo

endereco = input('Qual é o seu endereço? ') # Entrada endereço

anoNascimento = input('Qual é o seu ano de nascimento? ') # Entrada ano em que nasceu

idade = 2026 - int(anoNascimento)

print ('Olá ' + str(name) + '! Você tem ' + str(idade) + ' anos, ' + str(sexo) + ' e mora em ' + str(endereco) + '.')
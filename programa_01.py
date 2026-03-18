print ('Olá Mundo!')

name = input('Qual é o seu nome? ')
print ('Olá ' + name + '!')

sexo = input('Qual é o seu sexo? ')

endereco = input('Qual é o seu endereço? ')

anoNascimento = input('Qual é o seu ano de nascimento? ')

idade = 2026 - int(anoNascimento)

print ('Olá ' + name + '! Você tem ' + idade + ' anos, ' + sexo + ' e mora em ' + endereco + '.')
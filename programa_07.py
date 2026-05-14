# Aula Python 14/05/2026
# Verificar idade se está apto para votar 

idade = int (input("Digite a sua idade: "))

if idade <= 15:
    print ("Você não pode votar.")
elif idade >= 16 and idade <= 70:
    print ("Você pode votar.")
else: 
    print ("Seu voto é opcional!")
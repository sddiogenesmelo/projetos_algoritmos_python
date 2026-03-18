# Faça um programa que calcule a idade do usuário (nome digitado) e se tiver menos de 16 anos não poderá votar, 
# so pode votar entre 17 e 70 anos e opção de voto com maior de 70 anos.

print("Olá seja bem vindo!")

nome = str(input("\nDigite seu nome:")) # Entrada do nome
idade = int(input("\nDigite sua idade:")) # Entrada da idade

if (idade <= 16):
    print (nome + " você não atingiu a idade para votar!") #Estrutura condicional se idade menor ou igual: Não vota

else:
    if (idade >= 71):
        print(nome + " seu voto é opcional.")# Estrutura condicional se idade maior que: Seu voto é opcional
    else:
        print("\nBem feito " + nome + " kkk, se fu*** você vai votar e ainda vai trabalhar como mesário.")
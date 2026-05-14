def soma (x, y):
    return x + y

def sub (x, y):
    return x - y

def mult (x, y):
    return x * y

def div (x, y):
    return x / y

x = float(input(f"\nDigite o primeiro valor: "))

y = float(input(f"\nDigite o segundo valor: "))

resultadoSoma = soma (x,y)
resultadoSub = sub (x, y)
resultadoDiv = div (x, y)
resultadoMult = mult (x, y)

print(f"\nSoma: {resultadoSoma}")
print(f"\nSubtração: {resultadoSub}")
print(f"\nMultiplicação: {resultadoMult}")
print(f"\nDivisão: {resultadoDiv}")
array=[13, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

numero = int(input('Digite um número: '))
resposta = ""
for alg in array:
  if numero in array:
    resposta=" Esta no array"
  else: 
    resposta=" Não esta no array"

print(str(numero)+resposta)
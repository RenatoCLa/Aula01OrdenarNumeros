resultado = []
desordenado = []

arquivo5000 = open('5000.txt', 'r')
conteudo = arquivo5000.read()
for line in conteudo:
    if line != '\n':
        desordenado.append(line)

print(desordenado)
print()

#Enquanto desordenado não estiver vazio
while len(desordenado) > 0:
  #cria uma variavel vazia chamada menor valor
  menor_valor = None
  #checa todos os numeros restantes
  for x in desordenado:
    #se não tiver um menor valor (ou seja, é o inicio de um novo loop) o primeiro numero será o menor valor
    if menor_valor is None:
      #menor valor é igual ao valor atual
      menor_valor = x
    #se a variavel menor valor não estiver vazia, compare ela com o numero atual
    #se o numero atual for menor, substitua a variavel
    elif menor_valor > x:
      menor_valor = x
  #remove o menor valor da lista de numeros
  desordenado.remove(menor_valor)
  #coloca esse valor na lista de numeros ordenada
  resultado.append(menor_valor)
  #limpa a variavel menor valor para ser utilizada no proximo número
  menor_valor = None

print(resultado)
input()

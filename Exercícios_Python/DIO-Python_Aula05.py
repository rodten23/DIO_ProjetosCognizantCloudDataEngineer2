# Listas podem misturar tipos de dados, mas  ideal é separa uma lista para cada tipo. Lista usam [].

lista = [1, 3, 5, 7, 2, 4, 9, 8]
lista_animal = ['cachorro',  'lobo', 'tartaruga', 'baleia', 'arara', 'tucano']

print('Animal na segunda posição:  ' + lista_animal[1])
print('*' * 45)

for ani in lista_animal:
      print(ani)
print('*' * 45)

soma = 0
for x in lista:
      print(x)
      soma += x
print('A soma de todos os valores é:  {}'.format(soma))
# Esse comando abaixo (sum) é um exemplo de porque não juntar vários tipos de dados numa lista.
# Nesse exemplo, se tivesse uma string, a soma não seria executada.
print('A soma de todos os valores é:  {}'.format( sum(lista)))
print('*' * 45)

print ('O maior valor da lista é:  {}.\nE o menor valor da lista é:  {}.\nIndependente das suas posições.'.format(max(lista), min(lista)))
print('*' * 45)

print ('O maior valor da lista_animal é:  {}.\nE o menor valor da lista_animal é:  {}.\nSendo maior e menor baseados na ordem alfabética '
       'e independente das suas posições.'.format(max(lista_animal), min(lista_animal)))
print('*' * 45)

if 'puma' in lista_animal:
      print('Já existe puma na listagem de animais.')
else:
      print('Puma ainda não está na listagem de animais. Estamos incluindo para você.')
      lista_animal.append('puma')
      print(lista_animal)
# Acima, consultou puma e, como não tinha, ele foi incluído como último da lista.

# Abaixo, o pop excluiu a baleia (posição 3). Sem indicar posição, pop excluirá o último da pilha.
lista_animal.pop(3)
print(lista_animal)
print('*' * 45)

# Já o remove exclui o nome que foi informado.
lista_animal.remove('tartaruga')
print(lista_animal)
print('*' * 45)

nova_lista = lista * 2
nova_lista_animal = lista_animal * 3
print(nova_lista)
print(nova_lista_animal)

# O sort ordena as listas.
nova_lista.sort()
nova_lista_animal.sort()
print(nova_lista)
print(nova_lista_animal)

# O reverse, inverte as listas.
nova_lista.reverse()
nova_lista_animal.reverse()
print(nova_lista)
print(nova_lista_animal)
print('*' * 45)

# Listas podem ter seus itens alterados, basta indicar o índice e o novo valor.
nova_lista[1] = 45
nova_lista_animal[0] = 'jararaca'
print(nova_lista)
print(nova_lista_animal)
print('*' * 45)

# Tuplas são um tipo de  listagem  que é imutável e usa ().

tupla = (1, 3, 9, 15, 23)
print(tupla)
print(tupla[2])
print('*' * 45)
# tupla[1] = 6  Isso aqui dá erro, pois tuplas não podem ser alteradas. Isso é uma desvantagem, mas pode ser um
# vantagem em outras situações.

# Len dá o total de elementos na lista ou tupla.
print('Quantos elementos tem na tupla?:  {}.\nQuantos elementos tem na lista?:  {}.\nQuantos elementos tem na nova_lista?:  {}.'
      '\nQuantos elementos tem na lista_animal?:  {}.\nQuantos elementos tem na nova_lista_animal?:  {}.'
      .format(len(tupla), len(lista), len(nova_lista), len(lista_animal), len(nova_lista_animal)))
print('*' * 45)

# Comandos tuple e list convertem listagens.
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print('Lista_animal transformada em tupla:  {}'.format(tupla_animal))

lista_da_tupla = list(tupla)
print(type(lista_da_tupla))
print('Tupla transfomada em lista:  {}'.format(lista_da_tupla))

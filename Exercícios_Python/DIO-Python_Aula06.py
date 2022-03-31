# Conjuntos (tipo set) são um tipo de listagem que não lida com  duplicidade, então ele só considera uma vez cada
# elemento, mesmo que este esteja repetido.

conjunto = {1, 2, 3 ,4, 3, 1}
print(type(conjunto))
print(conjunto)
print('*' * 45)

conjunto.add(5)
conjunto.discard(1)
print('Conjunto depois de add 5 e discard 1:  {}'.format(conjunto))
print('*' * 45)

conjunto_A = {1, 2, 3 , 4, 5}
conjunto_B = {5, 6, 7, 8, 9}
print('Conjunto_A:  {}   e   Conjunto_B:  {}'.format(conjunto_A, conjunto_B))
conjunto_uniao = conjunto_A.union(conjunto_B)
print('Conjunto_uniao depois de unir cojunto_A com conjunto_B: {} . Sendo desconsiderada repetição do 5.'.format(conjunto_uniao))
conjunto_interseccao = conjunto_A.intersection(conjunto_B)
print('Intersecção entre os conjuntos A e B: {}'.format(conjunto_interseccao))
conjunto_diferenca_A = conjunto_A.difference(conjunto_B)
print('Diferença (itens que só tem) no conjunto_A para o conjunto_B: {}'.format(conjunto_diferenca_A))
conjunto_diferenca_B = conjunto_B.difference(conjunto_A)
print('E aqui, a diferença (itens que só tem) no conjunto_B para o conjunto_A: {}'.format(conjunto_diferenca_B))
conjunto_diferenca_simetrica = conjunto_A.symmetric_difference(conjunto_B)
print('Já a diferença simétrica é juntar as diferenças de um conjunto para o outro: {}'.format(conjunto_diferenca_simetrica))
print('*' * 45)

conjunto_C = {'j', 'k', 'l', 'm'}
print('conjunto_C:  {}'.format(conjunto_C))
conjunto_D = {'j', 'k', 'l', 'm', 'n', 'o', 'p'}
print('conjunto_D:  {}'.format(conjunto_D))
conjunto_subset_CD = conjunto_C.issubset(conjunto_D)
conjunto_subset_DC = conjunto_D.issubset(conjunto_C)
conjunto_superset_CD = conjunto_C.issuperset(conjunto_D)
conjunto_superset_DC = conjunto_D.issuperset(conjunto_C)
print('Conjunto_C é um sub-conjunto (subset) de conjunto_D?  {}'.format(conjunto_subset_CD))
print('E agora, conjunto_D é um sub-conjunto (subset) de conjunto_C?  {}'.format(conjunto_subset_DC))
print('Já o conjunto_C é um super-conjunto (superset) de conjunto_D?  {}'.format(conjunto_superset_CD))
print('Por fim, conjunto_D é um super-conjunto (superset) de conjunto_C?  {}'.format(conjunto_superset_DC))
print('*' * 45)

# Abaixo, convertendo lista em conjunto, assim eliminamos as duplicidades.
lista = ['coelho', 'tigre', 'lebre', 'lebre', 'tigre', 'elefante']
print('Essa é a lista original:  {}'.format(lista))
conjunto_animais = set(lista)
print('Esse é o conjunto gerado a partir da lista original:  {}'.format(conjunto_animais))
lista_corrigida = list(conjunto_animais)
print('E essa é a lista final corrigida (sem duplicidades), gerado a partir do conjunto_animais:  {}'.format(lista_corrigida))

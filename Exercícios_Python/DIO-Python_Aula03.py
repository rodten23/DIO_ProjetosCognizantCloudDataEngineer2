# Primeira versão, mas errada, pois se for digitado errado duas vezes (notas maior que 10) programa continua.
# a = int(input('Digite a nota do primeiro bimestre: '))
# if a > 10:
#     a = int(input('Você digitou errado. Qual a nota do primeiro bimestre: '))
# b = int(input('Agora digite a nota do segundo bimestre: '))
# if b > 10:
#     b = int(input('Você digitou errado. Digite a nota do segundo bimestre: '))
# c = int(input('Agora é a vez da nota do terceiro bimestre: '))
# if c > 10:
#     c = int(input('Você digitou errado. Insira a nota do terceiro bimestre: '))
# d = int(input('Por fim, digite a nota do quarto bimestre: '))
# if d > 10:
#     d = int(input('Você digitou errado. Pode digitar agora a nota do quarto bimestre: '))
# media = ( a + b + c + d) / 4
# print('Média do aluno: {}'.format(media))

# Segunda versão, agora corrigida usando while.
# Também apliquei o sys.exit() para poder encerrar programa.
import sys

a = int(input('Digite a nota do PRIMEIRO bimestre:  '))
while a > 10:
    print('Você digitou errado.')
    a = input('Digite a nota do PRIMEIRO bimestre ou digite x para encerrar o programa:  ')
    if a == 'x':
          sys.exit()
    else:
          a = int(a)

b = int(input('Agora digite a nota do SEGUNDO bimestre:  '))
while b > 10:
    print('Você digitou errado.')
    b = input('Digite a nota do SEGUNDO bimestre ou digite x para encerrar o programa:  ')
    if b == 'x':
         sys.exit()
    else:
        b = int(b)

c = int(input('Agora é a vez da nota do TERCEIRO bimestre:  '))
while c > 10:
      print('Você digitou errado.')
      c = input('Digite a nota do TERCEIRO bimestre ou digite x para encerrar o programa:  ')
      if c == 'x':
            sys.exit()
      else:
            c = int(c)

d = int(input('Por fim, digite a nota do QUARTO bimestre:  '))
while d > 10:
      print('Você digitou errado.')
      d= input('Digite a nota do QUARTO bimestre ou digite x para encerrar o programa:  ')
      if d == 'x':
          sys.exit()
      else:
           d = int(d)

# if a != 'x' and b != 'x' and c != 'x' and d != 'x':
media = ( a + b + c + d) / 4
print('-' * 80)
print('Média do aluno: {}'.format(media))
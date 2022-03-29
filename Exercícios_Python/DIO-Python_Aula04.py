# # Aqui fiz o range de "1 até 101", porque se coloca só "100" ele vai de 0 a 99 e, se colacamos "1, 100" ele vai de 1 até 99.
# for x in range(1, 101):
#     print(x)

# a = int(input('Insira um número para descobrirmos se ele é primo ou não: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('O número {} é primo.'.format(a))
# else:
#     print('O número {} não é primo.'.format(a))

# a = int(input('Digite o número limite para analizarmos: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1,  num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print('{} é um número primo.'.format(num))

inicial = 0
while inicial <= 10:
    print(inicial)
    inicial += 1
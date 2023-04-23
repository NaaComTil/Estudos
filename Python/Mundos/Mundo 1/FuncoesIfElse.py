#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo <=3:
#    print('O Carro está novo!')
#else:
#    print('O Carro é velho!')

#print('---Versão SIMPLIFICADA---')
#ou
#print('O Carro está novo!' if tempo<=3 else 'O Carro está velho!')
#print('---FIM---')

#nome = str(input('Qual é seu nome? '))
#if nome == 'Itanaã':
#    print('Que nome lindo você tem!')
#print('Bom dia, {}!'.format(nome))

import random
numpe = random.randint(0,5)
print('Advinhe o número que a máquina pensou, de 0 a 5!')
numad = int(input('Digite sua resposta: '))
print(f"""O número pensado foi {numpe}
A sua resposta foi {numad}""")
if numad == numpe:
    print('Você advinhou o número!')
else:
    print('Você errou!')

print('---------------------------------------------------')

velo = float(input('Qual a velocidade do carro em Km? '))
if velo > 80:
    print(f'O carro foi multado com R${((velo-80)*700)/100:.2f}!')
    print(f'O valor da multa é {((velo-80)*700):.2f} / 100!')
else:
    print('O carro não foi multado.')

print('---------------------------------------------------')

print('O número é par ou impar?')
num = int(input('Digite um número: '))
print(f'{num} % 2 sobra {num%2}! Então...')
if num % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é impar!')

print('---------------------------------------------------')

print('Pegue o ônibus!')
km = int(input('Qual distancia em Km? '))
if km < 200:
    print(f"""Você irá andar {km}kms, e o preço por cada Km abaixo de 200kms é R$0.50,
    logo {km}*0.50 dá R${0.50*km}!""")
else:
    print(f"""Você irá andar {km}kms, e o preço por cada Km acima de 200kms é R$0.45,
    logo {km}*0.45 dá R${0.45*km}!""".format(km,km,0.45*km))

print('---------------------------------------------------')

print('O ano é bissexto?')
ano = int(input('Digite um ano: '))
print(f'O ano {ano} % 4 é igual a {ano/4}, então...'.format(ano,ano/4))
if ano % 4 == 0:
    print(f'O ano {ano} é um ano bissexto.')
else:
    print(f'O ano {ano} não é um ano bissexto.')

print('---------------------------------------------------')

num1 = menor = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite outro outro valor: '))
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
maior = num1
if num2>num1 and num2>num3:
    maior= num2
if num3>num1 and num3>num2:
    maior = num3
print(f"""0 maior valor digitado é: {maior} 
O menor valor digitado é: {menor}""")

print('---------------------------------------------------')

sala = float(input('Digite o salário do funcionário: '))
if sala > 1250:
    print(f'O aumento do salário é de 10%, agora, quem ganha {sala} passa a ganhar: {sala/100*10+sala}!')
else:
    print(f'O aumento do salário é de 15%, agora, quem ganha {sala} passa a ganhar: {sala/100*15+sala}!')
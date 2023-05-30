import random

ha = 'Hamburguer'
piz = 'Pizza'
bata = 'KARTOSHKA'
lanche = (ha, piz, bata)
for comida in lanche:
    print(f'Eu vou comer {comida}!')
print(f'Foram {len(lanche)} comidas!')

# for cominda in range(0,len(lanche))
#   print(f'Eu vou comer {lanche[cont]}') <- Mostre o conteúdo da variável que está de acordo com o
#                                            número do "cont".

print('------------------------------------')

tu = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
      'Onze', 'DOUZE', 'Treze(L)', 'Quatorze', 'Quinze', 'Dezesseis', 'Dessessete', 'Dezoito',
      'Dezenove', 'Vinte')
while True:
    an = int(input('Digite um número de 0-20, digite -1 para encerrar o programa: '))
    if an < 0 and an > 20:
        an = int(input('Você digitou um número inválido, tente novamente (0-20): '))
    elif an == -1:
        break
    print(f'Você digitou o número {tu[an]}!')

print('------------------------------------')

time = ('Time2', 'Time3', 'Time1', 'Time4')
print(f'O Time 2 está na {time.index("Time2")+1}º posição!')

print('------------------------------------')

sort = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
        random.randint(0, 10))
print('Os números sorteados foram: ', end='')
for so in sort:
    print(so, end=' ')
print(f"""\nO maior foi {max(sort)}
O menor foi {min(sort)}!""")
# \n corta o end=

print('------------------------------------')

tunu = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
        int(input('Digite outro outro número: ')), int(input('Digite outro outro outro número: ')))
if 3 in tunu:
    print(f'O valor 3 apareceu na {tunu.index(3)+1}º posição!')
else:
    print('Não há o valor 3 na lista!')
print('Os valores digitados são: ', end='')
for liso in tunu:
    if liso % 2 == 0:
        print(liso, end=' ')
# for liso in tuno lê toda a lista em procura do designado.


print('------------------------------------')

lista = ('Lapis', 1, 'Borracha', 2)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
# se a posição do "pos" for divisível por 2, isso quer dizer que é o nome do produto.
# exp: Borracha está na 2º posição, logo a posição dele é divisível por 2.

print('------------------------------------')

pala = ('Programador', 'Futuro', 'Mercado')
for posi in pala:
    print(f'\nNa palavra {posi.upper()} temos ', end='')
    for letra in posi:
        # Escaneie cada letra da variável e cheque pelo in.
        if letra.lower() in 'aeiou':
            print(letra, end=' ')  # SIM, ISSO FUNCIONA,
            # STRINGS SÃO LISTAS DE CARACTERES, ESSE TEMPO TODO.

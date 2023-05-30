# Dissecando Variáveis
algo = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está toda em maiúsculas? ', algo.isupper())
print('Está toda em menúsculas? ', algo.islower())
print('Tem letra maíuscula? ', algo.istitle())

# Print básico e formatações! {:^5}, {:.3f}, etc.
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
print(
    f'A soma é {n1+n2}, a divisão é {n1/n2:.2f}, a multiplicação é {n1*n2:.2f},', end=' ')
print(f'o resto da divisão é {n1//n2}, e a exponenciação é {n1**n2}!')
print('{:10}'.format('Obrigado!'))

# Tabuada
valor = int(input('Digite um valor: '))
print(f'A tabuada de {valor} é: '.format(valor))
print(f'{valor} vezes 2 é {valor*2}')
print(f'{valor} vezes 3 é {valor*3}')
print(f'{valor} vezes 4 é {valor*4}')
print(f'{valor} vezes 5 é {valor*5}')
print(f'{valor} vezes 6 é {valor*6}')
print(f'{valor} vezes 7 é {valor*7}')
print(f'{valor} vezes 8 é {valor*8}')
print(f'{valor} vezes 9 é {valor*9}')
print(f'{valor} vezes 10 é {valor*10}')

# Dias alugados
dias = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos KM rodados? '))
print(f'O total a pagar é R${dias*60+km*0.15:.2f}')

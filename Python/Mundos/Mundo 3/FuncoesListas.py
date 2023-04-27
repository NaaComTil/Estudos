lanches = ['pizza', 'hamburguer', 'suco']
lanches.append('cookie')
lanches.insert(0, 'refri')
# Agora lanches = Refri, Pizza, Hamburguer, Suco, Cookie
del lanches[0]
lanches.pop()
lanches.remove('suco')
# Agora lanches = Pizza, Hamburguer

values = list(range(1, 11))

values2 = [8, 4, 6, 3, 2, 9, 5]
values.sort()
values.sort(reverse=True)
len(values2)  # = 7

listaa = [2, 3, 4, 5]
listab = listaa
listab[2] = 8
# Agora, o indice 2 de listab e listaa tem o valor 8, igualar listas cria uma ligação entre elas.
# Para criar uma cópia de uma lista, use:
listac = listaa[:]

for c, v in enumerate(listaa):
    print(f'No indice {c} encontrei o valor {v}!')

print('------------------------------------')

vari = list()
for way in range(1, 6):
    vari.append(int(input(f'Digite o valor {way}: ')))
lisma = max(vari)
lisme = min(vari)
print(f'Você digitou a lista {vari}!')
print(f'O maior valor foi {max(vari)} na(s) posição(ões): ', end='')
for tries, tries2 in enumerate(vari):
    if tries2 == lisma:
        print(f'{tries}... ', end='')
print()
print(f'O menor valor foi {min(vari)} na(s) posição(ões): ', end='')
for tries3, tries4 in enumerate(vari):
    if tries4 == min(vari):
        print(f'{tries3}... ', end='')
print()

print('------------------------------------')

answer = 'S'
listnume = list()
while answer == 'S':
    adci = int(input('Digite um valor: '))
    if adci in listnume:
        print(f'Número {adci} já foi adicionado, tente novamente.')
    else:
        listnume.append(adci)
        print(
            f'Número {adci} adicionado com sucesso, a lista agora é {listnume}.')
    answer = str(input('Deseja continuar [S/N]? ')).upper().strip()
listnume.sort()
print('-'*30)
print(f'A sua lista final é {listnume}!')

print('------------------------------------')

answer2 = 'S'
listaip = list()
listaimp = list()
listapar = list()
while answer2 == 'S':
    listaip.append(int(input('Digite um valor: ')))
    answer2 = str(input('Deseja continuar? [S/N]: ')).upper().strip()
for ways, wayss in enumerate(listaip):
    if wayss % 2 == 0:
        listapar.append(wayss)
    else:
        listaimp.append(wayss)
print(f"""A lista final é: {listaip}!
A lista par final é: {listapar}!
A lista impar final é: {listaimp}!""")

print('------------------------------------')

list1 = []
for tries1 in range(0, 5):
    woep = int(input('Digite um valor: '))
    if tries1 == 0 or woep > list1[-1]:
        list1.append(woep)
        print('Adicionando ao final da lista...')
    else:
        posi = 0
        while posi < len(list1):
            if woep <= list1[posi]:
                list1.insert(posi, woep)
                print(f'Adicionado a posição {posi}!')
                break
            posi += 1
print('-'*30)
print(f'Os valores digitados em ordem foram {list1}!')

print('------------------------------------')

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é invalida!')

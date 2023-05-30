import random
import time

heavy = light = 0
alce = 'S'
dados = list()
galera = list()
while alce == 'S':
    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input('Digite um peso: ')))
    if len(galera) == 0:
        heavy = light = dados[1]
    else:
        if dados[1] > heavy:
            heavy = dados[1]
        elif dados[1] < light:
            light = dados[1]
    galera.append(dados[:])
    dados.clear()
    alce = str(input('Deseja continuar [S/N]? ')).strip().upper()
print('-=-'*30)
print(f'O maior peso foi de {heavy}kg, de ', end='')
for item in galera:
    if item[1] == heavy:
        print(f'[{item[0]}] ', end='')
print()
print(f'O menor peso foi de {light}kg, de ', end='')
for item in galera:
    if item[1] == light:
        print(f'[{item[0]}] ', end='')
print()

print('------------------------------------')

totlist = [[], []]
resval = 0
for valnume in range(1, 8):
    resval = int(input(f'Digite o {valnume}º número: '))
    if resval % 2 == 0:
        totlist[0].append(resval)
    else:
        totlist[1].append(resval)
totlist[0].sort()
totlist[1].sort()
print('-='*30)
print(f"""Os números pares são {totlist[0]}!
Os números impares são {totlist[1]}!""")

print('------------------------------------')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maiorterc = somapar = somasec = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'Digite o valor [{linha},{coluna}]: '))
print('-=-'*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^7}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
for linha in range(0, 3):
    somasec += matriz[linha][2]
for coluna in range(0, 3):
    if coluna == 0:
        maiorterc = matriz[1][coluna]
    elif matriz[1][coluna] > maiorterc:
        maiorterc = matriz[1][coluna]
print('-=-'*30)
print(f'A soma dos valores pares é {somapar}!')
print(f'A soma dos valores da terceira coluna é {somasec}!')
print(f'O maior dos valores da linha secundária é {maiorterc}!')

print('------------------------------------')

anspalp = int(input('Quantas vezes quer palpitar? '))
numerand = contrand = 0
palpi = list()
randpalp = list()
for palp in range(anspalp):
    contrand = 0
    for appends in range(0, 6):
        numerand = random.randint(1, 60)
        if numerand not in randpalp:
            randpalp.append(numerand)
            contrand += 1
        if contrand >= 6:
            break
    palpi.append(randpalp[:])
    randpalp.clear()
print(f'-=-=-=-= Sorteando {anspalp} jogos! -=-=-=-=')
for palpit in palpi:
    print(palpit)

print('------------------------------------')

answalu = 'S'
sala = list()
aluno = list()
mostra = 0
while answalu == 'S':
    aluno.append(str(input('Digite o nome de um aluno: ')))
    aluno.append(float(input('Digite a primeira nota do aluno: ')))
    aluno.append(float(input('Digite a segunda nota do aluno: ')))
    aluno.append((aluno[1]+aluno[2])/2)
    sala.append(aluno[:])
    aluno.clear()
    answalu = str(input('Deseja continuar [S/N]? ')).strip().upper()
print('-=-'*30)
for alunos, alunos2 in enumerate(sala):
    print(f'Aluno [{alunos}]    {sala[alunos][0]}        {sala[alunos][-1]}')
print('-=-'*30)
while mostra != 999:
    mostra = int(input("""Quer mostrar as notas de algum aluno (Digite 999 para interromper)?
    R: """))
    if mostra != 999:
        print(
            f'As notas de {sala[mostra][0]} são {sala[mostra][1]} e {sala[mostra][2]}!')
        print('-=-'*30)

# while numes != 1:
# Tradução: Enquanto "numes" for diferente de 1, faça "isso".

import random

re = str(input('Digite seu sexo [M, F ou INT]: '))
while re not in 'MFINT':
    re = str(input('Dado invalido! Digite seu sexo: ')).upper()
print('Sexo {} digitado com sucesso!'.format(re))

print('------------------------------------')

numpen = random.randint(0, 10)
numre = int(input('Digite o número pensado pelo computador, de 0 a 10: '))
tent = 1
dica = ''
while numpen != numre:
    if numpen < numre:
        dica = 'menos'
    else:
        dica = 'maior'
    numre = int(input('É {}, você errou! Tente novamente: '.format(dica)))
    tent += 1
print('Você acertou em {} tentativa(s)!'.format(tent))

print('------------------------------------')

res = 0
while res != 4:
    numprim = maior = int(input('Digite um número: '))
    numsecu = int(input('Digite outro número: '))
    res = int(input("""O quê deseja fazer com esse números? Digite a resposta:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Sair
    [Outros] Novos números
    Resposta: """))
    if res == 1:
        print('A soma de {} e {} é {}!'.format(
            numprim, numsecu, numprim+numsecu))
    elif res == 2:
        print('A multiplicação de {} e {} é {}!'.format(
            numprim, numsecu, numprim*numsecu))
    elif res == 3:
        if maior < numsecu:
            maior = numsecu
        print('O maior número entre {} e {} é {}!'.format(numprim, numsecu, maior))

print('------------------------------------')

numes = numini = int(input('Digite um número para saber seu fatorial: '))
numfat = numes*(numes-1)
numes -= 1
while numes != 1:
    numes -= 1
    numfat = numfat*numes
print('O fatorial de {} é {}!'.format(numini, numfat))

print('------------------------------------')

val = 0
maisnum = 1
print('Digite um número para ver os primeiros dez números da sua razão!')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
final = termo+(9)*razao
while val != final:
    val += razao
    print('{} '.format(val), end='-> ')
print('Acabou!')
while maisnum != 0:
    maisnum = int(input("""Deseja ver mais números? Quantos?
Digite 0 para encerrar o programa.
Resposta: """))
    if maisnum != 0:
        final2 = val+(maisnum)*razao
        while val != final2:
            val += razao
            print('{} '.format(val), end='-> ')
        if val == final:
            print('Esses foram os numeros extras!')
print('O programa acabou!')

print('------------------------------------')

fina = 0
numesc = sequ = int(input("""Digite um número para ver os primeiros 10 termos da sequência de Fibonacci!
R: """))
while fina != 10:
    sequ += numesc+numesc
    fina += 1
    print('{} '.format(sequ), end='-> ')
print('Acabou!')

print('------------------------------------')

veze = to = so = 0
print("""Digite valores para saber sua soma! 
(Digite 999 para encerrar o programa)
[ ---------------------- ]""")
while veze != 999:
    so += veze
    to += 1
    veze = int(input('Digite o {}º valor: '.format(to)))
print("""[ ---------------------- ]
Foram digitados {}º valores. A soma de todos eles é: {}!""".format(to-1, so))

print('------------------------------------')

respo = ''
t = v = me = ma = med = s = 0
print("""Digite valores para saber sua média, menor e maior valor.""")
while respo != 'N':
    t += 1
    v = int(input('Digite o {}º valor: '.format(t)))
    s += v
    if t == 1:
        ma = me = v
    else:
        if v > ma:
            ma = v
        elif v < me:
            me = v
    respo = str(input('Deseja continuar? [S/N] '))
med = s/t
print("""A média dos números digitados é {}! 
O maior e menor valor foram, respectivamente, {} e {}!""".format(med, ma, me))

print('------------------------------------')

print('Bem vinde ao Banco CEV.')
print('-'*30)
saq = int(input('Informe quanto quer sacar: R$'))
ced = 50
totced = 0
while True:
    # Se o saque(saq) for maior que a cédula atual, então saq é subtraido
    # pelas cedulas necessárias, assim adicionando +1 no saq de cédulas (totced).
    if saq >= ced:
        saq -= ced
        totced += 1
    # CASO a cédula de R$50(ced) não consiga mais subtrair do saque(saq) [linha 10]... OU SEJA,
    # se o saq chegar a ser menor que R$50, então, a cédula vira de R$20.
    # Caso fique menor que R$20, vira R$10, e assim vai subtraindo o total e repetindo o while
    # e o print até o total ser 0 e o while dar break. (GENIAL!)
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}!')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if saq == 0:
            break
print('-'*30)
print('Acabou!')

print('------------------------------------')

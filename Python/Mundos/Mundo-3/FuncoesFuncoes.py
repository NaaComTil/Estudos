import datetime


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valodobra = [2, 3, 5, 8, 5, 9]
dobra(valodobra)
print(valodobra)

print('------------------------------------')


def voto(anonasc):
    anonasc = datetime.date.today().year - anonasc
    if anonasc > 65:
        situ = 'OPCIONAL'
    elif anonasc >= 18:
        situ = 'OBRIGATÓRIO'
    elif anonasc > 15:
        situ = 'OPCIONAL'
    else:
        situ = 'NEGADO'
    print(f'Com {anonasc} anos, seu voto é: {situ}!')


voto(int(input('Digite seu ano de nascimento: ')))

print('------------------------------------')


def fatorial(n=1, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=False))

print('------------------------------------')


def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gol(s)!')


n = str(input('Nome do jogador: '))
g = str(input('Quantos gols fez? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

print('------------------------------------')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido!')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')

print('------------------------------------')

# sum(lista)/len(lista) = média da lista FILHA DA PUTA
# return r = (lista) para voltar a lista pra vc como variável

print('------------------------------------')

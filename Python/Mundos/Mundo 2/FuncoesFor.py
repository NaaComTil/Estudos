import time
import datetime

ini = int(input('Início: '))
fim = int(input('Final: '))
passo = int(input('De quanto em quanto? '))
for c in range(ini, fim+1 if fim>ini else fim-1, passo if passo<0 else passo*(-1)):
    time.sleep(1)
    print(c)

print('------------------------------------')

soma = 0
for num in range(1,501,2):
    if num%3==0:
        soma = soma+num
print(soma)

print('------------------------------------')

for nume in range(0,51,2):
    print(nume)

print('------------------------------------')

valor = int(input('Digite um valor para ver sua tabuada: '))
for tab in range(1,11):
    print('{} x {} = {}'.format(valor,tab,valor*tab))

print('------------------------------------')

somas = 0
for cont in range(0,6):
    primv = int(input('Digite um valor: '))
    if primv%2==0:
        somas = primv+somas 
print('A soma de todos os números pares é {}!'.format(somas))

print('------------------------------------')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decim = termo+(10-1)*razao
for val in range(termo, decim+razao, razao):
    print('{} '.format(val), end='-> ')
print('Acabou!')

print('------------------------------------')

vala = int(input('Digite um número para saber se ele é número primo: '))
totpri = 0
for valu in range(1,vala+1):
    if vala%valu==0:
        # Cores:
        print('>', end=' ')
        # Contador de divisões:
        totpri += 1
    print('{} '.format(valu), end=' ')
print('O número {} foi divisível {} vezes! Então...'.format(vala,totpri))
if totpri > 2:
    print('O número {} não é um número primo!'.format(vala))
else:
    print('O número {} é um número primo!'.format(vala))

print('------------------------------------')

frase1 = str(input('Digite a frase inteira: ')).upper().strip()
palav = frase1.split()
junto = ''.join(palav)
inver = ''
# Pegando o número de letras e atribuindo elas ao contrário para atribuir a variável inver:
for letra in range(len(junto)-1, -1, -1):
    inver += junto[letra]
print('O inverso de {} é {}!'.format(junto,inver))
if inver==junto:
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada não é um palindromo!')

print('------------------------------------')

anoat = datetime.date.today().year
totmaior = totmenor = 0
for pess in range(1,8):
    idad = int(input('Digite o ano de nascimento da {}º pessoa: '.format(pess)))
    idad = anoat - idad
    if idad >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Existem, respectivamente, {} e {} pessoas maiores e menores de idade!'.format(totmaior,totmenor))

print('------------------------------------')

pemaior = pemenor = 0
for pesso in range(1,8):
    peso = float(input('Digite o peso da {}º pessoa: '.format(pesso)))
    if pesso == 1:
        pemaior = peso
        pemenor = peso
    else:
        if peso > pemaior:
            pemaior = peso
        elif peso < pemenor:
            pemenor = peso
print('O maior e menor peso foram, respectivamente, {} e {}!'.format(pemaior,pemenor))

print('------------------------------------')

velh = mumen = totida = 0
nomvelh = ''
for pessoa in range(1,5):
    no = str(input('Digite o nome da {}º pessoa: '.format(pessoa))).strip().upper()
    ida = int(input('Digite a idade da {}º pessoa: '.format(pessoa)))
    se = str(input('Digite o sexo da {}º pessoa (F, M ou Intersex): '.format(pessoa))).strip().upper()
    if pessoa == 1:
        velh = ida
    else:
        if ida > velh and se == 'M':
            nomvelh = no
        elif ida < 20 and se == 'F':
            mumen += 1
    totida += ida
medi = totida/4
print("""A média de idade do grupo é {}!
O homem mais velho é {}!
Existe(m) {} mulher(es) com menos de 20 anos!""".format(medi,nomvelh,mumen))
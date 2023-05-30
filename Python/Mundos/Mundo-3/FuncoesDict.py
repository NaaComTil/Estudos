import operator
import datetime
import time
import random
naa = {'Nome': 'Itanaã', 'Idade': 17, 'Identidade': 'N/A'}
naa['Sexo'] = 'M'
del naa['Identidade']
print(naa['Nome'])
print(naa.values())  # dict_values(['Itanaã', 17, 'M'])
print(naa.keys())  # dict_keys(['Nome', 'Idade', 'Sexo'])
# dict_items([('Nome', 'Itanaã'), ('Idade', 17), ('Sexo', 'M')])
print(naa.items())

print('-=-'*30)

for key, value in naa.items():  # Para cada key e value no item naa, faça:
    print(f'{key} é {value}!')
# Nome é Itanaã!
# Idade é 17!
# Sexo é M!

print('-=-'*30)

vic = {'Idade': 17, 'Sexo': 'M'}
vic['Nome'] = str(input('Qual o nome de Red? '))
regis = list()
regis.append(naa.copy())
regis.append(vic.copy())
print(regis[0])  # {'Nome': 'Itanaã', 'Idade': 17, 'Sexo': 'M'}
print(regis[1])  # {'Idade': 17, 'Sexo': 'M', 'Nome': 'Victor'}

print('------------------------------------')

stud = dict()
stud['Nome'] = str(input('Digite o nome do aluno: '))
stud['Média'] = float(input('Digite a média do aluno: '))
if stud['Média'] >= 6:
    stud['Situação'] = 'Aprovado'
else:
    stud['Situação'] = 'Reprovado'
for chastud, valstud in stud.items():
    print(f'{chastud} é igual a {valstud}!')

print('------------------------------------')

results = dict()
results['Jogador1'] = random.randint(1, 6)
results['Jogador2'] = random.randint(1, 6)
results['Jogador3'] = random.randint(1, 6)
results['Jogador4'] = random.randint(1, 6)
ranking = list()
ranking = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
print('-=-'*30)
for player, dado in results.items():
    time.sleep(1)
    print(f'O {player} tirou {dado}!')
print('-=-'*30)
print(' == RANKING DOS JOGADORES == ')
for itemrank, valrank in enumerate(ranking):
    time.sleep(1)
    print(f'{itemrank+1}º:  {valrank[0]} com {valrank[1]}!')

print('------------------------------------')

doc = dict()
doc['Nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
doc['Idade'] = datetime.date.today().year - anonasc
doc['CTPS'] = int(input('Carteira de trabalho (0 = não tem): '))
if doc['CTPS'] != 0:
    doc['Ano de Contratação'] = int(input('Ano de contratação: '))
    doc['Salário'] = float(input('Salário: R$'))
    doc['Ano de Aposentadoria'] = (doc['Ano de contratação'] + 35) - anonasc
print('-=-'*30)
for keydoc, valudoc in doc.items():
    print(f'{keydoc} é igual a {valudoc}!')

print('------------------------------------')

jogafut = dict()
levan = list()
futres = 'S'
showjog = 0
while futres == 'S':
    jogafut['Nome'] = str(input('Nome: '))
    partidas = int(input('Número de partidas: '))
    jogafut['Gols'] = list()
    totgols = 0
    for jogo in range(partidas):
        jogafut['Gols'].append(
            int(input(f'Quantos gols na {jogo}ª partida? ')))
    for parts, gols in enumerate(jogafut['Gols']):
        totgols += gols
    jogafut['Total de Gols'] = totgols
    levan.append(jogafut.copy())
    jogafut.clear()
    futres = str(input('Deseja continuar [S/N]? ')).strip().upper()
print('-=-'*30)
print('Cod / Nome / Gols / TotalDeGols')
for indilevan, itemlevan in enumerate(levan):
    print(
        f'{indilevan}  {itemlevan["Nome"]}         {itemlevan["Gols"]}     {itemlevan["Total de Gols"]}')
print('-=-'*30)
while showjog != 999:
    showjog = int(input("""Quer mostrar qual jogador? (Digite 999 para interromper)
    R: """))
    if showjog >= len(levan):
        print(f'ERRO! Não existe jogador com o código {showjog}!')
    else:
        if showjog != 999:
            print(f'- LEVANTAMENTO DO JOGADOR {levan[showjog]["Nome"]}!')
            for partfut, goljog in enumerate(levan[showjog]["Gols"]):
                print(f'Na partida {partfut}, fez {goljog} gols!')
            print('-=-'*30)

print('------------------------------------')

respdict = 'S'
regist = list()
perregi = dict()
totpere = somaper = medper = 0
while respdict == 'S':
    perregi['Nome'] = str(input('Nome: ')).strip()
    perregi['Sexo'] = str(input('Sexo [M/F/INT]: ')).upper().strip()
    perregi['Idade'] = int(input('Idade: '))
    regist.append(perregi.copy())
    perregi.clear()
    totpere += 1
    respdict = str(input('Deseja continuar [S/N]? ')).upper().strip()
print('-=-'*30)
print(f'- O grupo tem {totpere} pessoas!')
print('-=-'*30)
for itemregi, dictregi in enumerate(regist):
    somaper += dictregi['Idade']
print(f'- A média de idade é de {somaper/totpere}!')
print('- As mulheres cadastradas foram: ', end='')
for itemregi, dictregi in enumerate(regist):
    if 'F' in dictregi['Sexo']:
        print(dictregi['Nome'], end=' ')
print('\n- As pessoas acima da idade média são: ')
for itemregi, dictregi in enumerate(regist):
    if dictregi['Idade'] > somaper/totpere:
        print(
            f'{dictregi["Nome"]} de sexo {dictregi["Sexo"]} e idade {dictregi["Idade"]}!')

print('------------------------------------')

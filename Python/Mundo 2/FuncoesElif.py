casa = int(input('Digite o valor da casa: R$'))
sala = int(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos irá pagar: '))
if casa/(anos*12) > (sala*30)/100:
    print("""30% do seu salário é igual a R${:.2f}
    Seu empréstimo foi negado!""".format((sala*30)/100))
else:
    print("""30% do seu salário é igual a R${:.2f}.
    O empréstimo será de R${:.2f} por mês!""".format((sala*30)/100,casa/(anos*12)))

print('------------------------------------')

num= int(input("Digite um numero inteiro: "))
print("""Escolha uma das bases para convers ão :
[1] converter para BINARIO
[2] converter para OCTAL
[3] Converter para HEXADECIMAL""")
opção = int(input('Sua opçāo: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}!'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é igual a {}!'.format (num,oct(num)[2:]))
elif opção == 5:
    print('{} Convertido para HEXADECIMAL é igual a {}!'.format(num,hex(num)[2:]))
else:
    print('Opção invalida, tende novamente!')


print('------------------------------------')

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
if num1>num2:
    print('O primeiro valor ({}) é maior!'.format(num1))
if num2>num1:
    print('O segundo valor ({}) é maior!'.format(num2))
if num1 == num2:
    print('O primeiro ({}) e segundo ({}) valor são iguais!'.format(num1,num2))

print('------------------------------------')

from datetime import date #Frescura
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print("""Você tem {} ano(s), você ainda vai se alistar!
    Ainda faltam {} meses!""".format(idade,((idade-18)*(-1))*12))
elif idade == 18:
    print('Você tem {} anos, está na hora de se alistar!'.format(idade))
elif idade > 18:
    print("""Você tem {} anos(s), já passou a hora de se alistar!
    Está {} meses atrasado!""".format(idade,(idade-18)*12))

print('------------------------------------')

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano #Lembrar de  importar
if idade <= 9:
    print('Você tem {} ano(s), e é um nadador MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, e é um nadador INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, e é um nadador JUNIOR!'.format(idade))
elif idade == 20:
    print('Você tem {} anos, e é um nadador SÊNIOR!'.format(idade))
else:
    print('Você tem {} anos, e é um nadador MASTER!'.format(idade))

print('------------------------------------')

reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda reta: '))
reta3 = int(input('Digite a terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    tri = True
    print('Os valores formam um triângulo!')
    if reta1 == reta2 and reta2 == reta3:
        print('O triângulo é equilátero!')
    elif reta1 == reta2 and reta1 != reta3:
        print('O triângulo é isóceles!')
    elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
        print('O triângulo é escaleno!')
else:
    Tri = False
    print('Os valores não formam um triângulo!')

print('------------------------------------')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
if peso/altura**2 < 18.5:
    print('Seu IMC é {:.2f}, e você está abaixo do peso!'.format(peso/altura**2))
elif peso/altura**2 >= 18.5 and peso/altura**2 <= 25:
    print('Seu IMC é {:.2f}, e você está no peso ideal!'.format(peso/altura**2))
elif peso/altura**2 < 25 and peso/altura**2 <= 30:
    print('Seu IMC é {:.2f}, e você está acima do peso!'.format(peso/altura**2))
elif peso/altura**2 < 30 and peso/altura**2 <= 40:
    print('Seu IMC é {:.2f}, e você está com obesidade!'.format(peso/altura**2))
else:
    print('Seu IMC é {:.2f}, e você está com obsesidade mórbida!'.format(peso/altura**2))

print('------------------------------------')
    
preço = int(input('Digite o preço do produto: R$'))
paga = int(input("""Digite a forma de pagamento:
[1] Para dinheiro/cheque.
[2] A vista no cartão.
[3] Parcelar no cartão.
Resposta: """))
if paga == 1:
    print("""Você pagou em cheque/Dinheiro, 10% de desconto!
    Você vai pagar R${} no produto desejado!""".format(preço-((preço*10)/100)))
elif paga == 2:
    print("""Você pagou a vista no cartão, 5% de desconto!
    Você vai pagar R${} no produto desejado!""".format(preço-((preço*5)/100)))
elif paga == 3:
    parce = int(input("""Em quantas vezes quer parcelar? """))
    if parce == 2:
        print('Você pagou o preço original do produto em duas parcelas de R${}!'.format(preço/2))
    else:
        print("""Você pagou no cartão {} parcelas com 20% de juros no preço do produto!
        O preço do produto com 20% de juros é R${}!
        Assim, pagando {} parcelas de R${:.2f}!"""
                    .format(parce,preço+((preço*20)/100),parce,(preço+((preço*20)/100))/parce))

print('------------------------------------')

import random
from time import sleep
print("""[ PEDRA, PAPEL e TESOURA! ]
O computador já escolheu!
[ ---------------------- ]""")
esc = str(input('PEDRA, PAPEL, ou TESOURA? ').upper().strip())
comp = random.choice(['PAPEL','PEDRA','TESOURA'])
print('[ ---------------------- ]')

print('[ ---------------------- ]')
#EMPATE
if comp == esc:
    print("""Você jogou {} e o computador {}!
    Foi um empate!""".format(esc,comp))
#VITÓRIAS
elif comp == 'TESOURA' and esc == 'PEDRA':
    print("""Você jogou {} e o computador {}!
    Você ganhou!""".format(esc,comp))
elif comp == 'PAPEL' and esc == 'TESOURA':
    print("""Você jogou {} e o computador {}!
    Você ganhou!""".format(esc,comp))
elif comp == 'PEDRA' and esc == 'PAPEL':
    print("""Você jogou {} e o computador {}!
    Você ganhou!""".format(esc,comp))
#DERROTAS
elif esc == 'TESOURA' and comp == 'PEDRA':
    print("""Você jogou {} e o computador {}!
    Você perdeu!""".format(esc,comp))
elif esc == 'PAPEL' and comp == 'TESOURA':
    print("""Você jogou {} e o computador {}!
    Você perdeu!""".format(esc,comp))
elif esc == 'PEDRA' and comp == 'PAPEL':
    print("""Você jogou {} e o computador {}!
    Você perdeu!""".format(esc,comp))
print('[ ---------------------- ]')
print('[FIM DE JOGO]')
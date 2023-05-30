import random
import math
Num = random.uniform(1, 1000)
print(f'O número gerado e arredondado é: {math.trunc(Num)}')

print('------------------------------------')

cat1 = int(input('Digite o valor do cateto oposto: '))
cat2 = int(input('Digite o valor do cateto adjacente: '))
print(
    f'A hipotenusa do cateto oposto {cat1} e cateto adjacente {cat2} é igual a {math.hypot(cat1,cat2)}!')

print('------------------------------------')

ang = int(input('Digite um angulo: '))
print(f"""O Cosseno, Seno e Tangente de {ang}, respectivamente, 
são: {math.cos(ang):.3f}, {math.sin(ang):.3f} e {math.tan(ang):.3f}!""")

print('------------------------------------')

print('Escolha um aluno aleatório!')
alu1 = str(input('Primeiro aluno: ')).strip()
alu2 = str(input('Segundo aluno: ')).strip()
alu3 = str(input('Terceiro aluno ')).strip()
alu4 = str(input('Quarto aluno: ')).strip()
esco = random.choice((alu1, alu2, alu3, alu4))
print('O aluno escolhido foi ', esco, '!')

print('------------------------------------')

Lista = (alu1, alu2, alu3, alu4)
print(f'Os alunos são {alu1}, {alu2}, {alu3} e {alu4}.')
print('E a ordem de apresentação deles é:')
print(random.sample(Lista, len(Lista)))

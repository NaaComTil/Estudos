# frase[] - Cita a cadeia de caracteres, nesse exemplo: frase[9::3], vai começar pelo caracter 9 até o final,
# pulando de 3 e 3 caracteres, nesse caso, mostrará 'VE YO'. *Print de como funciona no Notion*

# len(frase) - Conta os caracteres na frase.
# frase.count(o,0,13) - Conta, do caractere 0 a 13, as letras "o" na frase da variável.

# frase.find('deo') - Acha o "deo" na frase e cita o número no qual o caractere começa, caso não exista,
# o valor é mostrado como -1, nesse caso, os caracteres 'deo', começa na cadeia 11.
# frase.rfind('deo') - Acha o "deo" na parte que mais estiver a direita e cita o número no qual o
# caractere começa.

# 'curso' in frase - Fala se é true ou falso que existe 'curso' na setença.

# frase.replace ('Python','Android') - Substitui os caracteres 'Python' por 'Android'
# frase.upper() / lower() - Coloca os caracteres em maiúsculo e menúsculo, respectivamente.
# frase.capitalize() - Deixa todos os caracteres em menúsculo, exceto o primeiro caractere da string.

# frase.title() - Conta quantos caracteres tem na string, sem contar os espaços e deixa todos os caracteres,
# exceto os de começo de palavras, em menúsculo, como exemplo, a string fica assim: 'Curso Em Video Python'.

# frase.strip() - Remove todos os espaços do final e inicio da cadeia de caracteres, exceto os entre
# caracteres. *Print de como funciona no Notion*
# frase.rstrip() - Remove todos os espaços do final da cadeia de caracteres.
# frase.lstrip() - Remove todos os espaços do inicio da cadeia de caracteres.

# frase.split() - Pega os caracteres que são separados por espaço e transforma eles em uma lista, criando
# uma divisão a cada espaço.
# '-'.join(frase) - Substitui os espaços pelo quê estiver em aspas, nesse caso, ficaria Curso-em-Vídeo-Python.

# Colocar esses comandos entre o print()!

nom = str(input('Digite seu nome completo: ')).strip()
print("Analisando seu nome...")
print(f'Seu nome em maiúsculo é {nom.upper()}!')
print(f'Seu nome em minúsculo é {nom.lower()}!')
print('Seu nome tem ao todo {} letras!'.format(len(nom)-nom.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras!'
      .format(nom.split()[0], nom.find(' ')))
# nom.find(' '), lê a posição do primeiro espaço da cadeia de caracteres,
# logo, dizendo quantas letras tem o primeiro nome! (Esperto!)

print('-------------------------------')

numero = int(input('Digite um número de 1000 a 9999: '))
print(f"""Milhar é {numero//1%10}
Centena é {numero//10%10}
Dezena é {numero//100%10}
Unidade é {numero//1000%10}""")
# Dividindo os números, ele consegue nulificar os números não existentes, por exemplo: se o usuário
# digitasse 123.

print('-------------------------------')

nomeci = input('Digite o nome de uma cidade: ').upper().strip().split()
print('Sua cidade começa com o nome SANTO?', 'SANTO' in nomeci[0])

print('-------------------------------')

nomepe = input('Digite o nome de uma pessoas: ').upper().strip()
print('A pessoa tem Silva no nome? ', 'SILVA' in nomepe)

print('-------------------------------')

frase = str(input('Escreva uma frase: ')).upper().strip()
print(f"A letra (A) aparece {frase.count('A')} vez(es)!")
print(f"A letra (A) aparece na posição {frase.find('A')+1} pela primeira vez!")
print(f"A letra (A) aparece na posição {frase.rfind('A')+1} pela ultima vez!")

print('-------------------------------')

nomep = input('Digite seu nome completo').strip().split()
print(f"""Muito prazer em te conhecer! 
Seu primeiro nome é: {nomep[0]}!
Seu ultimo nome é: {nomep[-1]}!""")

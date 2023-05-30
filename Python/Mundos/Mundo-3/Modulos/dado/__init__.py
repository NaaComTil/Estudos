def leiaDinheiro(msg):
    floats = False
    while not floats:
        entrada = str(input(msg).replace(',','.')).strip()
        if entrada.isalpha() or not '.' in entrada or entrada == '':
            print('ERRO! Digite um número inteiro válido!')
        else:
            floats = True
            return float(entrada)
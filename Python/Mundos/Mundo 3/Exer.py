print('Pegue o ônibus!')
km = int(input('Qual distancia em Km? '))
if km < 200:
    print(f"""Você irá andar {km}kms, e o preço por cada Km abaixo de 200kms é R$0.50,
    logo {km}*0.50 dá R${0.50*km}!""")
else:
    print(f"""Você irá andar {km}kms, e o preço por cada Km acima de 200kms é R$0.45,
    logo {km}*0.45 dá R${0.45*km}!""".format(km,km,0.45*km))
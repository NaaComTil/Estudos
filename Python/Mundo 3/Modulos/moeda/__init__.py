def resumo(num, au, red):
    print('-=-'*20)
    print(f'RESUMO DO VALOR'.center(70))
    print('-=-'*20)
    print(f'Preço analisado:     R${num}'.replace('.',','))
    print(f'Metade do preço:     R${num/2}'.replace('.',','))
    print(f'Dobro do preço:      R${num*2}'.replace('.',','))
    print(f'{au}% de aumento:    R${num/100*au+num}'.replace('.',','))
    print(f'{red}% de desconto:  R${num-((num*red)/100)}'.replace('.',','))
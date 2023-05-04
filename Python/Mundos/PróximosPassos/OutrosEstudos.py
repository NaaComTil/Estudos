# FUNÇÕES ANÔNIMAS
média = lambda a,b,c:(a+b)/c
print(média(2,7,2))
print('-='*10)

# Ou de forma mais avançada:
r = lambda x,func:x+func(x) # Passei 2 para o X, e para a função, passei uma nova lambda que recebe x e
res=r(2, lambda x:x*x) # multiplica ele por ele mesmo. Ou seja, a conta final é 2+func(2*2), 2+4 = 6.
print(res)
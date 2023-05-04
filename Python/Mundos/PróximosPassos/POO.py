# BASE / PAI / SUPERCLASSE:
class NPC:
    
    # Caso houvesse um comando como nome = 'vazio', seria um ATRIBUTO da CLASSE.

    # MÉTODO construtor da CLASSE PAI, é ai aonde você define os ATRIBUTOS dos OBJETOS:
    def __init__(self, nom='', ida=0, ocu=''):
        self.nome = nom
        self.idade = ida
        self.ocupacao = ocu

    # Outro MÉTODO (ou function) da CLASSE PAI para OBJETOS:
    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Ocupação: {self.ocupacao}')
        print('-='*20)


# Criando uma CLASSE FILHO a partir da CLASSE PAI:
class Programador(NPC):
    
    # Definindo os ATRIBUTOS da CLASSE FILHO:
    def __init__(self, nom='', ida=0):
        self.ocupacao = 'Programador'
        
        # Com o super(), você chama a CLASSE PAI, neste caso, chamando o construtor da CLASSE PAI, colocando apenas o nome e a idade na CLASSE FILHO:
        super().__init__(nom, ida, self.ocupacao)


    # Criando METODO da CLASSE FILHO:
    def inf(self):
        print('Classe filho: Programador.')

        # Herdando METODO da CLASSE PAI:
        # (Nota: se quiser herdar o METODO da CLASSE PAI sem adicionar mais nada, remova o "()" da function)
        super().info()


class Medico(NPC):
    def __init__(self, nom='', ida=0):
        self.ocupacao = 'Médico'
        super().__init__(nom, ida, self.ocupacao)

    def inf(self):
        print('Classe filho: Médico.')
        super().info()


# Criando um OBJETO/INSTÂNCIA:
npc1 = Medico('Medico', 17)
npc1.nome = 'Naã'

# Auto-lembrete amigável, de Naã para Naã:
# NÃO USA PRINT NA FUNCTION, SEU ANIMAL, JÁ TEM PRINT DENTRO DA FUNCTION, COMO TU VAI DAR PRINT NO PRINT? VAI RETORNAR NONE, BURRO DO CARALHO.
npc1.inf()

print('------------------------------------')

import datetime, random

class Registro:
    anoat = datetime.date.today().year
    
    def __init__(self, nome, idade, id=0):
        self.nome = nome
        self.idade = idade

    # MÉTODO para CLASSE, se usa cls:
    @classmethod
    def poranonas(cls, nome, ano_nasc):
        idade = cls.anoat - ano_nasc
        return cls(nome, idade)
    
    # MÉTODO estático não se usa nada em seus parâmetros.
    @staticmethod
    def idgen():
        id = random.randint(0, 10)
        return id
        
        
    
p1 = Registro.poranonas('Naã', 2006)
print(p1.nome, p1.idade)
print(p1.idgen())

print('------------------------------------')

class Produto:
    def __init__(self, nome, preco=0):
        self.nome = nome
        self.preco = preco
    
    # Getter
    @property
    def preco(self):
        return self._preco
    
    # Setter
    @preco.setter
    def preco(self, valor):
        self._preco = valor
        

pro1 = Produto('Maçã', 2)
print(pro1.preco)

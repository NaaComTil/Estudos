Algoritmo "SeletorDePessoas"

Var
   Sexo, Prox: Caractere
   Idade, CorCab, Cont, Homem, Mulher: Inteiro
Inicio
   Repita
      Escreval (" ")
      Escreval ("Seletor de pessoas!")
      Escreval ("-------------------")
      Escreval ("Qual o Sexo? [M/F] ")
      leia (Sexo)
      Escreval ("Idade? ")
      leia (Idade)
      Escreval ("-------------------")
      Escreval ("Cor de cabelo")
      Escreval ("[1] Preto")
      Escreval ("[2] Castanho")
      Escreval ("[3] Loiro")
      Escreval ("[4] Ruivo")
      leia (CorCab)
      se (Sexo = "M") e (Idade > 18) e (CorCab = 2) entao
         Homem <- Homem+1
      Fimse
      se (Sexo = "F") e (Idade >= 25) e (Idade <= 30) e (CorCab = 3) entao
         Mulher <- Mulher+1
      Fimse
      Escreval ("Próxima? [S/N] ")
      leia (Prox)
   até (Prox = "N")
   Escreval ("O número de homens com +18 de cabelo castanho foi ", Homem)
   Escreval ("O número de mulheres entre 25-30 anos loiras foi ", Mulher)
Fimalgoritmo
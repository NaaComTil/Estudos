Algoritmo "DiferencaGols"
Var
   Valor1, Valor2, Soma, Diferenca: Inteiro
   Result: Caractere
Inicio
   Escreva ("Quantos Gols fez o primeiro time? ")
   Leia (Valor1)
   Escreva ("Quantos Gols fez o segundo time? ")
   Leia (Valor2)
   Soma <- Valor1-Valor2

   se (Soma <= -1) entao
      Diferenca <- Soma*(-1)
   senao
      Diferenca <- Soma
   fimse

   se (Diferenca = 0) entao
      Result <- "EMPATE"
   senao
      Se (Diferenca <= 2) entao
         Result <- "Equilibrado"
      senao
         se (Diferenca >= 3) entao
            Result <- "GOLEADA"
         fimse
      fimse
   fimse
   Escreva ("A diferença foi de", diferenca, ", então foi ", Result)
Fimalgoritmo
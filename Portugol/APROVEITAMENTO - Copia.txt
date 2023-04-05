Algoritmo "Aproveitamento"
Var
   Aprove, Aprova: Caractere
   N1, N2, Media: Real
Inicio
   Escreva ("Primeira Nota: ")
   Leia (N1)
   Escreva ("Segunda Nota: ")
   Leia (N2)
   Media <- (N1+N2)/2
   Se (Media <= 4.9) entao
      Aprove <- "F"
   senao
      Se (Media >= 5) entao
         Aprove <- "E"
         Se (Media >= 6) entao
            Aprove <- "D"
            Se (Media >= 7) entao
               Aprove <- "C"
               Se (Media >= 8) entao
                  Aprove <- "B"
                  Se (Media >= 9) entao
                     Aprove <- "A"
                  Fimse
               Fimse
            Fimse
         Fimse
      Fimse
   Fimse
   se (Media >= 7) entao
      Aprova <- "APROVADO"
   senao
      senao
      se (Media >= 5) e (Media < 7) entao
         Aprova <- "RECUPERAÇÃO"
         Aprova <- "REPROVADO"
      fimse
   Fimse
   Escreva ("A média é", Media, " e está ", Aprova, " com o aproveitamento de ", Aprove)
Fimalgoritmo
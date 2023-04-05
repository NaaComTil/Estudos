Algoritmo "ContarAteQuando"

Var
   NI, NF: Inteiro
Inicio
   Escreva ("Numero Inicial: ")
   leia (NI)
   Escreva ("Numero Final: ")
   leia (NF)
   Escreval ("----------------------------")
   se (NI < NF) entao
      Escreva (NI, "...")
         Enquanto (NI < NF) faca
         NI <- NI+1
         Escreva (NI, "...")
         FimEnquanto
   senao
      Escreva (NI, "...")
         Enquanto (NI > NF) faca
         NI <- NI-1
         Escreva (NI, "...")
         FimEnquanto
   FimSe
Fimalgoritmo
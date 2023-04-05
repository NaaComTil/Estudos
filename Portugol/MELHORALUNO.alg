Algoritmo "MelhorAluno"

Var
   Nome, Vencedor: Caractere
   NumeroAlunos, Maior, Nota: Inteiro
Inicio
   Escreva ("Quantos alunos a turma tem? ")
   leia (NumeroAlunos)
   Escreval ("----------------------------")
   Enquanto (NumeroAlunos > 0) faca
      Escreval ("ALUNO", NumeroAlunos)
      Escreva ("Nome do aluno: ")
      leia (Nome)
      Escreva ("Nota do Aluno: ")
      leia (Nota)
      Escreval ("----------------------------")
      se (Maior < Nota) entao
         Vencedor <- Nome
         Maior <- Nota
      fimSe
      NumeroAlunos <- NumeroAlunos-1
   FimEnquanto
   Escreva ("O Aluno vencedor foi ", Vencedor, " com a nota ", Maior)
Fimalgoritmo
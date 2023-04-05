algoritmo "Triângulos"
var
valor1, valor2, valor3: real
Equi, Esca, Tri: logico
inicio
      Escreva ("Digite o primeiro valor: ")
leia (valor1)
     Escreva ("Digite o segundo valor: ")
leia (valor2)
     Escreva ("Digite o terceiro valor: ")
leia (valor3)

Tri <- (valor1 < valor2+ valor3) e (valor2 < valor1 + valor3) e (valor3 < valor1 + valor2)
Equi <-  (valor1 = valor2) e (valor2 = valor3)
Esca <- (valor1 <> valor2) e (valor2 <> valor3) e (valor1 <> valor3)

     se (Tri = falso) entao
        Escreva ("Os valores NÃO formam um triangulo!")
     fimse
        
     se (Tri = Verdadeiro) e (Esca = Falso) e (Equi = Verdadeiro) entao
        Escreval ("Os valores formam um triangulo Equilátero!")
     fimse
     
     se (Tri = Verdadeiro) e (Esca = Verdadeiro) e (Equi = Falso) entao
        Escreval ("Os valores formam um triangulo Escaleno!")
     fimse
fimalgoritmo
algoritmo "Empréstimo"
var
Valor, Juros, ValorComJuros, Parcelas, ValorParcela, Total, TotalComJuros: real
inicio
Escreva ("Qual o valor do empréstimo? ")
leia (Valor)
Juros <- (Valor * 20)/100
ValorComJuros <- Valor+Juros
Escreva ("Em quantas parcelas? ")
leia (Parcelas)
ValorParcela <- ValorComJuros/Parcelas
Escreval ("Serão, então,", Parcelas, " parcelas de R$", ValorParcela, "! Visto que:")
Escreval ("R$", valor, "+20% de juros(R$", Juros, ") é igual a R$", ValorComJuros, ",")
Escreva ("que divido por", Parcelas, " é igual a R$", ValorParcela, "!")
fimalgoritmo
var tot = soma = 0

function adicionar() {
    //Adicionar ao select o número inputado.
    var numad = Number(document.querySelector('input#inum').value)
    var sel = document.querySelector('select#icaixa')
    var adcnum = document.createElement('option')
    adcnum.text = `Valor "${numad}" adicionado!`
    sel.appendChild(adcnum)
    // Quantos valores foram inputados
    tot++
    // Soma de todos os valores
    soma += numad
    // Maior e menor valor inputados
    if (tot == 1) {
        return maior = menor = numad
    } else {
        if (numad > maior) {
            return maior = numad
        } else if (numad < menor) {
            return menor = numad
        }
    }
}

function finalizar() {
    var diva = document.querySelector('div#res')
    diva.innerHTML = ''
    diva.innerHTML += `O total de valores digitado foi ${tot}.`
    diva.innerHTML += `<br> O maior valor informado foi ${maior}.`
    diva.innerHTML += `<br> O menor valor informado foi ${menor}.`
    diva.innerHTML += `<br> A soma de todos os valores foi ${soma}`
    diva.innerHTML += `<br> A média dos valores digitados é ${soma/tot}`
}
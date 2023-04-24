function contar() {
    var iini = Number(document.querySelector('input#iini').value)
    var ifim = Number(document.querySelector('input#ifim').value)
    var ipas = Number(document.querySelector('input#ipas').value)
    var res = document.querySelector('div#res')
    window.alert(`iini é ${iini}, ifim é ${ifim}, ipas é ${ipas}`)
    res.style.textAlign = 'center'
    if (ipas == 0) {
        window.alert('[ERRO] Passo inválido, considerando passo "1"!')
        var ipas = 1
    }
    if (ifim > iini) {
        for (iini; iini <= ifim; iini += ipas) {
            res.innerHTML += `${iini} -> `
        }
        res.innerHTML += `Acabou! `
    } else if (ifim < iini) {
        for (iini; iini >= ifim; iini -= ipas) {
            res.innerHTML += `${iini} \u{1F449} `
        } 
        res.innerHTML += `Acabou! \u{1F3C1} `
    } else {
        res.innerHTML += `Impossível contar! `
    }	
}
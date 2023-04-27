function contar() {
    var iini = Number(document.querySelector('input#iini').value)
    var ifim = Number(document.querySelector('input#ifim').value)
    var ipas = Number(document.querySelector('input#ipas').value)
    var res = document.querySelector('p#resp')
    window.alert(`iini é ${iini}, ifim é ${ifim}, ipas é ${ipas}`)
    res.style.textAlign = 'center'
    res.innerHTML = ``
    if (ifim > iini) {
        for (iini; iini <= ifim; iini += ipas) {
            res.innerHTML += `${iini} \u{1F449} `
        }
        res.innerHTML += `Acabou! \u{1F3C1} `
    } else if (ifim < iini) {
        for (iini; iini >= ifim; iini -= ipas) {
            res.innerHTML += `${iini} \u{1F449} `
        } 
        res.innerHTML += `Acabou! \u{1F3C1} `
    } else {
        res.innerHTML += `Impossível contar! Acabou! \u{1F3C1} `
    }	
}
function contar() {
    var iini = Number(document.querySelector('input#iini').value)
    var ifim = Number(document.querySelector('input#ifim').value)
    var ipas = Number(document.querySelector('input#ipas').value)
    window.alert(`iini é ${iini}, ifim é ${ifim}, ipas é ${ipas}`)
    var res = document.querySelector('div#res')
    if (ifim > iini) {
        for (iini; iini <= ifim; iini += ipas) {
            res.style.textAlign = 'center'
            res.innerHTML += `${iini} -> `
        }
    } else {
        for (iini; iini >= ifim; iini -= ipas) {
            res.style.textAlign = 'center'
            res.innerHTML += `${iini} -> `
        }
    }
    res.innerHTML += `Acabou!`
}
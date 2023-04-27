// Variáveis compostas
let valores = [8, 1 , 7, 4, 2, 9]

for (let pos=0; pos < valores.length; pos++) {
    console.log(`A posição ${pos} tem o valor ${valores[pos]}.`)
}

console.log('-----------------------------')

for(var pos in valores) {
    console.log(`A posição ${pos} tem o valor ${valores[pos]}.`)
}

console.log('-----------------------------')

//FUNCTIONS//

function parimp(n) {
    if(n%2==0) {
        return 'par'
    } else {
        return 'impar'
    }
}

let res = parimp(11)
console.log(res)
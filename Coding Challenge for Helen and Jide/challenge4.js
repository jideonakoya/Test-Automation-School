//Print a table containing multiplication tables

const multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

function multiplicationTable(nos) {
    for (let i = 0; i < multipliers.length; i++){
        let product = nos * multipliers[i];
        console.table(nos + '*' + multipliers[i] + '=' + product)
               
        
    }
}
let x = multiplicationTable(7);



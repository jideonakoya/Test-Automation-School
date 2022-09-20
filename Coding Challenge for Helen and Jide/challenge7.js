//Sort an array of numbers in descending order


const Order = [1, 6, 2, 7, 100, 4, 8, 3]
function descendingOrderArray(nos){
    return nos.sort((a,b)=>b-a);
    
    }
    
    console.log(descendingOrderArray(Order))
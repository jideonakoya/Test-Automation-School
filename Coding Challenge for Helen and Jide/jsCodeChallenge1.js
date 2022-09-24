// calculate the sum of numbers within an array

const nosArray = [1, 3, 8, 9, 3, 7, 700, 887, 565];

function Add(nosArray) {

    const arraySum = nosArray.length;
    let totalSum = 0;

    for (let i = 0; i < arraySum; i++){
        totalSum = totalSum + nosArray[i];
    }
    return(totalSum);
    
}
console.log(Add(nosArray)) 
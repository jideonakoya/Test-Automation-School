// function MyFunction(){ //function declaration
//     console.log('My first function!');
// }

// MyFunction();// function call

// function greeting(name){
//     console.log('Good morning, ' + name)
// }
// greeting('Jide')


// function addNumbers (firstNumber, secondNumber) { //Declared function
//     const sum = firstNumber + secondNumber;
//     return sum;
// }

function areaOfRectangle(length, breadth) {
    const product = length * breadth
    return product;
    areaOfRectangle(4, 7)
}
console.log(areaOfRectangle(4, 7) + 'cm');


// const myGreet = function greet (name) { //Expressed function
//     console.log('Good morning, ' + name);
    
// };
// myGreet('Nick')


function greetings (greet){    //Callback function
greet()
}

function callback() {
    console.log('Good morning')
}

greetings(callback)
// Create a function that reverses an array


function reverseNames (names) {
    let output = [];
    for (let i=names.length-1; i>=0; i--) {
        output.push(names[i]);

    }
    return output
} 

console.log(reverseNames(['Tola', 'Jane', 'Kunle', 'Ahmed', 'Buchi', 2, 8]))
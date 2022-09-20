// Return the number of vowels in a string

const vowels = ['a', 'e', 'i', 'o', 'u']

function countVowels(string) {
    let count = 0
    for (let letter of string.toLowerCase()){
        if (vowels.includes(letter)){
            count = count + 1;
        }
    }
    return count
}

const thing = 'Calculator'
console.log(countVowels(thing))

// Create a function that filters out negative numbers


const sampleNumber = [-10, 30, 20, 40, 50]
function filterNegativeNos(nos){
    return nos.filter((a)=>(a<0));
    
    }
    
    console.log(filterNegativeNos(sampleNumber))
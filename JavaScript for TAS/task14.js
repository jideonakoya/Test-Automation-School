// Task 14 - Create books objects and loop through and log to the console the ones whose reading status is true

const books = [{
    title: 'Rich dad, poor dad',
    description: 'Investment',
    numberOfPages: 266,
    author: 'Robert Kiyosaki',
    reading: true,
    
},
{
    title: 'Thinkiing for a change',
    description: 'Motivational',
    numberOfPages: 266,
    author: 'John Maxwell',
    reading: true,
},
{
    title: 'The power of influence',
    description: 'Leadership',
    numberOfPages: 157,
    author: "John maxwell",
    reading: false,
},
]

for(let i=0; i < books.length; i++){
    if (books[i].reading===true)
    console.log(books[i])
}
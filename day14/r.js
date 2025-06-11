console.log('Hello, world!');
console.log('div');
const doc = document.getElementsByTagName("div")
let div = doc[1];
div.textContent = 'Australia';


const headings = document.getElementsByTagName("h2")
for(i = 0 ; i<headings.length ; i++)
headings[i].style.fontStyle = "italic"
console.log(headings)



let numbers = [];
let number;

while (true) {
    number = parseInt(prompt("Enter a number (0 to stop):"));
    if (number === 0) {
        break;
    }
    numbers.push(number);
}

numbers.sort((a, b) => b - a);

document.body.innerHTML += "<h2>Numbers in descending order:</h2>";
let list = "<ul>";
for (let i = 0; i < numbers.length; i++) {
    list += "<li>" + numbers[i] + "</li>";
}
list += "</ul>";
document.body.innerHTML += list;

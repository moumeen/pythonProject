function rollDice(sides) {
    return Math.floor(Math.random() * sides) + 1;
}

let sides = parseInt(prompt("Enter the number of sides on the dice:"));
let rolls = [];
let rollResult;

while (true) {
    rollResult = rollDice(sides);
    rolls.push(rollResult);

    if (rollResult === sides) {
        break;
    }
}

let listHtml = "<ul>";
for (let i = 0; i < rolls.length; i++) {
    listHtml += "<li>" + rolls[i] + "</li>";
}
listHtml += "</ul>";

document.getElementById("rollResults").innerHTML = listHtml;

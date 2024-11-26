function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

let rolls = [];
let rollResult;

while (rollResult !== 6) {
    rollResult = rollDice();
    rolls.push(rollResult);
}

let listHtml = "<ul>";
for (let i = 0; i < rolls.length; i++) {
    listHtml += "<li>" + rolls[i] + "</li>";
}
listHtml += "</ul>";

document.getElementById("rollResults").innerHTML = listHtml;

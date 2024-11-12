const numDice = prompt("How many dice rolls would you like?");
let sum = 0;

for (let i = 0; i < numDice; i++) {
    let roll = Math.floor(Math.random() * 6) + 1;
    sum += roll;
}

document.write("The sum of the dice rolls is: " + sum);

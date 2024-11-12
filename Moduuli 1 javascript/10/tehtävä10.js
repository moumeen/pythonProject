const numDice = prompt("Enter the number of dice:");
const targetSum = prompt("Enter the sum you're interested in:");

const simulations = 10000;
let count = 0;

for (let i = 0; i < simulations; i++) {
    let sum = 0;
    for (let j = 0; j < numDice; j++) {
        sum += Math.floor(Math.random() * 6) + 1;
    }
    if (sum == targetSum) {
        count++;
    }
}

const probability = (count / simulations) * 100;
document.write("Probability to get sum " + targetSum + " with " + numDice + " dice is " + probability.toFixed(2) + "%");

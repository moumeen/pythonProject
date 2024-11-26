let numbers = [];
let number;

while (true) {
    number = parseInt(prompt("Enter a number:"));

    if (numbers.includes(number)) {
        alert("This number has already been given. Stopping.");
        break;
    }

    numbers.push(number);
}

numbers.sort((a, b) => a - b);

console.log("Entered numbers in ascending order:");
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

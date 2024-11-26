let numbers = [];
for (let i = 0; i < 5; i++) {
    let num = parseInt(prompt(`Enter number ${i + 1}:`));
    numbers.push(num);
}

let reversedNumbers = "";
for (let i = numbers.length - 1; i >= 0; i--) {
    reversedNumbers += numbers[i] + " ";
}

alert("Numbers in reverse order: " + reversedNumbers.trim());

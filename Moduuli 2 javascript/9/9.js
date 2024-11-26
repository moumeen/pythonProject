function even(arr) {
    let evenNumbers = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % 2 === 0) {
            evenNumbers.push(arr[i]);
        }
    }
    return evenNumbers;
}

let numbers = [2, 7, 4];
let evenNums = even(numbers);

document.getElementById("originalArray").innerHTML = "Original Array: " + numbers;
document.getElementById("evenArray").innerHTML = "Even Numbers: " + evenNums;

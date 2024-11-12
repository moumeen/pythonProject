if (confirm("Should I calculate the square root?")) {
    const number = prompt("Enter a number:");

    if (number < 0) {
        document.write("The square root of a negative number is not defined.");
    } else {
        const squareRoot = Math.sqrt(number);
        document.write("The square root of " + number + " is " + squareRoot);
    }
} else {
    document.write("The square root is not calculated.");
}

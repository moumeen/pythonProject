const startYear = prompt("Enter the start year:");
const endYear = prompt("Enter the end year:");
const ul = document.createElement("ul");

for (let year = startYear; year <= endYear; year++) {
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        let li = document.createElement("li");
        li.textContent = year;
        ul.appendChild(li);
    }
}

document.body.appendChild(ul);

let dogNames = [];

for (let i = 0; i < 6; i++) {
    let name = prompt("Enter the name of dog " + (i + 1));
    dogNames.push(name);
}

dogNames.sort().reverse();

let list = "<ul>";
for (let i = 0; i < dogNames.length; i++) {
    list += "<li>" + dogNames[i] + "</li>";
}
list += "</ul>";

document.body.innerHTML += list;

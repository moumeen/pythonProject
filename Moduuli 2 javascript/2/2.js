let numParticipants = parseInt(prompt("How many participants?"));
let participants = [];

for (let i = 0; i < numParticipants; i++) {
    let name = prompt("Enter the name of participant " + (i + 1));
    participants.push(name);
}

participants.sort();

let list = "<ol>";
for (let i = 0; i < participants.length; i++) {
    list += "<li>" + participants[i] + "</li>";
}
list += "</ol>";

document.body.innerHTML += list;

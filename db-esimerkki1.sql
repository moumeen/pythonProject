-- Luodaan paikallinen käyttäjä "coding"
-- CREATE USER coding@localhost IDENTIFIED BY ‘salapala‘

-- poistetaan tietokanta, jos on jo olemassa
Drop DATABASE IF EXISTS ANKKALINNA
-- Luodaan ankkalinnatietokanta
Create DATABASE ankkalinna;

create database ankkalinna;
USE ankkalinna;

create table ankkalinnalainen(
ID int not null auto_increment,
etunimi varchar(40),
sukunimi varchar(40),
primary key (id)
);

create table lemmikki(
ID int not null auto_increment,
nimi varchar(40),
primary key (id)
);

create table omistaa(
lemmikki_ID int,
ankkalinnalainen_ID int,
primary key (lemmikki_ID,ankkalinnalainen_ID),
foreign key (lemmikki_ID) references lemmikki(ID),
foreign key (ankkalinnalainen_ID) references ankkalinnalainen(ID)
);

insert into ankkalinnalainen(etunimi, sukunimi)
values("Aku", "Ankka"),("Roope", "Ankka"),
("Tupu", "Ankka"), ("Milla", "Magia"), ("Mikki", "Hiiri");

insert into lemmikki(nimi)
values ("Pulivari"), ("Pluto"), ("Korri");

insert into omistaa(lemmikki_ID, ankkalinnalainen_ID)
values(1,1),(1,3),(2,5),(3,4);

-- Annetaan käyttäjälle luku- ja päivitysoikeudet tietokantaan ankkalin
GRANT SELECT, INSERT, UPDATE ON database_name.* TO coding@localhost;
-- kirjautuminen käyttäjällä (terminaali) : mysql -u coding -p salapala


-- hae lemmikit taulun kaikki sisältö
SELECT * FROM lemmikki;
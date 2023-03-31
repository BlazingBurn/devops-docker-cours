CREATE DATABASE sampledb;
USE sampledb;

CREATE TABLE fruits (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL,
    couleur VARCHAR(20) NOT NULL,
    prix FLOAT NOT NULL
);

INSERT INTO fruits (nom, couleur, prix) VALUES
    ('Banane', 'Jaune', 0.99),
    ('Pomme', 'Rouge', 1.49),
    ('Orange', 'Orange', 1.29),
    ('Fraise', 'Rouge', 2.99);
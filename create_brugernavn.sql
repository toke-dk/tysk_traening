DROP TABLE brugernavn;

CREATE TABLE brugernavn(
    brugernavn varchar(12),
    adgangskode varchar(12),
    tid_sekunder int,
    PRIMARY KEY (brugernavn)
);

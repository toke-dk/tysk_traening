-- psql -h toke-sprog.cr0dt7iqlyfp.eu-central-1.rds.amazonaws.com -f create_brugernavn.sql sprog_app_dev sprog_app_user
DROP TABLE brugernavn;

CREATE TABLE brugernavn(
    brugernavn varchar(12),
    adgangskode varchar(12),
    tid_sekunder int,
    PRIMARY KEY (brugernavn)
);

-- psql -h toke-sprog.cr0dt7iqlyfp.eu-central-1.rds.amazonaws.com -f create.sql sprog_app sprog_app_user
DROP TABLE ord;

CREATE TABLE ord(
    tysk varchar(250),
    dansk varchar(250)
);
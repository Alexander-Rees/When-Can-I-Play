CREATE DATABASE [DB_NAME];
GRANT ALL PRIVILEGES ON [DB_NAME].* TO 'webapp'@'%';
FLUSH PRIVILEGES;

USE DB_NAME;

CREATE TABLE administrator
(
    adminID      INT AUTO_INCREMENT NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    email        VARCHAR(50) NOT NULL,
    first_name   VARCHAR(50) NOT NULL,
    middle_name  VARCHAR(50),
    last_name    VARCHAR(50) NOT NULL,
    PRIMARY KEY (adminID),
    CONSTRAINT Unique_Contact_Info UNIQUE (phone_number, email)
);

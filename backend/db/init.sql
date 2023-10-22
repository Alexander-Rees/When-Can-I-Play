CREATE DATABASE [When_Can_I_Play_DB];
GRANT ALL PRIVILEGES ON [When_Can_I_Play_DB].* TO 'webapp'@'%';
FLUSH PRIVILEGES;

USE When_Can_I_Play_DB;

CREATE TABLE slots
(
    slotID      INT AUTO_INCREMENT NOT NULL,
    startTime        datetime NOT NULL,
    endTime          datetime NOT NULL,
    sport   VARCHAR(50) NOT NULL,
    createdAt   datetime default CURRENT_TIMESTAMP NOT NULL,
    updatedAt    datetime default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP NOT NULL,
    subSection ENUM('1A', '1B', '2A', '2B')
    PRIMARY KEY (slotID),
);

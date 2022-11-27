--liquibase formatted sql

--changeset jfs:1
CREATE DATABASE IF NOT EXISTS `isbn22` DEFAULT CHARACTER SET latin1 
COLLATE latin1_swedish_ci;
USE `isbn22`;

CREATE TABLE IF NOT EXISTS `isbn22`.`isbn` (
  `isbn_id` INT NOT NULL AUTO_INCREMENT,
  `isbn` CHAR(13) NOT NULL,
  `year` VARCHAR(4) NULL DEFAULT NULL,
  `publisher` VARCHAR(50) NULL DEFAULT NULL,
  `author` VARCHAR(250) NULL DEFAULT NULL,
  `title` VARCHAR(500) NOT NULL,
  `genre` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`isbn_id`),
  UNIQUE INDEX `isbn` (`isbn` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 3022
DEFAULT CHARACTER SET = utf8mb3;


CREATE TABLE IF NOT EXISTS `isbn22`.`cQuery` (
  `cq_id` INT NOT NULL AUTO_INCREMENT,
  `cq_name` VARCHAR(100) NOT NULL,
  `cq_desc` TEXT NOT NULL,
  `cq_type` VARCHAR(100) NOT NULL,
  `cq_query` VARCHAR(500) NOT NULL,
  `cq_creator` VARCHAR(100) NOT NULL,
  `cq_created` DATE NOT NULL,
  PRIMARY KEY (`cq_id`),
  UNIQUE INDEX `cq_name_value_UNIQUE` (`cq_name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2028
DEFAULT CHARACTER SET = utf8mb3;


CREATE TABLE IF NOT EXISTS `isbn22`.`cqType` (
  `cqType_id` INT NOT NULL AUTO_INCREMENT,
  `cqType_name` VARCHAR(100) NOT NULL,
  `cqType_desc` TEXT NOT NULL,
  PRIMARY KEY (`cqType_id`),
  UNIQUE INDEX `cqType_name_value_UNIQUE` (`cqType_name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;

--changeset jfs:2
USE isbn22;
CREATE TABLE IF NOT EXISTS `isbn22`.`genre` (
  `genre_id` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(13) NOT NULL,
  `description` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`genre_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

--changeset jfs:3
USE isbn22;
INSERT INTO genre(value, description) VALUES ('1', 'tech');
INSERT INTO genre(value, description) VALUES ('2', 'hobby');
INSERT INTO genre(value, description) VALUES ('3', 'cooking');
INSERT INTO genre(value, description) VALUES ('4', 'fiction');
INSERT INTO genre(value, description) VALUES ('5', 'non-fiction');

--changeset jfs:4
USE isbn22;
INSERT INTO cqType(cqType_name, cqType_desc) VALUES ('test', 'testing query');
INSERT INTO cqType(cqType_name, cqType_desc) VALUES ('search', 'search query');

--changeset jfs:5
--11-14-2022
USE isbn22;
ALTER TABLE genre MODIFY COLUMN value int;

--changeset jfs:6
--11-14-2022
ALTER TABLE isbn MODIFY COLUMN genre int;

--changeset jfs:7
--11-14-2022
ALTER TABLE isbn ADD CONSTRAINT FK_genreisbn FOREIGN KEY(genre) 
REFERENCES genre(value) ON DELETE CASCADE ON UPDATE CASCADE;

--changeset jfs:8
--11-14-2022
USE isbn22;
ALTER TABLE cqType ADD COLUMN cqType_value varchar(11) NOT NULL AFTER cqType_id;
UPDATE cqType SET cqType_value = '1' WHERE cqType_name = 'test';
UPDATE cqType SET cqType_value = '2' WHERE cqType_name = 'search';
ALTER TABLE cqType ADD UNIQUE(cqType_value);

--changeset jfs:9
--11-14-2022
USE isbn22;
ALTER TABLE cQuery ADD CONSTRAINT FK_cqTypecQuery FOREIGN KEY(cq_type)
REFERENCES cqType(cqType_value) ON DELETE CASCADE ON UPDATE CASCADE;

--changeset jfs:10
--11-14-2022
--add another query type
USE isbn22;
INSERT INTO cqType (cqType_value, cqType_name, cqType_desc) 
VALUES ('4', 'list', 'general list of records');

-- MySQL dump performed 11/14/2022 isbn22dump11_14_2022.sql

--changeset jfs:11
--11-19-2022
-- create cqType view to display value, name, and desc
USE isbn22;
CREATE OR REPLACE VIEW cqTypeView AS SELECT cqType_value AS "value",
            cqType_name AS "name", cqType_desc AS "description" FROM cqType;

--changeset jfs:12
--11-24-2022
--add parameters column to cQuery
USE isbn22;
ALTER TABLE cQuery ADD COLUMN cq_parameters TINYINT(1) AFTER cq_created;

--changeset jfs:13
--11-24-2022
--set cQuery.cq_parameters NOT NULL
USE isbn22;
ALTER TABLE cQuery MODIFY cq_parameters TINYINT(1) NOT NULL;

--changeset jfs:14
--11-26-2022
--add column "cq_filter" to cQuery to hold actual query text
USE isbn22;
ALTER TABLE cQuery ADD COLUMN cq_filter VARCHAR(500) AFTER cq_type;
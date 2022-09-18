
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema wowprmds
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `isbn22` DEFAULT CHARACTER SET utf8 ;
USE `isbn22` ;

-- -----------------------------------------------------
-- Table `isbn22`.`isbn`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `isbn22`.`isbn` (
  `isbn_id` INT(11) NOT NULL AUTO_INCREMENT,
  `isbn` CHAR(13) NOT NULL,
  `year` SMALLINT(4),
  `publisher` VARCHAR(50),
  `author` VARCHAR(50),
  `title` VARCHAR(100) NOT NULL,
  `genre` VARCHAR(50),
  PRIMARY KEY (`isbn_id`),
  UNIQUE INDEX `isbn_value_UNIQUE` (`isbn` ASC))
ENGINE = InnoDB;

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema wowprmds
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `isbn22` DEFAULT CHARACTER SET utf8 ;
USE `isbn22` ;

-- -----------------------------------------------------
-- Table `isbn22`.`cqType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `isbn22`.`cqType` (
  `cqType_id` INT(11) NOT NULL AUTO_INCREMENT,
  `cqType_name` VARCHAR(100) NOT NULL,
  `cqType_desc` TEXT(1000) NOT NULL,
  PRIMARY KEY (`cqType_id`),
  UNIQUE INDEX `cqType_name_value_UNIQUE` (`cqType_name` ASC))
ENGINE = InnoDB;35.5
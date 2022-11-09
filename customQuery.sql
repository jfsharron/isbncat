-- Active: 1667085731689@@192.168.2.107@3306@isbn22
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema wowprmds
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `isbn22` DEFAULT CHARACTER SET utf8 ;
USE `isbn22` ;

-- -----------------------------------------------------
-- Table `isbn22`.`customQuery`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `isbn22`.`cQuery` (
  `cq_id` INT(11) NOT NULL AUTO_INCREMENT,
  `cq_name` VARCHAR(100) NOT NULL,
  `cq_desc` TEXT(1000) NOT NULL,
  `cq_type` VARCHAR(100) NOT NULL,
  `cq_query` VARCHAR(500) NOT NULL,
  `cq_creator` VARCHAR(100) NOT NULL,
  `cq_created` DATE NOT NULL,
  PRIMARY KEY (`cq_id`),
  UNIQUE INDEX `cq_name_value_UNIQUE` (`cq_name` ASC))
ENGINE = InnoDB;

ALTER TABLE cQuery AUTO_INCREMENT=2022;
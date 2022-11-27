-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: isbn22
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `DATABASECHANGELOG`
--

DROP TABLE IF EXISTS `DATABASECHANGELOG`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DATABASECHANGELOG` (
  `ID` varchar(255) NOT NULL,
  `AUTHOR` varchar(255) NOT NULL,
  `FILENAME` varchar(255) NOT NULL,
  `DATEEXECUTED` datetime NOT NULL,
  `ORDEREXECUTED` int NOT NULL,
  `EXECTYPE` varchar(10) NOT NULL,
  `MD5SUM` varchar(35) DEFAULT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `COMMENTS` varchar(255) DEFAULT NULL,
  `TAG` varchar(255) DEFAULT NULL,
  `LIQUIBASE` varchar(20) DEFAULT NULL,
  `CONTEXTS` varchar(255) DEFAULT NULL,
  `LABELS` varchar(255) DEFAULT NULL,
  `DEPLOYMENT_ID` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DATABASECHANGELOG`
--

LOCK TABLES `DATABASECHANGELOG` WRITE;
/*!40000 ALTER TABLE `DATABASECHANGELOG` DISABLE KEYS */;
INSERT INTO `DATABASECHANGELOG` VALUES ('1','jfs','changelog.sql','2022-11-09 19:07:54',1,'EXECUTED','8:a55707768d31cea835f8631aa455e5c7','sql','',NULL,'4.6.1',NULL,NULL,'8020871241'),('2','jfs','changelog.sql','2022-11-12 19:54:42',2,'EXECUTED','8:e6a2750d431acca7bf04ec816bb63b96','sql','',NULL,'4.6.1',NULL,NULL,'8282881193'),('3','jfs','changelog.sql','2022-11-12 19:54:42',3,'EXECUTED','8:258dde88bfa051f91e1477a9a1120157','sql','',NULL,'4.6.1',NULL,NULL,'8282881193'),('4','jfs','changelog.sql','2022-11-12 19:54:42',4,'EXECUTED','8:be743e8de036c3545bf4d603a79e2745','sql','',NULL,'4.6.1',NULL,NULL,'8282881193'),('5','jfs','changelog.sql','2022-11-14 23:17:31',5,'EXECUTED','8:aa83c8994885da856b84e673ddd4787b','sql','',NULL,'4.6.1',NULL,NULL,'8467849821'),('6','jfs','changelog.sql','2022-11-14 23:24:04',6,'EXECUTED','8:9fd6d35b41d8736316598f7e2029459b','sql','',NULL,'4.6.1',NULL,NULL,'8468244266'),('7','jfs','changelog.sql','2022-11-14 23:24:07',7,'EXECUTED','8:126de58ee647dd3cfc3633d355a1bf66','sql','',NULL,'4.6.1',NULL,NULL,'8468244266'),('8','jfs','changelog.sql','2022-11-14 23:24:08',8,'EXECUTED','8:3ab5ca63265b45afc639dd384ca5e267','sql','',NULL,'4.6.1',NULL,NULL,'8468244266'),('9','jfs','changelog.sql','2022-11-14 23:24:09',9,'EXECUTED','8:08e5c4c27a731b4a0db80c1c311a39e1','sql','',NULL,'4.6.1',NULL,NULL,'8468244266'),('10','jfs','changelog.sql','2022-11-14 23:24:09',10,'EXECUTED','8:455042bdc9be4dc05481557d2785392a','sql','',NULL,'4.6.1',NULL,NULL,'8468244266');
/*!40000 ALTER TABLE `DATABASECHANGELOG` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DATABASECHANGELOGLOCK`
--

DROP TABLE IF EXISTS `DATABASECHANGELOGLOCK`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DATABASECHANGELOGLOCK` (
  `ID` int NOT NULL,
  `LOCKED` bit(1) NOT NULL,
  `LOCKGRANTED` datetime DEFAULT NULL,
  `LOCKEDBY` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DATABASECHANGELOGLOCK`
--

LOCK TABLES `DATABASECHANGELOGLOCK` WRITE;
/*!40000 ALTER TABLE `DATABASECHANGELOGLOCK` DISABLE KEYS */;
INSERT INTO `DATABASECHANGELOGLOCK` VALUES (1,_binary '\0',NULL,NULL);
/*!40000 ALTER TABLE `DATABASECHANGELOGLOCK` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cQuery`
--

DROP TABLE IF EXISTS `cQuery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cQuery` (
  `cq_id` int NOT NULL AUTO_INCREMENT,
  `cq_name` varchar(100) NOT NULL,
  `cq_desc` text NOT NULL,
  `cq_type` varchar(100) NOT NULL,
  `cq_query` varchar(500) NOT NULL,
  `cq_creator` varchar(100) NOT NULL,
  `cq_created` date NOT NULL,
  PRIMARY KEY (`cq_id`),
  UNIQUE KEY `cq_name_value_UNIQUE` (`cq_name`),
  KEY `FK_cqTypecQuery` (`cq_type`),
  CONSTRAINT `FK_cqTypecQuery` FOREIGN KEY (`cq_type`) REFERENCES `cqType` (`cqType_value`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2029 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cQuery`
--

LOCK TABLES `cQuery` WRITE;
/*!40000 ALTER TABLE `cQuery` DISABLE KEYS */;
INSERT INTO `cQuery` VALUES (2028,'test01','test set','2','SELECT * FROM isbn where year=2014','jfsharron','2022-11-13');
/*!40000 ALTER TABLE `cQuery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cqType`
--

DROP TABLE IF EXISTS `cqType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cqType` (
  `cqType_id` int NOT NULL AUTO_INCREMENT,
  `cqType_value` varchar(11) NOT NULL,
  `cqType_name` varchar(100) NOT NULL,
  `cqType_desc` text NOT NULL,
  PRIMARY KEY (`cqType_id`),
  UNIQUE KEY `cqType_name_value_UNIQUE` (`cqType_name`),
  UNIQUE KEY `cqType_value` (`cqType_value`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cqType`
--

LOCK TABLES `cqType` WRITE;
/*!40000 ALTER TABLE `cqType` DISABLE KEYS */;
INSERT INTO `cqType` VALUES (2,'1','test','testing query'),(3,'2','search','search query'),(4,'4','list','general list of records');
/*!40000 ALTER TABLE `cqType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `genre_id` int NOT NULL AUTO_INCREMENT,
  `value` int DEFAULT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`genre_id`),
  UNIQUE KEY `value` (`value`),
  UNIQUE KEY `value_2` (`value`),
  UNIQUE KEY `value_3` (`value`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,1,'tech'),(2,2,'hobby'),(3,3,'cooking'),(4,4,'fiction'),(5,5,'non-fiction');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `isbn`
--

DROP TABLE IF EXISTS `isbn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `isbn` (
  `isbn_id` int NOT NULL AUTO_INCREMENT,
  `isbn` char(13) NOT NULL,
  `year` varchar(4) DEFAULT NULL,
  `publisher` varchar(50) DEFAULT NULL,
  `author` varchar(250) DEFAULT NULL,
  `title` varchar(500) NOT NULL,
  `genre` int DEFAULT NULL,
  PRIMARY KEY (`isbn_id`),
  UNIQUE KEY `isbn` (`isbn`),
  KEY `FK_genreisbn` (`genre`),
  CONSTRAINT `FK_genreisbn` FOREIGN KEY (`genre`) REFERENCES `genre` (`value`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3082 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `isbn`
--

LOCK TABLES `isbn` WRITE;
/*!40000 ALTER TABLE `isbn` DISABLE KEYS */;
INSERT INTO `isbn` VALUES (3022,'9780073517216','2009','McGraw-Hill Education','Julia Case Bradley, Anita Millspaugh','Programming In Visual C# 2008',1),(3023,'9780201563177','1992','Addison-Wesley Professional','W. Richard Stevens, W... Richard Stevens','Advanced Programming In The UNIX Environment',1),(3024,'9781593272203','2010','No Starch Press','Michael Kerrisk','The Linux Programming Interface - A Linux And UNIX System Programming Handbook',1),(3025,'9780764548338','2002','Wiley','Guy Lotgering, Universal Command Guide (UCG) Training Team','Universal Command Guide - For Operating Systems',1),(3026,'9781565924277','1999','O\'Reilly Media, Inc.','Arnold Robbins, \"OReilly & Associates\"','UNIX In A Nutshell - A Desktop Quick Reference For System V Release 4 And Solaris 7',1),(3027,'9780471168942','1997','John Wiley & Sons Incorporated','Lowell Jay Arthur, Ted Burns','UNIX Shell Programming',1),(3028,'9780672311079','1997','Sams Publishing','Dave Taylor, James C. Armstrong (Jr.)','Teach Yourself UNIX In 24 Hours',1),(3029,'9781491931257','2018','O\'Reilly Media','Jason Edelman, Scott S. Lowe, Matt Oswalt','Network Programmability And Automation',1),(3030,'9781491979808','2017','O\'Reilly Media','Lorin Hochstein, Rene Moser','Ansible: Up And Running - Automating Configuration Management And Deployment The Easy Way',1),(3031,'9781491924358','2016','O\'Reilly Media','Kief Morris','Infrastructure As Code - Managing Servers In The Cloud',1),(3032,'9781449387860','2011','O\'Reilly Media, Inc.','Gary Donahue','Network Warrior',1),(3033,'9781578700479','1998','Sams Publishing','Tim Hill','Windows NT Shell Scripting',1),(3034,'9780132360395','2008','Prentice-Hall PTR','Mark G. Sobell','A Practical Guide To Ubuntu Linux',1),(3035,'9780596000257','2000','','Ellen Siever','Linux In A Nutshell - A Quick Desktop Reference',1),(3036,'9781593273897','2012','No Starch Press','William E. Shotts, Jr.','The Linux Command Line - A Complete Introduction',1),(3037,'9780134496009','2016','Addison-Wesley Professional','Stephen G. Kochan, Patrick Wood','Shell Programming In Unix, Linux And OS X',1),(3038,'9781118983843','2015','John Wiley & Sons','Richard Blum, Christine Bresnahan','Linux Command Line And Shell Scripting Bible',1),(3039,'9781119722335','2020','John Wiley & Sons','David Clinton, Christopher Negus','Ubuntu Linux Bible',1),(3040,'9780134277554','2017','Prentice Hall','Evi Nemeth, Garth Snyder, Ben Whaley, Trent Hein','Unix And Linux System Administration Handbook',1),(3041,'9780130206015','2001','Prentice Hall','Evi Nemeth, Garth Snyder, Adam Boggs, Scott Seebass, Trent H. Hein, Trent R. Hein','Unix System Administration Handbook',1),(3042,'9781509300914','2016','Microsoft Press','Paolo Pialorsi','Programming Microsoft Office 365 - Covers Microsoft Graph, Office 365 Applications, Sharepoint Add-Ins, Office 365 Groups, And More',1),(3043,'9781788990554','2018','Packt Publishing','Mokhtar Ebrahim, Andrew Mallett','Mastering Linux Shell Scripting - Second Edition',1),(3044,'9781784399597','2015','Packt Publishing','Jay LaCroix','Mastering Linux Network Administration',1),(3045,'9781800564640','2020','','Jay LaCroix','Mastering Ubuntu Server - Third Edition - Gain Expertise In The Art Of Deploying, Configuring, Managing, And Troubleshooting Ubuntu Server',1),(3046,'9781838981778','2020','','Donald A. Tevault','Mastering Linux Security And Hardening - Protect Your Linux Systems From Intruders, Malware Attacks, And Other Cyber Threats, 2Nd Edition',1),(3047,'9780471946939','2007','Wrox','Andrew Watt','Professional Windows PowerShell',1),(3048,'9780982131428','2010','','Don Jones, Jeffery Hicks','Windows PowerShell 2.0 - TFM',1),(3049,'9781617294167','2016','Manning Publications','Donald W. Jones, Jeffrey Hicks','Learn Windows Powershell In A Month Of Lunches',1),(3050,'9781617295096','2017','Manning Publications','Don Jones, Jeffery Hicks','Learn PowerShell Scripting In A Month Of Lunches',1),(3051,'9781593279189','2020','No Starch Press','Adam Bertram','PowerShell For Sysadmins - Workflow Automation Made Easy',1),(3052,'9781565924956','1998','O\'Reilly Media','Johan Vromans','Perl 5 Pocket Reference',1),(3053,'9780596000035','2000','O\'Reilly Media','Gregor N. Purdy','CVS Pocket Reference',1),(3054,'9781565927094','1999','Oreilly & Associates Incorporated','Robert Eckstein','XML Pocket Reference',1),(3055,'9781491927571','2016','O\'Reilly Media','Daniel J. Barrett','Linux Pocket Guide',1),(3056,'9781449305352','2011','O\'Reilly Media, Inc.','John Smart','Jenkins - The Definitive Guide',1),(3057,'9781784390891','2015','Packt Publishing','Jonathan McAllister','Mastering Jenkins',1),(3058,'9781492057697','2020','O\'Reilly Media','Noah Gift, Kennedy Behrman, Alfredo Deza, Robert Jordan, Grig Gheorghiu','Python For DevOps - Learn Ruthlessly Effective Automation',1),(3059,'9781449316389','2012','O\'Reilly Media, Inc.','Jon Loeliger, Matthew McCullough','Version Control With Git - Powerful Tools And Techniques For Collaborative Software Development',1),(3060,'9781119572671','2019','John Wiley & Sons','Sarah Guthals, Phil Haack','GitHub For Dummies',1),(3061,'9781839214189','2020','','PAUL. CRICKARD','DATA ENGINEERING WITH PYTHON - Work With Massive Datasets To Design Data Models And Automate... Data Pipelines Using Python',1),(3062,'9781617293726','2018','Manning Publications','Marko Luksa','Kubernetes In Action',1),(3063,'9781838820756','2020','','','KUBERNETES WORKSHOP - A New, Interactive Approach To Learning Kubernetes',1),(3064,'9781838983444','2020','','Vincent Sesto, Onur Yilmaz, Sathsara Sarathchandra, Aric Renzo, Engy Fouda','The The Docker Workshop - Learn How To Use Docker Containers Effectively To Speed Up The Development Process',1),(3065,'9781617296987','2020','Manning Publications','Jeffery D. Smith','Operations Anti-Patterns, DevOps Solutions',1),(3066,'9781491929124','2016','O\'Reilly Media','Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy','Site Reliability Engineering - How Google Runs Production Systems',1),(3067,'9781492040767','2019','O\'Reilly Media','John Arundel, Justin Domingus','Cloud Native DevOps With Kubernetes - Building, Deploying, And Scaling Modern Applications In The Cloud',1),(3068,'9781838552183','2019','','Rafal Leszko','Continuous Delivery With Docker And Jenkins',1),(3069,'9781484269206','2021','Apress','Anders Lisdorf','Cloud Computing Basics - A Non-Technical Introduction',1),(3070,'9798653385322','2020','','Henry Stromm','Learn Microsoft Azure For Beginners',1),(3071,'9781617294440','2017','Manning Publications','David Clinton','Learn Amazon Web Services In A Month Of Lunches',1),(3072,'9781617297625','2020','Manning Publications','Iain Foulds','Learn Azure In A Month Of Lunches, Second Edition',1),(3073,'9781305880290','2016','Cengage Learning','Mark Shellman, Sasha Vodnik','New Perspectives Microsoft Office 365 & Access 2016: Intermediate',1),(3074,'9780789735973','2007','Que Publishing','Roger Jennings','Special Edition Using Microsoft Office Access 2007',1),(3075,'9780072263503','2007','McGraw-Hill Prof Med/Tech','Virginia Andersen','Microsoft Office Access 2007: The Complete Reference',1),(3076,'9781617297519','2020','Manning Publications','Ken Youens-Clark','Tiny Python Projects',1),(3077,'9781617295508','2020','Manning Publications','Reuven M. Lerner','Python Workout - 50 Ten-Minute Exercises',1),(3078,'9781617295980','2019','Manning Publications','David Kopec','Classic Computer Science Problems In Python',1),(3079,'9780134000022','2015','Pearson Education','Steve Suehring','Linux Firewalls - Enhancing Security With Nftables And Beyond',1),(3080,'9780201835953','2007','','Luke Hohmann','Innovation Games - Creating Breakthrough Products Through Collaborative Play',1),(3081,'9781449357016','2014','Oreilly & Associates Incorporated','Mark Lutz','Python Pocket Reference',1);
/*!40000 ALTER TABLE `isbn` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-14 23:29:41

# HeidiSQL Dump 
#
# --------------------------------------------------------
# Host:                 127.0.0.1
# Database:             newsinfo
# Server version:       5.4.3-beta-community
# Server OS:            Win32
# Target-Compatibility: Standard ANSI SQL
# HeidiSQL version:     3.1 RC1 Revision: 1064
# --------------------------------------------------------

/*!40100 SET CHARACTER SET latin1;*/
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ANSI';*/
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;*/


#
# Database structure for database 'newsinfo'
#

CREATE DATABASE /*!32312 IF NOT EXISTS*/ "newsinfo" /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

USE "newsinfo";


#
# Table structure for table 'matches'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "matches" (
  "match_id" int(11) NOT NULL AUTO_INCREMENT,
  "team1" varchar(50) DEFAULT NULL,
  "team2" varchar(50) DEFAULT NULL,
  "match_date" date DEFAULT NULL,
  "venue" varchar(100) DEFAULT NULL,
  "status" varchar(50) DEFAULT 'Upcoming',
  PRIMARY KEY ("match_id")
) AUTO_INCREMENT=5 /*!40100 DEFAULT CHARSET=utf8 COLLATE=utf8_bin*/;



#
# Dumping data for table 'matches'
#

/*!40000 ALTER TABLE "matches" DISABLE KEYS;*/
LOCK TABLES "matches" WRITE;
REPLACE INTO "matches" ("match_id", "team1", "team2", "match_date", "venue", "status") VALUES
	(2,'CSK','MI','2025-03-22','cheapak','completed');
REPLACE INTO "matches" ("match_id", "team1", "team2", "match_date", "venue", "status") VALUES
	(3,'RCB','DC','2025-03-23','Modi','Completed');
REPLACE INTO "matches" ("match_id", "team1", "team2", "match_date", "venue", "status") VALUES
	(4,'KKR','SRH','4532-03-14','vjk','completed');
UNLOCK TABLES;
/*!40000 ALTER TABLE "matches" ENABLE KEYS;*/


#
# Table structure for table 'newsdetails'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "newsdetails" (
  "Newsid" int(11) NOT NULL AUTO_INCREMENT,
  "newshead" varchar(50) DEFAULT NULL,
  "upload" varchar(50) DEFAULT NULL,
  "category" varchar(50) DEFAULT NULL,
  "Description" varchar(250) DEFAULT NULL,
  PRIMARY KEY ("Newsid")
) AUTO_INCREMENT=6 /*!40100 DEFAULT CHARSET=utf8 COLLATE=utf8_bin*/;



#
# Dumping data for table 'newsdetails'
#

/*!40000 ALTER TABLE "newsdetails" DISABLE KEYS;*/
LOCK TABLES "newsdetails" WRITE;
REPLACE INTO "newsdetails" ("Newsid", "newshead", "upload", "category", "Description") VALUES
	(1,'priya','8975456987','seattlecbe5@gmail.com','cbe');
REPLACE INTO "newsdetails" ("Newsid", "newshead", "upload", "category", "Description") VALUES
	(3,'Exam Results','13.02.2025','Sports','result has released');
REPLACE INTO "newsdetails" ("Newsid", "newshead", "upload", "category", "Description") VALUES
	(4,'india won tas today','2025-02-13','Sports','nil');
REPLACE INTO "newsdetails" ("Newsid", "newshead", "upload", "category", "Description") VALUES
	(5,'Exam Results','2025-02-13','Study','sds');
UNLOCK TABLES;
/*!40000 ALTER TABLE "newsdetails" ENABLE KEYS;*/


#
# Table structure for table 'register'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "register" (
  "Regid" int(11) NOT NULL AUTO_INCREMENT,
  "rname" varchar(50) DEFAULT NULL,
  "contact" varchar(50) DEFAULT NULL,
  "email" varchar(50) DEFAULT NULL,
  "Address" varchar(250) DEFAULT NULL,
  "city" varchar(50) DEFAULT NULL,
  "role" varchar(50) DEFAULT NULL,
  "uname" varchar(50) DEFAULT NULL,
  "password" varchar(50) DEFAULT NULL,
  PRIMARY KEY ("Regid")
) AUTO_INCREMENT=5 /*!40100 DEFAULT CHARSET=utf8 COLLATE=utf8_bin*/;



#
# Dumping data for table 'register'
#

/*!40000 ALTER TABLE "register" DISABLE KEYS;*/
LOCK TABLES "register" WRITE;
REPLACE INTO "register" ("Regid", "rname", "contact", "email", "Address", "city", "role", "uname", "password") VALUES
	(4,'sandhya','09876543210','srcw2338b106@srcw.ac.in','neelambur','coimbatore','User','sandhya','123');
UNLOCK TABLES;
/*!40000 ALTER TABLE "register" ENABLE KEYS;*/


#
# Table structure for table 'scores'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "scores" (
  "match_id" int(11) NOT NULL DEFAULT '0',
  "team" varchar(50) NOT NULL DEFAULT '',
  "runs" int(11) DEFAULT NULL,
  "wickets" int(11) DEFAULT NULL,
  "overs" float DEFAULT NULL,
  PRIMARY KEY ("match_id","team"),
  CONSTRAINT "scores_ibfk_1" FOREIGN KEY ("match_id") REFERENCES "matches" ("match_id") ON DELETE CASCADE
) /*!40100 DEFAULT CHARSET=utf8 COLLATE=utf8_bin*/;



#
# Dumping data for table 'scores'
#

/*!40000 ALTER TABLE "scores" DISABLE KEYS;*/
LOCK TABLES "scores" WRITE;
REPLACE INTO "scores" ("match_id", "team", "runs", "wickets", "overs") VALUES
	(2,'MI',130,8,'19');
UNLOCK TABLES;
/*!40000 ALTER TABLE "scores" ENABLE KEYS;*/
/*!40101 SET SQL_MODE=@OLD_SQL_MODE;*/
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;*/

-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: warsztat1
-- ------------------------------------------------------
-- Server version	5.7.20-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Message`
--

DROP TABLE IF EXISTS `Message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_user` int(11) NOT NULL,
  `to_user` int(11) NOT NULL,
  `text_message` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `create_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `from_user` (`from_user`),
  KEY `to_user` (`to_user`),
  CONSTRAINT `Message_ibfk_1` FOREIGN KEY (`from_user`) REFERENCES `Users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Message_ibfk_2` FOREIGN KEY (`to_user`) REFERENCES `Users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Message`
--

LOCK TABLES `Message` WRITE;
/*!40000 ALTER TABLE `Message` DISABLE KEYS */;
INSERT INTO `Message` VALUES (1,1,24,'moja pierwsza wiadomość','2017-11-22'),(2,1,24,'moja pierwsza wiadomość','2017-11-22'),(3,1,24,'moja pierwsza wiadomość','2017-11-22'),(4,1,24,'moja pierwsza wiadomość','2017-11-22'),(5,1,24,'moja pierwsza wiadomość','2017-11-22'),(6,1,24,'moja pierwsza wiadomość','2017-11-22'),(7,5,15,'moja inna pierwsza wiadomość','2017-11-20'),(8,1,24,'czesc','2017-11-25'),(9,23,24,'czesc','2017-11-25'),(10,23,1,'czesc','2017-11-25'),(11,23,1,'czesc poraz kolejny','2017-11-25'),(12,23,1,'czesc poraz','2017-11-26'),(13,1,15,'zadzwoń jak wróciszpython3 message_option.py -u marcin -p marcin123 -l!','2017-11-26'),(14,1,23,'jesteś już?','2017-11-26'),(15,1,1,'jesteś już?','2017-11-26'),(16,1,16,'co na obiad?','2017-11-26');
/*!40000 ALTER TABLE `Message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emeil` varchar(255) COLLATE utf8_polish_ci NOT NULL,
  `username` varchar(255) COLLATE utf8_polish_ci NOT NULL,
  `hashed_password` varchar(255) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `emeil` (`emeil`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'trellcia@poczta.onet.pl','marcin','aaaaaaaaaaaaaaaa6d81e7e6f38e17e05008b5c49810f5f83d8cbc44d02794b41641fc9c07fed8ec'),(3,'mala@mapl.pl','figofago','mojeaaaaaaaaaaaa9b8bde6643d2caab26b2d5759fa06af8a1c4c93886e399662497d7c5809575dc'),(5,'met@pl.pl','paparapa1','mojeaaaaaaaaaaaa9b8bde6643d2caab26b2d5759fa06af8a1c4c93886e399662497d7c5809575dc'),(12,'kott@pl.pl','paparapa1','mojeaaaaaaaaaaaa9b8bde6643d2caab26b2d5759fa06af8a1c4c93886e399662497d7c5809575dc'),(13,'mala@koko.pl','ola','xKQjwf6OvbFp1RmIdb6f0461733b547831507860f2fb58aaceff67768eef353333f2277d37c938a1'),(14,'marcin@op.pl','marcin','HrH7goonqwMKo0j64d1e5eae5c117fa7b403eecbfb787129780be39a66e918c6dec5e5c89f68e27b'),(15,'tola@tola.pl','tola','8j0vtQULbwbQOIHW1feff745878ead8bb1568553d82295cece0fb1607f94ac8042d7016e6a2e650d'),(16,'bolola@bolola.pl','marcin','67MaYodtGH4aZFYN235a9da06962911a5ac4fece4247b7f46917ec8453151e28535b72455ea25b62'),(20,'bolas@bolas.pl','marcin','DjYrawAQXT9quhSS6982b5f1d6fedaaf809f7e08593953ad0d944b21e0c24fdad881712005211572'),(21,'wladek@wladek.pl','wladek','TZ6I1suOqCa7D7Hg47baf6039be8b6bbd6842951fc8fab2862bbd28bd3b61fe11e0c6f4205969919'),(22,'wladziu@wladek.pl','wladek','XXTPULI9cveKDGvWed82596e83313fec49978269f83e3e992e5daa7366de9ba2d68a472e5ef2697d'),(23,'mariola@mariola.pl','mariola','DDNyt1LXx0zH74Lf40068c19bb56d9a61a4d30d0ac608aa7222430ab874618fa208cfdb87e3871eb'),(24,'mariola123@mariola.pl','mariola','onxOMCqxwQThqZ9Zf2e1531779df2b787e7e4e242105339846ef8139dafa88e577f9803dbcf5f53d');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-26 10:55:56

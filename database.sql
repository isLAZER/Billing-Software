-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: python
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `item_storage`
--

DROP TABLE IF EXISTS `item_storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_storage` (
  `ITEM_ID` int NOT NULL AUTO_INCREMENT,
  `ITEM_CODE` varchar(4) DEFAULT NULL,
  `STORED_ITEMS` int DEFAULT NULL,
  PRIMARY KEY (`ITEM_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_storage`
--

LOCK TABLES `item_storage` WRITE;
/*!40000 ALTER TABLE `item_storage` DISABLE KEYS */;
INSERT INTO `item_storage` VALUES (1,'N1',100),(2,'N2',100),(3,'N3',100),(4,'N4',100),(5,'N5',100),(6,'N6',100),(7,'N7',100),(8,'N8',100);
/*!40000 ALTER TABLE `item_storage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productinfo`
--

DROP TABLE IF EXISTS `productinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productinfo` (
  `ITEM_CODE` varchar(4) NOT NULL,
  `ITEM_NAME` varchar(15) DEFAULT NULL,
  `PRICE` int DEFAULT NULL,
  `DISCOUNT` varchar(5) DEFAULT NULL,
  `BRAND` varchar(15) DEFAULT NULL,
  `CATEGORY` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ITEM_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productinfo`
--

LOCK TABLES `productinfo` WRITE;
/*!40000 ALTER TABLE `productinfo` DISABLE KEYS */;
INSERT INTO `productinfo` VALUES ('N1','Xbox',49999,'5%','Microsoft','Console'),('N2','PlayStation',34999,'12%','Sony','Console'),('N3','Minecraft',2999,'20%','Microsoft','Video Game'),('N4','Switch',31999,'10%','Nintendo','Console'),('N5','Pokemon',1999,'5%','Nintendo','Video Game'),('N6','Spiderman',3999,'5%','Sony','Video Game'),('N7','Super Mario',2499,'8%','Nintendo','Video Game'),('N8','Mario Kart',2199,'10%','Nintendo','Video Game');
/*!40000 ALTER TABLE `productinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `R_ID` int NOT NULL AUTO_INCREMENT,
  `ITEM_CODE` varchar(4) DEFAULT NULL,
  `SELLING_PRICE` int DEFAULT NULL,
  `COST_PRICE` int DEFAULT NULL,
  PRIMARY KEY (`R_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES (1,'N1',49999,39000),(2,'N2',34999,30000),(3,'N3',2999,1900),(4,'N4',31999,30000),(5,'N5',1999,900),(6,'N6',3999,3100),(7,'N7',2499,2100),(8,'N8',2199,1800);
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stocks`
--

DROP TABLE IF EXISTS `stocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stocks` (
  `ITEM_CODE` varchar(5) NOT NULL,
  `PRICE` int DEFAULT NULL,
  `STOCK` int DEFAULT NULL,
  `SUPPLIER_ID` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`ITEM_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocks`
--

LOCK TABLES `stocks` WRITE;
/*!40000 ALTER TABLE `stocks` DISABLE KEYS */;
INSERT INTO `stocks` VALUES ('N1',49999,59,'S002'),('N2',34999,60,'S004'),('N3',2999,80,'S001'),('N4',31999,11,'S002'),('N5',1999,100,'S001'),('N6',3999,80,'S003'),('N7',2499,100,'S002'),('N8',2199,100,'S005');
/*!40000 ALTER TABLE `stocks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `S.NO` int NOT NULL AUTO_INCREMENT,
  `SUPP_ID` varchar(5) DEFAULT NULL,
  `SUPP_NAME` varchar(20) DEFAULT NULL,
  `CONTACT` varchar(15) DEFAULT NULL,
  `LOCATION` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`S.NO`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'S001','Mark incorp.','7055 822371','US'),(2,'S002','Suncity Lmt.','7055 837912','US'),(3,'S003','Berlint Corp.','7055 773854','US'),(4,'S004','Ken COR.','7055 647944','US'),(5,'S005','Forger Corp.','7055 934664','US');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-03 17:45:23

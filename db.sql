-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: aaa
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (9,'Зайцев Роман Григорьевич'),(10,'Трофимов Петр Олегович'),(11,'Иванов Егор Григорьевич'),(12,'Горбунов Иван Григорьевич'),(13,'Виноградов Михаил Вячеславович'),(14,'Матвеев Александр Григорьевич'),(15,'Виноградов Олег Артемович'),(16,'Богданов Владимир Артемович'),(17,'Кузнецов Олег Петрович'),(18,'Богданов Максим Юрьевич'),(19,'Трофимов Виктор Сергеевич'),(20,'Сидоров Виктор Борисович'),(21,'Федоров Роман Анатольевич'),(22,'Федоров Кирилл Владимирович'),(23,'Лебедев Артем Михайлович'),(24,'Матвеев Максим Игоревич'),(25,'Титов Роман Сидорович'),(26,'Матвеев Роман Григорьевич'),(27,'Титов Виталий Сидорович'),(28,'Смирнов Андрей Николаевич'),(29,'Трофимов Виталий Алексеевич'),(30,'Петров Сергей Олегович'),(31,'Куликов Максим Васильевич'),(32,'Зайцев Виталий Олегович'),(33,'Куликов Алексей Петрович'),(34,'Куликов Владимир Михайлович'),(35,'Виноградов Дмитрий Николаевич'),(36,'Горбунов Артем Петрович'),(37,'Федоров Роман Вячеславович'),(38,'Соколов Николай Васильевич'),(39,'Смирнов Виктор Васильевич'),(40,'Кузнецов Максим Вячеславович'),(41,'Лебедев Максим Викторович'),(42,'Иванов Андрей Алексеевич'),(43,'Куликов Сергей Андреевич'),(44,'Сидоров Дмитрий Егорович'),(45,'Куликов Андрей Григорьевич'),(46,'Морозов Сергей Олегович'),(47,'Сидоров Алексей Михайлович'),(48,'Лебедев Игорь Анатольевич'),(49,'Петров Виталий Михайлович'),(50,'Куликов Кирилл Борисович'),(51,'Сидоров Егор Борисович'),(52,'Попов Александр Сидорович'),(53,'Смирнов Александр Васильевич'),(54,'Кузнецов Олег Игоревич'),(55,'Новиков Игорь Григорьевич'),(56,'Зайцев Дмитрий Иванович'),(57,'Матвеев Михаил Алексеевич'),(58,'Матвеев Владимир Григорьевич'),(59,'Соколов Артем Вячеславович'),(60,'Трофимов Александр Алексеевич'),(61,'Трофимов Андрей Игоревич'),(62,'Горбунов Николай Артемович'),(63,'Волков Петр Артемович'),(64,'Богданов Петр Игоревич'),(65,'Иванов Петр Андреевич'),(66,'Богданов Виктор Олегович'),(67,'Зайцев Олег Артемович'),(68,'Петров Андрей Григорьевич'),(69,'Иванов Виталий Владимирович'),(70,'Лебедев Сергей Николаевич'),(71,'Виноградов Николай Артемович'),(72,'Куликов Иван Алексеевич'),(73,'Иванов Андрей Николаевич'),(74,'Богданов Петр Сидорович'),(75,'Иванов Николай Васильевич'),(76,'Соколов Михаил Анатольевич'),(77,'Зайцев Кирилл Егорович'),(78,'Соколов Кирилл Викторович'),(79,'Иванов Максим Игоревич'),(80,'Петров Алексей Викторович'),(81,'Соколов Кирилл Викторович'),(82,'Сидоров Иван Игоревич'),(83,'Виноградов Кирилл Николаевич'),(84,'Попов Сергей Юрьевич'),(85,'Богданов Александр Егорович'),(86,'Виноградов Станислав Иванович'),(87,'Куликов Виталий Сергеевич'),(88,'Кузнецов Алексей Алексеевич'),(89,'Лебедев Иван Васильевич'),(90,'Богданов Виктор Михайлович'),(91,'Новиков Андрей Иванович'),(92,'Сидоров Олег Вячеславович'),(93,'Сидоров Владимир Олегович'),(94,'Матвеев Михаил Андреевич'),(95,'Федоров Виктор Вячеславович'),(96,'Зайцев Дмитрий Юрьевич'),(97,'Иванов Олег Борисович'),(98,'Зайцев Владимир Вячеславович'),(99,'Смирнов Николай Петрович'),(100,'Федоров Андрей Юрьевич'),(101,'Попов Иван Васильевич'),(102,'Попов Владимир Анатольевич'),(103,'Богданов Михаил Петрович'),(104,'Смирнов Владимир Николаевич'),(105,'Титов Станислав Михайлович'),(106,'Титов Егор Анатольевич'),(107,'Матвеев Олег Вячеславович'),(108,'Кузнецов Михаил Васильевич');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dish_name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Суп',150.00),(2,'Курица с картофелем',300.00),(3,'Салат Цезарь',250.00),(4,'Сок',50.00),(5,'Пицца',500.00),(6,'Кофе',100.00),(7,'Борщ',200.00),(8,'Компот',50.00),(9,'Рыба с рисом',350.00),(10,'Зеленый чай',80.00),(11,'Шашлык',600.00),(12,'Пиво',120.00),(13,'Лапша удон',764.04),(14,'Суши',654.58),(15,'Блины',820.17),(16,'Лазанья',878.45),(17,'Тушёная капуста',412.05),(18,'Чай',161.74),(19,'Ризотто',504.77),(20,'Салат Цезарь',822.18),(21,'Рыба с рисом',680.97),(22,'Роллы',841.16),(23,'Пельмени',625.52),(24,'Кофе',835.57),(25,'Вареники',381.41),(26,'Капучино',683.87),(27,'Смузи',373.23),(28,'Чизкейк',714.57),(29,'Пицца',995.74),(30,'Сэндвич',218.27),(31,'Компот',484.56),(32,'Пюре из брокколи',161.63),(33,'Курица с картофелем',709.64),(34,'Грибной суп',298.18),(35,'Брускетта',891.04),(36,'Греческий салат',609.38),(37,'Суп',711.96),(38,'Паста',843.02),(39,'Жареная рыба',570.32),(40,'Стейк',837.11),(41,'Куринный бургер',732.35),(42,'Карпаччо',703.10),(43,'Мороженое',603.07),(44,'Куриный шашлык',133.80),(45,'Картофельное пюре',338.76),(46,'Сок',362.33),(47,'Омлет',182.18),(48,'Свинина на гриле',935.28),(49,'Пиво',701.05),(50,'Овощной салат',630.35),(51,'Латте',120.48),(52,'Торт',426.80),(53,'Крабовый салат',504.02),(54,'Зеленый чай',645.65),(55,'Шоколадный торт',997.64),(56,'Рататуй',789.45),(57,'Борщ',940.98),(58,'Лимонад',275.08),(59,'Фруктовый салат',903.59),(60,'Гуляш',633.59),(61,'Крем-суп',573.04),(62,'Шашлык',293.39);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `name_id` int NOT NULL,
  `order_description_id` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `status` varchar(50) NOT NULL,
  `table_name` int NOT NULL,
  `waiter_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name_id` (`name_id`),
  KEY `order_description_id` (`order_description_id`),
  KEY `fk_waiter` (`waiter_id`),
  CONSTRAINT `fk_waiter` FOREIGN KEY (`waiter_id`) REFERENCES `waiters` (`id`) ON DELETE SET NULL,
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`name_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (201,'2024-11-25','10:02:00',97,'50',445.00,'Оформлен',4,55),(202,'2024-11-21','14:38:00',61,'62',125.00,'Оформлен',3,53),(203,'2024-11-26','16:18:00',90,'12;31;54',1072.00,'Готовится',2,56),(204,'2024-11-26','17:52:00',105,'62;8',537.00,'Оформлен',1,44),(205,'2024-11-26','08:45:00',36,'38',406.00,'Готовится',4,45),(206,'2024-11-23','14:21:00',34,'17',154.00,'Оплачен',2,53),(207,'2024-11-25','22:58:00',88,'50',201.00,'Готовится',4,57),(208,'2024-11-27','09:01:00',57,'2',329.00,'Готовится',1,58),(209,'2024-11-26','08:20:00',65,'22;12',446.00,'Оплачен',2,41),(210,'2024-11-23','21:40:00',9,'33;52',631.00,'Оформлен',6,51),(211,'2024-11-22','16:10:00',52,'44',442.00,'Готовится',1,49),(212,'2024-11-22','08:30:00',29,'20',387.00,'Готовится',3,50),(213,'2024-11-21','21:12:00',67,'1;22;51',858.00,'Готовится',4,43),(214,'2024-11-26','13:19:00',41,'10;26;50',1114.00,'Оплачен',1,53),(215,'2024-11-23','19:19:00',71,'33',103.00,'Оформлен',1,54),(216,'2024-11-24','17:21:00',81,'11',187.00,'Оформлен',2,41),(217,'2024-11-27','12:20:00',64,'4;60;5',901.00,'Оформлен',5,49),(218,'2024-11-24','09:44:00',14,'55',492.00,'Оформлен',6,51),(219,'2024-11-27','10:41:00',42,'54;58',647.00,'Готовится',5,41),(220,'2024-11-24','21:28:00',12,'39',428.00,'Готовится',1,57),(221,'2024-11-27','22:57:00',70,'20;52;10',1191.00,'Оформлен',2,57),(222,'2024-11-22','11:12:00',85,'3',473.00,'Готовится',5,41),(223,'2024-11-27','11:31:00',33,'40;3',597.00,'Готовится',6,45),(224,'2024-11-21','09:55:00',74,'5',271.00,'Оформлен',6,57),(225,'2024-11-22','08:32:00',11,'11;38;61',899.00,'Готовится',5,52),(226,'2024-11-21','08:44:00',15,'40',131.00,'Оплачен',2,56),(227,'2024-11-22','13:41:00',15,'4;43',656.00,'Оформлен',2,53),(228,'2024-11-23','10:31:00',88,'21;18;37',1097.00,'Оплачен',2,44),(229,'2024-11-27','14:21:00',74,'62',477.00,'Оплачен',4,45),(230,'2024-11-25','22:49:00',28,'47;30',532.00,'Оплачен',5,60),(231,'2024-11-26','09:35:00',25,'61;7;6',633.00,'Готовится',6,59),(232,'2024-11-25','18:43:00',93,'25;16;49',1022.00,'Оплачен',1,54),(233,'2024-11-25','10:59:00',67,'19;51',249.00,'Оплачен',4,41),(234,'2024-11-22','12:04:00',84,'17;53;48',814.00,'Оформлен',3,47),(235,'2024-11-25','14:31:00',33,'17',379.00,'Оформлен',2,48),(236,'2024-11-26','18:15:00',87,'57;30;35',1027.00,'Оформлен',3,53),(237,'2024-11-25','20:24:00',95,'14',184.00,'Готовится',1,57),(238,'2024-11-25','20:40:00',99,'5',475.00,'Оплачен',2,47),(239,'2024-11-26','16:41:00',70,'21',223.00,'Оформлен',2,58),(240,'2024-11-22','16:50:00',42,'52;42;6',1167.00,'Готовится',3,42),(241,'2024-11-26','15:06:00',53,'49',407.00,'Оформлен',6,42),(242,'2024-11-21','08:17:00',107,'35;23;21',1179.00,'Готовится',1,57),(243,'2024-11-24','18:50:00',35,'28',187.00,'Оформлен',2,50),(244,'2024-11-25','12:47:00',97,'45;26',715.00,'Готовится',1,41),(245,'2024-11-25','08:53:00',19,'8;60',614.00,'Готовится',6,56),(246,'2024-11-22','20:52:00',36,'48;5',861.00,'Оформлен',1,52),(247,'2024-11-23','10:19:00',95,'45;35;3',1233.00,'Готовится',1,46),(248,'2024-11-26','15:09:00',79,'46;28;12',1075.00,'Оформлен',1,47),(249,'2024-11-24','21:56:00',88,'11;36;46',826.00,'Оформлен',2,47),(250,'2024-11-27','12:41:00',54,'9',387.00,'Готовится',1,52),(251,'2024-11-22','11:32:00',81,'7',455.00,'Оформлен',1,44),(252,'2024-11-26','08:28:00',51,'1',243.00,'Готовится',3,42),(253,'2024-11-26','17:02:00',23,'15',293.00,'Оплачен',3,52),(254,'2024-11-23','15:20:00',55,'32',373.00,'Оформлен',2,46),(255,'2024-11-26','09:53:00',50,'5',266.00,'Оплачен',6,43),(256,'2024-11-21','08:07:00',25,'48',342.00,'Оплачен',5,43),(257,'2024-11-22','17:52:00',30,'53;28;37',858.00,'Оплачен',1,60),(258,'2024-11-22','21:15:00',49,'21',365.00,'Оплачен',3,46),(259,'2024-11-25','15:20:00',51,'44',205.00,'Оплачен',6,60),(260,'2024-11-21','20:34:00',34,'13;27',377.00,'Готовится',5,50),(261,'2024-11-24','18:11:00',57,'50',116.00,'Оплачен',3,56),(262,'2024-11-26','09:08:00',62,'40',475.00,'Оплачен',1,53),(263,'2024-11-24','15:17:00',20,'2;13;16',1028.00,'Готовится',1,52),(264,'2024-11-24','12:54:00',93,'12;53',474.00,'Готовится',3,41),(265,'2024-11-26','19:47:00',103,'16;2;55',983.00,'Оформлен',5,46),(266,'2024-11-24','21:26:00',66,'9',206.00,'Готовится',4,47),(267,'2024-11-22','08:03:00',46,'17;40;5',1281.00,'Оплачен',5,45),(268,'2024-11-27','11:16:00',72,'4;27;21',994.00,'Оплачен',2,52),(269,'2024-11-27','09:10:00',59,'36',407.00,'Оплачен',5,44),(270,'2024-11-26','18:19:00',48,'61;1',401.00,'Готовится',1,59),(271,'2024-11-21','12:11:00',44,'51',380.00,'Оплачен',3,59),(272,'2024-11-27','13:46:00',12,'11;24',929.00,'Оплачен',3,58),(273,'2024-11-24','19:18:00',37,'30',467.00,'Оплачен',5,55),(274,'2024-11-22','13:44:00',77,'51;32;56',930.00,'Оплачен',1,57),(275,'2024-11-23','20:13:00',53,'16;17;15',809.00,'Оформлен',1,56),(276,'2024-11-22','11:28:00',41,'43;56',677.00,'Готовится',6,43),(277,'2024-11-27','15:53:00',67,'55;21;33',1294.00,'Оплачен',2,50),(278,'2024-11-25','12:38:00',89,'10;56;40',995.00,'Готовится',5,41),(279,'2024-11-23','08:21:00',45,'16;50',850.00,'Оплачен',2,53),(280,'2024-11-26','08:46:00',67,'21;24',532.00,'Оформлен',1,55),(281,'2024-11-21','09:22:00',12,'23;54',796.00,'Оплачен',6,43),(282,'2024-11-21','19:46:00',32,'26',267.00,'Готовится',6,57),(283,'2024-11-26','22:33:00',76,'32;47',682.00,'Готовится',6,48),(284,'2024-11-27','19:37:00',31,'4;16;56',836.00,'Оплачен',5,41),(285,'2024-11-27','13:29:00',29,'47',241.00,'Оплачен',3,42),(286,'2024-11-25','13:01:00',68,'5;61',922.00,'Оплачен',2,56),(287,'2024-11-27','13:17:00',57,'36;62',655.00,'Оформлен',6,59),(288,'2024-11-24','09:21:00',55,'57',256.00,'Готовится',3,53),(289,'2024-11-22','18:22:00',76,'26',272.00,'Готовится',1,47),(290,'2024-11-26','20:05:00',19,'27;33',744.00,'Готовится',1,41),(291,'2024-11-23','22:22:00',16,'35;42;34',587.00,'Готовится',6,54),(292,'2024-11-25','20:31:00',71,'1;29;13',647.00,'Готовится',1,57),(293,'2024-11-23','19:34:00',88,'30',121.00,'Оплачен',2,58),(294,'2024-11-24','16:04:00',97,'22',350.00,'Оплачен',1,49),(295,'2024-11-26','21:05:00',87,'29',351.00,'Оплачен',4,52),(296,'2024-11-27','13:40:00',93,'24;57;45',779.00,'Оплачен',2,42),(297,'2024-11-25','15:55:00',74,'48',465.00,'Оплачен',3,41),(298,'2024-11-26','08:24:00',38,'15;55',676.00,'Оплачен',2,57),(299,'2024-11-23','17:03:00',19,'12;30',948.00,'Оплачен',4,50),(300,'2024-11-23','16:34:00',20,'62',110.00,'Оформлен',6,60);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `waiters`
--

DROP TABLE IF EXISTS `waiters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `waiters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `orders_completed` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `waiters`
--

LOCK TABLES `waiters` WRITE;
/*!40000 ALTER TABLE `waiters` DISABLE KEYS */;
INSERT INTO `waiters` VALUES (41,'Иванов Иван Иванович',11),(42,'Петров Петр Петрович',5),(43,'Сидоров Сидор Сидорович',5),(44,'Алексеев Алексей Алексеевич',4),(45,'Михайлов Михаил Михайлович',4),(46,'Кузнецов Николай Николаевич',4),(47,'Смирнов Сергей Сергеевич',6),(48,'Попов Василий Васильевич',2),(49,'Лебедев Александр Александрович',3),(50,'Новиков Дмитрий Дмитриевич',5),(51,'Федоров Андрей Андреевич',2),(52,'Морозов Олег Олегович',7),(53,'Волков Артем Артемович',8),(54,'Соколов Константин Константинович',3),(55,'Зайцев Антон Антонович',3),(56,'Егоров Вячеслав Вячеславович',6),(57,'Беляев Роман Романович',10),(58,'Павлов Виктор Викторович',4),(59,'Богданов Владимир Владимирович',4),(60,'Виноградов Денис Денисович',4);
/*!40000 ALTER TABLE `waiters` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-02 22:54:55

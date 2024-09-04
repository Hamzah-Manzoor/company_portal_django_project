-- MySQL dump 10.13  Distrib 8.3.0, for macos12.6 (x86_64)
--
-- Host: localhost    Database: employee_portal
-- ------------------------------------------------------
-- Server version	8.0.38

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
-- Table structure for table `Admin`
--

DROP TABLE IF EXISTS `Admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Admin` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `friday_lunch_iterator` int NOT NULL,
  `weekday_lunch_iterator` int NOT NULL,
  `lunch_time` time(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin`
--

LOCK TABLES `Admin` WRITE;
/*!40000 ALTER TABLE `Admin` DISABLE KEYS */;
INSERT INTO `Admin` VALUES (1,3,15,'15:00:00.000000');
/*!40000 ALTER TABLE `Admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AllocatedLeaves`
--

DROP TABLE IF EXISTS `AllocatedLeaves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AllocatedLeaves` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `annual_leaves` int NOT NULL,
  `casual_leaves` int NOT NULL,
  `medical_leaves` int NOT NULL,
  `designation_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `designation_id` (`designation_id`),
  CONSTRAINT `AllocatedLeaves_designation_id_b7b3e2f5_fk_Position_id` FOREIGN KEY (`designation_id`) REFERENCES `Position` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AllocatedLeaves`
--

LOCK TABLES `AllocatedLeaves` WRITE;
/*!40000 ALTER TABLE `AllocatedLeaves` DISABLE KEYS */;
INSERT INTO `AllocatedLeaves` VALUES (1,10,10,10,1),(2,10,10,10,2),(3,3,3,3,3),(4,6,6,6,5),(5,7,7,7,6),(6,5,5,5,4);
/*!40000 ALTER TABLE `AllocatedLeaves` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Announcements`
--

DROP TABLE IF EXISTS `Announcements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Announcements` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `details` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Announcements`
--

LOCK TABLES `Announcements` WRITE;
/*!40000 ALTER TABLE `Announcements` DISABLE KEYS */;
INSERT INTO `Announcements` VALUES (1,'Test Announcement One','2024-08-02','This is a detail.'),(2,'Test Announcement Two','2024-08-04','This is a detail.');
/*!40000 ALTER TABLE `Announcements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add announcements',6,'add_announcements'),(22,'Can change announcements',6,'change_announcements'),(23,'Can delete announcements',6,'delete_announcements'),(24,'Can view announcements',6,'view_announcements'),(25,'Can add events',7,'add_events'),(26,'Can change events',7,'change_events'),(27,'Can delete events',7,'delete_events'),(28,'Can view events',7,'view_events'),(29,'Can add allocated leaves',8,'add_allocatedleaves'),(30,'Can change allocated leaves',8,'change_allocatedleaves'),(31,'Can delete allocated leaves',8,'delete_allocatedleaves'),(32,'Can view allocated leaves',8,'view_allocatedleaves'),(33,'Can add leaves taken',9,'add_leavestaken'),(34,'Can change leaves taken',9,'change_leavestaken'),(35,'Can delete leaves taken',9,'delete_leavestaken'),(36,'Can view leaves taken',9,'view_leavestaken'),(37,'Can add position',10,'add_position'),(38,'Can change position',10,'change_position'),(39,'Can delete position',10,'delete_position'),(40,'Can view position',10,'view_position'),(41,'Can add employees',11,'add_employees'),(42,'Can change employees',11,'change_employees'),(43,'Can delete employees',11,'delete_employees'),(44,'Can view employees',11,'view_employees'),(45,'Can add feedback',12,'add_feedback'),(46,'Can change feedback',12,'change_feedback'),(47,'Can delete feedback',12,'delete_feedback'),(48,'Can view feedback',12,'view_feedback'),(49,'Can add admin',13,'add_admin'),(50,'Can change admin',13,'change_admin'),(51,'Can delete admin',13,'delete_admin'),(52,'Can view admin',13,'view_admin'),(53,'Can add lunch menu',14,'add_lunchmenu'),(54,'Can change lunch menu',14,'change_lunchmenu'),(55,'Can delete lunch menu',14,'delete_lunchmenu'),(56,'Can view lunch menu',14,'view_lunchmenu'),(57,'Can add lunch review',15,'add_lunchreview'),(58,'Can change lunch review',15,'change_lunchreview'),(59,'Can delete lunch review',15,'delete_lunchreview'),(60,'Can view lunch review',15,'view_lunchreview'),(61,'Can add project',16,'add_project'),(62,'Can change project',16,'change_project'),(63,'Can delete project',16,'delete_project'),(64,'Can view project',16,'view_project');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Employees_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Employees_id` FOREIGN KEY (`user_id`) REFERENCES `Employees` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-08-07 11:32:58.945443','1','CEO',1,'[{\"added\": {}}]',10,1),(2,'2024-08-07 11:33:03.530706','2','CTO',1,'[{\"added\": {}}]',10,1),(3,'2024-08-07 11:33:10.798565','3','HR',1,'[{\"added\": {}}]',10,1),(4,'2024-08-07 11:33:17.566230','4','Team Lead',1,'[{\"added\": {}}]',10,1),(5,'2024-08-07 11:33:33.203220','5','Senior Software Engineer',1,'[{\"added\": {}}]',10,1),(6,'2024-08-07 11:33:45.978014','6','Software Engineer',1,'[{\"added\": {}}]',10,1),(7,'2024-08-07 11:34:12.791363','1','FridayIterator: 3, WeekdayIterator: 15, LunchTime: 15:00:00',1,'[{\"added\": {}}]',13,1),(8,'2024-08-07 11:34:31.900422','1','CEO',1,'[{\"added\": {}}]',8,1),(9,'2024-08-07 11:34:38.430958','2','CTO',1,'[{\"added\": {}}]',8,1),(10,'2024-08-07 11:34:44.298298','3','HR',1,'[{\"added\": {}}]',8,1),(11,'2024-08-07 11:34:49.783679','4','Senior Software Engineer',1,'[{\"added\": {}}]',8,1),(12,'2024-08-07 11:34:54.398195','5','Software Engineer',1,'[{\"added\": {}}]',8,1),(13,'2024-08-07 11:35:01.901005','6','Team Lead',1,'[{\"added\": {}}]',8,1),(14,'2024-08-07 11:40:58.614010','1','Ali Afzal - Feedback',1,'[{\"added\": {}}]',12,1),(15,'2024-08-07 11:41:08.766220','2','Ali Afzal - Feedback',1,'[{\"added\": {}}]',12,1),(16,'2024-08-07 11:41:56.009388','1','Home Connect',1,'[{\"added\": {}}]',16,1),(17,'2024-08-07 11:42:02.942670','2','Facebook',1,'[{\"added\": {}}]',16,1),(18,'2024-08-07 11:42:33.577783','1','Test Event One',1,'[{\"added\": {}}]',7,1),(19,'2024-08-07 11:42:52.646302','2','Test Event Two',1,'[{\"added\": {}}]',7,1),(20,'2024-08-07 11:43:18.202425','1','Test Announcement One',1,'[{\"added\": {}}]',6,1),(21,'2024-08-07 11:43:35.725121','2','Test Announcement Two',1,'[{\"added\": {}}]',6,1),(22,'2024-08-07 11:44:04.505125','1','One',1,'[{\"added\": {}}]',14,1),(23,'2024-08-07 11:44:07.355088','2','Two',1,'[{\"added\": {}}]',14,1),(24,'2024-08-07 11:44:09.986981','3','Three',1,'[{\"added\": {}}]',14,1),(25,'2024-08-07 11:44:12.506596','4','Four',1,'[{\"added\": {}}]',14,1),(26,'2024-08-07 11:44:15.054272','5','Five',1,'[{\"added\": {}}]',14,1),(27,'2024-08-07 11:44:17.772952','6','Six',1,'[{\"added\": {}}]',14,1),(28,'2024-08-07 11:44:21.073914','7','Seven',1,'[{\"added\": {}}]',14,1),(29,'2024-08-07 11:44:24.257923','8','Eight',1,'[{\"added\": {}}]',14,1),(30,'2024-08-07 11:44:26.557221','9','Nine',1,'[{\"added\": {}}]',14,1),(31,'2024-08-07 11:44:28.524865','10','Ten',1,'[{\"added\": {}}]',14,1),(32,'2024-08-07 11:44:35.325835','11','Eleven',1,'[{\"added\": {}}]',14,1),(33,'2024-08-07 11:44:39.794151','12','Twelve',1,'[{\"added\": {}}]',14,1),(34,'2024-08-07 11:44:43.647753','13','Thirteen',1,'[{\"added\": {}}]',14,1),(35,'2024-08-07 11:44:46.976518','14','Fourteen',1,'[{\"added\": {}}]',14,1),(36,'2024-08-07 11:44:50.012537','15','Fifteen',1,'[{\"added\": {}}]',14,1),(37,'2024-08-07 11:44:52.529555','16','Sixteen',1,'[{\"added\": {}}]',14,1),(38,'2024-08-07 11:44:56.011568','17','Seventeen',1,'[{\"added\": {}}]',14,1),(39,'2024-08-07 11:45:00.895089','18','Eighteen',1,'[{\"added\": {}}]',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'events','announcements'),(7,'events','events'),(8,'leaves','allocatedleaves'),(9,'leaves','leavestaken'),(13,'lunch','admin'),(14,'lunch','lunchmenu'),(15,'lunch','lunchreview'),(16,'projects','project'),(5,'sessions','session'),(11,'users','employees'),(12,'users','feedback'),(10,'users','position');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-07 11:29:56.969066'),(2,'contenttypes','0002_remove_content_type_name','2024-08-07 11:29:56.987866'),(3,'auth','0001_initial','2024-08-07 11:29:57.075794'),(4,'auth','0002_alter_permission_name_max_length','2024-08-07 11:29:57.096948'),(5,'auth','0003_alter_user_email_max_length','2024-08-07 11:29:57.101499'),(6,'auth','0004_alter_user_username_opts','2024-08-07 11:29:57.106028'),(7,'auth','0005_alter_user_last_login_null','2024-08-07 11:29:57.110860'),(8,'auth','0006_require_contenttypes_0002','2024-08-07 11:29:57.113195'),(9,'auth','0007_alter_validators_add_error_messages','2024-08-07 11:29:57.118082'),(10,'auth','0008_alter_user_username_max_length','2024-08-07 11:29:57.122849'),(11,'auth','0009_alter_user_last_name_max_length','2024-08-07 11:29:57.127782'),(12,'auth','0010_alter_group_name_max_length','2024-08-07 11:29:57.139764'),(13,'auth','0011_update_proxy_permissions','2024-08-07 11:29:57.145064'),(14,'auth','0012_alter_user_first_name_max_length','2024-08-07 11:29:57.149551'),(15,'users','0001_initial','2024-08-07 11:29:57.295445'),(16,'admin','0001_initial','2024-08-07 11:29:57.349010'),(17,'admin','0002_logentry_remove_auto_add','2024-08-07 11:29:57.356719'),(18,'admin','0003_logentry_add_action_flag_choices','2024-08-07 11:29:57.365726'),(19,'admin','0004_auto_20240807_1328','2024-08-07 11:29:57.367059'),(20,'events','0001_initial','2024-08-07 11:29:57.381768'),(21,'leaves','0001_initial','2024-08-07 11:29:57.394376'),(22,'leaves','0002_initial','2024-08-07 11:29:57.449331'),(23,'lunch','0001_initial','2024-08-07 11:29:57.487944'),(24,'projects','0001_initial','2024-08-07 11:29:57.494436'),(25,'projects','0002_initial','2024-08-07 11:29:57.550888'),(26,'sessions','0001_initial','2024-08-07 11:29:57.563183'),(27,'events','0002_events_created_at_events_created_by_and_more','2024-08-08 05:34:57.341295');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3gtp5ow935foml8hlfc3ds175jfb58hx','.eJxVjMEOwiAQRP-Fs2mAhYIeTfwOsmwXaSy1kfZgjP8uJj1o5vbezLxEwG3NYav8COMgTkKLwy-LSDeev4LLMt2fzKHgjFcuPK_dbmt3KThO5737d5Cx5rb2oL1j5VIiIBml6a00thFtPKAkZxWQcoQtQENSDqKlHsEwJH9k8f4A-pE4Jg:1slSyT:zzNe8oz4Gv4pAHGY9_fbYGukNaIrAg_rvWoZS0mwUBM','2024-09-17 12:49:33.220897'),('gd3v72vvezbmwwd9j4zcdrrl6tf63umo','.eJxVjMsOgjAUBf-la0Pa0hcuTfyO5txysUSKxMLCGP9dTVjodmbOeYqIbc1xq3yPYy-OQovDLyOkK89fwWWZbg_mWDDjwoXntdltbc4F43Ta27-DjJo_60EmS9S7AQHSJpIptJIYxujkCK6F7pRjUuyhnGmV8RaspScN1QUSrzc1bziZ:1sbgUT:cvXRqIQp5LHZYVH5wvdMbRcHU0KM4qVg8r1BQteNUrM','2024-08-21 13:14:09.913714'),('uyalxwo0z5f8o5uewehila5iuov0g3r3','.eJxVjDsOAiEUAO9CbQgf4YGlvWcgwHvIqoFk2a2MdzckW2g7M5k3C3HfatgHrWFBdmGSnX5ZivlJbQp8xHbvPPe2rUviM-GHHfzWkV7Xo_0b1Djq3AonnSoFU0EpPJE-g9PWoE7CorQOTDGUFBrwOTuVvRHgBVDRBsgT-3wB2Dw3lQ:1slSrr:fwV0pODEoNJ_FVKqsiV5aw29A8XgA-eIzfIbOgPCvSk','2024-09-17 12:42:43.486588');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employees`
--

DROP TABLE IF EXISTS `Employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `date_of_joining` date DEFAULT NULL,
  `birthdate` date NOT NULL,
  `annual_leaves_taken` int NOT NULL,
  `casual_leaves_taken` int NOT NULL,
  `medical_leaves_taken` int NOT NULL,
  `unpaid_leaves_taken` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `role` varchar(255) NOT NULL,
  `position_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `Employees_position_id_1b16458e_fk_Position_id` (`position_id`),
  CONSTRAINT `Employees_position_id_1b16458e_fk_Position_id` FOREIGN KEY (`position_id`) REFERENCES `Position` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employees`
--

LOCK TABLES `Employees` WRITE;
/*!40000 ALTER TABLE `Employees` DISABLE KEYS */;
INSERT INTO `Employees` VALUES (1,'','admin@example.com','pbkdf2_sha256$870000$JCHaLGF11EE4CMBYoAvvu3$6NhIQfKeQbKSOCkyX2RG/cGFm2OUWjYE/ZgppQPXqaM=',NULL,'1990-05-15',0,0,0,0,1,1,1,'2024-09-03 12:42:43.484509','Employee',NULL),(2,'Ali Afzal','ali.afzal@example.com','pbkdf2_sha256$870000$FpvaN9Qpgqy1CLjjbyz4Tk$KQ5KD2KFxpaDpNqBz2Z96bH4ApMkzJiqxLdo8+a/xTU=','2024-08-07','1990-05-15',5,2,1,0,1,0,0,'2024-09-03 12:49:33.216382','CEO',1),(3,'Abrar Ahmed','abrar.ahmed@example.com','pbkdf2_sha256$720000$oWgkSbNByGVCsHr4uSZNF8$wXY6NdXa0Me9sZDPMVesnNYSCy74jhvVRXTEVTJNb3Q=','2024-08-20','2023-11-23',0,0,0,0,1,0,0,NULL,'S-HR',3),(10,'Chaypi','test.email@example.com','pbkdf2_sha256$720000$FfsQEqOuA8NlZGgw1KP3oQ$IvUV9fZkRBO7mzhg91dcoTUQ0n2iBsmzHjt0ZoW6Mjo=','2024-08-14','2024-08-13',0,0,0,0,1,0,0,NULL,'Project Manager',3);
/*!40000 ALTER TABLE `Employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employees_groups`
--

DROP TABLE IF EXISTS `Employees_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employees_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `employees_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Employees_groups_employees_id_group_id_39f88451_uniq` (`employees_id`,`group_id`),
  KEY `Employees_groups_group_id_848d56d4_fk_auth_group_id` (`group_id`),
  CONSTRAINT `Employees_groups_employees_id_b14172ff_fk_Employees_id` FOREIGN KEY (`employees_id`) REFERENCES `Employees` (`id`),
  CONSTRAINT `Employees_groups_group_id_848d56d4_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employees_groups`
--

LOCK TABLES `Employees_groups` WRITE;
/*!40000 ALTER TABLE `Employees_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `Employees_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employees_user_permissions`
--

DROP TABLE IF EXISTS `Employees_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employees_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `employees_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Employees_user_permissio_employees_id_permission__57318b40_uniq` (`employees_id`,`permission_id`),
  KEY `Employees_user_permi_permission_id_972d47b8_fk_auth_perm` (`permission_id`),
  CONSTRAINT `Employees_user_permi_permission_id_972d47b8_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `Employees_user_permissions_employees_id_8f9bda8e_fk_Employees_id` FOREIGN KEY (`employees_id`) REFERENCES `Employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employees_user_permissions`
--

LOCK TABLES `Employees_user_permissions` WRITE;
/*!40000 ALTER TABLE `Employees_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `Employees_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Events`
--

DROP TABLE IF EXISTS `Events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Events` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  `updated_by_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Events_created_by_id_788f4567_fk_Employees_id` (`created_by_id`),
  KEY `Events_updated_by_id_95f49b40_fk_Employees_id` (`updated_by_id`),
  CONSTRAINT `Events_created_by_id_788f4567_fk_Employees_id` FOREIGN KEY (`created_by_id`) REFERENCES `Employees` (`id`),
  CONSTRAINT `Events_updated_by_id_95f49b40_fk_Employees_id` FOREIGN KEY (`updated_by_id`) REFERENCES `Employees` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Events`
--

LOCK TABLES `Events` WRITE;
/*!40000 ALTER TABLE `Events` DISABLE KEYS */;
INSERT INTO `Events` VALUES (1,'Test Event One','2024-08-21','10:00 AM - 4:00 PM','This is a description.','2024-08-08 05:34:57.239346',NULL,'2024-08-08 05:34:57.298942',NULL),(2,'Test Event Two','2024-08-19','10:00 AM - 7:00 PM','This is a description.','2024-08-08 05:34:57.239346',NULL,'2024-08-08 05:34:57.298942',NULL),(3,'Test Event for Time','2024-08-19','10:00 AM - 7:00 PM','Checking Mixins!','2024-08-08 05:37:40.694731',2,'2024-08-08 05:46:26.598325',2);
/*!40000 ALTER TABLE `Events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Feedback`
--

DROP TABLE IF EXISTS `Feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` longtext NOT NULL,
  `employee_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Feedback_employee_id_32b8e9ff_fk_Employees_id` (`employee_id`),
  CONSTRAINT `Feedback_employee_id_32b8e9ff_fk_Employees_id` FOREIGN KEY (`employee_id`) REFERENCES `Employees` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Feedback`
--

LOCK TABLES `Feedback` WRITE;
/*!40000 ALTER TABLE `Feedback` DISABLE KEYS */;
INSERT INTO `Feedback` VALUES (1,'This is a feedback.',2),(2,'This is a second feedback.',2);
/*!40000 ALTER TABLE `Feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LeavesTaken`
--

DROP TABLE IF EXISTS `LeavesTaken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LeavesTaken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `reason` longtext NOT NULL,
  `leave_type` varchar(50) NOT NULL,
  `leave_taken_count` int NOT NULL,
  `status` varchar(20) NOT NULL,
  `employee_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `LeavesTaken_employee_id_id_c2a8ff4f_fk_Employees_id` (`employee_id_id`),
  CONSTRAINT `LeavesTaken_employee_id_id_c2a8ff4f_fk_Employees_id` FOREIGN KEY (`employee_id_id`) REFERENCES `Employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LeavesTaken`
--

LOCK TABLES `LeavesTaken` WRITE;
/*!40000 ALTER TABLE `LeavesTaken` DISABLE KEYS */;
/*!40000 ALTER TABLE `LeavesTaken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LunchMenu`
--

DROP TABLE IF EXISTS `LunchMenu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LunchMenu` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dish_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LunchMenu`
--

LOCK TABLES `LunchMenu` WRITE;
/*!40000 ALTER TABLE `LunchMenu` DISABLE KEYS */;
INSERT INTO `LunchMenu` VALUES (1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five'),(6,'Six'),(7,'Seven'),(8,'Eight'),(9,'Nine'),(10,'Ten'),(11,'Eleven'),(12,'Twelve'),(13,'Thirteen'),(14,'Fourteen'),(15,'Fifteen'),(16,'Sixteen'),(17,'Seventeen'),(18,'Eighteen');
/*!40000 ALTER TABLE `LunchMenu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LunchReview`
--

DROP TABLE IF EXISTS `LunchReview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LunchReview` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `likes` json NOT NULL,
  `dislikes` json NOT NULL,
  `lunch_menu_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `LunchReview_lunch_menu_id_f785410f_fk_LunchMenu_id` (`lunch_menu_id`),
  CONSTRAINT `LunchReview_lunch_menu_id_f785410f_fk_LunchMenu_id` FOREIGN KEY (`lunch_menu_id`) REFERENCES `LunchMenu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LunchReview`
--

LOCK TABLES `LunchReview` WRITE;
/*!40000 ALTER TABLE `LunchReview` DISABLE KEYS */;
INSERT INTO `LunchReview` VALUES (1,'2024-08-07','[]','[]',11),(2,'2024-08-08','[]','[]',12),(3,'2024-09-03','[]','[]',11);
/*!40000 ALTER TABLE `LunchReview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Position`
--

DROP TABLE IF EXISTS `Position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Position` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Position`
--

LOCK TABLES `Position` WRITE;
/*!40000 ALTER TABLE `Position` DISABLE KEYS */;
INSERT INTO `Position` VALUES (1,'CEO'),(2,'CTO'),(3,'HR'),(5,'Senior Software Engineer'),(6,'Software Engineer'),(4,'Team Lead');
/*!40000 ALTER TABLE `Position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Projects`
--

DROP TABLE IF EXISTS `Projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Projects` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `stack` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Projects`
--

LOCK TABLES `Projects` WRITE;
/*!40000 ALTER TABLE `Projects` DISABLE KEYS */;
INSERT INTO `Projects` VALUES (1,'Home Connect','MERN'),(2,'Facebook','React and Django');
/*!40000 ALTER TABLE `Projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Projects_team_members`
--

DROP TABLE IF EXISTS `Projects_team_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Projects_team_members` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `project_id` bigint NOT NULL,
  `employees_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Projects_team_members_project_id_employees_id_4ac4a25d_uniq` (`project_id`,`employees_id`),
  KEY `Projects_team_members_employees_id_065b2ba5_fk_Employees_id` (`employees_id`),
  CONSTRAINT `Projects_team_members_employees_id_065b2ba5_fk_Employees_id` FOREIGN KEY (`employees_id`) REFERENCES `Employees` (`id`),
  CONSTRAINT `Projects_team_members_project_id_7506a8cd_fk_Projects_id` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Projects_team_members`
--

LOCK TABLES `Projects_team_members` WRITE;
/*!40000 ALTER TABLE `Projects_team_members` DISABLE KEYS */;
INSERT INTO `Projects_team_members` VALUES (1,1,2),(2,2,2);
/*!40000 ALTER TABLE `Projects_team_members` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-03 23:10:24

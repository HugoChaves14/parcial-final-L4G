


-- Volcando estructura de base de datos para parcial2_l4g
CREATE DATABASE IF NOT EXISTS `parcial2_l4g` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `parcial2_l4g`;

-- Volcando estructura para tabla parcial2_l4g.sessions
CREATE TABLE IF NOT EXISTS `sessions` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sessions_subjects` (`subject_id`),
  CONSTRAINT `sessions_subjects` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial2_l4g.sessions: ~8 rows (aproximadamente)
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
INSERT INTO `sessions` (`id`, `subject_id`, `name`, `description`, `date`, `start_time`, `end_time`) VALUES
	(86, 6, 'session1', 'dasdsadsadsadsds', '2021-04-16', '19:41:00', '20:43:00'),
	(87, 9, 'session electiva', 'fdsfdsfdsfdfds', '2021-04-10', '17:44:00', '20:45:00'),
	(88, 6, 'sesion2', 'fdfdsfd', '2021-04-10', '19:59:00', '20:59:00'),
	(89, 11, 'seddion', 'sdfsadas', '2021-04-09', '18:28:00', '20:26:00'),
	(90, 9, 'session 3', 'fsdfd', '2021-04-21', '18:56:00', '20:54:00'),
	(97, 6, 'finalll', 'dasddssds', '2021-06-30', '19:41:00', '20:43:00'),
	(102, 6, 'hugoexpo', 'dasdsadsadsadsds', '2021-06-16', '19:41:00', '20:43:00'),
	(103, 6, 'practica', 'dasdsadsadsadsds', '2021-06-18', '19:41:00', '20:43:00');
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;

-- Volcando estructura para tabla parcial2_l4g.students
CREATE TABLE IF NOT EXISTS `students` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `idn` varchar(50) NOT NULL DEFAULT '0',
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(255) NOT NULL,
  `semester` tinyint(4) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=238 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial2_l4g.students: ~11 rows (aproximadamente)
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` (`id`, `idn`, `name`, `surname`, `phone`, `email`, `semester`) VALUES
	(213, '1234', 'brayner', 'barrr', '32302', 'bray@gmail.com', 2),
	(214, '321', 'sadsad', 'cdsfdsf', '213213', 'vydys@gmis.com', 6),
	(215, '1234567', 'dsf', 'berge', '13123', 'bdb@gmial.com', 4),
	(216, '13221323', 'hugo', 'chaves', '3213123', 'hgo@gmial.com', 5),
	(217, '66666', 'prueba', 'asdsad', '213123', 'brayner@gmail.com', 8),
	(218, '12323', 'sdsad', 'sddsa', '21312', 'fsas@sdsa', 2),
	(219, '1244', 'prueva hufo', 'sadas', '423413', 'vew@fskaf', 2),
	(220, '1244222', 'prueva52', 'sada55s22', '423413', 'vew@fsk55af', 2),
	(221, '1244333', 'prueva52...3', 'sada55s22', '423413', 'vew@fsk533af', 2),
	(234, '98765', 'chirulo', 'barragan', '42341s3', 'vssew@k533af', 2),
	(237, '09090', 'luisr', 'garcia', '32322', 'lu@gmail.com', 2);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;

-- Volcando estructura para tabla parcial2_l4g.student_sessions
CREATE TABLE IF NOT EXISTS `student_sessions` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `student_id` int(11) unsigned NOT NULL,
  `session_id` int(11) unsigned NOT NULL,
  `check_attendance` tinyint(4) DEFAULT NULL COMMENT '1 = si asistio, 2= no asistio',
  PRIMARY KEY (`id`),
  KEY `student_sessions_students` (`student_id`),
  KEY `student_sessions_sessions` (`session_id`),
  CONSTRAINT `student_sessions_sessions` FOREIGN KEY (`session_id`) REFERENCES `sessions` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `student_sessions_students` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3722 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial2_l4g.student_sessions: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `student_sessions` DISABLE KEYS */;
INSERT INTO `student_sessions` (`id`, `student_id`, `session_id`, `check_attendance`) VALUES
	(3697, 219, 86, 1),
	(3698, 219, 88, 1),
	(3699, 219, 97, 2),
	(3700, 213, 86, 2),
	(3701, 213, 88, 2),
	(3702, 213, 97, 2),
	(3714, 219, 102, 2),
	(3715, 213, 102, 2),
	(3720, 219, 103, 1),
	(3721, 213, 103, 2);
/*!40000 ALTER TABLE `student_sessions` ENABLE KEYS */;

-- Volcando estructura para tabla parcial2_l4g.student_subjects
CREATE TABLE IF NOT EXISTS `student_subjects` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `student_id` int(11) unsigned NOT NULL,
  `subject_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_subjects_subjects` (`subject_id`),
  KEY `student_subjects_students` (`student_id`),
  CONSTRAINT `student_subjects_students` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `student_subjects_subjects` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=931 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial2_l4g.student_subjects: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `student_subjects` DISABLE KEYS */;
INSERT INTO `student_subjects` (`id`, `student_id`, `subject_id`) VALUES
	(923, 219, 6),
	(924, 213, 6);
/*!40000 ALTER TABLE `student_subjects` ENABLE KEYS */;

-- Volcando estructura para tabla parcial2_l4g.subjects
CREATE TABLE IF NOT EXISTS `subjects` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `semester` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=462 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial2_l4g.subjects: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `subjects` DISABLE KEYS */;
INSERT INTO `subjects` (`id`, `name`, `semester`) VALUES
	(6, 'lenguaje de 4 generacion', 5),
	(7, 'bases de datos 2', 5),
	(8, 'calculo', 5),
	(9, 'electiva', 4),
	(10, 'redes', 4),
	(11, 'fundamentos', 5),
	(457, 'etica', 5),
	(458, 'matematicas', 2),
	(459, 'religion', 2),
	(461, 'naturales', 2);
/*!40000 ALTER TABLE `subjects` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

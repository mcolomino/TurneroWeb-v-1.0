-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-04-2024 a las 22:46:25
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `turnero`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultorio`
--

CREATE TABLE `consultorio` (
  `id` int(11) NOT NULL,
  `consultorio` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `consultorio`
--

INSERT INTO `consultorio` (`id`, `consultorio`) VALUES
(1, 'Capitalis'),
(2, 'San Luis');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `idpac` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `dni` char(12) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `mail` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`idpac`, `nombre`, `dni`, `telefono`, `mail`) VALUES
(1, 'Alicia', '12345678', '1111', 'alicia@gmail.com'),
(2, 'Belen', '23456789', '2221', 'belen@gmail.com'),
(3, 'Cecilia', '34557635', '', ''),
(4, 'Daniela', '111', '11', '1@gmail.com'),
(5, 'Eliana', '8888', '035', 's@w');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos`
--

CREATE TABLE `turnos` (
  `idturno` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `horaturno` char(5) NOT NULL,
  `idprofesional` int(11) NOT NULL,
  `idpaciente` int(11) NOT NULL,
  `actividad` varchar(10) NOT NULL,
  `estado` varchar(15) NOT NULL,
  `horallega` char(5) NOT NULL,
  `horaatiende` char(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `turnos`
--

INSERT INTO `turnos` (`idturno`, `fecha`, `horaturno`, `idprofesional`, `idpaciente`, `actividad`, `estado`, `horallega`, `horaatiende`) VALUES
(1, '2024-04-20', '15:00', 1, 4, 'Consulta', 'Atendido', '12:30', '16:30'),
(2, '2024-04-19', '11:30', 1, 2, 'Control', 'En Espera', '16:29', ''),
(3, '2024-04-23', '11:30', 1, 4, 'Control', 'En Agenda', '', ''),
(4, '2024-04-20', '15:00', 1, 1, 'Consulta', 'Ausente', '', ''),
(5, '2024-04-22', '11:30', 1, 5, 'Control', 'Cancelado', '', ''),
(6, '2024-04-22', '14:45', 1, 1, 'Control', 'En Agenda', '', ''),
(7, '2024-04-30', '12:34', 1, 1, 'Consulta', 'En Espera', '', ''),
(8, '2024-04-23', '11:30', 1, 4, 'Control', 'En Agenda', '', ''),
(9, '2024-04-19', '15:00', 25, 3, 'Consulta', 'En Agenda', '', ''),
(10, '2024-04-19', '18:00', 25, 5, 'Control', 'En Agenda', '', ''),
(11, '2024-04-25', '08:00', 25, 3, 'Control', 'En Agenda', '', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idusu` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `mail` varchar(80) NOT NULL,
  `clave` char(102) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `profesional` char(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idusu`, `nombre`, `mail`, `clave`, `telefono`, `profesional`) VALUES
(1, 'Maximiliano Illanes', 'Maxi@gmail.com', '', '353-4111222', 'SI'),
(2, 'Secre Vero', 'Vero@gmail.com', 'a', '353-4222111', 'NO'),
(25, 'Mario Colomino', 'marioacolomino@gmail.com', '11', '111111', 'SI');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `consultorio`
--
ALTER TABLE `consultorio`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`idpac`);

--
-- Indices de la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD PRIMARY KEY (`idturno`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idusu`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `consultorio`
--
ALTER TABLE `consultorio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `idpac` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `turnos`
--
ALTER TABLE `turnos`
  MODIFY `idturno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idusu` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

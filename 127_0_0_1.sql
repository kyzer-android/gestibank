-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  mar. 03 sep. 2019 à 17:25
-- Version du serveur :  10.4.6-MariaDB
-- Version de PHP :  7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `gestibank`
--
CREATE DATABASE IF NOT EXISTS `gestibank` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `gestibank`;

-- --------------------------------------------------------

--
-- Structure de la table `admin`
--

CREATE TABLE `admin` (
  `ID` varchar(10) NOT NULL,
  `NOM` varchar(30) NOT NULL,
  `PRENOM` varchar(20) NOT NULL,
  `TYPE_USER` enum('ADMIN','AGENT','CLIENT') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `agent`
--

CREATE TABLE `agent` (
  `ID` varchar(10) NOT NULL,
  `NOM` varchar(30) NOT NULL,
  `PRENOM` int(20) NOT NULL,
  `TYPE_USER` enum('ADMIN','AGENT','CLIENT') NOT NULL,
  `MATRICULE` int(10) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `TEL` varchar(15) NOT NULL,
  `DEBUT_CONTRAT` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `ID` varchar(10) NOT NULL,
  `NOM` varchar(30) NOT NULL,
  `PRENOM` varchar(20) NOT NULL,
  `TYPE_USER` enum('ADMIN','AGENT','CLIENT') NOT NULL,
  `MAIL` varchar(50) NOT NULL,
  `TEL` varchar(15) NOT NULL,
  `ADRESSE` varchar(100) NOT NULL,
  `JUSTIFICATIF` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `demande_creacompte`
--

CREATE TABLE `demande_creacompte` (
  `ID` varchar(10) NOT NULL,
  `NOM` varchar(30) NOT NULL,
  `PRENOM` varchar(20) NOT NULL,
  `MAIL` varchar(50) NOT NULL,
  `TEL` varchar(15) NOT NULL,
  `ADRESSE` varchar(100) NOT NULL,
  `JUSTIFICATIF` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `ID` varchar(10) NOT NULL,
  `NOM` varchar(30) NOT NULL,
  `PRENOM` varchar(20) NOT NULL,
  `TYPE_USER` enum('ADMIN','AGENT','CLIENT') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='UTILISATEUR';

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `agent`
--
ALTER TABLE `agent`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `demande_creacompte`
--
ALTER TABLE `demande_creacompte`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

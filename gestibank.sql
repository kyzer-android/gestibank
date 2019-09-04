-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  mer. 04 sep. 2019 à 11:33
-- Version du serveur :  5.7.17
-- Version de PHP :  5.6.30

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
  `PRENOM` varchar(20) NOT NULL,
  `TYPE_USER` enum('ADMIN','AGENT','CLIENT') NOT NULL,
  `MATRICULE` varchar(10) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `TEL` varchar(15) NOT NULL,
  `DEBUT_CONTRAT` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `agent`
--

INSERT INTO `agent` (`ID`, `NOM`, `PRENOM`, `TYPE_USER`, `MATRICULE`, `EMAIL`, `TEL`, `DEBUT_CONTRAT`) VALUES
('0000', 'nom_agent_00', 'prenom_agent_00', 'AGENT', 'AGT000', 'agent000@gestibank.com', '3609080946', '2019-09-03'),
('0001', 'nom_agent_01', 'prenom_agent_01', 'AGENT', 'AGT001', 'agent001@gestibank.com', '5167470252', '2019-09-03'),
('00010', 'nom_agent_010', 'prenom_agent_010', 'AGENT', 'AGT0010', 'agent0010@gestibank.com', '8952636963', '2019-09-03'),
('00011', 'nom_agent_011', 'prenom_agent_011', 'AGENT', 'AGT0011', 'agent0011@gestibank.com', '2268210031', '2019-09-03'),
('00012', 'nom_agent_012', 'prenom_agent_012', 'AGENT', 'AGT0012', 'agent0012@gestibank.com', '5426554989', '2019-09-03'),
('00013', 'nom_agent_013', 'prenom_agent_013', 'AGENT', 'AGT0013', 'agent0013@gestibank.com', '1649515046', '2019-09-03'),
('00014', 'nom_agent_014', 'prenom_agent_014', 'AGENT', 'AGT0014', 'agent0014@gestibank.com', '4636670807', '2019-09-03'),
('00015', 'nom_agent_015', 'prenom_agent_015', 'AGENT', 'AGT0015', 'agent0015@gestibank.com', '6803652932', '2019-09-03'),
('00016', 'nom_agent_016', 'prenom_agent_016', 'AGENT', 'AGT0016', 'agent0016@gestibank.com', '8165526108', '2019-09-03'),
('00017', 'nom_agent_017', 'prenom_agent_017', 'AGENT', 'AGT0017', 'agent0017@gestibank.com', '3410073052', '2019-09-03'),
('00018', 'nom_agent_018', 'prenom_agent_018', 'AGENT', 'AGT0018', 'agent0018@gestibank.com', '7537632766', '2019-09-03'),
('00019', 'nom_agent_019', 'prenom_agent_019', 'AGENT', 'AGT0019', 'agent0019@gestibank.com', '4836208193', '2019-09-03'),
('0002', 'nom_agent_02', 'prenom_agent_02', 'AGENT', 'AGT002', 'agent002@gestibank.com', '5172067376', '2019-09-03'),
('0003', 'nom_agent_03', 'prenom_agent_03', 'AGENT', 'AGT003', 'agent003@gestibank.com', '3667215906', '2019-09-03'),
('0004', 'nom_agent_04', 'prenom_agent_04', 'AGENT', 'AGT004', 'agent004@gestibank.com', '7958429685', '2019-09-03'),
('0005', 'nom_agent_05', 'prenom_agent_05', 'AGENT', 'AGT005', 'agent005@gestibank.com', '3307686902', '2019-09-03'),
('0006', 'nom_agent_06', 'prenom_agent_06', 'AGENT', 'AGT006', 'agent006@gestibank.com', '7327726343', '2019-09-03'),
('0007', 'nom_agent_07', 'prenom_agent_07', 'AGENT', 'AGT007', 'agent007@gestibank.com', '6074454949', '2019-09-03'),
('0008', 'nom_agent_08', 'prenom_agent_08', 'AGENT', 'AGT008', 'agent008@gestibank.com', '4907754524', '2019-09-03'),
('0009', 'nom_agent_09', 'prenom_agent_09', 'AGENT', 'AGT009', 'agent009@gestibank.com', '5339624041', '2019-09-03');

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

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`ID`, `NOM`, `PRENOM`, `TYPE_USER`, `MAIL`, `TEL`, `ADRESSE`, `JUSTIFICATIF`) VALUES
('0020', 'nom_client0', 'prenom_client_00', 'CLIENT', 'client000@gestibank.com', '1591651137', 'adresse', 'None'),
('0021', 'nom_client1', 'prenom_client_01', 'CLIENT', 'client001@gestibank.com', '2114476714', 'adresse', 'None'),
('00210', 'nom_client10', 'prenom_client_010', 'CLIENT', 'client0010@gestibank.com', '2712218931', 'adresse', 'None'),
('00211', 'nom_client11', 'prenom_client_011', 'CLIENT', 'client0011@gestibank.com', '1621350855', 'adresse', 'None'),
('00212', 'nom_client12', 'prenom_client_012', 'CLIENT', 'client0012@gestibank.com', '6236813923', 'adresse', 'None'),
('00213', 'nom_client13', 'prenom_client_013', 'CLIENT', 'client0013@gestibank.com', '1220106972', 'adresse', 'None'),
('00214', 'nom_client14', 'prenom_client_014', 'CLIENT', 'client0014@gestibank.com', '8687723056', 'adresse', 'None'),
('00215', 'nom_client15', 'prenom_client_015', 'CLIENT', 'client0015@gestibank.com', '3942108260', 'adresse', 'None'),
('00216', 'nom_client16', 'prenom_client_016', 'CLIENT', 'client0016@gestibank.com', '7751113673', 'adresse', 'None'),
('00217', 'nom_client17', 'prenom_client_017', 'CLIENT', 'client0017@gestibank.com', '8491009279', 'adresse', 'None'),
('00218', 'nom_client18', 'prenom_client_018', 'CLIENT', 'client0018@gestibank.com', '6990882199', 'adresse', 'None'),
('00219', 'nom_client19', 'prenom_client_019', 'CLIENT', 'client0019@gestibank.com', '5895902279', 'adresse', 'None'),
('0022', 'nom_client2', 'prenom_client_02', 'CLIENT', 'client002@gestibank.com', '2373173270', 'adresse', 'None'),
('0023', 'nom_client3', 'prenom_client_03', 'CLIENT', 'client003@gestibank.com', '2121142588', 'adresse', 'None'),
('00230', 'nom_client30', 'prenom_client_030', 'CLIENT', 'client0030@gestibank.com', '5586587503', 'adresse', 'None'),
('00231', 'nom_client31', 'prenom_client_031', 'CLIENT', 'client0031@gestibank.com', '2012685521', 'adresse', 'None'),
('00232', 'nom_client32', 'prenom_client_032', 'CLIENT', 'client0032@gestibank.com', '5470227543', 'adresse', 'None'),
('00233', 'nom_client33', 'prenom_client_033', 'CLIENT', 'client0033@gestibank.com', '3868881183', 'adresse', 'None'),
('00234', 'nom_client34', 'prenom_client_034', 'CLIENT', 'client0034@gestibank.com', '2649698700', 'adresse', 'None'),
('00235', 'nom_client35', 'prenom_client_035', 'CLIENT', 'client0035@gestibank.com', '4334156135', 'adresse', 'None'),
('00236', 'nom_client36', 'prenom_client_036', 'CLIENT', 'client0036@gestibank.com', '4477194821', 'adresse', 'None'),
('00237', 'nom_client37', 'prenom_client_037', 'CLIENT', 'client0037@gestibank.com', '1327469521', 'adresse', 'None'),
('00238', 'nom_client38', 'prenom_client_038', 'CLIENT', 'client0038@gestibank.com', '4204874426', 'adresse', 'None'),
('00239', 'nom_client39', 'prenom_client_039', 'CLIENT', 'client0039@gestibank.com', '6372251443', 'adresse', 'None'),
('0024', 'nom_client4', 'prenom_client_04', 'CLIENT', 'client004@gestibank.com', '1286981320', 'adresse', 'None'),
('00240', 'nom_client40', 'prenom_client_040', 'CLIENT', 'client0040@gestibank.com', '3079744237', 'adresse', 'None'),
('00241', 'nom_client41', 'prenom_client_041', 'CLIENT', 'client0041@gestibank.com', '8510941640', 'adresse', 'None'),
('00242', 'nom_client42', 'prenom_client_042', 'CLIENT', 'client0042@gestibank.com', '7925963014', 'adresse', 'None'),
('00243', 'nom_client43', 'prenom_client_043', 'CLIENT', 'client0043@gestibank.com', '7083008760', 'adresse', 'None'),
('00244', 'nom_client44', 'prenom_client_044', 'CLIENT', 'client0044@gestibank.com', '3046352064', 'adresse', 'None'),
('00245', 'nom_client45', 'prenom_client_045', 'CLIENT', 'client0045@gestibank.com', '7244433766', 'adresse', 'None'),
('00246', 'nom_client46', 'prenom_client_046', 'CLIENT', 'client0046@gestibank.com', '8813129548', 'adresse', 'None'),
('00247', 'nom_client47', 'prenom_client_047', 'CLIENT', 'client0047@gestibank.com', '1640411848', 'adresse', 'None'),
('00248', 'nom_client48', 'prenom_client_048', 'CLIENT', 'client0048@gestibank.com', '7234658935', 'adresse', 'None'),
('00249', 'nom_client49', 'prenom_client_049', 'CLIENT', 'client0049@gestibank.com', '7598052223', 'adresse', 'None'),
('0025', 'nom_client5', 'prenom_client_05', 'CLIENT', 'client005@gestibank.com', '3355341846', 'adresse', 'None'),
('0026', 'nom_client6', 'prenom_client_06', 'CLIENT', 'client006@gestibank.com', '6209803454', 'adresse', 'None'),
('0027', 'nom_client7', 'prenom_client_07', 'CLIENT', 'client007@gestibank.com', '3735497702', 'adresse', 'None'),
('0028', 'nom_client8', 'prenom_client_08', 'CLIENT', 'client008@gestibank.com', '8794021876', 'adresse', 'None'),
('0029', 'nom_client9', 'prenom_client_09', 'CLIENT', 'client009@gestibank.com', '3792806645', 'adresse', 'None');

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
  `JUSTIFICATIF` varchar(30) NOT NULL,
  `affect` varchar(15) DEFAULT NULL,
  `valide` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `demande_creacompte`
--

INSERT INTO `demande_creacompte` (`ID`, `NOM`, `PRENOM`, `MAIL`, `TEL`, `ADRESSE`, `JUSTIFICATIF`, `affect`, `valide`) VALUES
('1000', 'nom0', 'prenom_0', 'guest000@gestibank.com', '3391679156', 'adresse', 'None', NULL, NULL),
('1001', 'nom1', 'prenom_1', 'guest001@gestibank.com', '2113474599', 'adresse', 'None', NULL, NULL),
('1002', 'nom2', 'prenom_2', 'guest002@gestibank.com', '4761751125', 'adresse', 'None', NULL, NULL),
('1003', 'nom3', 'prenom_3', 'guest003@gestibank.com', '6737112155', 'adresse', 'None', NULL, NULL),
('1004', 'nom4', 'prenom_4', 'guest004@gestibank.com', '1923698368', 'adresse', 'None', NULL, NULL),
('1005', 'nom5', 'prenom_5', 'guest005@gestibank.com', '3913586189', 'adresse', 'None', NULL, NULL),
('1006', 'nom6', 'prenom_6', 'guest006@gestibank.com', '8834178517', 'adresse', 'None', NULL, NULL),
('1007', 'nom7', 'prenom_7', 'guest007@gestibank.com', '5330974348', 'adresse', 'None', NULL, NULL),
('1008', 'nom8', 'prenom_8', 'guest008@gestibank.com', '8446748659', 'adresse', 'None', NULL, NULL),
('1009', 'nom9', 'prenom_9', 'guest009@gestibank.com', '3180386407', 'adresse', 'None', NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `login`
--

CREATE TABLE `login` (
  `ID` varchar(10) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `TYPE_USER` enum('ADMIN','AGENT','CLIENT') NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `login`
--

INSERT INTO `login` (`ID`, `Password`, `TYPE_USER`) VALUES
('0010', 'test', 'CLIENT'),
('0020', 'secondtest', 'AGENT');

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
-- Index pour la table `login`
--
ALTER TABLE `login`
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

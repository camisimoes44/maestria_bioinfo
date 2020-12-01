-- phpMyAdmin SQL Dump
-- version 4.6.3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 27-11-2020 a las 13:09:24
-- Versión del servidor: 5.7.13
-- Versión de PHP: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bioinfo`
--
CREATE DATABASE IF NOT EXISTS `bioinfo` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `bioinfo`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `expertise_levels`
--

CREATE TABLE `expertise_levels` (
  `level` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `labels`
--

CREATE TABLE `labels` (
  `label` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `user` varchar(30) CHARACTER SET utf8 NOT NULL,
  `name` varchar(30) CHARACTER SET utf8 NOT NULL,
  `surname` varchar(30) CHARACTER SET utf8 NOT NULL,
  `email` varchar(50) CHARACTER SET utf8 NOT NULL,
  `level` varchar(30) CHARACTER SET utf8 NOT NULL,
  `password` varchar(150) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_classification`
--

CREATE TABLE `user_classification` (
  `user_ID` varchar(50) NOT NULL COMMENT 'User associated to classification',
  `variant_ID` int(11) NOT NULL COMMENT 'Variant classified',
  `label_ID` varchar(30) NOT NULL COMMENT 'Label applied by the user',
  `is_correct` tinyint(1) NOT NULL COMMENT 'Classification result. If =1, the classification was correct',
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Date/time of classification'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Represents the classifications of variants made by the users';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `variants`
--

CREATE TABLE `variants` (
  `ID` int(11) NOT NULL,
  `Chr` varchar(2) NOT NULL,
  `Gene.refGene` varchar(63) NOT NULL,
  `Start` decimal(38,0) NOT NULL,
  `End` decimal(38,0) NOT NULL,
  `Ref` varchar(3527) NOT NULL,
  `Alt` varchar(454) NOT NULL,
  `Func.refGene` varchar(21) NOT NULL,
  `GeneDetail.refGene` varchar(936) DEFAULT NULL,
  `ExonicFunc.refGene` varchar(26) DEFAULT NULL,
  `AAChange.refGene` varchar(2622) DEFAULT NULL,
  `cytoBand` varchar(8) DEFAULT NULL,
  `snp138` varchar(11) DEFAULT NULL,
  `avsnp150` varchar(12) DEFAULT NULL,
  `CLNALLELEID` decimal(38,0) NOT NULL,
  `CLNDN` varchar(1061) NOT NULL,
  `CLNDISDB` varchar(2708) NOT NULL,
  `CLNREVSTAT` varchar(46) NOT NULL,
  `CLNSIG` varchar(44) NOT NULL,
  `MIM` decimal(38,0) DEFAULT NULL,
  `Phenotype` varchar(134) DEFAULT NULL,
  `esp6500siv2_all` decimal(38,6) DEFAULT NULL,
  `1000g2015aug_all` decimal(38,9) DEFAULT NULL,
  `1000g2015aug_afr` decimal(38,4) DEFAULT NULL,
  `1000g2015aug_eas` decimal(38,4) DEFAULT NULL,
  `1000g2015aug_eur` decimal(38,4) DEFAULT NULL,
  `ExAC_ALL` decimal(38,9) DEFAULT NULL,
  `ExAC_AFR` decimal(38,8) DEFAULT NULL,
  `ExAC_AMR` decimal(38,8) DEFAULT NULL,
  `ExAC_EAS` decimal(38,4) DEFAULT NULL,
  `ExAC_FIN` decimal(38,4) DEFAULT NULL,
  `ExAC_NFE` decimal(38,8) DEFAULT NULL,
  `ExAC_OTH` decimal(38,4) DEFAULT NULL,
  `ExAC_SAS` decimal(38,8) DEFAULT NULL,
  `gnomAD_genome_AF` decimal(38,8) DEFAULT NULL,
  `gnomAD_genome_AF_popmax` decimal(38,8) DEFAULT NULL,
  `gnomAD_genome_AF_male` decimal(38,8) DEFAULT NULL,
  `gnomAD_genome_AF_female` decimal(38,8) DEFAULT NULL,
  `gnomAD_genome_AF_raw` decimal(38,8) DEFAULT NULL,
  `gnomAD_genome_AF_afr` decimal(38,4) DEFAULT NULL,
  `gnomAD_genome_AF_sas` tinyint(1) DEFAULT NULL,
  `gnomAD_genome_AF_amr` decimal(38,4) DEFAULT NULL,
  `gnomAD_genome_AF_eas` decimal(38,4) DEFAULT NULL,
  `gnomAD_genome_AF_nfe` decimal(38,8) DEFAULT NULL,
  `gnomAD_genome_AF_fin` decimal(38,4) DEFAULT NULL,
  `gnomAD_genome_AF_asj` decimal(38,4) DEFAULT NULL,
  `gnomAD_genome_AF_oth` decimal(38,4) DEFAULT NULL,
  `gnomAD_genome_non_topmed_AF_popmax` decimal(38,8) DEFAULT NULL,
  `gnomAD_genome_non_neuro_AF_popmax` decimal(38,8) DEFAULT NULL,
  `gnomAD_genome_non_cancer_AF_popmax` tinyint(1) DEFAULT NULL,
  `gnomAD_genome_controls_AF_popmax` decimal(38,4) DEFAULT NULL,
  `Kaviar_AF` decimal(38,7) DEFAULT NULL,
  `Kaviar_AC` decimal(38,0) DEFAULT NULL,
  `Kaviar_AN` decimal(38,0) DEFAULT NULL,
  `SIFT_score` decimal(38,3) DEFAULT NULL,
  `SIFT_converted_rankscore` decimal(38,3) DEFAULT NULL,
  `SIFT_pred` varchar(1) DEFAULT NULL,
  `Polyphen2_HDIV_score` decimal(38,3) DEFAULT NULL,
  `Polyphen2_HDIV_rankscore` decimal(38,3) DEFAULT NULL,
  `Polyphen2_HDIV_pred` varchar(1) DEFAULT NULL,
  `Polyphen2_HVAR_score` decimal(38,3) DEFAULT NULL,
  `Polyphen2_HVAR_rankscore` decimal(38,3) DEFAULT NULL,
  `Polyphen2_HVAR_pred` varchar(1) DEFAULT NULL,
  `LRT_score` decimal(38,3) DEFAULT NULL,
  `LRT_converted_rankscore` decimal(38,3) DEFAULT NULL,
  `LRT_pred` varchar(1) DEFAULT NULL,
  `MutationTaster_score` decimal(38,14) DEFAULT NULL,
  `MutationTaster_converted_rankscore` decimal(38,3) DEFAULT NULL,
  `MutationTaster_pred` varchar(1) DEFAULT NULL,
  `MutationAssessor_score` decimal(38,3) DEFAULT NULL,
  `MutationAssessor_score_rankscore` decimal(38,3) DEFAULT NULL,
  `MutationAssessor_pred` varchar(1) DEFAULT NULL,
  `FATHMM_score` decimal(38,2) DEFAULT NULL,
  `FATHMM_converted_rankscore` decimal(38,3) DEFAULT NULL,
  `FATHMM_pred` varchar(1) DEFAULT NULL,
  `PROVEAN_score` decimal(38,2) DEFAULT NULL,
  `PROVEAN_converted_rankscore` decimal(38,3) DEFAULT NULL,
  `PROVEAN_pred` varchar(1) DEFAULT NULL,
  `VEST3_score` decimal(38,3) DEFAULT NULL,
  `VEST3_rankscore` decimal(38,3) DEFAULT NULL,
  `MetaSVM_score` decimal(38,3) DEFAULT NULL,
  `MetaSVM_rankscore` decimal(38,3) DEFAULT NULL,
  `MetaSVM_pred` varchar(1) DEFAULT NULL,
  `MetaLR_score` decimal(38,3) DEFAULT NULL,
  `MetaLR_rankscore` decimal(38,3) DEFAULT NULL,
  `MetaLR_pred` varchar(1) DEFAULT NULL,
  `M-CAP_score` decimal(38,3) DEFAULT NULL,
  `M-CAP_rankscore` decimal(38,3) DEFAULT NULL,
  `M-CAP_pred` varchar(1) DEFAULT NULL,
  `REVEL_score` decimal(38,3) DEFAULT NULL,
  `REVEL_rankscore` decimal(38,3) DEFAULT NULL,
  `MutPred_score` varchar(5) DEFAULT NULL,
  `MutPred_rankscore` decimal(38,3) DEFAULT NULL,
  `CADD_raw` decimal(38,3) DEFAULT NULL,
  `CADD_raw_rankscore` decimal(38,3) DEFAULT NULL,
  `CADD_phred` decimal(38,3) DEFAULT NULL,
  `DANN_score` decimal(38,3) DEFAULT NULL,
  `DANN_rankscore` decimal(38,3) DEFAULT NULL,
  `fathmm-MKL_coding_score` decimal(38,3) DEFAULT NULL,
  `fathmm-MKL_coding_rankscore` decimal(38,3) DEFAULT NULL,
  `fathmm-MKL_coding_pred` varchar(1) DEFAULT NULL,
  `Eigen_coding_or_noncoding` varchar(1) DEFAULT NULL,
  `Eigen-raw` decimal(38,3) DEFAULT NULL,
  `Eigen-PC-raw` decimal(38,3) DEFAULT NULL,
  `GenoCanyon_score` decimal(38,3) DEFAULT NULL,
  `GenoCanyon_score_rankscore` decimal(38,3) DEFAULT NULL,
  `integrated_fitCons_score` decimal(38,3) DEFAULT NULL,
  `integrated_fitCons_score_rankscore` decimal(38,3) DEFAULT NULL,
  `integrated_confidence_value` decimal(38,0) DEFAULT NULL,
  `GERP++_RS` decimal(38,6) DEFAULT NULL,
  `GERP++_RS_rankscore` decimal(38,3) DEFAULT NULL,
  `phyloP100way_vertebrate` decimal(38,3) DEFAULT NULL,
  `phyloP100way_vertebrate_rankscore` decimal(38,3) DEFAULT NULL,
  `phyloP20way_mammalian` decimal(38,3) DEFAULT NULL,
  `phyloP20way_mammalian_rankscore` decimal(38,3) DEFAULT NULL,
  `phastCons100way_vertebrate` decimal(38,3) DEFAULT NULL,
  `phastCons100way_vertebrate_rankscore` decimal(38,3) DEFAULT NULL,
  `phastCons20way_mammalian` decimal(38,3) DEFAULT NULL,
  `phastCons20way_mammalian_rankscore` decimal(38,3) DEFAULT NULL,
  `SiPhy_29way_logOdds` decimal(38,3) DEFAULT NULL,
  `SiPhy_29way_logOdds_rankscore` decimal(38,3) DEFAULT NULL,
  `Interpro_domain` varchar(589) DEFAULT NULL,
  `GTEx_V6p_gene` varchar(2111) DEFAULT NULL,
  `GTEx_V6p_tissue` varchar(2272) DEFAULT NULL,
  `regsnp_fpr` decimal(38,15) DEFAULT NULL,
  `regsnp_disease` varchar(2) DEFAULT NULL,
  `regsnp_splicing_site` varchar(3) DEFAULT NULL,
  `GWAVA_region_score` decimal(38,2) DEFAULT NULL,
  `GWAVA_tss_score` decimal(38,2) DEFAULT NULL,
  `GWAVA_unmatched_score` decimal(38,0) DEFAULT NULL,
  `Eigen` decimal(38,4) DEFAULT NULL,
  `genomicSuperDups` varchar(47) DEFAULT NULL,
  `gwasCatalog` varchar(647) DEFAULT NULL,
  `chr.vcf` varchar(2) NOT NULL,
  `start.vcf` decimal(38,0) NOT NULL,
  `ref.vcf` varchar(3528) NOT NULL,
  `alt.vcf` varchar(455) NOT NULL,
  `info.vcf` varchar(5865) NOT NULL,
  `type` varchar(14) DEFAULT NULL,
  `Entrez` decimal(38,0) DEFAULT NULL,
  `EnsemblID` varchar(15) DEFAULT NULL,
  `Genes` varchar(67) DEFAULT NULL,
  `Cyto` varchar(15) DEFAULT NULL,
  `InterVar_automated` varchar(22) DEFAULT NULL,
  `PVS1` tinyint(1) DEFAULT NULL,
  `PS1` tinyint(1) DEFAULT NULL,
  `PS2` tinyint(1) DEFAULT NULL,
  `PS3` tinyint(1) DEFAULT NULL,
  `PS4` tinyint(1) DEFAULT NULL,
  `PM1` tinyint(1) DEFAULT NULL,
  `PM2` tinyint(1) DEFAULT NULL,
  `PM3` tinyint(1) DEFAULT NULL,
  `PM4` tinyint(1) DEFAULT NULL,
  `PM5` tinyint(1) DEFAULT NULL,
  `PM6` tinyint(1) DEFAULT NULL,
  `PP1` tinyint(1) DEFAULT NULL,
  `PP2` tinyint(1) DEFAULT NULL,
  `PP3` tinyint(1) DEFAULT NULL,
  `PP4` tinyint(1) DEFAULT NULL,
  `PP5` tinyint(1) DEFAULT NULL,
  `BA1` tinyint(1) DEFAULT NULL,
  `BS1` tinyint(1) DEFAULT NULL,
  `BS2` tinyint(1) DEFAULT NULL,
  `BS3` tinyint(1) DEFAULT NULL,
  `BS4` tinyint(1) DEFAULT NULL,
  `BP1` tinyint(1) DEFAULT NULL,
  `BP2` tinyint(1) DEFAULT NULL,
  `BP3` tinyint(1) DEFAULT NULL,
  `BP4` tinyint(1) DEFAULT NULL,
  `BP5` tinyint(1) DEFAULT NULL,
  `BP6` tinyint(1) DEFAULT NULL,
  `BP7` tinyint(1) DEFAULT NULL,
  `freq.max` decimal(38,9) DEFAULT NULL,
  `is_conflict` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `expertise_levels`
--
ALTER TABLE `expertise_levels`
  ADD PRIMARY KEY (`level`);

--
-- Indices de la tabla `labels`
--
ALTER TABLE `labels`
  ADD PRIMARY KEY (`label`);

--
-- Indices de la tabla `user_classification`
--
ALTER TABLE `user_classification`
  ADD PRIMARY KEY (`user_ID`,`variant_ID`),
  ADD KEY `FK_LabelClassification` (`label_ID`),
  ADD KEY `FK_VariantClassification` (`variant_ID`);

--
-- Indices de la tabla `variants`
--
ALTER TABLE `variants`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `is_conflict` (`is_conflict`),
  ADD KEY `CLNSIG` (`CLNSIG`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `variants`
--
ALTER TABLE `variants`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `user_classification`
--
ALTER TABLE `user_classification`
  ADD CONSTRAINT `FK_LabelClassification` FOREIGN KEY (`label_ID`) REFERENCES `labels` (`label`),
  ADD CONSTRAINT `FK_VariantClassification` FOREIGN KEY (`variant_ID`) REFERENCES `variants` (`ID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

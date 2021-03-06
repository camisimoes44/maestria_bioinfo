--
-- Database: `bioinfo`
--
CREATE DATABASE IF NOT EXISTS `bioinfo` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `bioinfo`;

-- --------------------------------------------------------

--
-- Structure of table `variants`
--
CREATE TABLE variants (
	`Chr` DECIMAL(38, 0) NOT NULL, 
	`Start` DECIMAL(38, 0) NOT NULL, 
	`End` DECIMAL(38, 0) NOT NULL, 
	`Ref` VARCHAR(3527) NOT NULL, 
	`Alt` VARCHAR(76) NOT NULL, 
	`Func.refGene` VARCHAR(15) NOT NULL, 
	`Gene.refGene` VARCHAR(11) NOT NULL, 
	`GeneDetail.refGene` VARCHAR(444), 
	`ExonicFunc.refGene` VARCHAR(26), 
	`AAChange.refGene` VARCHAR(134), 
	`cytoBand` VARCHAR(137) NOT NULL, 
	`ExAC_ALL` VARCHAR(137), 
	`ExAC_AFR` VARCHAR(92), 
	`ExAC_AMR` VARCHAR(95), 
	`ExAC_EAS` VARCHAR(95), 
	`ExAC_FIN` VARCHAR(95), 
	`ExAC_NFE` VARCHAR(50), 
	`ExAC_OTH` VARCHAR(48), 
	`ExAC_SAS` VARCHAR(49), 
	avsnp147 VARCHAR(51), 
	`SIFT_score` VARCHAR(50), 
	`SIFT_pred` VARCHAR(48), 
	`Polyphen2_HDIV_score` VARCHAR(48), 
	`Polyphen2_HDIV_pred` VARCHAR(11), 
	`Polyphen2_HVAR_score` VARCHAR(11), 
	`Polyphen2_HVAR_pred` VARCHAR(11), 
	`LRT_score` VARCHAR(9), 
	`LRT_pred` VARCHAR(8), 
	`MutationTaster_score` VARCHAR(5), 
	`MutationTaster_pred` VARCHAR(11), 
	`MutationAssessor_score` VARCHAR(11), 
	`MutationAssessor_pred` VARCHAR(5), 
	`FATHMM_score` VARCHAR(11), 
	`FATHMM_pred` VARCHAR(5), 
	`PROVEAN_score` VARCHAR(5), 
	`PROVEAN_pred` VARCHAR(6), 
	`VEST3_score` VARCHAR(5), 
	`CADD_raw` VARCHAR(6), 
	`CADD_phred` VARCHAR(6), 
	`DANN_score` VARCHAR(6), 
	`fathmm-MKL_coding_score` VARCHAR(6), 
	`fathmm-MKL_coding_pred` VARCHAR(6), 
	`MetaSVM_score` VARCHAR(6), 
	`MetaSVM_pred` VARCHAR(6), 
	`MetaLR_score` VARCHAR(6), 
	`MetaLR_pred` VARCHAR(6), 
	`integrated_fitCons_score` VARCHAR(5), 
	integrated_confidence_value VARCHAR(6), 
	`GERP++_RS` VARCHAR(6), 
	`phyloP7way_vertebrate` VARCHAR(6), 
	`phyloP20way_mammalian` VARCHAR(6), 
	`phastCons7way_vertebrate` VARCHAR(6), 
	`phastCons20way_mammalian` DECIMAL(38, 3), 
	`SiPhy_29way_logOdds` DECIMAL(38, 3), 
	regsnp_fpr VARCHAR(17), 
	regsnp_disease VARCHAR(6), 
	regsnp_splicing_site VARCHAR(6), 
	`GWAVA_region_score` DECIMAL(38, 3), 
	`GWAVA_tss_score` DECIMAL(38, 3), 
	`GWAVA_unmatched_score` DECIMAL(38, 3), 
	`AF` DECIMAL(38, 8), 
	`AF_popmax` DECIMAL(38, 8), 
	`AF_male` DECIMAL(38, 8), 
	`AF_female` DECIMAL(38, 8), 
	`AF_raw` DECIMAL(38, 8), 
	`AF_afr` DECIMAL(38, 8), 
	`AF_sas` DECIMAL(38, 8), 
	`AF_amr` DECIMAL(38, 8), 
	`AF_eas` DECIMAL(38, 8), 
	`AF_nfe` DECIMAL(38, 8), 
	`AF_fin` DECIMAL(38, 8), 
	`AF_asj` DECIMAL(38, 8), 
	`AF_oth` DECIMAL(38, 8), 
	`non_topmed_AF_popmax` DECIMAL(38, 8), 
	`non_neuro_AF_popmax` DECIMAL(38, 8), 
	`non_cancer_AF_popmax` DECIMAL(38, 8), 
	`controls_AF_popmax` DECIMAL(38, 8), 
	`InterVar_automated` VARCHAR(22), 
	`PVS1` VARCHAR(22), 
	`PS1` VARCHAR(22), 
	`PS2` VARCHAR(22), 
	`PS3` VARCHAR(22), 
	`PS4` VARCHAR(22), 
	`PM1` VARCHAR(22), 
	`PM2` DECIMAL(38, 8), 
	`PM3` BOOL, 
	`PM4` DECIMAL(38, 8), 
	`PM5` VARCHAR(10), 
	`PM6` BOOL, 
	`PP1` DECIMAL(38, 4), 
	`PP2` VARCHAR(10), 
	`PP3` BOOL, 
	`PP4` BOOL, 
	`PP5` BOOL, 
	`BA1` BOOL, 
	`BS1` BOOL, 
	`BS2` BOOL, 
	`BS3` BOOL, 
	`BS4` BOOL, 
	`BP1` BOOL, 
	`BP2` BOOL, 
	`BP3` BOOL, 
	`BP4` BOOL, 
	`BP5` BOOL, 
	`BP6` BOOL, 
	`BP7` BOOL, 
	`Kaviar_AF` DECIMAL(38, 7), 
	`Kaviar_AC` DECIMAL(38, 7), 
	`Kaviar_AN` DECIMAL(38, 7), 
	`CLNALLELEID` DECIMAL(38, 7), 
	`CLNDN` VARCHAR(339), 
	`CLNDISDB` VARCHAR(217), 
	`CLNREVSTAT` VARCHAR(533), 
	`CLNSIG` VARCHAR(349), 
	`Eigen` VARCHAR(173), 
	`Otherinfo` VARCHAR(238), 
	mmmmm VARCHAR(505), 
	nnnnn VARCHAR(285), 
	ooooo VARCHAR(513), 
	ppppp VARCHAR(280), 
	qqqqq VARCHAR(561), 
	rrrrr VARCHAR(476), 
	sssss VARCHAR(175), 
	ttttt VARCHAR(334), 
	uuuuu VARCHAR(562), 
	vvvvv VARCHAR(233), 
	wwwww VARCHAR(261), 
	xxxxx VARCHAR(256), 
	yyyyy VARCHAR(442), 
	zzzzz VARCHAR(262), 
	aaaaaa VARCHAR(226), 
	bbbbbb VARCHAR(574), 
	cccccc VARCHAR(279), 
	dddddd VARCHAR(251), 
	eeeeee VARCHAR(314), 
	ffffff VARCHAR(92), 
	gggggg VARCHAR(59), 
	hhhhhh VARCHAR(15), 
	iiiiii VARCHAR(11), 
	jjjjjj VARCHAR(19), 
	kkkkkk VARCHAR(19), 
	llllll VARCHAR(54), 
	mmmmmm VARCHAR(12), 
	nnnnnn VARCHAR(15), 
	oooooo VARCHAR(59), 
	pppppp VARCHAR(15), 
	qqqqqq VARCHAR(15), 
	rrrrrr VARCHAR(19), 
	ssssss VARCHAR(19), 
	tttttt VARCHAR(54), 
	uuuuuu VARCHAR(12), 
	vvvvvv VARCHAR(15), 
	wwwwww VARCHAR(11), 
	xxxxxx VARCHAR(19), 
	yyyyyy VARCHAR(54), 
	zzzzzz VARCHAR(54), 
	aaaaaaa VARCHAR(51), 
	bbbbbbb VARCHAR(51), 
	ccccccc VARCHAR(51), 
	ddddddd VARCHAR(15), 
	eeeeeee VARCHAR(47), 
	fffffff VARCHAR(51), 
	ggggggg VARCHAR(51), 
	hhhhhhh VARCHAR(54), 
	iiiiiii VARCHAR(51), 
	jjjjjjj VARCHAR(15), 
	kkkkkkk VARCHAR(55), 
	lllllll VARCHAR(19), 
	mmmmmmm VARCHAR(54), 
	nnnnnnn VARCHAR(15), 
	ooooooo VARCHAR(15), 
	ppppppp VARCHAR(20), 
	qqqqqqq VARCHAR(55), 
	rrrrrrr VARCHAR(12), 
	sssssss VARCHAR(51), 
	ttttttt VARCHAR(56), 
	uuuuuuu VARCHAR(12), 
	vvvvvvv VARCHAR(15), 
	wwwwwww VARCHAR(32), 
	xxxxxxx VARCHAR(55), 
	yyyyyyy VARCHAR(12), 
	zzzzzzz VARCHAR(32), 
	aaaaaaaa VARCHAR(56), 
	bbbbbbbb VARCHAR(15), 
	cccccccc VARCHAR(31), 
	dddddddd VARCHAR(32), 
	eeeeeeee VARCHAR(28), 
	ffffffff VARCHAR(15), 
	gggggggg VARCHAR(32), 
	hhhhhhhh VARCHAR(31), 
	iiiiiiii VARCHAR(31), 
	jjjjjjjj VARCHAR(28), 
	kkkkkkkk VARCHAR(32), 
	llllllll VARCHAR(47), 
	mmmmmmmm VARCHAR(68), 
	nnnnnnnn VARCHAR(36), 
	oooooooo VARCHAR(35), 
	pppppppp VARCHAR(35), 
	qqqqqqqq VARCHAR(36), 
	rrrrrrrr VARCHAR(67), 
	ssssssss VARCHAR(432), 
	tttttttt VARCHAR(304), 
	uuuuuuuu VARCHAR(39), 
	vvvvvvvv VARCHAR(35), 
	wwwwwwww VARCHAR(594), 
	xxxxxxxx VARCHAR(500), 
	yyyyyyyy VARCHAR(53), 
	zzzzzzzz VARCHAR(51), 
	aaaaaaaaa VARCHAR(246), 
	bbbbbbbbb VARCHAR(53), 
	CHECK (`PM3` IN (0, 1)), 
	CHECK (`PM6` IN (0, 1)), 
	CHECK (`PP3` IN (0, 1)), 
	CHECK (`PP4` IN (0, 1)), 
	CHECK (`PP5` IN (0, 1)), 
	CHECK (`BA1` IN (0, 1)), 
	CHECK (`BS1` IN (0, 1)), 
	CHECK (`BS2` IN (0, 1)), 
	CHECK (`BS3` IN (0, 1)), 
	CHECK (`BS4` IN (0, 1)), 
	CHECK (`BP1` IN (0, 1)), 
	CHECK (`BP2` IN (0, 1)), 
	CHECK (`BP3` IN (0, 1)), 
	CHECK (`BP4` IN (0, 1)), 
	CHECK (`BP5` IN (0, 1)), 
	CHECK (`BP6` IN (0, 1)), 
	CHECK (`BP7` IN (0, 1))
);

--
-- Add the ID column as the first one of the table `variants`.
-- This must be done AFTER importing the CSV into MySQL.
--
ALTER TABLE variants ADD COLUMN `ID` int NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;


--
-- Estructura de tabla para la tabla `expertise_levels`
--

CREATE TABLE `expertise_levels` (
  `level` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Expertise levels of the users';

--
-- Volcado de datos para la tabla `expertise_levels`
--

INSERT INTO `expertise_levels` (`level`) VALUES
('Advanced Beginner'),
('Competent'),
('Expert'),
('Novice'),
('Proficient');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `labels`
--

CREATE TABLE `labels` (
  `label` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Labels to apply to variant classification';

--
-- Volcado de datos para la tabla `labels`
--

INSERT INTO `labels` (`label`) VALUES
('Benign'),
('Likely Benign'),
('Likely Pathogenic'),
('Pathogenic'),
('VUS');

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

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `user_classification`
--
ALTER TABLE `user_classification`
  ADD PRIMARY KEY (`user_ID`,`variant_ID`),
  ADD KEY `FK_LabelClassification` (`label_ID`),
  ADD KEY `FK_VariantClassification` (`variant_ID`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `user_classification`
--
ALTER TABLE `user_classification`
  ADD CONSTRAINT `FK_LabelClassification` FOREIGN KEY (`label_ID`) REFERENCES `labels` (`label`),
  ADD CONSTRAINT `FK_VariantClassification` FOREIGN KEY (`variant_ID`) REFERENCES `variants` (`ID`);

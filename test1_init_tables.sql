DROP TABLE IF EXISTS T_indicators;
DROP TABLE IF EXISTS T_resources;
DROP TABLE IF EXISTS T_years;
DROP TABLE IF EXISTS T_values;
DROP TABLE IF EXISTS T_multiplication;
DROP TABLE IF EXISTS T_convertation;


CREATE TABLE T_indicators (
id INTEGER PRIMARY KEY AUTOINCREMENT,
indicator VARCHAR(155) NOT NULL
);

CREATE TABLE T_resources (
id INTEGER PRIMARY KEY AUTOINCREMENT,
resource VARCHAR(155) NOT NULL
);

CREATE TABLE T_years (
id INTEGER PRIMARY Key AUTOINCREMENT,
year INTEGER NOT NULL
);

CREATE TABLE T_values (
id INTEGER PRIMARY Key AUTOINCREMENT,
indicator VARCHAR(155) NOT NULL,
resource VARCHAR(155) NOT NULL,
year INTEGER NOT NULL,
unit VARCHAR(155) NOT NULL,
value FLOAT NOT NULL
);



CREATE TABLE T_multiplication (
id INTEGER PRIMARY Key AUTOINCREMENT,
name VARCHAR(155) NOT NULL,
calc_unit VARCHAR(155) NOT NULL,
e INTEGER NOT NULL,
base_unit VARCHAR(155) NOT NULL
);

CREATE TABLE T_convertation (
id INTEGER PRIMARY Key AUTOINCREMENT,
name VARCHAR(155) NOT NULL,
unit VARCHAR(155) NOT NULL,
k FLOAT NOT NULL,
res_unit VARCHAR(155) NOT NULL
);

INSERT INTO T_indicators (indicator) VALUES ('Energy resource');
INSERT INTO T_resources (resource) VALUES ('Natural gas');
INSERT INTO T_years (year) VALUES
(2017),
(2018),
(2019),
(2020),
(2021);

--

INSERT INTO T_values (indicator, resource, year, unit, value) VALUES
('Energy resource', 'Natural gas', 2017, 'Mtoe', 148.67),
('Energy resource', 'Natural gas', 2018, 'Mtoe', 149.33),
('Energy resource', 'Natural gas', 2019, 'Mtoe', 150.00),
('Energy resource', 'Natural gas', 2020, 'Mtoe', 150.67),
('Energy resource', 'Natural gas', 2021, 'Mtoe', 151.33),

('Water', 'Water resource', 2017, 'Mtoe', 148.67),
('Water', 'Water resource', 2018, 'Mtoe', 149.33),
('Water', 'Water resource', 2019, 'Mtoe', 150.00),
('Water', 'Water resource', 2020, 'Mtoe', 150.67),
('Water', 'Water resource', 2021, 'Mtoe', 151.33);

--

INSERT INTO T_multiplication (name, calc_unit, e, base_unit) VALUES
('Twh <--> wh', 'Twh', -12, 'wh'),
('Gft3ng <--> ft3ng', 'Gft3ng', -9, 'ft3ng'),
('Gtce <--> tce', 'Gtce', -9, 'tce'),
('Gtoe <--> toe', 'Gtoe', -9, 'toe'),
('MMbtu <--> btu', 'MMbtu', -6, 'btu'),
('Mj <--> j', 'Mj', -6, 'j'),
('Kboe <--> boe', 'Kboe', -3, 'boe'),
('Mtoe <--> toe', 'Mtoe', -6, 'toe'),
('Ktoe <--> toe', 'Ktoe', -3, 'toe'),
('Gj <--> j', 'Gj', -9, 'j'),
('Mboe <--> boe', 'Mboe', -6, 'boe'),
('Mtce <--> tce', 'Mtce', -6, 'tce'),
('Gm3ng <--> m3ng', 'Gm3ng', -9, 'm3ng'),
('Bboe <--> boe', 'Bboe', -9, 'boe'),
('Qbtu <--> btu', 'Qbtu', -15, 'btu'),
('Mm3ng <--> m3ng', 'Mm3ng', -6, 'm3ng'),
('Mft3ng <--> ft3ng', 'Mft3ng', -6, 'ft3ng'),
('Gwh <--> wh', 'Gwh', -9, 'wh');

INSERT INTO T_convertation (name, unit, k, res_unit) VALUES
('tce --> m3ng', 'tce', 751.4768963, 'm3ng'),
('ft3ng --> wh', 'ft3ng', 301.277062, 'wh'),
('btu --> j', 'btu', 1055.060005, 'j'),
('boe --> btu', 'boe', 580.00001, 'btu'),
('toe --> tce', 'toe', 1.4285714, 'tce'),
('j --> wh', 'j', 0.000277778, 'wh'),
('toe --> boe', 'toe', 6.8419054, 'boe'),
('m3ng --> ft3ng', 'm3ng', 35.958043, 'ft3ng');

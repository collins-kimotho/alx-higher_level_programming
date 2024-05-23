-- Script to create a new database and table

-- Create the database if it doesn't exist
CREAT DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database
USE hbtn_0d_usa;

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS `hbtn_od_usa.states` (
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
	name VARCHAR(256) NOT NULL
);

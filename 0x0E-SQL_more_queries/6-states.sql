-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn database
USE hbtn_0d_usa;

-- Create the sates table
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	name VARCHAR(256) NOT NULL
):

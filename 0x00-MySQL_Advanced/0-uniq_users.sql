-- Create table with id, email & name attributes
-- if exists, it should not fail
-- script can be executed in any database

CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL AUTO_INCREMENT ,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	PRIMARY KEY(id)

);

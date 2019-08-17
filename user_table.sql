CREATE TABLE Users
(
     id SERIAL PRIMARY KEY,
     fname varchar(25) NOT NULL,
 	lname varchar(25),
 	email varchar(50) NOT NULL,
 	phone_number varchar(20) NOT NULL,
	username varchar(15) NOT NULL,
	pwd varchar(50) NOT NULL
 );
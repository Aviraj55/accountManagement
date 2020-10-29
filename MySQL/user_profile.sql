	create table account_management.user_profile (
	userId int NOT NULL AUTO_INCREMENT,
    firstName varchar(255),
    lastName varchar(255),
    address1 varchar(255),
    address2 varchar(100),
    city varchar(55),
    state varchar(20),	
    phoneNumber varchar(15) UNIQUE NOT NULL,
    emailAddress varchar(320) UNIQUE NOT NULL,
    birthday date,
    PRIMARY KEY (userID)
);



CREATE TABLE account_management.login_info (
	userId int NOT NULL AUTO_INCREMENT, 
	userName varchar(255) NOT NULL UNIQUE,
    passCode varchar(1024) NOT NULL,
    
    CONSTRAINT fk_userID
    FOREIGN KEY (userId)
		REFERENCES account_management.user_profile(userId)
);
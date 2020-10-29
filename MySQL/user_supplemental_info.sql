CREATE TABLE account_management.user_supplemental_info(
	userId int,
	bio varchar(255),
    occupation varchar(255),
    workplace varchar(255),
    
    CONSTRAINT supp_user_profile_fk
    FOREIGN KEY (userId)
		REFERENCES account_management.user_profile(userId)
    
);
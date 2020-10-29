use account_management;

select l.userId,
	   l.userName,
       u.firstName,
       u.lastName,
       u.address1,
       u.address2,
       u.city,
       u.state,
       u.phoneNumber,
       u.emailAddress,
       u.birthday,
       usi.bio,
       usi.occupation,
       usi.workplace
       from login_info as l
	join user_profile as u
	on l.userId = u.userId
    join user_supplemental_info as usi
    on usi.userID = u.userId

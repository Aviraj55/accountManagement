# accountManagement
accountManagement is a project in MySQL and Python used for handling and managing a user account system using AWS AuroraDB RDS and API Gateway.

# Features

* Get user data from username
* Add user

# TODO

* Add friends


## Usage
* On an existing AWS account, use AWS RDS and create a DB with the files under the MySQL directory.

* Copy paste python files into AWS Lambda. Create a file named "rds_config" containing your username and password for the RDS database. 

* Create AWS Gateway REST API connecting to each lambda function to enable REST API


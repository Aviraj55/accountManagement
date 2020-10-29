import json
import sys
import logging
import rds_config
import pymysql
from hash import hashPasscode

# rds settings
rds_host = "my-db-instance-1.chnpa6xuu6y1.us-east-2.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)


try:
    conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error(
        "ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    print("ERROR COULD NOT CONNECT")
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
print("CONNECTION SUCCESS")


def lambda_add_user(event, context):

    responseObject = {}
    body = {}

    user_name = None
    password = None
    first_name = None
    last_name = None
    address1 = None
    address2 = None
    city = None
    state = None
    phone_number = None
    email_address = None
    birthday = None

    if "userName" in event["queryStringParameters"]:
        user_name = event["queryStringParameters"]["userName"]

    if "password" in event["queryStringParameters"]:
        password = event["queryStringParameters"]["password"]
        password = hashPasscode(password)

    if "firstName" in event["queryStringParameters"]:
        first_name = event["queryStringParameters"]["firstName"]

    if "lastName" in event["queryStringParameters"]:
        last_name = event["queryStringParameters"]["lastName"]

    if "address1" in event["queryStringParameters"]:
        address1 = event["queryStringParameters"]["address1"]

    if "address2" in event["queryStringParameters"]:
        address2 = event["queryStringParameters"]["address2"]

    if "city" in event["queryStringParameters"]:
        city = event["queryStringParameters"]["city"]

    if "state" in event["queryStringParameters"]:
        state = event["queryStringParameters"]["state"]

    if "phoneNumber" in event["queryStringParameters"]:
        phone_number = event["queryStringParameters"]["phoneNumber"]

    if "emailAddress" in event["queryStringParameters"]:
        email_address = event["queryStringParameters"]["emailAddress"]

    if "birthday" in event["queryStringParameters"]:
        birthday = event["queryStringParameters"]["birthday"]

    if not user_name or not password or not first_name or not last_name or not email_address:
        responseObject["header"] = {}
        responseObject["header"]["Content-Type"] = 'application/json'
        responseObject["statusCode"] = 400
        responseObject["message"] = 'missing required field'
        responseObject["body"] = {}
        return responseObject

    with conn.cursor() as cur:

        cur.execute("USE account_management;")
        cur.execute("INSERT INTO login_info (userName, passCode) VALUES \
    (%s, %s)", (user_name,), (password,))

    return responseObject

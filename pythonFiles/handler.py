import sys
import logging
import json
import datetime
import rds_config
import pymysql
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


def lambda_handler(name: str):
    # RETURN USER DATA GIVEN USERNAME

    body = {}
    with conn.cursor() as cur:
        cur.execute("select l.userId, \
                l.userName,\
                u.firstName,\
                u.lastName,\
                u.address1,\
                u.address2,\
                u.city,\
                u.state,\
                u.phoneNumber,\
                u.emailAddress,\
                u.birthday,\
                usi.bio,\
                usi.occupation,\
                usi.workplace\
                from login_info as l\
                join user_profile as u\
                on l.userId=u.userId\
                join user_supplemental_info as usi\
                on usi.userID=u.userId\
                where l.userName = %s", (name,))

        rows = cur.fetchall()

        body["userId"] = rows[0][0]
        body["userName"] = rows[0][1]
        body["firstName"] = rows[0][2]
        body["lastName"] = rows[0][3]
        body["address1"] = rows[0][4]
        body["address2"] = rows[0][5]
        body["city"] = rows[0][6]
        body["state"] = rows[0][7]
        body["phoneNumber"] = rows[0][8]
        body["emailAddress"] = rows[0][9]
        body["birthday"] = rows[0][10],
        body["bio"] = rows[0][11]
        body["occupation"] = rows[0][12]
        body["workplace"] = rows[0][13]

        t = body["birthday"][0]
        t.strftime("%y-%m-%d")
        del body["birthday"]

        body["birthday"] = str(t)
        print(body["birthday"])

    return json.dumps(body)


print(lambda_handler("eeakleil"))

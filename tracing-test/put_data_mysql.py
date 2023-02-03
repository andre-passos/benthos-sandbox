import random

import mysql.connector             
from mysql.connector import Error  
from faker import Faker

Faker.seed(33422)
fake = Faker()

conn = mysql.connector.connect(host="localhost",port=3307, database="4steps",
                               user="root", password="root")
cursor = conn.cursor()
  
row = [fake.first_name(), random.randint(0,99), fake.date_of_birth()]
createtable = """ CREATE TABLE IF NOT EXISTS `data` 
                    ( 
                    `id`         bigint(20) NOT NULL      AUTO_INCREMENT,
                    `datetime`   timestamp  NULL          DEFAULT CURRENT_TIMESTAMP,
                    `channel`    int(11)                  DEFAULT NULL,
                    `value`      float                    DEFAULT NULL,

                    PRIMARY KEY (`id`)
                    ); """

dropprocedure = """drop procedure if exists generate_data;"""

createprocedure = """CREATE PROCEDURE generate_data()
                        BEGIN
                        DECLARE i INT DEFAULT 0;
                        WHILE i < 100000 DO
                            INSERT INTO `data` (`datetime`,`value`,`channel`) VALUES (
                            FROM_UNIXTIME(UNIX_TIMESTAMP('2018-01-01 01:00:00')+FLOOR(RAND()*31536000)),
                            ROUND(RAND()*100,2),
                            1
                            );
                            SET i = i + 1;
                        END WHILE;
                        END; """

runprocedure = """CALL generate_data();"""

cursor.execute( createtable )
conn.commit()
cursor.execute( dropprocedure )
conn.commit()
cursor.execute( createprocedure )
conn.commit()
cursor.execute( runprocedure )
conn.commit()
cursor.close() 

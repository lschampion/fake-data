
import mysql.connector
from faker import Faker
import math
import random
import time
fake = Faker(locale='zh_CN')   

# print(fake.name())
# print(fake.address())
# print(fake.company())
# print(fake.date(pattern="%Y-%m-%d", end_datetime=None))
# print(fake.date_time(tzinfo=None, end_datetime=None))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="test"
)


mycursor = mydb.cursor()
mycursor.execute("select max(s_id) s_id from student")
s_id_max=0
for x in mycursor:
    s_id_max=x[0]+1
print("s_id_max:",s_id_max)
insert_template="insert into student values(%s , %s, %s , %s,%s)"

sex_list=["男","女"]

while True:
    vs=(s_id_max,fake.name(),fake.date(pattern="%Y-%m-%d", end_datetime=None),sex_list[random.randint(1,2)%2],time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
    time.sleep(3)
    print(vs)
    mycursor.execute(insert_template, vs)
    mydb.commit()
    s_id_max+=1

mydb.close()

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
  if x[0] is not None:
    s_id_max=x[0]+1
  else:
    s_id_max=0
print("s_id_max:",s_id_max)

mycursor.execute("select max(a_id) a_id from address")
a_id_max=0
for x in mycursor:
  if x[0] is not None:
    a_id_max=x[0]+1
  else:
    a_id_max=0
print("a_id_max:",a_id_max)
insert_template_student="insert into student values(%s , %s, %s)"
insert_template_address="insert into address values(%s , %s, %s)"

sex_list=["男","女"]

while True:
    vs=(s_id_max,fake.name(),sex_list[random.randint(1,2)%2])
    va=(a_id_max,fake.address(),fake.city_name())

    time.sleep(3)
    print(vs,"  ---  ",va)
    mycursor.execute(insert_template_student, vs)
    mycursor.execute(insert_template_address, va)

    mydb.commit()
    s_id_max+=1
    a_id_max+=1

mydb.close()
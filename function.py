import mysql.connector

# CONNECTION TO MYSQL DB
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="jerseystorefoe")
mycursor=mydb.cursor()


# FUNCTION FOR ADDING USER DATA TO DATABASE
def add_userdata_to_db(data):
    dholu=data['username']
    bholu=data['email']
    chutki=data['password']
    sqlform="insert into login (username, email, password) values (%s,%s,%s)"
    datainpt1=[(dholu,bholu,chutki)]
    mycursor.executemany(sqlform,datainpt1)
    mydb.commit()
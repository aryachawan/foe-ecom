import mysql.connector
import re


# CONNECTION TO MYSQL DB
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="jerseystorefoe")
mycursor=mydb.cursor()


# FUNCTION FOR ADDING USER DATA TO DATABASE
def login_add_userdata_to_db(data):
    dholu=data['username']
    bholu=data['email']
    chutki=data['password']
    sqlform="insert into login (username, email, password) values (%s,%s,%s)"
    datainpt1=[(dholu,bholu,chutki)]
    mycursor.executemany(sqlform,datainpt1)
    mydb.commit()

# FUNCTION FOR LOADING USER DATA
def login_get_user_data():
    sqlform1="select * from login"
    mycursor.execute(sqlform1)
    logindata=mycursor.fetchall() #INITIAL DATA IS FETCHED IN THE FORM OF TUPLE
    logindata_dict=[] #DICTIONARY FOR STORING LOGIN DATA
    for i in logindata:
        dict_temp={
            "username":i[1],
            "email":i[2],
            "password":i[3]
        }
        logindata_dict.append(dict_temp)
    return logindata_dict

# FUNCTION FOR LOADING INVENTORY DATA
def inventory_get_user_data():
    sqlform="select * from inventory"
    mycursor.execute(sqlform)
    inventorydata=mycursor.fetchall()
    inventorydata_dict=[]
    for i in inventorydata:
        dict_temp={
            "name":i[1],
            "size":i[2],
            "price":i[3]
        }
        inventorydata_dict.append(dict_temp)
    return inventorydata_dict

# PASSWORD STRENGTH CALCULATOR FUNCTION
def checkpasswordstrength(siu):    
    password=siu
    uppercase_pattern = re.compile(r"[A-Z]")
    lowercase_pattern = re.compile(r"[a-z]")
    digit_pattern = re.compile(r"\d")
    special_char_pattern = re.compile(r"[\W_]")

    has_uppercase = uppercase_pattern.search(password)
    has_lowercase = lowercase_pattern.search(password)
    has_digit = digit_pattern.search(password)
    has_special_char = special_char_pattern.search(password)

    password_score = 0

    if has_uppercase:
        password_score += 20
    if has_lowercase:
        password_score += 20
    if has_digit:
        password_score += 20
    if has_special_char:
        password_score += 20
    if len(password) >= 7:
        password_score += 20
    if len(password) <=3:
        password_score -= 10

    return password_score

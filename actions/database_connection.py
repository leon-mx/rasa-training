import mysql.connector
def save_data(name, age, phone):
    mydb = mysql.connector.connect(host = "localhost", port = "3306", user = "root", password = "", database = "mydata")
    mydata = mydb.cursor()
    # mydata.execute("CREATE TABLE USER_DETAILS(NAME VARCHAR(30), AGE INT(2), PHONE VARCHAR(10));")
    mydata.execute('INSERT INTO USER_DETAILS(NAME, AGE, PHONE) VALUES ("{}", {}, "{}");'.format(name, age, phone))
    mydb.commit()

def save_form(name, phone, email):
    mydb = mysql.connector.connect(host = "localhost", port = "3306", user = "root", password = "", database = "mydata")
    mydata = mydb.cursor()
    # mydata.execute("CREATE TABLE USER_FORM(NAME VARCHAR(30), PHONE VARCHAR(10), EMAIL VARCHAR(30));")
    mydata.execute('INSERT INTO USER_FORM(NAME, PHONE, EMAIL) VALUES ("{}", {}, "{}");'.format(name, phone, email))
    mydb.commit()

# How to search information in the database
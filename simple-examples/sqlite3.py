import sqlite3
# he is basic simple sqlite operations
# thank you
# by Ubeyde
# python_version = '3.6.52
# sqlite_version = '3.21.0'


def create_database():
    con  = sqlite3.connect("Database.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_info(Username VARCHAR,Password VARCHAR)")
    con.commit()
    con.close()

def insert_values():
    a = input("username:")
    b = input("Password")
    database = sqlite3.connect("Database.db")
    cursor = database.cursor()
    cursor.execute("INSERT INTO user_info VALUES(?,?)",(a,b))
    database.commit()
    database.close()


def select_values():
    con = sqlite3.connect("Database.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM  user_info")
    rows = cursor.fetchall()
    for i in rows:
        print(i[0])

def delete_values():
    query = input("login values:")
    cn = sqlite3.connect("Database.db")
    cursor = cn.cursor()
    cursor.execute("DELETE FROM user_info WHERE Password = (?) ",(query,))
    cn.commit()
    cn.close()
    print("Deleting completed :)")

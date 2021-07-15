import pymysql

db = pymysql.connect('localhost','root','123456','crm')
cursor = db.cursor()
def getAllNum(sql):
    cursor.execute(sql)
    num = cursor.fetchone()
    return num[0]



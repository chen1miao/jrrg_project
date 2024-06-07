import mysql.connector

def connect_sql(params=None, fetchone=False):
    try:
        db = mysql.connector.connect(
            host='172.24.116.145',
            port=3306,
            user='root',
            password='wxwwxw2022',
            database='stock_data'
        )
        
        return db
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None
db=connect_sql()  
sql='CREATE TABLE IF NOT EXISTS test_(trade_date DATE PRIMARY KEY,open FLOAT)'
cursor = db.cursor()
cursor.execute(sql)
db.commit()
sql1='INSERT INTO test_(trade_date, open) VALUES (%s, %s)'
value=('20180701',2.3)
cursor.execute(sql1,value)
db.commit()


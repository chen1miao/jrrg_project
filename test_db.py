import json
from db import app, execute_sql_query
import mysql.connector


def execute_sql_query(sql, params=None, fetchone=False):
    try:
        # 
        db = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='wxwwxw2022',
            database='stock_data'
        )

        # 
        cursor = db.cursor(dictionary=True)
        #  SQL 
        cursor.execute(sql, params)
        # 
        if fetchone:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        # 
        cursor.close()
        # 
        db.commit()

        # 
        db.close()

        return result

    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None

date='2023-06-05'
open=7.35
update_user_params=(open,date)
#select_query1 = 'SELECT open FROM sh1 WHERE trade_date = %s'
update_query = "UPDATE sh1 SET open = %s WHERE trade_date = %s"
open=execute_sql_query(update_query,update_user_params)
'''open=open[0]
open=open['open']
print(open)'''
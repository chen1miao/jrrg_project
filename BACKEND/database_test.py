import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import tushare as ts
import os
import tushare as ts
import pymysql
import mysql.connector

def execute_sql(params=None, fetchone=False):
    try:
        db = mysql.connector.connect(
            host='172.27.142.184',
            port=3306,
            user='root',
            password='0406722cm',
            database='lfcx_db'
        )
        print(1)
        return db  # 返回数据库连接对象

    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None

db = execute_sql()
if db:  # 检查是否成功连接数据库
    cursor = db.cursor()
    tb='wxw_test'
    sql = f"CREATE TABLE IF NOT EXISTS {tb} (trade_date DATE PRIMARY KEY,open FLOAT)"
    cursor.execute(sql)
    db.commit()

    sql1 = f"INSERT INTO {tb}(trade_date,open) VALUES(%s,%s)"
    # 提供示例数据，实际应该传递参数给 execute 函数
    cursor.execute(sql1, ('2024-06-03', 100))
    db.commit()
else:
    print("Failed to connect to the database.")
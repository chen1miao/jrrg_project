'''params：（可选）SQL查询中的参数，用于传递给查询语句中的占位符。
fetchone：（可选）一个布尔值，用于指定是否只获取查询结果的第一行。'''
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import tushare as ts
import os
import tushare as ts
import pymysql
import mysql.connector
from sqlalchemy import create_engine
ts.set_token('7366b088a1d55d30e06073e16adbc90ab29d9b598d2ec03cb5795247')
pro = ts.pro_api()
stock_code_list=[['000001.sz','sz1'],['000002.sz','sz2'],['000008.sz','sz3'],['000027.sz','sz4'],['000028.sz','sz5'],['600000.sh','sh1'],['600004.sh','sh2'],['600007.sh','sh3'],['600056.sh','sh4'],['600064.sh','sh5']]


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


def get_data_and_store(code, start, end, db,name):
    table_name=name
    if db:  # 检查是否成功连接数据库
        cursor = db.cursor()
        sql=f"CREATE TABLE IF NOT EXISTS {table_name}(trade_date DATE PRIMARY KEY,open FLOAT,high FLOAT,low FLOAT,close FLOAT,volume FLOAT)"
        cursor.execute(sql)
        db.commit()
    else:
        print("Failed to connect to the database.")
    df = pro.daily(ts_code=code, autype='qfq', start_date=start, end_date=end)
    df.index = pd.to_datetime(df.trade_date)
    df = df[['open', 'high', 'low', 'close', 'vol']]
    print(df)
    try:
        # 存储数据到数据库中
        for index, row in df.iterrows():
            sql = f"INSERT INTO {table_name}(trade_date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (index.strftime('%Y-%m-%d'), row['open'], row['high'], row['low'], row['close'], row['vol'])
            cursor = db.cursor(dictionary=True)
            cursor.execute(sql,values)
            db.commit()
        print("数据已成功存储到数据库中！")
    except Exception as e:
        print("存储数据时出现错误:", e)


def main():
    db=connect_sql()
    
    inp_start='20230605'
    inp_end='20240602'
    for inp_code in stock_code_list:
        get_data_and_store(inp_code[0],inp_start,inp_end,db,inp_code[1])
    #get_data('000001.SZ','20180701','20180718')


if __name__ == "__main__":
    main()



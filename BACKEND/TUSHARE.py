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
def execute_sql(params=None, fetchone=False):
    try:
        db = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='wxwwxw2022',
            database='stock_data'
        )
        '''cursor = db.cursor(dictionary=True)
        #  SQL 
        #cursor.execute(sql, params)
        if fetchone:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        cursor.close()
        db.commit()
        db.close()'''
        return db
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None
def main():
    '''df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
    print(df)'''
    print(1)
    sql='CREATE TABLE IF NOT EXISTS data (trade_date DATE PRIMARY KEY,open FLOAT,high FLOAT,low FLOAT,close FLOAT,volume FLOAT)'
    print(2)
    db=execute_sql()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)
    print("start")
    acquire_code(db)
    #get_data('000001.SZ','20180701','20180718')
def get_data_and_store(code, start, end,db):
    df = pro.daily(ts_code=code, autype='qfq', start_date=start, end_date=end)
    df.index = pd.to_datetime(df.trade_date)
    df = df[['open', 'high', 'low', 'close', 'vol']]
    print(df)
    try:
        # 存储数据到数据库中
        for index, row in df.iterrows():
            sql = 'INSERT INTO data (trade_date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s)'
            print(11)
            values = (index.strftime('%Y-%m-%d'), row['open'], row['high'], row['low'], row['close'], row['vol'])
            print(22)
            cursor = db.cursor(dictionary=True)
            cursor.execute(sql)
        
        print("数据已成功存储到数据库中！")
    
    except Exception as e:
        print("存储数据时出现错误:", e)
def acquire_code(db):   #只下载一只股票数据，且只用CSV保存   未来可以有自己的数据库
    inp_code =input("请输入股票代码:\n")
    inp_start = input("请输入开始时间:'\n'")
    inp_end = input("请输入结束时间:'\n'")
    get_data_and_store(inp_code,inp_start,inp_end,db)
    #print(df.info())
main()



'''def get_data(code,start,end):
    df=pro.daily(ts_code=code,autype='qfq',start_date=start,end_date=end)
    print(df)
    df.index = pd.to_datetime(df.trade_date)
    #设置把日期作为索引
    #df['ma'] = 0.0  # Backtrader需要用到
    #df['openinterest'] = 0.0  # Backtrader需要用到
    #定义两个新的列ma和openinterest
    df = df[['open', 'high', 'low', 'close', 'vol']]
    #重新设置df取值，并返回df
    return df'''

'''def write_to_sql(data, table, db):
    password = 'wxwwxw2022'
    ipaddress = 'localhost'
    port = '3306'
    engine = create_engine(
        f'mysql+pymysql://root:{password}@{ipaddress}:{port}/{db}?charset=utf8')  # 密码中包含特殊字符，如@等，所以密码中有特殊字符需要转码，否则在拼接时会认为是密码和IP地址拼接的@字符，为了避免特殊字符的影响，采用urlquote(特殊字符)解决问题
    try:
        data.to_sql(table, con=engine, if_exists='append', index=False) #append是向末尾追加元素
        # append表示在原有表基础上增加，但该表要有表头
    except Exception as e:
        print(e)'''


'''#输出统计各列的数据量
    print("—"*30)
    #分割线
    print(df.describe())
    #输出常用统计参数
    df.sort_index(inplace=True)
    print("—"*30)
    print(df)
    print("11111111111")
    #把股票数据按照时间正序排列
    path = os.path.join(os.path.join(os.getcwd(),
        "stoke_data"), inp_code + ".csv")
    #os.path地址拼接，''数据地址''为文件保存路径
    # path = os.path.join(os.path.join(os.getcwd(),"数据地址"),inp_code+"_30M.csv")
    df.to_csv(path)'''
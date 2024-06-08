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
'''
df = pro.daily(ts_code='000001.sz', autype='qfq', start_date='20240510', end_date='20240517')
df.index = pd.to_datetime(df.trade_date)
df = df[['open', 'high', 'low', 'close', 'vol']]
print(df)'''

# 查询多只股票基本信息
#sina数据
df = ts.realtime_quote(ts_code='600000.SH,000001.SZ,000001.SH')
print(df)


#东财数据
df = ts.realtime_quote(ts_code='600000.SH', src='dc')
print(df)

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

df = pro.daily(ts_code='000001.sz', autype='qfq', start_date='20240510', end_date='20240517')
df.index = pd.to_datetime(df.trade_date)
df = df[['open', 'high', 'low', 'close', 'vol']]
print(df)
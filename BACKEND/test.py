import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import tushare as ts
import os
import tushare as ts
import pymysql
import mysql.connector
from sqlalchemy import create_engine

'''ts.set_token('7366b088a1d55d30e06073e16adbc90ab29d9b598d2ec03cb5795247')
pro = ts.pro_api()'''
'''
df = pro.daily(ts_code='000001.sz', autype='qfq', start_date='20240510', end_date='20240517')
df.index = pd.to_datetime(df.trade_date)
df = df[['open', 'high', 'low', 'close', 'vol']]
print(df)'''

# 查询多只股票基本信息
#sina数据
stock_info_sz = ts.realtime_quote(ts_code='000001.sz,000002.sz,000008.sz,000009.sz,000019.sz,000027.sz,000028.sz,000069.sz,000155.SZ,000428.SZ')
stock_info_sh = ts.realtime_quote(ts_code='600000.sh,600004.sh,600007.sh,600056.sh,600064.sh,600031.sh,600089.sh,688046.SH,688113.SH,688131.SH')

stock_info_sz = stock_info_sz[['NAME', 'TS_CODE', 'DATE', 'TIME', 'OPEN','PRE_CLOSE','PRICE','HIGH','LOW','VOLUME','AMOUNT']]
stock_info_sh = stock_info_sh[['NAME', 'TS_CODE', 'DATE', 'TIME', 'OPEN','PRE_CLOSE','PRICE','HIGH','LOW','VOLUME','AMOUNT']]

stock_list_sh = []
if not stock_info_sh.empty:  # 确保DataFrame不为空
    for index, row in stock_info_sh.iterrows():
        stock_dict = {
            '股票代码': str(row['TS_CODE']),
            '名称': str(row['NAME']),
            '日期': str(row['DATE']),
            '时间': str(row['TIME']),
            '当日开盘价': str(row['OPEN']),
            '昨日收盘价': str(row['PRE_CLOSE']),
            '当前价格': str(row['PRICE']),
            '最高价': str(row['HIGH']),
            '最低价': str(row['LOW']),
            '成交量（股）': str(row['VOLUME']),
            '成交金额': str(row['AMOUNT']),
        }
        stock_list_sh.append(stock_dict)

stock_list_sz = []
if not stock_info_sz.empty:  # 确保DataFrame不为空
    for index, row in stock_info_sz.iterrows():
        stock_dict = {
            '股票代码': str(row['TS_CODE']),
            '名称': str(row['NAME']),
            '日期': str(row['DATE']),
            '时间': str(row['TIME']),
            '当日开盘价': str(row['OPEN']),
            '昨日收盘价': str(row['PRE_CLOSE']),
            '当前价格': str(row['PRICE']),
            '最高价': str(row['HIGH']),
            '最低价': str(row['LOW']),
            '成交量（股）': str(row['VOLUME']),
            '成交金额': str(row['AMOUNT']),
        }
        stock_list_sz.append(stock_dict)
print(stock_list_sz)
print(stock_list_sh)


#东财数据
#df = ts.realtime_quote(ts_code='600000.SH', src='dc')
#print(df)

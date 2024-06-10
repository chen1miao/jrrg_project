import pandas as pd
import pymysql
import matplotlib.pyplot as plt

sql_connection = pymysql.connect(host='172.24.127.174', user='root', password='0406722cm'
                                 ,db='lfcx_db', port=3306, autocommit=False, charset='utf8mb4')
'''for name in ['sh1','sh2','sh3','sh4','sh5','sz1','sz2','sz3','sz4','sz5']:
    sql = f"select * from lfcx_db.{name}"
    df_sql = pd.read_sql(sql,sql_connection)#参数：查询语句+连接配置

'''

name='sz10'    
sql = f"select * from lfcx_db.{name}"
df_sql = pd.read_sql(sql,sql_connection)#参数：查询语句+连接配置

maIntervalList = [5,10,30,60]
for maInterval in maIntervalList:
    df_sql['MA_' + str(maInterval)] = df_sql['close'].rolling(window=maInterval).mean()
start=1000000
money=start
stock=0
a=0
cnt=1
everyday={}
while cnt<=len(df_sql)-1:
    try:
        todaytotal=money+stock*df_sql.iloc[cnt]['close']
        if a==1:
            if df_sql.iloc[cnt-1]['MA_30']<df_sql.iloc[cnt-1]['close'] and df_sql.iloc[cnt]['MA_30']>df_sql.iloc[cnt]['close']:
                print("Sell Point on:" + str(df_sql.iloc[cnt]['trade_date']))
                money=money+stock*df_sql.iloc[cnt]['close']
                stock=0
                print(money,stock)
                total=money+stock*df_sql.iloc[cnt]['close']
                print(total)
                a=0
        if a==0:
            if df_sql.iloc[cnt-1]['MA_30']>df_sql.iloc[cnt-1]['close'] and df_sql.iloc[cnt]['MA_30']<df_sql.iloc[cnt]['close']:
                print("Buy Point on:" + str(df_sql.iloc[cnt]['trade_date']))
                stock=money//df_sql.iloc[cnt]['close']
                money=money-stock*df_sql.iloc[cnt]['close']
                print(money,stock)
                total=money+stock*df_sql.iloc[cnt]['close']
                print(total)
                a=1
        everyday[df_sql.iloc[cnt]['trade_date']]=(todaytotal,0)
        
    except: 
        everyday[df_sql.iloc[cnt]['trade_date']]=(start,0)
        pass
    cnt=cnt+1

cnt=0
while cnt<=len(df_sql)-1:
    try:
        everyday[df_sql.iloc[cnt]['trade_date']]=(everyday[df_sql.iloc[cnt]['trade_date']][0],df_sql.iloc[cnt]['close'])
    except:
        pass
    cnt=cnt+1

total=todaytotal
print(total)
print(everyday)
x = list(everyday.keys())
y1 = [x[0] for x in everyday.values()]
y2 = [x[1] for x in everyday.values()]

# 绘制折线图
fig,ax1=plt.subplots()
ax1.plot(x, y1, marker='.', linestyle='-',color='blue',markersize=1)
ax2=ax1.twinx()
ax2.plot(x, y2, marker='.', linestyle='-',color='salmon',markersize=1) 
'''plt.figure(figsize=(10, 6))  # 设置图形尺寸
plt.plot(x, y1, marker='.', linestyle='-',color='blue')  # 绘制折线图
plt.plot(x, y2, marker='.', linestyle='-',color='salmon') '''
plt.title('time-total')  # 设置标题
plt.xlabel('time')  # 设置x轴标签
plt.ylabel('total')  # 设置y轴标签
plt.xticks(rotation=45)  # 旋转x轴标签
plt.grid(True)  # 显示网格线
plt.tight_layout()  # 自动调整布局，防止标签重叠
plt.show()  # 显示图表
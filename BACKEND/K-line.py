import mplfinance as mpf
import pandas as pd
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
    
def draw_K_line(name,db):
    table_name=name
    query = f"SELECT * FROM {table_name}"
    # 从数据库中读取数据到DataFrame
    df = pd.read_sql(query, db)
    df.set_index('trade_date', inplace=True) #索引设置成交易时间
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']  
    df.index.name = 'Date'  
    df = df.astype(float) 
    # 显式转换索引为DatetimeIndex类型
    df.index = pd.to_datetime(df.index)


    kwargs = dict(type='candle', volume=True, show_nontrading=True, 
    style='yahoo', title=f"stock_{table_name}_K-line", ylabel='price')  
    mpf.plot(df, **kwargs, mav=(5, 10, 20)) 
    # 绘制K线图  
    #mpf.plot(df, type='candle', volume=True, show_nontrading=True)  



    
def main():
    db=connect_sql()
    name='sz1'
    draw_K_line(name,db)


if __name__ == "__main__":
    main()
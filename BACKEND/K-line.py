import mplfinance as mpf
import pandas as pd
import numpy as np
import mysql.connector

def connect_sql(params=None, fetchone=False):
    try:
        db = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='wxwwxw2022',
            database='stock_data'
        )
        
        return db
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None
    
def draw_K_line(name,db,stock_code):
    table_name=name
    query = f"SELECT * FROM {table_name}"
    # 从数据库中读取数据到DataFrame
    df = pd.read_sql(query, db)
    #df=df.iloc[1:100]
    df.set_index('trade_date', inplace=True) #索引设置成交易时间
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']  
    df.index.name = 'Date'  
    df = df.astype(float) 
    # 显式转换索引为DatetimeIndex类型
    df.index = pd.to_datetime(df.index)


    last_data = df.iloc[-1]


    title_font = {'fontname': 'Arial', 
              'size':     '16',
              'color':    'black',
              'weight':   'bold',
              'va':       'bottom',
              'ha':       'center'}
    large_red_font = {'fontname': 'Arial',
                  'size':     '24',
                  'color':    'red',
                  'weight':   'bold',
                  'va':       'bottom'}
    small_red_font = {'fontname': 'Arial',
                  'size':     '12',
                  'color':    'red',
                  'weight':   'bold',
                  'va':       'bottom'}
    # 小数字格式（显示其他价格信息）粗体绿色12号字
    small_green_font = {'fontname': 'Arial',
                        'size':     '12',
                        'color':    'green',
                        'weight':   'bold',
                        'va':       'bottom'}


    # 设置mplfinance的蜡烛颜色，up为阳线颜色，down为阴线颜色
    my_color = mpf.make_marketcolors(up='r',
                                    down='g',
                                    edge='inherit',
                                    wick='inherit',
                                    volume='inherit')
    # 设置图表的背景色
    my_style = mpf.make_mpf_style(marketcolors=my_color,
                                figcolor='(0.82, 0.83, 0.85)',
                                gridcolor='(0.82, 0.83, 0.85)')
    # 使用mpf.figure()函数可以返回一个figure对象，从而进入External Axes Mode，从而实现对Axes对象和figure对象的自由控制
    fig = mpf.figure(style=my_style, figsize=(12, 8), facecolor=(0.82, 0.83, 0.85))
    # 添加三个图表，四个数字分别代表图表左下角在figure中的坐标，以及图表的宽（0.88）、高（0.60）
    ax1 = fig.add_axes([0.06, 0.25, 0.88, 0.60])
    # 添加第二、三张图表时，使用sharex关键字指明与ax1在x轴上对齐，且共用x轴
    ax2 = fig.add_axes([0.06, 0.15, 0.88, 0.10], sharex=ax1)
    #ax3 = fig.add_axes([0.06, 0.05, 0.88, 0.10], sharex=ax1)
    # 设置三张图表的Y轴标签
    ax1.set_ylabel('price')
    ax2.set_ylabel('volume')
    #ax3.set_ylabel('macd')
    # 在figure对象上添加文本对象，用于显示各种价格和标题
    fig.text(0.50, 0.94, f"{stock_code}", **title_font)
    fig.text(0.05, 0.90, 'open/closse: ')
    fig.text(0.14, 0.89, f'{np.round(last_data["Open"], 3)} / {np.round(last_data["Close"], 3)}',**large_red_font)
    '''fig.text(0.14, 0.86, f'{last_data["change"]}')
    fig.text(0.22, 0.86, f'[{np.round(last_data["pct_change"], 2)}%]')'''
    fig.text(0.05, 0.86, f'{last_data.name.date()}')
    fig.text(0.40, 0.90, 'high: ')
    fig.text(0.45, 0.90, f'{last_data["High"]}',**small_red_font)
    fig.text(0.40, 0.86, 'low: ')
    fig.text(0.45, 0.86, f'{last_data["Low"]}',**small_green_font)
    fig.text(0.60, 0.90, 'volume(10000): ')
    fig.text(0.71, 0.90, f'{np.round(last_data["Volume"] / 10000, 3)}') 
    '''fig.text(0.55, 0.86, '额(亿元): ')
    fig.text(0.55, 0.86, f'{last_data["value"]}')
    fig.text(0.70, 0.90, '涨停: ')
    fig.text(0.70, 0.90, f'{last_data["upper_lim"]}')
    fig.text(0.70, 0.86, '跌停: ')
    fig.text(0.70, 0.86, f'{last_data["lower_lim"]}')
    fig.text(0.85, 0.90, '均价: ')
    fig.text(0.85, 0.90, f'{np.round(last_data["average"], 3)}')
    fig.text(0.85, 0.86, '昨收: ')
    fig.text(0.85, 0.86, f'{last_data["last_close"]}')'''


    
    mpf.plot(df, style=my_style, type='candle', ax=ax1,volume=ax2,mav=(5, 10, 20))
    mpf.show()

'''def which_stoke(stock_code):
    stock_code_list=[['000001.sz','sz1'],['000002.sz','sz2'],['000008.sz','sz3'],['000009.sz','sz4'],['000019.sz','sz5'],
                 ['000027.sz','sz6'],['000028.sz','sz7'],['000069.sz','sz8'],['000155.sz','sz9'],['000428.sz','sz10'],
                 ['600000.sh','sh1'],['600004.sh','sh2'],['600007.sh','sh3'],['600056.sh','sh4'],['600064.sh','sh5'],
                 ['600031.sh','sh6'],['600089.sh','sh7'],['688046.sh','sh8'],['688113.sh','sh9'],['688131.sh','sh10']]
    for each in stock_code_list:
        if stock_code==each[0]:
            return each[1]#返回的是表里的名字'''
    
def main():
    db=connect_sql()
    stock_code='600031.sz'
    stock_code_list=[['000001.sz','sz1'],['000002.sz','sz2'],['000008.sz','sz3'],['000009.sz','sz4'],['000019.sz','sz5'],
                 ['000027.sz','sz6'],['000028.sz','sz7'],['000069.sz','sz8'],['000155.sz','sz9'],['000428.sz','sz10'],
                 ['600000.sh','sh1'],['600004.sh','sh2'],['600007.sh','sh3'],['600056.sh','sh4'],['600064.sh','sh5'],
                 ['600031.sh','sh6'],['600089.sh','sh7'],['688046.sh','sh8'],['688113.sh','sh9'],['688131.sh','sh10']]
    for each in stock_code_list:
        name=each[1]
    
    draw_K_line(name,db,stock_code)


if __name__ == "__main__":
    main()
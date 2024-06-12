import os
from flask import Flask, request, session, jsonify, send_file
from flask_cors import CORS
from db import app, execute_sql_query  #  ensure you have implemented execute_sql_query correctly
import tushare as ts
import akshare as ak
import json
import mplfinance as mpf
import pandas as pd
import numpy as np
import io
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import pymysql

ts.set_token('7366b088a1d55d30e06073e16adbc90ab29d9b598d2ec03cb5795247')
pro = ts.pro_api()

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)  # enable CORS for all routes

def getresponse(code=200, msg=None, data=None):
    res = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return jsonify(res)

@app.route('/register', methods=['POST'])
def register():
    print(request.json)
    username = request.json['username']
    password = request.json['password']
    cash = request.json['cash']
    trans_cur=[]
    trans_cur.append({ 'trans_id': 0 })
    transaction_history=json.dumps(trans_cur)
    stock_list=['000001.sz','000002.sz','000008.sz','000009.sz','000019.sz',
                '000027.sz','000028.sz','000069.sz','000155.sz','000428.sz',
                '600000.sh','600004.sh','600007.sh','600056.sh','600064.sh',
                '600031.sh','600089.sh','688046.sh','688113.sh','688131.sh']
    hold_list=[]
    for each_stock_code in stock_list:
        stock_dic={'stock_code':each_stock_code,'amount':0}
        hold_list.append(stock_dic)
    holdings=json.dumps(hold_list)
    existing_user_sql = "SELECT * FROM user WHERE username = %s"
    existing_user_params = (username,)
    existing_user = execute_sql_query(existing_user_sql, existing_user_params, fetchone=True)

    if existing_user:
        return getresponse(400, "Username already exists")

    insert_user_sql = "INSERT INTO user (username, password,cash,transaction_history,holdings) VALUES (%s, %s,%s,%s,%s)"
    insert_user_params = (username, password, cash,transaction_history,holdings)
    execute_sql_query(insert_user_sql, insert_user_params)

    return getresponse(200, "Registration successful")

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    existing_user_sql = "SELECT * FROM user WHERE username = %s"
    existing_user_params = (username,)
    existing_user = execute_sql_query(existing_user_sql, existing_user_params, fetchone=True)

    sql = "SELECT * FROM user WHERE username = %s"
    params = (username, )
    user = execute_sql_query(sql, params, fetchone=True)

    if user :
        if user['password'] == password:
            print(user['username'], user['id'])
            session['user'] = user
            return getresponse(200, "Login successful", {"user": username, "id": user['id'],"pw":password})
        else:
            return getresponse(400, "密码错误")
        
    else:
        return getresponse(400, "用户名不存在")

@app.route('/change', methods=['POST'])
def change():
    print(request.json)
    username = request.json['username']
    password = request.json['password']
    existing_user_sql = "SELECT * FROM user WHERE username = %s"
    existing_user_params = (username,)
    existing_user = execute_sql_query(existing_user_sql, existing_user_params, fetchone=True)


    '''insert_user_sql = "UPDATE user SET password={password} WHERE username= %s"
    execute_sql_query(insert_user_sql)'''
    insert_user_sql = "UPDATE user SET password=%s WHERE username=%s"
    params = (password, username)
    execute_sql_query(insert_user_sql, params)

    return getresponse(200, "Registration successful")

@app.route('/getstock0', methods=['POST'])
def getstock0():
    stock_info=ak.stock_zh_a_spot_em()
    #df=df.iloc[1:201]
    stock_info = stock_info[['代码', '名称', '最新价', '涨跌幅', '涨跌额','成交量','成交额','最高','最低','今开','昨收']]
    stock_list = []
    if not stock_info.empty:  # 确保DataFrame不为空
        for index, row in stock_info.iterrows():
            stock_dict = {
                'stock_code': str(row['代码']),
                'stock_name': str(row['名称']),
                'updown_range': str(row['涨跌幅']),
                'updown_quantity': str(row['涨跌额']),
                'open_price': str(row['今开']),
                'close_price': str(row['昨收']),
                'cur_price': str(row['最新价']),
                'high_price': str(row['最高']),
                'low_price': str(row['最低']),
                'trade_volume': str(row['成交量']),
                'trade_amount': str(row['成交额'])
                }
            stock_list.append(stock_dict)

    return jsonify({'stock': stock_list})

@app.route('/getstock1', methods=['POST'])
def getstock1():
    stock_info_sh = ts.realtime_quote(ts_code='600000.sh,600004.sh,600007.sh,600056.sh,600064.sh,600031.sh,600089.sh,688046.SH,688113.SH,688131.SH')
    stock_info_sh = stock_info_sh[['NAME', 'TS_CODE', 'DATE', 'TIME', 'OPEN','PRE_CLOSE','PRICE','HIGH','LOW','VOLUME','AMOUNT']]
    stock_list = []
    if not stock_info_sh.empty:  # 确保DataFrame不为空
        for index, row in stock_info_sh.iterrows():
            stock_dict = {
                'stock_code': str(row['TS_CODE']),
                'stock_name': str(row['NAME']),
                'stock_date': str(row['DATE']),
                'stock_time': str(row['TIME']),
                'open_price': str(row['OPEN']),
                'close_price': str(row['PRE_CLOSE']),
                'cur_price': str(row['PRICE']),
                'high_price': str(row['HIGH']),
                'low_price': str(row['LOW']),
                'trade_volume': str(row['VOLUME']),
                'trade_amount': str(row['AMOUNT']),
            }
            stock_list.append(stock_dict)
    return jsonify({'stock':stock_list})

@app.route('/getstock2', methods=['POST'])
def getstock2():
    stock_info_sz = ts.realtime_quote(ts_code='000001.sz,000002.sz,000008.sz,000009.sz,000019.sz,000027.sz,000028.sz,000069.sz,000155.SZ,000428.SZ')

    stock_info_sz = stock_info_sz[['NAME', 'TS_CODE', 'DATE', 'TIME', 'OPEN','PRE_CLOSE','PRICE','HIGH','LOW','VOLUME','AMOUNT']]

    stock_list = []
    if not stock_info_sz.empty:  # 确保DataFrame不为空
        for index, row in stock_info_sz.iterrows():
            stock_dict = {
                'stock_code': str(row['TS_CODE']),
                'stock_name': str(row['NAME']),
                'stock_date': str(row['DATE']),
                'stock_time': str(row['TIME']),
                'open_price': str(row['OPEN']),
                'close_price': str(row['PRE_CLOSE']),
                'cur_price': str(row['PRICE']),
                'high_price': str(row['HIGH']),
                'low_price': str(row['LOW']),
                'trade_volume': str(row['VOLUME']),
                'trade_amount': str(row['AMOUNT']),
            }
            stock_list.append(stock_dict)
    return jsonify({'stock':stock_list})

#获取当前的价格
@app.route('/get_cur_price',methods=['POST'])
def get_cur_price():
    stock_code = request.json["code"]#传的就是股票的编号代码
    #这里获取以下这支股票此刻的实时价格、买入日期、买入时间
    df = ts.realtime_quote(ts_code=stock_code)
    cur_price=df['PRICE'].iloc[0]#这个要呈现给前端
    return jsonify({"cur_price":cur_price})

#写买入
@app.route('/transaction_in', methods=['POST'])
def transaction_in():#这里参数调入一个id吧
    #获取用户所含现金
    print(request.json)
    username = request.json["username"]
    amount_in = request.json["amount_in"]
    stock_code = request.json["stock_code"]
    
    select_query = "SELECT cash FROM user WHERE username = %s"
    cash=execute_sql_query(select_query, (username,))
    cash=cash[0]
    cash=cash['cash']#这下子cash应该是现金额了

    select_query1 = "SELECT transaction_history FROM user WHERE username = %s"
    #获取了这个用户的交易JSON数据
    transaction_result=execute_sql_query(select_query1, (username,))
    transaction_result=transaction_result[0]
    transaction_result=transaction_result['transaction_history']
    transaction_history=json.loads(transaction_result)#现在是一个list类型了

    select_query2 = "SELECT holdings FROM user WHERE username = %s"
    #获取了这个用户的交易JSON数据
    holdings_result=execute_sql_query(select_query2, (username,))
    holdings_result=holdings_result[0]
    holdings_result=holdings_result['holdings']
    holdings=json.loads(holdings_result)#list类型

    #从前端获取要买入的股票代码
    stock_code = request.json['stock_code']
    #这里获取以下这支股票此刻的实时价格、买入日期、买入时间
    df = ts.realtime_quote(ts_code=stock_code)
    cur_price=df['PRICE'].iloc[0]#这个要呈现给前端
    cur_date=(df['DATE'].astype(str)).iloc[0]
    cur_time=(df['TIME'].astype(str)).iloc[0]#这些最后都还要写入JSON

    #从前端获取买入量
    amount_in = request.json['amount_in']
    if False:
        pass
    else:
        #判断是否超本金了
        if cur_price*amount_in > cash:
           return getresponse(400, "您的金额不够,请减少购买量")
        else:
            #成功购入
            cash-=cur_price*amount_in

            #更新本金
            update_params=(cash,username)
            update_query = "UPDATE user SET cash = %s WHERE username = %s"
            execute_sql_query(update_query,update_params)

            #更新交易记录
            #新创建一个字典（存此条交易记录），填入transaction_history里，最后在转化为JSON存进数据库。
            trans_id=transaction_history[-1]['trans_id']+1#交易序列号比上一个加一
            add_new_trans={'trans_id':trans_id,'date':cur_date,'time':cur_time,
                     'stock_code':stock_code,'price':cur_price,
                     'amount':amount_in,'if_in':True}
            transaction_history.append(add_new_trans)
            update_query1 = "UPDATE user SET transaction_history = %s WHERE username = %s"
            # 将 Python 对象转换为 JSON 字符串
            transaction_history_json = json.dumps(transaction_history) 
            update_params1=(transaction_history_json,username)
            execute_sql_query(update_query1,update_params1 )

            #更新持有量
            stock_to_update=stock_code
            for each in holdings:
                if each['stock_code']==stock_to_update:
                    each['amount']+=amount_in
            # 将 Python 对象转换为 JSON 字符串
            holdings_json=json.dumps(holdings)
            update_query2 = "UPDATE user SET holdings = %s WHERE username = %s"
            update_params2=(holdings_json,username)
            #transaction_history_json = json.dumps(transaction_history) 
            execute_sql_query(update_query2,update_params2)
            
            return getresponse(200, "买入成功", {"cur_price":cur_price,"aaa": cur_price*amount_in})


#写卖出
@app.route('/transaction_out', methods=['POST'])
def transaction_out():
   #获取用户所含现金
    select_query = "SELECT cash FROM user WHERE username = %s"
    username = request.json["username"]
    stock_code = request.json["stock_code"]
    amount_out = request.json["amount_out"]

    cash=execute_sql_query(select_query, (username,))
    cash=cash[0]
    cash=cash['cash']#这下子cash应该是现金额了
    
    select_query1 = "SELECT transaction_history FROM user WHERE username = %s"
    #获取了这个用户的交易JSON数据
    transaction_result=execute_sql_query(select_query1, (username,))
    transaction_result=transaction_result[0]
    transaction_result=transaction_result['transaction_history']
    transaction_history=json.loads(transaction_result)#现在是一个list类型了

    select_query2 = "SELECT holdings FROM user WHERE username = %s"
    #获取了这个用户的交易JSON数据
    holdings_result=execute_sql_query(select_query2, (username,))
    holdings_result=holdings_result[0]
    holdings_result=holdings_result['holdings']
    holdings=json.loads(holdings_result)#list类型

    #从前端获取要买入的股票代码
    stock_code = request.json['stock_code']
    
    for each in holdings:
            if each['stock_code']==stock_code:
                amount_cur=each['amount']
    
    #这里获取以下这支股票此刻的实时价格、买入日期、买入时间
    df = ts.realtime_quote(ts_code=stock_code)
    cur_price=df['PRICE'].iloc[0]#这个要呈现给前端
    cur_date=(df['DATE'].astype(str)).iloc[0]
    cur_time=(df['TIME'].astype(str)).iloc[0]#这些最后都还要写入JSON

    #从前端获取买入量
    amount_out = request.json['amount_out']

    if False:
        pass
    else:
        #判断是否超过当前持有量
        if amount_out>amount_cur:
            return getresponse(400, "超过已有的持有量，请重新输入")
        else:
            #成功卖出
            cash+=cur_price*amount_out

            #更新本金
            update_query = "UPDATE user SET cash = %s WHERE username = %s"#不知道%s对不对啊，因为这应该是一个float
            update_params=(cash , username)
            execute_sql_query(update_query,update_params)

            #更新交易记录
            #新创建一个字典（存此条交易记录），填入transaction_history里，最后在转化为JSON存进数据库。
            trans_id=transaction_history[-1]['trans_id']+1#交易序列号比上一个加一
            add_new_trans={'trans_id':trans_id,'date':cur_date,'time':cur_time,
                     'stock_code':stock_code,'price':cur_price,
                     'amount':amount_out,'if_in':False}
            transaction_history.append(add_new_trans)
            update_query1 = "UPDATE user SET transaction_history = %s WHERE username = %s"
            # 将 Python 对象转换为 JSON 字符串
            transaction_history_json = json.dumps(transaction_history) 
            update_params1=(transaction_history_json,username)
            execute_sql_query(update_query1,update_params1)

            #更新股票持有量
            stock_to_update=stock_code
            for each in holdings:
                if each['stock_code']==stock_to_update:
                    each['amount']-=amount_out
            # 将 Python 对象转换为 JSON 字符串
            holdings_json=json.dumps(holdings)
            update_query2 = "UPDATE user SET holdings = %s WHERE username = %s"
            update_params2=(holdings_json,username)
            #transaction_history_json = json.dumps(transaction_history) 
            execute_sql_query(update_query2,update_params2)
            return getresponse(200, "卖出成功", {"aaa": cur_price*amount_out,"cur_price":cur_price})

@app.route('/strategy1_buy',methods=['POST'])
def strategy1_buy():
    sql_connection = pymysql.connect(host='localhost', user='root', password='0406722cm'
                                 ,db='lfcx_db', port=3306, autocommit=False, charset='utf8mb4')
    for buy_name in ['sh1','sh2','sh3','sh4','sh5','sh6','sh7','sh8','sh9','sh10',
                'sz1','sz2','sz3','sz4','sz5','sz6','sz7','sz8','sz9','sz10']:
        sql = f"select * from lfcx_db.{buy_name}"
        df_sql = pd.read_sql(sql,sql_connection)#参数：查询语句+连接配置

        maIntervalList = [5,10,20,60]
        for maInterval in maIntervalList:
            df_sql['MA_' + str(maInterval)] = df_sql['close'].rolling(window=maInterval).mean()
        today=len(df_sql)-1
       
        if df_sql.iloc[today-1]['MA_60']>df_sql.iloc[today-1]['MA_5'] and df_sql.iloc[today]['MA_60']<df_sql.iloc[today]['MA_5']:
            return getresponse(200, "建议买入", {"buy_name": buy_name})
        return getresponse(400, "不建议买入")
        
@app.route('/strategy1_sell',methods=['POST'])
def strategy_sell():
    sql_connection = pymysql.connect(host='localhost', user='root', password='0406722cm'
                                 ,db='lfcx_db', port=3306, autocommit=False, charset='utf8mb4')
    for sell_name in ['sh1','sh2','sh3','sh4','sh5','sh6','sh7','sh8','sh9','sh10',
                'sz1','sz2','sz3','sz4','sz5','sz6','sz7','sz8','sz9','sz10']:
        sql = f"select * from lfcx_db.{sell_name}"
        df_sql = pd.read_sql(sql,sql_connection)#参数：查询语句+连接配置

        maIntervalList = [5,10,20,60]
        for maInterval in maIntervalList:
            df_sql['MA_' + str(maInterval)] = df_sql['close'].rolling(window=maInterval).mean()
        today=len(df_sql)-1
        
        if df_sql.iloc[today-1]['MA_60']<df_sql.iloc[today-1]['MA_5'] and df_sql.iloc[today]['MA_60']>df_sql.iloc[today]['MA_5']:
            return getresponse(200, "建议卖出", {"sell_name": sell_name})
        return getresponse(400, "不建议卖出")
    
@app.route('/strategy2',methods=['POST'])  
def strategy2():
    sql_connection = pymysql.connect(host='localhost', user='root', password='0406722cm'
                                 ,db='lfcx_db', port=3306, autocommit=False, charset='utf8mb4')
    sr={}
    for name in ['sh1','sh2','sh3','sh4','sh5','sh6','sh7','sh8','sh9','sh10',
                'sz1','sz2','sz3','sz4','sz5','sz6','sz7','sz8','sz9','sz10']:
        sql = f"select * from lfcx_db.{name}"
        df_sql = pd.read_sql(sql,sql_connection)#参数：查询语句+连接配置
        df_sql['MA_30'] = df_sql['close'].rolling(window=30).mean()
        today=len(df_sql)-1
        ma=df_sql.iloc[today]['MA_30']
        p=df_sql.iloc[today]['close']
        ratio=(ma-p)/ma
        sr[name]=ratio

    buystock = sorted(sr, key=sr.get)[:3]
    sellstock = sorted(sr, key=sr.get, reverse=True)[:3]

    buy_name = str(buystock[0])
    sell_name = str(sellstock[0])
    code_map = {
        'sh1': '600000.sh','sh2': '600004.sh','sh3': '600007.sh','sh4': '600056.sh','sh5': '600064.sh',
        'sh6': '600031.sh','sh7': '600089.sh','sh8': '688046.sh','sh9': '688113.sh','sh10': '688131.sh'
    }

    buy_name = code_map.get(buy_name, buy_name)
    sell_name = code_map.get(sell_name, sell_name)
    '''000001.sz','000002.sz','000008.sz','000009.sz','000019.sz',
    '000027.sz','000028.sz','000069.sz','000155.sz','000428.sz','''
    return getresponse(200, "建议买入卖出的股票", {"buy_name":buy_name,"sell_name": sell_name})

@app.route('/risk1',methods=['POST'])#止盈
def risk1():
    username = request.json['user']
    select_query1 = "SELECT transaction_history FROM user WHERE username = %s"
    #获取了这个用户的交易JSON数据
    transaction_result=execute_sql_query(select_query1, (username,))
    transaction_result=transaction_result[0]
    transaction_result=transaction_result['transaction_history']
    transaction_list=json.loads(transaction_result)#现在是一个list类型了
    transaction_list.pop(0)

    transaction_in_list=transaction_list
    transaction_in_list = [each for each in transaction_in_list if each.get('if_in')]

    for each in transaction_in_list:
        each.pop('date')
        each.pop('if_in')
        each.pop('time')
        each.pop('trans_id')
        each.pop('amount')
        df = ts.realtime_quote(ts_code=each.get('stock_code'))
        cur_price=df['PRICE'].iloc[0]
        each['cur_price']=cur_price
        #当前价格'cur_price'。股票代码'stock_code'。买入价格'price'。
    
    for each in transaction_in_list:
        if each.get('cur_price')<0.9*each.get('price'):
            return getresponse(200, "建议卖出", {"stop1": each.get('stock_code')})
    return getresponse(400, "不建议卖出")

@app.route('/risk2',methods=['POST'])#止盈
def risk2():
    username = request.json['user']
    select_query1 = "SELECT transaction_history FROM user WHERE username = %s"
    #获取了这个用户的交易JSON数据
    transaction_result=execute_sql_query(select_query1, (username,))
    transaction_result=transaction_result[0]
    transaction_result=transaction_result['transaction_history']
    transaction_list=json.loads(transaction_result)#现在是一个list类型了
    transaction_list.pop(0)

    transaction_in_list=transaction_list
    transaction_in_list = [each for each in transaction_in_list if each.get('if_in')]

    for each in transaction_in_list:
        each.pop('date')
        each.pop('if_in')
        each.pop('time')
        each.pop('trans_id')
        each.pop('amount')
        df = ts.realtime_quote(ts_code=each.get('stock_code'))
        cur_price=df['PRICE'].iloc[0]
        each['cur_price']=cur_price
        #当前价格'cur_price'。股票代码'stock_code'。买入价格'price'。
    
    for each in transaction_in_list:
        if each.get('cur_price')>1.2*each.get('price'):
            return getresponse(200, "建议卖出", {"stop2": each.get('stock_code')})
    return getresponse(400, "不建议卖出")


    
@app.route('/backtest',methods=['POST'])
def backtest():
    sql_connection = pymysql.connect(host='localhost', user='root', password='0406722cm'
                                 ,db='lfcx_db', port=3306, autocommit=False, charset='utf8mb4')
    name = request.json["stock_code"]
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


@app.route('/logout')
def logout():
    session.clear()
    return getresponse(200, "Logout successful")

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    uploads_dir = 'uploads'
    file_path = os.path.join(uploads_dir, filename)
    return send_file(file_path, as_attachment=True)

@app.route('/uploads', methods=['POST'])
def uploads_file():
    file = request.files['file']
    file_path = save_file(file)
    return jsonify({'file_path': file_path}), 201

def save_file(file):
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    file_path = f'uploads/{file.filename}'
    file.save(file_path)
    file_path = file_path.replace("uploads/", "http://127.0.0.1:5001/download/")
    return file_path

@app.route('/kline',methods=['POST'])
def kline():
    print(request.json)
    stock_code = request.json["stock_code"]
    stock_code_list=[['000001.SZ','sz1'],['000002.SZ','sz2'],['000008.SZ','sz3'],['000009.SZ','sz4'],['000019.SZ','sz5'],
                 ['000027.SZ','sz6'],['000028.SZ','sz7'],['000069.SZ','sz8'],['000155.SZ','sz9'],['000428.SZ','sz10'],
                 ['600000.SH','sh1'],['600004.SH','sh2'],['600007.SH','sh3'],['600056.SH','sh4'],['600064.SH','sh5'],
                 ['600031.SH','sh6'],['600089.SH','sh7'],['688046.SH','sh8'],['688113.SH','sh9'],['688131.SH','sh10']]
    for each in stock_code_list:
        if stock_code==each[0]:
            name=each[1]
    db = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='0406722cm',
            database='lfcx_db'
        )
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
    
    mpf.plot(df, style=my_style, type='candle', ax=ax1,volume=ax2,mav=(5, 10, 20))
    img_buffer = io.BytesIO()
    mpf.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    
    # 返回图像数据给前端
    return send_file(img_buffer, mimetype='image/png')

#用户有多少钱
@app.route('/get_cash', methods=['POST'])
def get_cash():
    username = request.json['user']
    existing_user_sql = "SELECT cash FROM user WHERE username = %s"
    existing_user_params = (username,)
    cash = execute_sql_query(existing_user_sql, existing_user_params)
    cash=cash[0]
    cash=cash['cash']
    return jsonify({'cash':cash})

#展示买入记录
@app.route('/TransactionInDisplay', methods=['POST'])
def TransactionInDisplay():
    #全部存在一个列表里
    #这里就是要获取用户名
    username = request.json["user"]
    select_query1 = "SELECT transaction_history FROM user WHERE username = %s"
    #获取了这个用户的交易JSON数据
    transaction_result=execute_sql_query(select_query1, (username,))
    transaction_result=transaction_result[0]
    transaction_result=transaction_result['transaction_history']
    transaction_list=json.loads(transaction_result)#现在是一个list类型了
    transaction_list.pop(0)
    transaction_in_list=transaction_list
    transaction_in_list = [each for each in transaction_in_list if each.get('if_in')]

    for each in transaction_in_list:
        each.pop('if_in')
        each.pop('time')
        each.pop('trans_id')
        #加上一个总金额
        total=each.get('amount')*each.get('price')
        each['total']=total
         
    #买入的交易记录，这个stock得改一下吧
    return jsonify({'stock_in':transaction_in_list})

#展示卖出记录
@app.route('/TransactionOutHistoryDisplay', methods=['POST'])
def TransactionOutHistoryDisplay():

    #全部存在一个列表里
    #这里就是要获取用户名
    username = request.json["user"]
    select_query1 = "SELECT transaction_history FROM user WHERE username = %s"
    #获取了这个用户的交易JSON数据
    transaction_result=execute_sql_query(select_query1, (username,))
    transaction_result=transaction_result[0]
    transaction_result=transaction_result['transaction_history']
    transaction_list=json.loads(transaction_result)#现在是一个list类型了
    transaction_list.pop(0)

    transaction_out_list=transaction_list

    transaction_out_list = [each for each in transaction_out_list if not each.get('if_in')]


    for each in transaction_out_list:
        each.pop('if_in')
        each.pop('time')
        each.pop('trans_id')
        #加上一个总金额
        total=each.get('amount')*each.get('price')
        each['total']=total

    
    #买入的交易记录，这个stock得改一下吧
    return jsonify({'stock_out':transaction_out_list})


@app.route('/HoldingsDisplay', methods=['POST'])
def HoldingsDisplay():

    #这里就是要获取用户名(从前端传入)
    username = request.json["user"]

    select_query2 = "SELECT holdings FROM user WHERE username = %s"
    #获取了这个用户的交易JSON数据
    holdings_result=execute_sql_query(select_query2, (username,))
    holdings_result=holdings_result[0]
    holdings_result=holdings_result['holdings']
    holdings_list=json.loads(holdings_result)#list类型

    

    holdings_list = [each for each in holdings_list if not each['amount']==0]
    for each in holdings_list:
        df = ts.realtime_quote(ts_code=each.get('stock_code'))#这个变量名不知道对不对啊
        cur_price=df['PRICE'].iloc[0]
        each['price']=cur_price#添加现有价格

    return jsonify({'stock_hold':holdings_list})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

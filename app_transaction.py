import os
from flask import Flask, request, session, jsonify, send_file
from flask_cors import CORS
from db import app, execute_sql_query  #  ensure you have implemented execute_sql_query correctly
import tushare as ts
import json

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

'''def getstockdata(code=None,name=None,open=None,close=None,low=None,high=None,volume=None):
    res = {
        "code":code,
        "name":name,
        "open":open,
        "close":close,
        "low":low,
        "high":high,
        "volume":volume
    }
    return jsonify(res)

@app.route('/stockdata', methods=['POST'])
def stockdata():
    print(request.json)
    code=request'''
    

@app.route('/register', methods=['POST'])
def register():
    print(request.json)
    username = request.json['username']
    password = request.json['password']
    existing_user_sql = "SELECT * FROM user WHERE username = %s"
    existing_user_params = (username,)
    existing_user = execute_sql_query(existing_user_sql, existing_user_params, fetchone=True)

    if existing_user:
        return getresponse(400, "Username already exists")

    insert_user_sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
    insert_user_params = (username, password)
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

#写买入
@app.route('/transaction_in', methods=['POST'])
def transaction_in(id_num):#这里参数调入一个id吧
    #获取用户所含现金
    select_query = "SELECT cash FROM user WHERE id = %d"
    cash=execute_sql_query(select_query, id_num)

    select_query1 = "SELECT transaction_history FROM user WHERE id = %d"
    #获取了这个用户的交易JSON数据
    transaction_result=execute_sql_query(select_query1, id_num)
    transaction_history=json.loads(transaction_result)#把JSON改成了python中的字典

    select_query2 = "SELECT holdings FROM user WHERE id = %d"
    #获取了这个用户的交易JSON数据
    holdings_result=execute_sql_query(select_query2, id_num)
    holdings=json.loads(holdings_result)#把JSON改成了python中的字典

    #从前端获取要买入的股票代码
    stock_code = request.json['stock_code']
    #这里获取以下这支股票此刻的实时价格、买入日期、买入时间
    df = ts.realtime_quote(ts_code=stock_code)
    cur_price=df['PRICE'].iloc[0]#这个要呈现给前端
    cur_date=(df['DATE'].astype(str)).iloc[0]
    cur_time=(df['TIME'].astype(str)).iloc[0]#这些最后都还要写入JSON

    #从前端获取买入量
    amount_in = request.json['amount_in']
    if amount_in%100!=0 or amount_in<1:
        #返回前端告诉用户不是100的整数倍，不行
        pass
    else:
        #判断是否超本金了
        if cur_price*amount_in > cash:
            #返回前端告诉用户不是100的整数倍，不行
            pass
        else:
            #成功购入
            cash-=cur_price*amount_in

            #更新本金
            update_query = "UPDATE user SET cash = %s WHERE id = %d"
            execute_sql_query(update_query, cash , id_num)

            #更新交易记录
            #新创建一个字典（存此条交易记录），填入transaction_history里，最后在转化为JSON存进数据库。
            trans_id=transaction_history[-1]['trans_id']+1#交易序列号比上一个加一
            add_new_trans={'trans_id':trans_id,'date':cur_date,'time':cur_time,
                     'stock_code':stock_code,'price':cur_price,
                     'amount':amount_in,'if_in':True}
            transaction_history.append(add_new_trans)
            update_query1 = "UPDATE user SET transaction_history = %s WHERE id = %d"
            # 将 Python 对象转换为 JSON 字符串
            transaction_history_json = json.dumps(transaction_history) 
            execute_sql_query(update_query1, transaction_history_json,id_num)

            #更新持有量
            stock_to_update=stock_code
            for each in holdings:
                if each['stock_code']==stock_to_update:
                    each['amount']+=amount_in
            # 将 Python 对象转换为 JSON 字符串
            holdings_json=json.dumps(holdings)
            update_query2 = "UPDATE user SET holdings = %s WHERE id = %d"
            #transaction_history_json = json.dumps(transaction_history) 
            execute_sql_query(update_query2, holdings_json,id_num)
            





#写卖出
@app.route('/transaction_out', methods=['POST'])
def transaction_out(id_num):
   #获取用户所含现金
    select_query = "SELECT cash FROM user WHERE id = %d"
    cash=execute_sql_query(select_query, id_num)

    select_query1 = "SELECT transaction_history FROM user WHERE id = %d"
    #获取了这个用户的交易JSON数据
    transaction_result=execute_sql_query(select_query1, id_num)
    transaction_history=json.loads(transaction_result)#把JSON改成了python中的字典
    
    #从前端获取要买入的股票代码
    stock_code = request.json['stock_code']
    select_query2 = "SELECT holdings FROM user WHERE id = %d"
    #获取了这个用户的交易JSON数据
    holdings_result=execute_sql_query(select_query2, id_num)
    holdings=json.loads(holdings_result)#把JSON改成了python中的字典
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
    if amount_out%100!=0 or amount_out!=(amount_cur%100) or amount_out<1:
        #返回前端告诉用户卖出量不符合要求
        pass
    else:
        #判断是否超过当前持有量
        if amount_out>amount_cur:
            #返回前端告诉用户卖出量太大
            pass
        else:
            #成功卖出
            cash+=cur_price*amount_out

            #更新本金
            update_query = "UPDATE user SET cash = %s WHERE id = %d"#不知道%s对不对啊，因为这应该是一个float
            execute_sql_query(update_query, cash , id_num)

            #更新交易记录
            #新创建一个字典（存此条交易记录），填入transaction_history里，最后在转化为JSON存进数据库。
            trans_id=transaction_history[-1]['trans_id']+1#交易序列号比上一个加一
            add_new_trans={'trans_id':trans_id,'date':cur_date,'time':cur_time,
                     'stock_code':stock_code,'price':cur_price,
                     'amount':amount_out,'if_in':False}
            transaction_history.append(add_new_trans)
            update_query1 = "UPDATE user SET transaction_history = %s WHERE id = %d"
            # 将 Python 对象转换为 JSON 字符串
            transaction_history_json = json.dumps(transaction_history) 
            execute_sql_query(update_query1, transaction_history_json,id_num)

            #更新股票持有量
            stock_to_update=stock_code
            for each in holdings:
                if each['stock_code']==stock_to_update:
                    each['amount']-=amount_out
            # 将 Python 对象转换为 JSON 字符串
            holdings_json=json.dumps(holdings)
            update_query2 = "UPDATE user SET holdings = %s WHERE id = %d"
            #transaction_history_json = json.dumps(transaction_history) 
            execute_sql_query(update_query2, holdings_json,id_num)




   

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

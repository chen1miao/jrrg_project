import json
from db import app, execute_sql_query
import mysql.connector


def execute_sql_query(sql, params=None, fetchone=False):
    try:
        # 
        db = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='wxwwxw2022',
            database='stock_data'
        )

        # 
        cursor = db.cursor(dictionary=True)
        #  SQL 
        cursor.execute(sql, params)
        # 
        if fetchone:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        # 
        cursor.close()
        # 
        db.commit()

        # 
        db.close()

        return result

    except mysql.connector.Error as e:
        print("MySQL Error:", e)
        return None




trans_cur=[]
trans_cur.append({ 'trans_id': 0 })
#print(type(trans_cur),trans_cur)
transaction_history=json.dumps(trans_cur)
#print(type(transaction_history),transaction_history)
'''hold_cur=[]
hold_cur.append()'''
id=0
create_sql='CREATE TABLE IF NOT EXISTS test_json (id INT PRIMARY KEY,transaction_history JSON)'
execute_sql_query(create_sql)


'''insert_user_sql = 'INSERT INTO test_json(id,transaction_history) VALUES (%s,%s)'
insert_user_params = (id,transaction_history)
execute_sql_query(insert_user_sql, insert_user_params)'''
id_num=0
select_user_params=(id_num,)
select_query1 = 'SELECT transaction_history FROM test_json WHERE id = %s'
transaction_result=execute_sql_query(select_query1,select_user_params)#这里读到的是一个列表，里面只有一个元素选取的格子里的东西
transaction_result=transaction_result[0]#选到了格子里的东西{'transaction_history': '[{"trans_id": 0}, {"price": 9.9, "trans_id": 1}, {"price": 9.9, "trans_id": 2}]'}

transaction_result=transaction_result['transaction_history']#是str类型[{"trans_id": 0}, {"price": 9.9, "trans_id": 1}, {"price": 9.9, "trans_id": 2}, {"price": 9.9, "trans_id": 3}]
#print(type(transaction_result))
transaction_history=json.loads(transaction_result)#转化成了list类型
print(transaction_history,type(transaction_history))


cur_price=9.9
#print(type(transaction_history[-1]['trans_id']))
trans_id=transaction_history[-1]['trans_id']+1#交易序列号比上一个加一
add_new_trans={'trans_id':trans_id,'price':cur_price}
print(add_new_trans)
transaction_history.append(add_new_trans)
print(transaction_history)
# 将 Python 对象转换为 JSON 字符串
transaction_history_json = json.dumps(transaction_history)
#print(type(transaction_history_json))



update_query1 = "UPDATE test_json SET transaction_history = %s WHERE id = %s"
#transaction_history_json = json.dumps(transaction_history) 
update_user_params=(transaction_history_json,id_num)
execute_sql_query(update_query1,update_user_params )
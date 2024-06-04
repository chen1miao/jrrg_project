import pymysql
import random
#创建与数据库的连接
# 创建连接
# host      主机名字，本机一般都是localhost
# user      用户名
# password  用户密码
# charset   数据库编码
conn = pymysql.connect(host='localhost',user='root',password='root',charset='utf8mb4')
# 创建游标
cursor = conn.cursor()
# 创建数据库的sql(使用if判断是否已经存在数据库，数据库不存在时才会创建，否则会报错)
sql = "CREATE DATABASE IF NOT EXISTS new_db"#new_db是要创建的数据库名字

# 执行创建数据库的sql语句
cursor.execute(sql)
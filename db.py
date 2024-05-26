# db.py

from flask import Flask
import mysql.connector

app = Flask(__name__, static_url_path='/Frontend')
app.config.from_pyfile('config.py')
app.secret_key = "dasfsfhgdfggdfjgjfy"
def execute_sql_query(sql, params=None, fetchone=False):
    try:
        # 
        db = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            port=app.config['MYSQL_PORT'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
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


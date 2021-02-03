import pymysql
from flask import Flask
from flask import jsonify
from flask import flash, request
from mysql_config import mysql

app = Flask(__name__)


@app.route('/emp')
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, phone, address FROM rest_emp")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)

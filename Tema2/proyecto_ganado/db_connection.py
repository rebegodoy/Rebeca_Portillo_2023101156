import pymysql

def get_db_connection():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root',   
        database='EXAMEN', 
        port=3307,
        auth_plugin_map={
            "caching_sha2_password": "pymysql.auth.caching_sha2_password"
        }
    )
    return conn

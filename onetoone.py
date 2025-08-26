import pymysql

def sql_server():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Atmecs!1234',
        database='userdata'
    )

def get_users_with_profiles():
    conn = sql_server()
    cursor = conn.cursor()

    query = """
        S"""

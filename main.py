import pymysql

host = 'localhost'
user = 'root'
password = ''
database = 'Документооборот'


try:
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='Документооборот',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successfully connected...")

    try:
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `Содержание документов`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("#"*20)
    finally:
        connection.close()
except Exception as ex:
    print("Connection refused...")
    print(ex)

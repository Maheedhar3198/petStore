# import csv
#
#
# def test_user_info():
#     with open('testdata\\registrationData.csv', 'r') as file:
#         reader = csv.reader(file)
#         rows = list(reader)
#         if len(rows) >= 1:
#             print(rows[1])
#         else:
#             print("Error: CSV does not have a second row")
#         second_row = rows[1]
#
#     if len(second_row) >= 3:
#         print(f"{second_row[3]}")
#         print(f"{second_row[4]}")
#     else:
#         print("There is no firstname and last name in data")
#
#     last_row = rows[-1]
#     print(last_row) #last row of csv file will be printed
#
#     #last row user id need to be incremented for the next use
#     last_user_id = int(last_row[0])
#     next_user_registration = last_user_id + 1
#     print(next_user_registration)


import pymysql
from sql_database import sql_server

def test_last_userid_from_db():
    database = sql_server()
    cursor = database.cursor()

    cursor.execute("SELECT MAX(`User ID`) FROM Users")
    result = cursor.fetchone()

    if result[0] is None:
        print("Table is empty")
    else:
        last_user_id = int(result[0])
        next_user_id = last_user_id + 1
        print(f"Last User ID: {last_user_id}")
        print(f"Next User ID: {next_user_id}")
        return next_user_id

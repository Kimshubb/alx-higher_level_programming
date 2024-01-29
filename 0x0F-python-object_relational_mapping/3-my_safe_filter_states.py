#!/usr/bin/python3
import sys
import MySQLld

def filter_states_by_name(username, password, database, state_name):
    """
    filter states by name
     Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.

    Returns:
        None
    """
    connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            password=password,
            db=database)
    cursor = connection.cursor()
    query = """SELECT * FROM states WHERE name = %s ORDER BY states.id ASC;"""
    cursor.execute(query,(state_name,))
    results = cursor.fetchall()
    for result in results:
        print(result)
        cursor.close()
        connection.close()
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        filter_states_by_name(username,password, database, state_name)

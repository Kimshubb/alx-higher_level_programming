#!/usr/bin/python3
import MySQLdb
import sys

def list_states_with_n(username, password, database):
    """
    Lists states from MySql db that starts with 'N'
    Args: username(STR) : MySQL username
          password(str) :MySQL password
          database(str) :MySql database
    returns:
            none
    """
    connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username
            password=password
            db=database
            )
    cursor = connection.cursor()
    query = SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;
    cursor.execute(query)
    results = cursor.fetchall()
    print("Number of results: {}".format(len(results)))
    for result in results:
        print(result)
    cursor.close()
    connection.close()
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)
        username = sys.argv[1]
        password = sys.arg[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        filter_states_with_n(username, password, database)


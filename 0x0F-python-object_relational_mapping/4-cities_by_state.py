#!/usr/bin/python3
import sys
import MySQLdb
"""Lists all citites in a state"""
def list_cities_by_state(username, password, database, state_name):
    connection = MySQLdb.connect(host="localhost", port=3306, user=username, password=password, db=database)
    cursor = connection.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM cities INNERJOIN states.id=cities.state_id"""
    result = cursor.fetchall()
    for result in results:
        print (result)
    cursor.close()
    connection.close()
if __name__ == "__name__":
    if len(sys.argv) != 4:
        print("Usage: <4-cities_by_state.py><username><password><database><state_name>")
        sys.exit(1)

        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_cities_by_state(username, password, database)



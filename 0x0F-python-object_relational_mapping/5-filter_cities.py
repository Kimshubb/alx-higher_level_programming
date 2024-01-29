#!/usr/bin/python3
"""Filters cities by state"""
def filter_by_state(username, password, database, state_name):
    connection = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = connection.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;"""
    cursor.execute(query, (state_name))
    results = cursor.fetchall()
    for result in results:
        print(result)
        cursor.close()
        connection.close()
if __name__ == "__name__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        filter_by_state(username, password, database, state_name)


#!/usr/bin/python3
import MySQLdb
import sys
"""Lists all states from database hbtn_0e_0_usa sorted in order of states.id"""
def list_states(username, password, database_name):
    """Usage: ./script.py <username> <password> <database_name>"""
    try:
        db = MySQLdb.connect(
                host="localhost",
                user=username,
                password=password,
                db_name=database_name,
                port=3306
                )
        cursor = db.cursor()
        cursor.execute("SELECT id, name FROM states ORDER BY id")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

 if __name__ == "__main__":
     if len(sys.argv) != 4:
         print("Usage: ./script.py <username> <password> <database_name>")
     else:
         username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
         list_states(username, password, database_name)

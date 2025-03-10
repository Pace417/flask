import sqlite3
con = sqlite3.connect("databaseExample.db")
cur = con.cursor()
cur.execute(""" DELETE FROM Employee
                WHERE EmpID = 1122
            """)
con.commit()

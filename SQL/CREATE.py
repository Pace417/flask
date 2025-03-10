import sqlite3
con = sqlite3.connect("databaseExample.db")
cur = con.cursor()
cur.execute("""
            CREATE TABLE Employee(
            EmpID INTEGER NOT NULL PRIMARY KEY,
            EmpName VARCHAR(20) NOT NULL,
            HireDate DATE,
            Salary CURRENCY
            )
""")

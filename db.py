import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

query = """
CREATE TABLE IF NOT EXISTS FACTORY (
FACTORY_ID INT PRIMARY KEY NOT NULL,
ORG_ID INT NOT NULL,
COUNTRY VARCHAR(10),
EXECUTION_DATE DATE,
FAIL_RATE FLOAT
)
"""

conn.execute(query)
cur = conn.cursor()
cur.execute("INSERT INTO FACTORY (FACTORY_ID,ORG_ID,COUNTRY,EXECUTION_DATE,FAIL_RATE) \
      VALUES (1, 123, 'VN', '2022-08-01', 0.5 )")
cur.execute("INSERT INTO FACTORY (FACTORY_ID,ORG_ID,COUNTRY,EXECUTION_DATE,FAIL_RATE) \
      VALUES (2, 234, 'VN', '2022-08-01', 0.3 )")
cur.execute("INSERT INTO FACTORY (FACTORY_ID,ORG_ID,COUNTRY,EXECUTION_DATE,FAIL_RATE) \
      VALUES (3, 124, 'CN', '2022-08-02', 0.6 )")
cur.execute("INSERT INTO FACTORY (FACTORY_ID,ORG_ID,COUNTRY,EXECUTION_DATE,FAIL_RATE) \
      VALUES (4, 126, 'JP', '2022-08-02', 0.2 )")
cur.execute("INSERT INTO FACTORY (FACTORY_ID,ORG_ID,COUNTRY,EXECUTION_DATE,FAIL_RATE) \
      VALUES (5, 235, 'US', '2022-08-03', 0.4 )")
print("Table created successfully")
conn.commit()
cur.close()

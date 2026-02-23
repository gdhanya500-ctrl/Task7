import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
product TEXT,
quantity INTEGER,
price REAL
)
""")

# insert data
data = [
("Pen",10,5),
("Pencil",20,2),
("Notebook",15,50),
("Pen",5,5),
("Notebook",10,50)
]

cursor.executemany("INSERT INTO sales VALUES (?,?,?)", data)
conn.commit()

# SQL query
query = """
SELECT product,
SUM(quantity) AS total_qty,
SUM(quantity*price) AS revenue
FROM sales
GROUP BY product
"""

# load into pandas
df = pd.read_sql_query(query, conn)

# print output
print(df)

# plot chart
df.plot(kind="bar", x="product", y="revenue")
plt.show()

# save chart
plt.savefig("sales_chart.png")

conn.close()
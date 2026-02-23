# Task 7 — Basic Sales Summary using SQLite + Python

## Objective
This project demonstrates how to use SQL inside Python to extract simple sales information such as total quantity sold and total revenue, and display the results using printed output and a basic bar chart.

---

## Tools Used
- Python  
- SQLite (built into Python)  
- pandas  
- matplotlib  

---

## Dataset
A small SQLite database file **sales_data.db** was created with one table:

**Table Name:** sales  

**Columns**
- product (TEXT)
- quantity (INTEGER)
- price (REAL)

Sample sales records were inserted using Python.

---

## Steps Performed
1. Created SQLite database using sqlite3
2. Created sales table
3. Inserted sample data
4. Ran SQL query to calculate total quantity and revenue per product
5. Loaded results into pandas DataFrame
6. Printed results
7. Generated bar chart using matplotlib
8. Saved chart as image

---

## SQL Query Used
```sql
SELECT product,
SUM(quantity) AS total_qty,
SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
```

---

## Output
The script generates:
- Printed table showing product totals
- Bar chart visualization of revenue per product

---

## Files Included
- task7.py → Python script
- sales_data.db → SQLite database
- sales_chart.png → Bar chart image
- output.png → Screenshot of result

---

## Learning Outcome
This task helped me learn:
- How Python connects to databases
- How to execute SQL queries inside Python
- How GROUP BY works in SQL
- How pandas processes query results
- How matplotlib visualizes data

---

## Conclusion
This project demonstrates how SQL, Python, and visualization libraries can be combined to analyze and present data effectively.

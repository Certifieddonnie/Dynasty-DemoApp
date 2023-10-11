import mysql.connector
import csv

# CSV file path
csv_file = 'bounty.csv'

# MySQL database connection
conn = mysql.connector.connect(
    host='localhost',
    user='dev',
    password='pwd',
    database='dynasty'
)
cursor = conn.cursor()

# Read CSV file
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Get column headers

    # Create SQL table
    create_table_query = f"CREATE TABLE IF NOT EXISTS fruits (id INT AUTO_INCREMENT PRIMARY KEY, {', '.join([f'{column} VARCHAR(500)' for column in header[1:]])})"
    cursor.execute(create_table_query)

    # Insert data into the SQL table
    insert_query = f"INSERT INTO fruits ({', '.join(header)}) VALUES ({', '.join(['%s'] * len(header))})"
    for row in csv_reader:
        cursor.execute(insert_query, row)

# Commit the changes and close the connection
conn.commit()
conn.close()

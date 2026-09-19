import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Create the students table
cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
""")

# Insert data
students = [
    ("Mike", 21, "Information Technology"),
    ("John", 22, "Computer Science"),
    ("Sarah", 20, "Business Studies")
]

cursor.executemany("""
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
""", students)

# Save changes
connection.commit()

# Retrieve data
cursor.execute("SELECT * FROM students")
records = cursor.fetchall()

# Display data
print("Students in the database:")

for record in records:
    print(
        "ID:", record[0],
        "Name:", record[1],
        "Age:", record[2],
        "Course:", record[3]
    )

# Close connection
connection.close()
import sqlite3
db_path="./podcasts.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables=cursor.fetchall()

tables_to_delete=[table[0] for table in tables if table[0].endswith("_episode")]

for table in tables_to_delete:
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")
        print(f"Table {table} deleted successfully")
    except sqlite3.Error as e:
        print(f"Error deleting table {table}: {e}")

conn.commit()
conn.close()
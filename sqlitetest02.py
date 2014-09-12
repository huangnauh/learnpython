import os
import os.path
import sqlite3
db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'
db_exists = os.path.exists(db_filename)
with sqlite3.connect(db_filename) as conn:
    if not db_exists:
        with open(schema_filename,'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        conn.execute("""
        insert into project (name,description,deadline)
        values ('huang','learn python','2014-8-30')
        """)
        conn.execute("""
        insert into task (details,status,deadline,project)
        values ('writes about select','done','2014-8-16','huang')
        """)
        conn.execute("""
        insert into task (details,status,deadline,project)
        values ('write about random', 'waiting', '2010-10-10', 'huang')
        """)
        conn.execute("""
            insert into task (details, status, deadline, project)
            values ('write about sqlite3', 'active', '2010-10-17', 'huang')
            """)
    else:
        print("Database exists,assume schema does,too")
    cursor = conn.cursor()
    cursor.execute("""
    select id,priority,details,status, deadline
    from task where project = 'huang'
    """)
    for row in cursor.fetchall():
        task_id,priority,details,status, deadline = row
        print('%2d {%d} %-20s [%-8s] (%s)' % (task_id, priority, details, status, deadline))
import sqlite3
import sys

db_filename = 'todo.db'

sql = "select id, details, deadline from task"

def show_deadline(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    for col in ['id', 'details', 'deadline']:
        print '  column:', col
        print '    value :', row[col]
        print '    type  :', type(row[col])
    return

print 'Without type detection:'

with sqlite3.connect(db_filename) as conn:
    show_deadline(conn)

print '\nWith type detection:'

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    show_deadline(conn)
    
import logging
import sqlite3
import sys
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-10s) %(message)s',
                    )

db_filename = 'todo.db'
isolation_level = "IMMEDIATE"

def writer():
    my_name = threading.currentThread().name
    logging.debug('connecting')
    with sqlite3.connect(db_filename, isolation_level=isolation_level) as conn:
        cursor = conn.cursor()
        logging.debug('connected')
        cursor.execute('update task set priority = priority + 1')
        logging.debug('changes made')
        logging.debug('waiting to synchronize')
        ready.wait() # synchronize
        logging.debug('PAUSING')
        time.sleep(1)
        conn.commit()
        logging.debug('CHANGES COMMITTED')
    return

def reader():
    my_name = threading.currentThread().name
    with sqlite3.connect(db_filename, isolation_level=isolation_level) as conn:
        cursor = conn.cursor()
        logging.debug('waiting to synchronize')
        ready.wait() # synchronize
        logging.debug('wait over')
        cursor.execute('select id,priority,details,status, deadline from task')
        logging.debug('SELECT EXECUTED')
        time.sleep(2)
        results = cursor.fetchall()
        logging.debug('results fetched')
    return

if __name__ == '__main__':
    ready = threading.Event()

    threads = [
        threading.Thread(name='Reader 1', target=reader),
        threading.Thread(name='Reader 2', target=reader),
        threading.Thread(name='Writer 1', target=writer),
        threading.Thread(name='Writer 2', target=writer),
        ]
    
    [ t.start() for t in threads ]
    
    time.sleep(1)
    logging.debug('setting ready')
    ready.set()

    [ t.join() for t in threads ]
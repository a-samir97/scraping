import sqlite3

def connect_database(): 
    try:
        conn = sqlite3.connect("inmobly_database.db")
    except:
        raise Exception
    finally:
        conn.close()

def create_table():
    try:
        conn = sqlite3.connect("inmobly_database.db")
        conn.execute('''
            CREATE TABLE IF NOT EXISTS scraping
            (
                ID INTEGER PRIMARY KEY     AUTOINCREMENT,
                thumbnail_image           TEXT    NOT NULL,
                original_image           TEXT    NOT NULL,
                views            TEXT     NOT NULL,
                title            TEXT NOT NULL,
                duration         TEXT NOT NULL,
                vedio_url        TEXT NOT NULL);
            ''')
    
    except Exception:
        raise Exception
    
    finally:
        conn.close()


def insert_data(data_info):
    try:
        conn = sqlite3.connect('inmobly_database.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO scraping (thumbnail_image, original_image, title, views, duration, vedio_url) 
            VALUES (?, ?, ?, ?, ?, ? );
            """, 
                (
                    data_info['thumbnail_image'],
                    data_info['original_image'],
                    data_info['title'],
                    data_info['views'],
                    data_info['duration'],
                    data_info['vedio_url']
                )
            )
        conn.commit()
    
    except Exception:
        raise Exception
    
    finally:
        conn.close()

def get_all_data():
    try:
        conn = sqlite3.connect('inmobly_database.db')
        cursor = conn.execute("SELECT thumbnail_image, original_image, title, views, duration, vedio_url from scraping")
        
        for row in cursor:
            print ("thumbnail_image = ", row[0])
            print ("original_image = ", row[1])
            print ("title = ", row[2])
            print ("views = ", row[3])
            print("duration = ", row[4])
            print("vedio_url = ", row[5], '\n') 
            
    except Exception:
        raise Exception
    
    finally:
        conn.close()

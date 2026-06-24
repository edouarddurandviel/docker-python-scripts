
import mariadb
import requests
from assets import config
import sys

def getDataFromJsonPlaceholder():
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/todos")
        r.status_code
        return r
        
    except:
        print(f"[jsonplaceholder] Error jsonPlaceholder is unvailable: {e}")
        sys.exit(1)
        
        


def getCompanyUsers():
    try:
        cnx = mariadb.connect(**config.conn_params)
        print(cnx)
        cur = cnx.cursor()
        cur.execute("SELECT id, email FROM user")
        row = cur.fetchall()
        return row
    
    except mariadb.Error as e:
        print(f"[MariaDB] Error connecting to MariaDB: {e}")
        sys.exit(1)
        
    finally:
        if 'cnx' in locals() and cnx:
            cnx.close()
            print("[MariaDB] Connection closed.")
            
            
def getVersionFromMariaDB():
    try:
        cnx = mariadb.connect(**config.conn_params)
        print(cnx)
        cur = cnx.cursor()
        cur.execute("SELECT VERSION();")
        row = cur.fetchone()
     
        return row[0]
    
    except mariadb.Error as e:
        print(f"[MariaDB] Error connecting to MariaDB: {e}")
        sys.exit(1)
        
    finally:
        if 'cnx' in locals() and cnx:
            cnx.close()
            print("[MariaDB] Connection closed.")


def loadDataInMariaDB(fileRoot):
    try:
        cnx = mariadb.connect(**config.conn_params)
        
        print(cnx)
        cur = cnx.cursor()
        
        root = r"fileRoot"
        root = fileRoot.replace("\\", "/")

        sql = f"LOAD DATA LOCAL INFILE '{root}' INTO TABLE imports FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n' IGNORE 1 LINES;"
        cur.execute(sql)
        cnx.commit()
    
    except mariadb.Error as e:
        print(f"[MariaDB] Error connecting to MariaDB: {e}")
        sys.exit(1)
        
    finally:
        if 'cnx' in locals() and cnx:
            cnx.close()
            print("[MariaDB] Connection closed.")

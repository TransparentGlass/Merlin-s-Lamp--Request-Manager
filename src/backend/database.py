from PyQt6.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector
from backend.Request import Request


class databaseManager:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'merlinDB'
        }
    
    def execute_query(self, query, params=None):
        """A single point of failure/success for all write operations."""
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Integrity Error: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                
    def fetch_data(self, query, params=None):
        """A single point for all read operations."""
        # Similar logic to execute_query but returns cursor.fetchall()
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor(dictionary=True    )
            cursor.execute(query, params or ())
            result = cursor.fetchall()
            return result

        except mysql.connector.Error as e:
            print(f"Integrity Error: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                
    def fetch_one(self, query, params=None):
        """A single point for all read operations."""
        # Similar logic to execute_query but returns cursor.fetchone()
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params or ())
            result = cursor.fetchone()
            return result

        except mysql.connector.Error as e:
            print(f"Integrity Error: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        
    def submit_request(self, title, content, request_type, user_id = None) -> bool:
        query = "INSERT INTO requests (title, content, request_type, user_id) VALUES (%s,%s,%s,%s)"
        params = (title, content, request_type, user_id)
        return self.execute_query(query, params)
    
    ##TODO: fetch request and show them, place them in a frame, update priority and status if edited by an admin
    
    def fetch_requests(self) -> list[Request]:
        query = "SELECT * from requests limit 10"
        requests = self.fetch_data(query)
        
        request_list = []
        for r in requests:
            newRequest = Request(r.get('title'), r.get('request_type'), r.get('content'), r.get('date'), self.fetch_username(r.get('user_id')), r.get('id'))
            request_list.append(newRequest)
            print(f"added request #{r}")
            
        return request_list if request_list else None
            
    def fetch_username(self, user_id) -> str:
        query = "Select (user_name) from users WHERE user_id = %s"
        params = (user_id, )
        result = self.fetch_one(query, params)
        return str(result['user_name']) if result else ""
        


            
# db = databaseManager()
# db.fetch_requests()

# print(f"Username: {db.fetch_username('1')}")
        
        
        
    
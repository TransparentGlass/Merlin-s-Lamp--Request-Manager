from PyQt6.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector
import Request


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
        
    def submit_request(self, title, content, request_type, user_id = None) -> bool:
        query = "INSERT INTO requests (title, content, request_type, user_id) VALUES (%s,%s,%s,%s)"
        params = (title, content, request_type, user_id)
        return self.execute_query(query, params)
    
    ##TODO: fetch request and show them, place them in a frame, update priority and status if edited by an admin
        
        
        
    
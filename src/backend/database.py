from PyQt6.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector
from backend.Request import Request, StatusType, Priority
import bcrypt



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
        
        except UnboundLocalError as e:
            print(f"Cannot access database. Please turn on XAMPP")
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
        
    def submit_request(self, title, content, request_type, username) -> bool:
        query = "INSERT INTO requests (title, content, request_type, user_id) VALUES (%s,%s,%s,%s)"
        params = (title, content, request_type, self.fetch_user_id(username))
        return self.execute_query(query, params)
    
    def fetch_requests(self, filter_prio = None, filter_status = None, filter_type = None) -> list[Request]:
        base_query = "SELECT * from requests"
        params = []

        active_filters = {}
        if filter_prio:
            active_filters['priority'] = filter_prio
        if filter_status:
            active_filters['status'] = filter_status
        if filter_type:
            active_filters['request_type'] = filter_type
            
            
        if not active_filters:
            # THE "NO FILTERS" STATE: Just run the base query
            final_query = base_query
        else:
            # Build the WHERE clause dynamically
            conditions = [f"{column} = %s" for column in active_filters.keys()]
            final_query = f"{base_query} WHERE {' AND '.join(conditions)}"
            params = list(active_filters.values())
            
        requests = self.fetch_data(final_query, params)
        
        if not requests:
            print("Fetch request is empty")
            return None
        
        request_list = []
        for r in requests:
            newRequest = Request(r.get('title'), 
                                 r.get('request_type'),
                                 Priority[r.get('priority')],
                                 StatusType[r.get('status')],
                                 r.get('content'),
                                 r.get('date'),
                                 r.get('user_id'),
                                 r.get('upvote'),
                                 r.get('id')
                                 )
            request_list.append(newRequest)
            # print(f"added request #{r}")
            
        return request_list if request_list else None
    
    def fetch_username(self, user_id) -> str:
        query = "Select (user_name) from users WHERE user_id = %s"
        params = (user_id, )
        result = self.fetch_one(query, params)
        return str(result['user_name']) if result else ""
    
    def fetch_user_id(self, username) -> int:
        query = "Select (user_id) from users WHERE user_name = %s limit 1"
        params = (username, )
        result = self.fetch_one(query, params)
        return int(result['user_id']) if result else None

    def update_priority(self, req_id: int, priority: Priority) -> bool:
        query = "UPDATE requests SET priority = %s WHERE id = %s limit 1"
        params = (priority.name, req_id)
        
        try:
            self.execute_query(query, params)
            return True
        except Exception as e:
            print(f"Error: Database update failed: {e}")
            return False
    
    def update_status(self,req_id: int, status: StatusType) -> bool:
        query = "UPDATE requests SET status = %s WHERE id = %s limit 1"
        params = (status.name, req_id)
        
        try:
            self.execute_query(query, params)
            return True
        except Exception as e:
            print(f"Error: Database update failed: {e}")
            return False

    def userRegister(self, username, password) -> bool:
        query = "Select 1 FROM users where user_name = %s limit 1"
        param = (username, )
        if self.fetch_one(query, param):
            # print("user exists, try another name to register")
            return False
        
        newpassword = password.encode('utf-8')
        hashed = bcrypt.hashpw(newpassword, bcrypt.gensalt()).decode('utf-8')
        
        query = "INSERT INTO users (user_name, password_hash) values (%s, %s)"
        param = (username, hashed)
        if self.execute_query(query, param):
            # print(f"Successfully signed in as {username}")
            return True
        return False
    
    def userLogin(self, username, password) -> bool:
        query = "SELECT password_hash FROM users WHERE user_name = %s LIMIT 1"
        param = (username,)
        
        result = self.fetch_one(query, param)
        if not result:
            print("Login failed: User does not exist")
            return False
        
        stored_hash = result["password_hash"]
        
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
            # print(f"Welcome back, {username}!")
            return True
        else:
            # print("Login failed: Incorrect password.")
            return False
        
    def upvote(self, id):
        query = "UPDATE requests SET upvote = upvote + 1 WHERE id = %s"
        param = (id,)
        if self.execute_query(query, param):
            return True
        return False
    
    def undoVote(self, id):
        query = "UPDATE requests SET upvote = upvote - 1 WHERE id = %s"
        param = (id,)
        if self.execute_query(query, param):
            return True
        return False
        
        
        
# db = databaseManager()
# db.fetch_requests()

# print(f"Username: {db.fetch_username('1')}")
        
        
        
    
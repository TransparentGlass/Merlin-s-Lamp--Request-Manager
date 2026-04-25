from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class DB_Util:
    def __init__(self):
        self.username = "root"
        self.password = ""
        self.database = "merlinDB"
    
    def connectDB(self):
        db = QSqlDatabase.addDatabase(self.database)
        db.setUserName(self.username)
        db.setPassword(self.password)
        db.setHostName("localhost")   
        
        if not db.open:
            print("Connetion failed")
            return False 
        
        
        print("Success, connected to db")
        return True   
        
    
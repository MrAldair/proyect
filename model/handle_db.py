import sqlite3

class HandleDB():
    
    #Tabla Users
    def __init__(self):
        self._con = sqlite3.connect("./requests.db")
        self._cur = self._con.cursor()
        
    def get_all(self):
        data = self._cur.execute("SELECT * FROM users")
        return data.fetchall()
    
    def get_only(self, data_user):
        data = self._cur.execute("SELECT * FROM users WHERE employee_id = '{}'".format(data_user))
        return data.fetchone()
    
    def insert(self, data_user):
        self._cur.execute("INSERT INTO users VALUES('{}','{}','{}','{}','{}','{}')".format(
            data_user["id"],
            data_user["first_name"],
            data_user["last_name"],
            data_user["employee_id"],
            data_user["department_id"],
            data_user["password_user"],
        ))
        self._con.commit()
        
    #Tabla Requests
class Requests():
    
    def __init__(self):
        self._con = sqlite3.connect("./requests.db")
        self._cur = self._con.cursor()
    
    def get_all(self):
        data = self._cur.execute("SELECT * FROM requests")
        return data.fetchall()
    
    def get_only(self, data_user):
        data = self._cur.execute("SELECT * FROM requests WHERE employee_id = '{}'".format(data_user))
        return data.fetchone()
    
    def insert(self, data_user):
        self._cur.execute("""
    INSERT INTO requests (
        employee_id,
        employee_name,
        user_id,
        warning_id,
        status_id,
        reason_id,
        reason
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
""", (
    data_user['employee_id'],
    data_user['employee_name'],
    data_user['user_id'],
    data_user['warning_id'],
    data_user['status_id'],
    data_user['reason_id'],
    data_user['reason']
))
        self._con.commit()
        
    def __del__(self):
        self._con.close()
    
    
db = Requests()
print(db.get_only(2274))
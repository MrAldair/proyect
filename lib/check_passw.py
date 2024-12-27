from model.handle_db import HandleDB
from werkzeug.security import check_password_hash

def check_user(employee_id, passw):
    user = HandleDB()
    filter_user = user.get_only(employee_id)
    if filter_user:
        same_passw = check_password_hash(filter_user[5], passw)
        if same_passw:
            return filter_user
    return None
from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.user import User
from lib.check_passw import check_user

app = FastAPI()

template = Jinja2Templates(directory="./view")

@app.get("/", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.post("/", response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.get("/signup", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})

@app.get("/user", response_class=HTMLResponse)
def user(req: Request):
    
    return RedirectResponse("/")
    #return template.TemplateResponse("user.html", {"request": req})

@app.post("/user", response_class=HTMLResponse)
def user(req: Request, employee_id: str = Form(), password_user: str = Form()):
    verify = check_user(employee_id, password_user)
    if verify:
        return template.TemplateResponse("user.html", {"request": req, "data_user": verify})
    
    return RedirectResponse("/")

#Manda formulario para dar de alta usuario
@app.post("/data-processing")
def data_processing(first_name: str = Form(), last_name: str = Form(), employee_id: str = Form(), department_id: str = Form(), password_user: str = Form()):
    
    data_user = {
        "first_name": first_name,
        "last_name": last_name,
        "employee_id": employee_id,
        "department_id": department_id,
        "password_user": password_user
    }
    db = User(data_user)
    db.create_user()
    
    return RedirectResponse("/")




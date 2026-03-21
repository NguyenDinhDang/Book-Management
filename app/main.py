from fastapi import FastAPI

app = FastAPI() #tạo app đây là trái tim server

#database tạm thời chỉ là list trong ram
tasks = []
@app.get("/") # báo cho FastAPI biết: "khi ai gọi GET tới / thì chạy hàm bên dưới
def hello():
    return {"massage": "Hello World!"}

@app.get("/tasks") 
def getTask():
    return tasks
#POST /task nhận task mới từ body sang list 
@app.post("/task")  
def create_task(task:dict):
    tasks.append(task)
    return {"message": "Thêm task thành công","task": task}


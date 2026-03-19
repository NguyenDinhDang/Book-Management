from fastapi import FastAPI

app = FastAPI() #tạo app đây là trái tim server 

@app.get("/") # báo cho FastAPI biết: "khi ai gọi GET tới / thì chạy hàm bên dưới
def hello():
    return {"massage": "Hello World!"}


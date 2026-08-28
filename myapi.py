from fastapi import FastAPI, Path, HTTPException
"""
Một app cơ bản phải có CURD cơ bản create, update, read, delete
GET - Lấy dữ liệu
POST - Thêm dữ liệu
PUT - Cập nhật dữ liệu
DELETE - Xóa dữ liệu
"""

app = FastAPI()

students = {
    110125113: {
        "name": "Nguyen",
        "age": "19",
        "major": "Information Technology"
    }
}
# lt lessthan, gt greater than
@app.get("/get-student/{student_id}") #dùng parameter để tìm kiếm API 
def get_student(student_id: int = Path(..., description="The id of the student you want to view")): # mô tả cho người dùng biết cần nhập gì 
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: str = None): # chuyển về tuỳ chọn không bắt buộc khi có none
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

